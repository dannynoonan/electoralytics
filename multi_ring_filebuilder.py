#!/usr/bin/env python
import argparse
import os

import pandas as pd
import numpy as np

from metadata import (
    THE_ONE_RING_CSV, AVG_WEIGHT_BY_YEAR_CSV, GROUP_AGGS_BY_YEAR_CSV, GROUPS_BY_YEAR_CSV, PIVOT_ON_YEAR_CSV, TOTALS_BY_YEAR_CSV, 
    BASE_DATA_DIR, GEN_DATA_DIR, GEN_ALT_GROUP_DIR, GEN_NO_SMALL_DIR, GEN_ALT_GROUP_NO_SMALL_DIR, GROUPS, ALT_GROUPS, 
    COL_ABBREV, COL_AVG_WEIGHT, COL_EC_VOTES, COL_EC_VOTES_NORM, COL_GROUP, COL_ALT_GROUP, COL_MOST_EC_VOTES, COL_PARTY, COL_POP_PER_EC, 
    COL_STATE, COL_STATE_COUNT, COL_STATES_IN_GROUP, COL_VOTE_WEIGHT, COL_VOTES_COUNTED, COL_VOTES_COUNTED_PCT, COL_YEAR
)

GROUPS_SER = pd.Series(np.array(GROUPS + ['Total']))

# disable unhelpful 'SettingWithCopyWarnings'
pd.options.mode.chained_assignment = None


print(f"Starting the electoralytics 'multi_ring_filebuilder' script. This process will:")
print(f"(1) load the superset of electoralytics data from {THE_ONE_RING_CSV} into a pandas dataframe")
print(f"(2) transform the source data into multiple formats optimized for plotly figure-building")
print(f"(3) output a truncated view of the data in the response, or if '--write=True' output the data to csv files")

# init default params
WRITE_TO_CSV = False
NO_SMALL = False
USE_ALT_GROUP = False

# init parser and recognized args
parser = argparse.ArgumentParser()
parser.add_argument("--small", "-s", help="True (default) or False: extract 'Small states' (4 EC votes or fewer) into their own Group")
parser.add_argument("--groups", "-g", help="Orig (default) or Alt: Orig=Northeast,Border,Confederate,Midwest,West. Alt=Union,Border,Confederate,West")
parser.add_argument("--write", "-w", help="True or False (default): write output to csv files")

# read cmd-line args
args = parser.parse_args()

# map args to params
if args.small:
    print(f"Argument 'small' was input as: {args.small}")
    if args.small in ['False','false']:
        NO_SMALL = True
        print(f"Setting NO_SMALL param to: {NO_SMALL}")
    elif args.small in ['True','true']:
        print(f"Keeping NO_SMALL param as: {NO_SMALL}")
    else:
        print(f"A 'small' value of {args.small} isn't recognized. Recognized values are: ['True','False']. Keeping NO_SMALL param as: {NO_SMALL}")
if args.groups:
    print(f"Argument 'groups' was input as: {args.groups}")
    if args.groups in ['Alt','alt','ALT']:
        USE_ALT_GROUP = True
        print(f"Setting USE_ALT_GROUP param to: {USE_ALT_GROUP}")
    elif args.groups in ['Default','default']:
        print(f"Keeping USE_ALT_GROUP param as: {USE_ALT_GROUP}")
    else:
        print(f"A 'groups' value of {args.groups} isn't recognized. Recognized values are: ['Alt','Default']. Keeping USE_ALT_GROUP param as: {USE_ALT_GROUP}")
if args.write:
    print(f"Argument 'write' was input as: {args.write}")
    if args.write in ['True','true']:
        WRITE_TO_CSV = True
        print(f"Setting WRITE_TO_CSV param to: {WRITE_TO_CSV}")
    elif args.write in ['False','false']:
        print(f"Keeping WRITE_TO_CSV param as: {WRITE_TO_CSV}")
    else:
        print(f"A 'write' value of {args.write} isn't recognized. Recognized values are: ['True','False']. Keeping WRITE_TO_CSV param as: {WRITE_TO_CSV}")


