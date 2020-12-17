import pandas as pd

from metadata import (
    GEN_DATA_DIR, PIVOT_ON_YEAR_CSV, SWALLOWED_VOTE_2020_CSV,
    COL_ABBREV, COL_STATE, COL_GROUP, COL_YEAR, COL_EC_VOTES, COL_EC_VOTES_NORM, COL_VOTES_COUNTED, COL_VOTES_COUNTED_PCT, 
    COL_VOTE_WEIGHT, COL_POP_PER_EC, COL_POP_PER_EC_SHORT, COL_PARTY
)


PIVOT_ON_YEAR_CSV = f"{GEN_DATA_DIR}/{PIVOT_ON_YEAR_CSV}"


class DataObject():

    def __init__(self):
        self.pivot_on_year_df = None
        self.melted_pivot_on_year_df = None
        self.all_years = None
        self.swallowed_vote_df = None

    # load pivot_on_year data from csv
    def load_pivot_on_year(self):
        print(f'loading {PIVOT_ON_YEAR_CSV}')

        self.pivot_on_year_df = pd.read_csv(PIVOT_ON_YEAR_CSV)
        self.pivot_on_year_df.drop('Unnamed: 0', axis=1, inplace=True)
        # rename pop per EC vote
        self.pivot_on_year_df.rename(columns={COL_POP_PER_EC: COL_POP_PER_EC_SHORT}, inplace=True)

        # extract valid election years (for request validation)
        self.all_years = self.pivot_on_year_df[COL_YEAR].unique()

    def melt_pivot_on_year(self):
        print(f'melting {PIVOT_ON_YEAR_CSV}')

        pivot_on_year_mod = self.pivot_on_year_df.rename(
            columns={COL_EC_VOTES: 'EC votes: Actual', COL_EC_VOTES_NORM: 'ECV: Adjusted for population'})

        self.melted_pivot_on_year_df = pd.melt(
            pivot_on_year_mod, 
            id_vars=[COL_ABBREV, COL_STATE, COL_GROUP, COL_YEAR, COL_VOTES_COUNTED, COL_VOTES_COUNTED_PCT, COL_POP_PER_EC_SHORT,
                    COL_VOTE_WEIGHT, COL_PARTY],
            var_name='Actual vs Adjusted EC votes^',
            value_name='EC votes^'
        )

    def load_swallowed_vote_sampler(self):
        print(f'loading {SWALLOWED_VOTE_2020_CSV}')
        self.swallowed_vote_df = pd.read_csv(SWALLOWED_VOTE_2020_CSV)
  
