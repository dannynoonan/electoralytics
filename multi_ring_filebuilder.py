#!/usr/bin/env python
import argparse
import os

import pandas as pd
import numpy as np

from metadata import Columns, DataDirs, DataFiles, ACW_GROUPS, CENSUS_GROUPS


cols = Columns()
ddirs = DataDirs()
dfiles = DataFiles()


# disable unhelpful 'SettingWithCopyWarnings'
pd.options.mode.chained_assignment = None

print(f"Starting the electoralytics 'multi_ring_filebuilder' script. This process will:")
print(f"(1) load the superset of electoralytics data from {dfiles.THE_ONE_RING} into a pandas dataframe")
print(f"(2) transform the source data into multiple formats optimized for plotly figure-building")
print(f"(3) output a truncated view of the data in the response, or if '--write=True' output the data to csv files")

# init default params
WRITE_TO_CSV = False
MAX_EC_FOR_SMALL = 0
GROUPS_DIR = ddirs.ACW

# init parser and recognized args
parser = argparse.ArgumentParser()
parser.add_argument("--small", "-s", help="0 (default), 3, 4, or 5: set max EC votes for 'Small states' Group")
parser.add_argument("--groups", "-g", help="ACW (default) or Census: ACW=Union,Confederate,Border,Postbellum; Census=Northeast,South,Midwest,West.")
parser.add_argument("--write", "-w", help="True or False (default): write output to csv files")

# read cmd-line args
args = parser.parse_args()

# map args to params
if args.small:
    print(f"Argument 'small' was input as: {args.small}")
    if args.small in ['3', '4', '5']:
        MAX_EC_FOR_SMALL = int(args.small)
        print(f"Setting MAX_EC_FOR_SMALL param to: {MAX_EC_FOR_SMALL}")
    elif args.small in ['0', 0]:
        print(f"Keeping MAX_EC_FOR_SMALL param as: {MAX_EC_FOR_SMALL}")
    else:
        print(f"A 'small' value of {args.small} isn't recognized. Recognized values are: [0, 3, 4, 5]. Keeping MAX_EC_FOR_SMALL param as: {MAX_EC_FOR_SMALL}")
if args.groups:
    print(f"Argument 'groups' was input as: {args.groups}")
    if args.groups in ['Census', 'census']:
        GROUPS_DIR = ddirs.CENSUS
        print(f"Setting GROUPS_DIR param to: {GROUPS_DIR}")
    elif args.groups in ['ACW', 'acw']:
        print(f"Keeping GROUPS_DIR param as: {GROUPS_DIR}")
    else:
        print(f"A 'groups' value of {args.groups} isn't recognized. Recognized values are: ['acw', 'census']. Keeping GROUPS_DIR param as: {GROUPS_DIR}")
if args.write:
    print(f"Argument 'write' was input as: {args.write}")
    if args.write in ['True', 'true']:
        WRITE_TO_CSV = True
        print(f"Setting WRITE_TO_CSV param to: {WRITE_TO_CSV}")
    elif args.write in ['False', 'false']:
        print(f"Keeping WRITE_TO_CSV param as: {WRITE_TO_CSV}")
    else:
        print(f"A 'write' value of {args.write} isn't recognized. Recognized values are: ['True', 'False']. Keeping WRITE_TO_CSV param as: {WRITE_TO_CSV}")


# adjust settings based on params
subdir = f"{ddirs.GEN}/{GROUPS_DIR}"
# Groups sourcing metadata
if GROUPS_DIR == ddirs.CENSUS:
    GROUPS = CENSUS_GROUPS
    COL_GROUP_SRC = cols.CENSUS_GROUP
else:
    GROUPS = ACW_GROUPS
    COL_GROUP_SRC = cols.ACW_GROUP
# Small Group extraction metadata
if MAX_EC_FOR_SMALL == 3:
    GROUPS.append('Small')
    subdir = f"{subdir}/{ddirs.SMALL_3}"
elif MAX_EC_FOR_SMALL == 4:
    GROUPS.append('Small')
    subdir = f"{subdir}/{ddirs.SMALL_4}"
elif MAX_EC_FOR_SMALL == 5:
    GROUPS.append('Small')
    subdir = f"{subdir}/{ddirs.SMALL_5}"