# adjust settings based on params
gen_data_dir = GEN_DATA_DIR
# Group: Northeast+Midwest+West, AltGroup: Union+West
if USE_ALT_GROUP:
    GROUPS = ALT_GROUPS
    COL_GROUP = COL_ALT_GROUP
    gen_data_dir = GEN_ALT_GROUP_DIR
# Small or No Small
if NO_SMALL:
    GROUPS.remove('Small')
    gen_data_dir = GEN_NO_SMALL_DIR
    if USE_ALT_GROUP:
        gen_data_dir = GEN_ALT_GROUP_NO_SMALL_DIR


# TODO modify csv file names based on input params


# load electoral college data
the_one_ring = pd.read_csv(THE_ONE_RING_CSV)

### TRANSFORM CSV DATA ###
# files to output: 
# * groups_by_year 
# * avg_weight_by_year 
# * silder_pivot 


# initialize new data frames
pivot_on_year = pd.DataFrame(
    columns=[COL_ABBREV, COL_STATE, COL_GROUP, COL_YEAR, COL_EC_VOTES, COL_VOTES_COUNTED, COL_VOTES_COUNTED_PCT, 
             COL_EC_VOTES_NORM, COL_POP_PER_EC, COL_VOTE_WEIGHT, COL_PARTY])
group_aggs_by_year = pd.DataFrame(
    columns=[COL_GROUP, COL_YEAR, COL_EC_VOTES, COL_VOTES_COUNTED, COL_VOTES_COUNTED_PCT, COL_EC_VOTES_NORM,
             COL_POP_PER_EC, COL_AVG_WEIGHT, COL_STATE_COUNT, COL_STATES_IN_GROUP])
totals_by_year = pd.DataFrame(columns=[COL_YEAR, COL_EC_VOTES, COL_VOTES_COUNTED, COL_POP_PER_EC, COL_MOST_EC_VOTES])


### LEGACY ###
avg_weight_by_year = pd.DataFrame({COL_GROUP: GROUPS_SER}) 
avg_weight_by_year.set_index(COL_GROUP, inplace=True)
# groups_by_year = pd.DataFrame({COL_GROUP: groups}) 
# groups_by_year.set_index(COL_GROUP, inplace=True)


