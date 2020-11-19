import pandas as pd
import numpy as np

from electoralytics.metadata import THE_ONE_RING_CSV, GROUPS_BY_YEAR_CSV, AVG_WEIGHT_BY_YEAR_CSV, ALL_YEARS_PIVOT_CSV



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

# initialize new data frames
groups_by_year = pd.DataFrame({COL_GROUP: groups})
avg_weight_by_year = pd.DataFrame({COL_GROUP: groups})
all_years_pivot = pd.DataFrame(columns=[COL_ABBREV, COL_STATE, COL_GROUP, COL_YEAR, COL_EC_VOTES, COL_VOTES_COUNTED,
                                       COL_VOTE_WEIGHT, COL_PARTY])

# set key/index for rows
groups_by_year = groups_by_year.set_index(COL_GROUP)
avg_weight_by_year = avg_weight_by_year.set_index(COL_GROUP)

year = 1828
while year <= 2016:

    # column names for current year
    ec_votes_col = f'{year} {COL_EC_VOTES}'
    votes_counted_col = f'{year} {COL_VOTES_COUNTED}'
    vote_weight_col = f'{year} {COL_VOTE_WEIGHT}'
    avg_weight_col = f'{year} {COL_AVG_WEIGHT}'
    party_col = f'{year} {COL_PARTY}'

    # extract electoral college data for year
    year_data = the_one_ring[[COL_ABBREV, COL_STATE, COL_GROUP, ec_votes_col, votes_counted_col, 
                              vote_weight_col, party_col]]

    # set state abbrev as key/index for each row
    year_data = year_data.set_index(COL_ABBREV)

    # DATA CLEANSING
    # remove states lacking vote weight for this year 
    year_data = year_data[pd.notnull(year_data[vote_weight_col])]

    # explicitly set type of votes counted and vote margin data to int (not sure why this isn't automatic)
    year_data[[votes_counted_col]] = year_data[[votes_counted_col]].astype(int)

    # extract US totals data before removing US column
    ec_total = year_data.loc['US'][ec_votes_col]
    pop_total = year_data.loc['US'][votes_counted_col]
    # calculate average popular vote per EC vote
    pop_per_ec = round(pop_total / ec_total)
    # remove US column
    year_data = year_data.drop('US')

    # map states having 4 or fewer electoral college votes to 'Small' Group
    year_data.loc[year_data[ec_votes_col] <= 4, COL_GROUP] = 'Small'


    # DATA PIVOTING: all_years_pivot
    # init table for this year
    year_pivot = year_data.rename(columns={ec_votes_col: COL_EC_VOTES, votes_counted_col: COL_VOTES_COUNTED, 
                                           vote_weight_col: COL_VOTE_WEIGHT, party_col: COL_PARTY})
    year_pivot[COL_YEAR] = [year] * len(year_pivot.index)

    # unset index so we can append to all_years_pivot
    year_pivot.reset_index(inplace=True)

    # append year_pivot to all_years_pivot
    all_years_pivot = pd.concat([all_years_pivot, year_pivot], ignore_index=True, sort=False)


    # DATA AGGREGATION: groups_by_year, avg_weight_by_year
    # aggregate EC votes and popular votes for each Group, assign summed values to new year_agg dataframe
    year_agg = year_data.groupby(COL_GROUP).agg({ec_votes_col: 'sum', votes_counted_col: 'sum'})
    # add Average weight column by dividing EC votes by popular votes and multiplying by national pop-per-EC factor
    year_agg[avg_weight_col] = pop_per_ec * year_agg[ec_votes_col] / year_agg[votes_counted_col]
    # add Total row to end of of year_agg
    total_row = pd.DataFrame([['Total', ec_total, pop_total, 1.0]], 
                             columns=[COL_GROUP, ec_votes_col, votes_counted_col, avg_weight_col])
    total_row = total_row.set_index(COL_GROUP)
    # append total_row by merging dataframes
    year_agg = year_agg.append(total_row)

    # combine year_agg into groups_by_year
    #pd.concat([groups_by_year, year_agg], axis=1)
    #pd.merge(groups_by_year, year_agg, left_index=True, right_index=True, how='outer')
    groups_by_year = groups_by_year.join(year_agg, how='outer')

    # extract avg_weight column into its own dataframe, rename column to be simply the year
    avg_weight_df = year_agg.drop([ec_votes_col, votes_counted_col], axis=1)
    avg_weight_df = avg_weight_df.rename(columns={avg_weight_col: year})
    avg_weight_by_year = avg_weight_by_year.join(avg_weight_df, how='outer')

    # increment to next election
    year = year + 4

    
# write groups_by_year to file
groups_by_year.to_csv(GROUPS_BY_YEAR_CSV)

# rename Total column and write avg_weight_by_year to file
avg_weight_by_year = avg_weight_by_year.rename(index={'Total': 'Nat\'l Average'})
avg_weight_by_year.to_csv(AVG_WEIGHT_BY_YEAR_CSV)

# write all_years_pivot to file
all_years_pivot.to_csv(ALL_YEARS_PIVOT_CSV)