else:
    subdir = f"{subdir}/{ddirs.NO_SMALL}"

GROUPS_SER = pd.Series(np.array(GROUPS + ['Total']))


# load electoral college data
the_one_ring = pd.read_csv(dfiles.THE_ONE_RING)

### TRANSFORM CSV DATA ###
# files to output: 
# * pivot_on_year 
# * group_aggs_by_year 
# * totals_by_year
# * avg_weight_by_year 


# initialize new data frames
pivot_on_year = pd.DataFrame(
    columns=[cols.ABBREV, cols.STATE, cols.GROUP, cols.YEAR, cols.EC_VOTES, cols.VOTES_COUNTED, cols.VOTES_COUNTED_NORM,
            cols.VOTES_COUNTED_PCT, cols.EC_VOTES_NORM, cols.POP_PER_EC, cols.VOTE_WEIGHT, cols.PARTY])
group_aggs_by_year = pd.DataFrame(
    columns=[cols.GROUP, cols.YEAR, cols.EC_VOTES, cols.VOTES_COUNTED, cols.VOTES_COUNTED_NORM, cols.VOTES_COUNTED_PCT, 
            cols.EC_VOTES_NORM, cols.POP_PER_EC, cols.AVG_WEIGHT, cols.STATE_COUNT, cols.STATES_IN_GROUP])
totals_by_year = pd.DataFrame(columns=[cols.YEAR, cols.EC_VOTES, cols.VOTES_COUNTED, cols.POP_PER_EC, cols.MOST_EC_VOTES])

### LEGACY, but still haven't transitioned off of ###
avg_weight_by_year = pd.DataFrame({cols.GROUP: GROUPS_SER}) 
avg_weight_by_year.set_index(cols.GROUP, inplace=True)