# begin iterating through years in the_one_ring
year = 1828
while year <= 2020:

    # column names for current year
    ec_votes_col = f'{year} {COL_EC_VOTES}'
    votes_counted_col = f'{year} {COL_VOTES_COUNTED}'
    vote_weight_col = f'{year} {COL_VOTE_WEIGHT}'
    avg_weight_col = f'{year} {COL_AVG_WEIGHT}'
    party_col = f'{year} {COL_PARTY}'

    # extract electoral college data for year
    year_data = the_one_ring[
        [COL_ABBREV, COL_STATE, COL_GROUP, ec_votes_col, votes_counted_col, vote_weight_col, party_col]]
    # rename columns and set row keys/index
    year_data.rename(columns={ec_votes_col: COL_EC_VOTES, votes_counted_col: COL_VOTES_COUNTED,
                              vote_weight_col: COL_VOTE_WEIGHT, party_col: COL_PARTY},
                    inplace=True)
    year_data.set_index(COL_ABBREV, inplace=True)

    
    # DATA CLEANSING
    # remove states lacking vote weight for this year 
    year_data = year_data[pd.notnull(year_data[COL_VOTE_WEIGHT])]
    
    # explicitly set type of votes counted data to int (not sure why this isn't automatic)
    year_data[[COL_VOTES_COUNTED]] = year_data[[COL_VOTES_COUNTED]].astype(int)

    # extract US totals data 
    ec_total = year_data.loc['US'][COL_EC_VOTES]
    pop_total = year_data.loc['US'][COL_VOTES_COUNTED]
    # calculate average popular vote per EC vote
    pop_per_ec = round(pop_total / ec_total)
    
    # remove US column from year_data
    year_data = year_data.drop('US')

    # map states having 4 or fewer electoral college votes to 'Small' Group
    if not NO_SMALL:
        year_data.loc[year_data[COL_EC_VOTES] <= 4, COL_GROUP] = 'Small'


    # DF 1: assemble year_pivot to append to pivot_on_year
    year_pivot = year_data
    # add/derive/populate year, votes counted pct, and ec votes normalized columns
    year_pivot[COL_YEAR] = [year] * len(year_pivot.index)
    year_pivot[COL_VOTES_COUNTED_PCT] = (100 * year_pivot[COL_VOTES_COUNTED] / pop_total).round(decimals=2)
    year_pivot[COL_EC_VOTES_NORM] = (year_pivot[COL_VOTES_COUNTED] / pop_per_ec).round(decimals=2)
    year_pivot[COL_POP_PER_EC] = round(year_pivot[COL_VOTES_COUNTED] / year_pivot[COL_EC_VOTES])
    # unset index so we can append 
    year_pivot.reset_index(inplace=True)
    # add placeholder row for any Group that isn't represented 
    for group in GROUPS:
        if len(year_pivot.loc[year_pivot[COL_GROUP] == group]) == 0:
            year_pivot_bonus = pd.DataFrame([['', '', group, year, 0, 0, 0, 0, 0, 0, '']],
                columns=[COL_ABBREV, COL_STATE, COL_GROUP, COL_YEAR, COL_EC_VOTES, COL_VOTES_COUNTED, 
                         COL_VOTES_COUNTED_PCT, COL_EC_VOTES_NORM, COL_POP_PER_EC, COL_VOTE_WEIGHT, COL_PARTY])
            year_pivot = pd.concat([year_pivot, year_pivot_bonus], ignore_index=True, sort=False)
    # append year_pivot to pivot_on_year
    pivot_on_year = pd.concat([pivot_on_year, year_pivot], ignore_index=True, sort=False)
        
        
    # DF 2: init year_totals to append to totals_by_year
    year_totals = pd.DataFrame([[year, ec_total, pop_total, pop_per_ec, year_data[COL_EC_VOTES].max()]],
                               columns=[COL_YEAR, COL_EC_VOTES, COL_VOTES_COUNTED, COL_POP_PER_EC, COL_MOST_EC_VOTES])
    totals_by_year = pd.concat([totals_by_year, year_totals], ignore_index=True, sort=False)  

    
    # DF 3: aggregate EC votes, popular votes, and states for each Group, assign summed values to new year_group_aggs dataframe
    year_group_aggs = year_data.groupby(COL_GROUP).agg(
        {COL_EC_VOTES: 'sum', COL_VOTES_COUNTED: 'sum', COL_STATE: 'count'})
    year_group_aggs_2 = year_data.groupby(COL_GROUP).agg({COL_ABBREV: ','.join})
    year_group_aggs_2.rename(columns={COL_ABBREV: COL_STATES_IN_GROUP}, inplace=True)
    year_group_aggs = year_group_aggs.join(year_group_aggs_2, how='outer')
    # add/derive/populate year, votes counted pct, and ec votes normalized columns
    year_group_aggs[COL_YEAR] = [year] * len(year_group_aggs)
    year_group_aggs[COL_VOTES_COUNTED_PCT] = (100 * year_group_aggs[COL_VOTES_COUNTED] / pop_total).round(decimals=2)
    year_group_aggs[COL_EC_VOTES_NORM] = (year_group_aggs[COL_VOTES_COUNTED] / pop_per_ec).round(decimals=2)
    year_group_aggs[COL_POP_PER_EC] = round(year_group_aggs[COL_VOTES_COUNTED] / year_group_aggs[COL_EC_VOTES])
    # unset index, rename columns, add year column
    year_group_aggs.reset_index(inplace=True)
    year_group_aggs.rename(columns={COL_STATE: COL_STATE_COUNT}, inplace=True)
    # add average weight column by dividing EC votes by popular votes and multiplying by national pop-per-EC factor
    year_group_aggs[COL_AVG_WEIGHT] = (pop_per_ec * year_group_aggs[COL_EC_VOTES] / year_group_aggs[COL_VOTES_COUNTED]).round(decimals=2)
    # add placeholder row for any Group that isn't represented 
    for group in GROUPS:
        if len(year_group_aggs.loc[year_group_aggs[COL_GROUP] == group]) == 0:
            year_group_aggs_bonus = pd.DataFrame([[group, year, 0, 0, 0, 0, 0, 0, 0, '']],
                columns=[COL_GROUP, COL_YEAR, COL_EC_VOTES, COL_VOTES_COUNTED, COL_VOTES_COUNTED_PCT, COL_EC_VOTES_NORM,
                         COL_POP_PER_EC, COL_AVG_WEIGHT, COL_STATE_COUNT, COL_STATES_IN_GROUP])
            year_group_aggs = pd.concat([year_group_aggs, year_group_aggs_bonus], ignore_index=True, sort=False)
    # append year_group_aggs to group_aggs_by_year
    group_aggs_by_year = pd.concat([group_aggs_by_year, year_group_aggs], ignore_index=True, sort=False)
    
    
    ### LEGACY ###
    # aggregate EC votes and popular votes for each Group, assign summed values to new year_agg dataframe
    year_agg = year_data.groupby(COL_GROUP).agg({COL_EC_VOTES: 'sum', COL_VOTES_COUNTED: 'sum'})
    # add Average weight column by dividing EC votes by popular votes and multiplying by national pop-per-EC factor
    year_agg[year] = pop_per_ec * year_agg[COL_EC_VOTES] / year_agg[COL_VOTES_COUNTED]

    # add Total row to end of of year_agg
    total_row = pd.DataFrame([['Total', ec_total, pop_total, 1.0]], 
                             columns=[COL_GROUP, COL_EC_VOTES, COL_VOTES_COUNTED, year])
    total_row = total_row.set_index(COL_GROUP)
    year_agg = year_agg.append(total_row)

    # combine year_agg into groups_by_year
    #pd.concat([groups_by_year, year_agg], axis=1)
    #pd.merge(groups_by_year, year_agg, left_index=True, right_index=True, how='outer')
    #groups_by_year = groups_by_year.join(year_agg, how='outer')

    # extract avg_weight column into its own dataframe, rename column to be simply the year
    avg_weight_df = year_agg.drop([COL_EC_VOTES, COL_VOTES_COUNTED], axis=1)
    avg_weight_by_year = avg_weight_by_year.join(avg_weight_df, how='outer')
    
    
    # increment to next election
    year = year + 4


