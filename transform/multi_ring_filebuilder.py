import pandas as pd
import numpy as np

from electoralytics.metadata import THE_ONE_RING_CSV, PIVOT_ON_YEAR_CSV, TOTALS_BY_YEAR_CSV, GROUP_AGGS_BY_YEAR_CSV



# load electoral college data
the_one_ring = pd.read_csv(THE_ONE_RING_CSV)

### TRANSFORM CSV DATA ###
# files to output: 
# * groups_by_year 
# * avg_weight_by_year 
# * silder_pivot 

# metadata
groups = pd.Series(np.array(['Small', 'Confederate', 'Border', 'Northeast', 'Midwest', 'West', 'Total']))
COL_ABBREV = 'Abbrev'
COL_STATE = 'State'
COL_GROUP = 'Group'
COL_YEAR = 'Year'
COL_EC_VOTES = 'EC votes'
COL_VOTES_COUNTED = 'Votes counted'
COL_VOTE_WEIGHT = 'Vote weight'
COL_AVG_WEIGHT = 'Average weight'
COL_PARTY = 'Party'
COL_POP_PER_EC = 'Population per EC vote'
COL_STATE_COUNT = 'State count'
COL_MOST_EC_VOTES = 'Most EC votes'
COL_VOTES_COUNTED_PCT = 'Votes counted %'

# initialize new data frames
pivot_on_year = pd.DataFrame(
    columns=[COL_ABBREV, COL_STATE, COL_GROUP, COL_YEAR, COL_EC_VOTES, COL_VOTES_COUNTED, 
             COL_VOTES_COUNTED_PCT, COL_VOTE_WEIGHT, COL_PARTY])
group_aggs_by_year = pd.DataFrame(
    columns=[COL_GROUP, COL_YEAR, COL_EC_VOTES, COL_VOTES_COUNTED, COL_AVG_WEIGHT, COL_STATE_COUNT])
totals_by_year = pd.DataFrame(columns=[COL_YEAR, COL_EC_VOTES, COL_VOTES_COUNTED, COL_POP_PER_EC, COL_MOST_EC_VOTES])

### LEGACY ###
avg_weight_by_year = pd.DataFrame({COL_GROUP: groups}) 
avg_weight_by_year = avg_weight_by_year.set_index(COL_GROUP)
# groups_by_year = pd.DataFrame({COL_GROUP: groups}) 
# groups_by_year = groups_by_year.set_index(COL_GROUP)

# begin iterating through years in the_one_ring
year = 1828
while year <= 2016:

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
    year_data = year_data.set_index(COL_ABBREV)

    
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
    year_data.loc[year_data[COL_EC_VOTES] <= 4, COL_GROUP] = 'Small'


    # DF 1: assemble year_pivot to append to pivot_on_year
    year_pivot = year_data
    # add and populate year and votes counted pct columns
    year_pivot[COL_YEAR] = [year] * len(year_pivot.index)
    year_pivot[COL_VOTES_COUNTED_PCT] = (year_pivot[COL_VOTES_COUNTED] / pop_total) * 100
    # unset index so we can append 
    year_pivot.reset_index(inplace=True)
    # add placeholder row for any Group that isn't represented 
    if len(year_pivot.loc[year_pivot['Group'] == 'West']) == 0:
        year_pivot_bonus = pd.DataFrame([['', '', 'West', year, 0, 0, 0, 0, '']],
            columns=[COL_ABBREV, COL_STATE, COL_GROUP, COL_YEAR, COL_EC_VOTES, COL_VOTES_COUNTED, 
                     COL_VOTES_COUNTED_PCT, COL_VOTE_WEIGHT, COL_PARTY])
        year_pivot = pd.concat([year_pivot, year_pivot_bonus], ignore_index=True, sort=False)
    # append year_pivot to pivot_on_year
    pivot_on_year = pd.concat([pivot_on_year, year_pivot], ignore_index=True, sort=False)
        
        
    # DF 2: init year_totals to append to totals_by_year
    year_totals = pd.DataFrame([[year, ec_total, pop_total, pop_per_ec, year_data[COL_EC_VOTES].max()]],
                               columns=[COL_YEAR, COL_EC_VOTES, COL_VOTES_COUNTED, COL_POP_PER_EC, COL_MOST_EC_VOTES])
    totals_by_year = pd.concat([totals_by_year, year_totals], ignore_index=True, sort=False)  

    
    # DF 3: aggregate EC votes and popular votes for each Group, assign summed values to new year_agg dataframe
    year_group_aggs = year_data.groupby(COL_GROUP).agg(
        {COL_EC_VOTES: 'sum', COL_VOTES_COUNTED: 'sum', COL_STATE: 'count'})
    # unset index, rename columns, add year column
    year_group_aggs.reset_index(inplace=True)
    year_group_aggs.rename(columns={COL_STATE: COL_STATE_COUNT}, inplace=True)
    year_group_aggs[COL_YEAR] = [year] * len(year_group_aggs)
    # add average weight column by dividing EC votes by popular votes and multiplying by national pop-per-EC factor
    year_group_aggs[COL_AVG_WEIGHT] = pop_per_ec * year_group_aggs[COL_EC_VOTES] / year_group_aggs[COL_VOTES_COUNTED]
    # add placeholder row for any Group that isn't represented 
    if len(year_group_aggs.loc[year_group_aggs['Group'] == 'West']) == 0:
        year_group_aggs_bonus = pd.DataFrame([['West', year, 0, 0, 0, 0]],
            columns=[COL_GROUP, COL_YEAR, COL_EC_VOTES, COL_VOTES_COUNTED, COL_AVG_WEIGHT, COL_STATE_COUNT])
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


# write pivot_on_year, totals_by_year, group_aggs_by_year to file
pivot_on_year.to_csv(PIVOT_ON_YEAR_CSV)
totals_by_year.to_csv(TOTALS_BY_YEAR_CSV)
group_aggs_by_year.to_csv(GROUP_AGGS_BY_YEAR_CSV)


### LEGACY ###
# write groups_by_year to file
#groups_by_year.to_csv(GROUPS_BY_YEAR_CSV)

# rename Total column and write avg_weight_by_year to file
avg_weight_by_year = avg_weight_by_year.rename(index={'Total': 'Nat\'l Average'})
avg_weight_by_year.to_csv(AVG_WEIGHT_BY_YEAR_CSV)