# begin iterating through years in the_one_ring
year = 1828
while year <= 2020:

    # column names for current year
    ec_votes_col = f'{year} {cols.EC_VOTES}'
    votes_counted_col = f'{year} {cols.VOTES_COUNTED}'
    vote_weight_col = f'{year} {cols.VOTE_WEIGHT}'
    avg_weight_col = f'{year} {cols.AVG_WEIGHT}'
    party_col = f'{year} {cols.PARTY}'

    # extract electoral college data for year
    year_data = the_one_ring[
        [cols.ABBREV, cols.STATE, COL_GROUP_SRC, ec_votes_col, votes_counted_col, vote_weight_col, party_col]]
    # rename columns and set row keys/index
    year_data.rename(columns={COL_GROUP_SRC: cols.GROUP, ec_votes_col: cols.EC_VOTES, votes_counted_col: cols.VOTES_COUNTED, 
                            vote_weight_col: cols.VOTE_WEIGHT, party_col: cols.PARTY},
                    inplace=True)
    year_data.set_index(cols.ABBREV, inplace=True)

    
    # DATA CLEANSING
    # remove states lacking votes counted for this year 
    year_data = year_data[pd.notnull(year_data[cols.VOTES_COUNTED])]
    # remove states where votes counted is 'Rejected'
    year_data = year_data[year_data[cols.VOTES_COUNTED] != 'Rejected']
    # set votes counted to 0 where votes counted is 'NoPop'
    year_data[cols.VOTES_COUNTED][year_data[cols.VOTES_COUNTED] == 'NoPop'] = 0
    
    # explicitly set type of votes counted data to int (not sure why this isn't automatic)
    year_data[[cols.VOTES_COUNTED]] = year_data[[cols.VOTES_COUNTED]].astype(int)

    # extract US totals data 
    ec_total = year_data.loc['US'][cols.EC_VOTES]
    pop_total = year_data.loc['US'][cols.VOTES_COUNTED]
    # calculate average popular vote per EC vote
    pop_per_ec = round(pop_total / ec_total)
    
    # remove US column from year_data
    year_data = year_data.drop('US')

    # map states having MAX_EC_FOR_SMALL or fewer electoral college votes to 'Small' Group
    if MAX_EC_FOR_SMALL > 0:
        year_data.loc[year_data[cols.EC_VOTES] <= MAX_EC_FOR_SMALL, cols.GROUP] = 'Small'


    # DF 1: assemble year_pivot to append to pivot_on_year
    year_pivot = year_data
    # add/derive/populate additional columns based on source data
    year_pivot[cols.YEAR] = [year] * len(year_pivot.index)
    year_pivot[cols.VOTES_COUNTED_NORM] = round(year_pivot[cols.VOTES_COUNTED] * year_pivot[cols.VOTE_WEIGHT])
    year_pivot[cols.VOTES_COUNTED_PCT] = (100 * year_pivot[cols.VOTES_COUNTED] / pop_total).round(decimals=2)
    year_pivot[cols.EC_VOTES_NORM] = (year_pivot[cols.VOTES_COUNTED] / pop_per_ec).round(decimals=2)
    year_pivot[cols.POP_PER_EC] = round(year_pivot[cols.VOTES_COUNTED] / year_pivot[cols.EC_VOTES])

    # unset index so we can append 
    year_pivot.reset_index(inplace=True)
    # add placeholder row for any Group that isn't represented 
    for group in GROUPS:
        if len(year_pivot.loc[year_pivot[cols.GROUP] == group]) == 0:
            year_pivot_bonus = pd.DataFrame([['', '', group, year, 0, 0, 0, 0, 0, 0, 0, '']],
                columns=[cols.ABBREV, cols.STATE, cols.GROUP, cols.YEAR, cols.EC_VOTES, cols.VOTES_COUNTED, cols.VOTES_COUNTED_NORM,
                         cols.VOTES_COUNTED_PCT, cols.EC_VOTES_NORM, cols.POP_PER_EC, cols.VOTE_WEIGHT, cols.PARTY])
                # columns=list(year_pivot.columns.values))
            year_pivot = pd.concat([year_pivot, year_pivot_bonus], ignore_index=True, sort=False)
    # append year_pivot to pivot_on_year
    pivot_on_year = pd.concat([pivot_on_year, year_pivot], ignore_index=True, sort=False)
        
        
    # DF 2: init year_totals to append to totals_by_year
    year_totals = pd.DataFrame([[year, ec_total, pop_total, pop_per_ec, year_data[cols.EC_VOTES].max()]],
                               columns=[cols.YEAR, cols.EC_VOTES, cols.VOTES_COUNTED, cols.POP_PER_EC, cols.MOST_EC_VOTES])
    totals_by_year = pd.concat([totals_by_year, year_totals], ignore_index=True, sort=False)  

    
    # DF 3: aggregate EC votes, popular votes, and states for each Group, assign summed values to new year_group_aggs dataframe
    # more data cleansing: drop states whose votes counted == 0
    year_data = year_data[year_data[cols.VOTES_COUNTED] > 0]
    # generate aggregate columns
    year_group_aggs = year_data.groupby(cols.GROUP).agg(
        {cols.EC_VOTES: 'sum', cols.VOTES_COUNTED: 'sum', cols.STATE: 'count'})
    year_group_aggs_2 = year_data.groupby(cols.GROUP).agg({cols.ABBREV: ','.join})
    year_group_aggs_2.rename(columns={cols.ABBREV: cols.STATES_IN_GROUP}, inplace=True)
    year_group_aggs = year_group_aggs.join(year_group_aggs_2, how='outer')
    # add/derive/populate additional columns
    year_group_aggs[cols.AVG_WEIGHT] = (pop_per_ec * year_group_aggs[cols.EC_VOTES] / year_group_aggs[cols.VOTES_COUNTED]).round(decimals=2)
    year_group_aggs[cols.YEAR] = [year] * len(year_group_aggs)
    year_group_aggs[cols.VOTES_COUNTED_NORM] = round(year_group_aggs[cols.VOTES_COUNTED] * year_group_aggs[cols.AVG_WEIGHT])
    year_group_aggs[cols.VOTES_COUNTED_PCT] = (100 * year_group_aggs[cols.VOTES_COUNTED] / pop_total).round(decimals=2)
    year_group_aggs[cols.EC_VOTES_NORM] = (year_group_aggs[cols.VOTES_COUNTED] / pop_per_ec).round(decimals=2)
    year_group_aggs[cols.POP_PER_EC] = round(year_group_aggs[cols.VOTES_COUNTED] / year_group_aggs[cols.EC_VOTES])
    # unset index, rename columns, add year column
    year_group_aggs.reset_index(inplace=True)
    year_group_aggs.rename(columns={cols.STATE: cols.STATE_COUNT}, inplace=True)
    # add placeholder row for any Group that isn't represented 
    for group in GROUPS:
        if len(year_group_aggs.loc[year_group_aggs[cols.GROUP] == group]) == 0:
            year_group_aggs_bonus = pd.DataFrame([[group, year, 0, 0, 0, 0, 0, 0, 0, 0, '']],
                columns=[cols.GROUP, cols.YEAR, cols.EC_VOTES, cols.VOTES_COUNTED, cols.VOTES_COUNTED_NORM, cols.VOTES_COUNTED_PCT, 
                        cols.EC_VOTES_NORM, cols.POP_PER_EC, cols.AVG_WEIGHT, cols.STATE_COUNT, cols.STATES_IN_GROUP])
            year_group_aggs = pd.concat([year_group_aggs, year_group_aggs_bonus], ignore_index=True, sort=False)
    # append year_group_aggs to group_aggs_by_year
    group_aggs_by_year = pd.concat([group_aggs_by_year, year_group_aggs], ignore_index=True, sort=False)
    
    
    ### LEGACY ###
    # aggregate EC votes and popular votes for each Group, assign summed values to new year_agg dataframe
    year_agg = year_data.groupby(cols.GROUP).agg({cols.EC_VOTES: 'sum', cols.VOTES_COUNTED: 'sum'})
    # add Average weight column by dividing EC votes by popular votes and multiplying by national pop-per-EC factor
    year_agg[year] = pop_per_ec * year_agg[cols.EC_VOTES] / year_agg[cols.VOTES_COUNTED]

    # add Total row to end of of year_agg
    total_row = pd.DataFrame([['Total', ec_total, pop_total, 1.0]], 
                             columns=[cols.GROUP, cols.EC_VOTES, cols.VOTES_COUNTED, year])
    total_row = total_row.set_index(cols.GROUP)
    year_agg = year_agg.append(total_row)

    # extract avg_weight column into its own dataframe, rename column to be simply the year
    avg_weight_df = year_agg.drop([cols.EC_VOTES, cols.VOTES_COUNTED], axis=1)
    avg_weight_by_year = avg_weight_by_year.join(avg_weight_df, how='outer')
    
    
    # increment to next election
    year = year + 4