PIVOT_ON_YEAR_CSV = f"{gen_data_dir}/{PIVOT_ON_YEAR_CSV}"
TOTALS_BY_YEAR_CSV = f"{gen_data_dir}/{TOTALS_BY_YEAR_CSV}"
GROUP_AGGS_BY_YEAR_CSV = f"{gen_data_dir}/{GROUP_AGGS_BY_YEAR_CSV}"
AVG_WEIGHT_BY_YEAR_CSV = f"{gen_data_dir}/{AVG_WEIGHT_BY_YEAR_CSV}"

print(f"Rows in {PIVOT_ON_YEAR_CSV}: {len(pivot_on_year)}")
print(f"{pivot_on_year}")
print(f"Rows in {TOTALS_BY_YEAR_CSV}: {len(totals_by_year)}")
print(f"{totals_by_year}")
print(f"Rows in {GROUP_AGGS_BY_YEAR_CSV}: {len(group_aggs_by_year)}")
print(f"{group_aggs_by_year}")
print(f"Rows in {AVG_WEIGHT_BY_YEAR_CSV}: {len(avg_weight_by_year)}")
print(f"{avg_weight_by_year}")


if WRITE_TO_CSV:
    if not os.path.exists(gen_data_dir):
        os.makedirs(gen_data_dir)

    # write pivot_on_year, totals_by_year, group_aggs_by_year to file
    pivot_on_year.to_csv(PIVOT_ON_YEAR_CSV)
    totals_by_year.to_csv(TOTALS_BY_YEAR_CSV)
    group_aggs_by_year.to_csv(GROUP_AGGS_BY_YEAR_CSV)


    ### LEGACY ###
    # write groups_by_year to file
    #groups_by_year.to_csv(GROUPS_BY_YEAR_CSV)

    # rename Total column and write avg_weight_by_year to file
    avg_weight_by_year.rename(index={'Total': 'Nat\'l Average'}, inplace=True)
    avg_weight_by_year.to_csv(AVG_WEIGHT_BY_YEAR_CSV)