PIVOT_ON_YEAR_CSV = f"{ddirs.BASE}/{subdir}/{dfiles.PIVOT_ON_YEAR}"
TOTALS_BY_YEAR_CSV = f"{ddirs.BASE}/{ddirs.GEN}/{dfiles.TOTALS_BY_YEAR}"
GROUP_AGGS_BY_YEAR_CSV = f"{ddirs.BASE}/{subdir}/{dfiles.GROUP_AGGS_BY_YEAR}"
AVG_WEIGHT_BY_YEAR_CSV = f"{ddirs.BASE}/{subdir}/{dfiles.AVG_WEIGHT_BY_YEAR}"

print(f"Rows in {PIVOT_ON_YEAR_CSV}: {len(pivot_on_year)}")
print(f"{pivot_on_year}")
print(f"Rows in {TOTALS_BY_YEAR_CSV}: {len(totals_by_year)}")
print(f"{totals_by_year}")
print(f"Rows in {GROUP_AGGS_BY_YEAR_CSV}: {len(group_aggs_by_year)}")
print(f"{group_aggs_by_year}")
print(f"Rows in {AVG_WEIGHT_BY_YEAR_CSV}: {len(avg_weight_by_year)}")
print(f"{avg_weight_by_year}")


if WRITE_TO_CSV:
    if not os.path.exists(f"{ddirs.BASE}/{subdir}"):
        os.makedirs(f"{ddirs.BASE}/{subdir}")

    # write pivot_on_year, totals_by_year, group_aggs_by_year to file
    pivot_on_year.to_csv(PIVOT_ON_YEAR_CSV)
    totals_by_year.to_csv(TOTALS_BY_YEAR_CSV)
    group_aggs_by_year.to_csv(GROUP_AGGS_BY_YEAR_CSV)


    ### LEGACY ###
    # rename Total column and write avg_weight_by_year to file
    avg_weight_by_year.rename(index={'Total': 'Nat\'l Average'}, inplace=True)
    avg_weight_by_year.to_csv(AVG_WEIGHT_BY_YEAR_CSV)
