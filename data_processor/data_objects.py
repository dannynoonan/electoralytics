import numpy as np
import pandas as pd

from metadata import (
    BASE_DATA_DIR, GEN_DATA_DIR, GEN_ALT_GROUP_DIR, GEN_NO_SMALL_DIR, GEN_ALT_GROUP_NO_SMALL_DIR,
    PIVOT_ON_YEAR_CSV, SWALLOWED_VOTE_2020_CSV, GROUP_AGGS_BY_YEAR_CSV,
    COL_ABBREV, COL_STATE, COL_GROUP, COL_YEAR, COL_EC_VOTES, COL_EC_VOTES_NORM, 
    COL_VOTES_COUNTED, COL_VOTES_COUNTED_NORM, COL_VOTES_COUNTED_PCT, COL_VOTE_WEIGHT, COL_LOG_VOTE_WEIGHT, 
    COL_POP_PER_EC, COL_POP_PER_EC_SHORT, COL_PARTY
)


class DataObject():

    def __init__(self):
        self.subdirs_loaded = []
        self.pivot_on_year_dfs = {}
        self.melted_ec_votes_pivot_dfs = {}
        self.melted_vote_count_pivot_dfs = {}
        self.group_aggs_by_year_dfs = {}
        self.all_years = None
        self.swallowed_vote_df = None


    def load_dfs_for_subdir(self, subdir=None):
        if not subdir:
            subdir = GEN_DATA_DIR
        if not subdir in self.subdirs_loaded:
            print(f"subdirs_loaded: '{self.subdirs_loaded}' does not include requested sudbdir '{subdir}', loading it now...")
            self.load_pivot_on_year(subdir=subdir)
            self.melt_pivot_on_year(subdir=subdir)
            self.load_group_aggs_by_year(subdir=subdir)
            self.subdirs_loaded.append(subdir)
            print(f"finished loading sudbdir '{subdir}'")


    # load pivot_on_year data from csv
    def load_pivot_on_year(self, subdir=None, update=False):
        if not subdir:
            subdir = GEN_DATA_DIR
        pivot_on_year_csv_path = f"{BASE_DATA_DIR}/{subdir}/{PIVOT_ON_YEAR_CSV}"

        # if df for subdir is already loaded and we're not updating, then we're done
        if subdir in self.pivot_on_year_dfs and not update:
            return

        # load df from csv, make modifications to be shared by all downstream users
        print(f"loading {pivot_on_year_csv_path}")
        df = pd.read_csv(pivot_on_year_csv_path)
        df.drop('Unnamed: 0', axis=1, inplace=True)
        # rename pop per EC vote
        df.rename(columns={COL_POP_PER_EC: COL_POP_PER_EC_SHORT}, inplace=True)
        # generate Vote Weight (log) column, workaround to choropleth lacking log color scale option
        df[COL_LOG_VOTE_WEIGHT] = np.log2(df[COL_VOTE_WEIGHT])

        # extract valid election years (for request validation)
        self.all_years = df[COL_YEAR].unique()
        # assign df to pivot_on_year_dfs at subdir 
        self.pivot_on_year_dfs[subdir] = df


    def melt_pivot_on_year(self, subdir=None, update=False):
        if not subdir:
            subdir = GEN_DATA_DIR

        # if df for subdir is already loaded and we're not updating, then we're done
        if subdir in self.melted_ec_votes_pivot_dfs and not update:
            return

        # if source pivot_on_year_df is empty, we don't have a df to melt 
        if not subdir in self.pivot_on_year_dfs:
            print(f"failure to melt pivot_on_year_df for subdir '{subdir}', source df self.pivot_on_year_dfs[{subdir}] is empty")
            return

        print(f"melting self.pivot_on_year_dfs[{subdir}] into melted_ec_votes_pivot_dfs and melted_vote_count_pivot_dfs")

        # melt EC votes and EC votes normalized into the same column to create melted_ec_votes_pivot_dfs
        cols = self.pivot_on_year_dfs[subdir].columns.values
        cols = cols[cols != COL_EC_VOTES]
        cols = cols[cols != COL_EC_VOTES_NORM]
        mod_pivot_on_year_df = self.pivot_on_year_dfs[subdir].rename(
            columns={COL_EC_VOTES: 'EC votes: Actual', COL_EC_VOTES_NORM: 'ECV: Adjusted for turnout'})
        
        melted_ec_votes_pivot_df = pd.melt(
            mod_pivot_on_year_df, 
            id_vars=cols,
            var_name='Actual vs Adjusted EC votes^',
            value_name='EC votes^'
        )

        # assign df to melted_ec_votes_pivot_dfs at subdir 
        self.melted_ec_votes_pivot_dfs[subdir] = melted_ec_votes_pivot_df

        # melt Vote count and Vote count normalized into the same column to create melted_vote_count_pivot_dfs
        cols = self.pivot_on_year_dfs[subdir].columns.values
        cols = cols[cols != COL_VOTES_COUNTED]
        cols = cols[cols != COL_VOTES_COUNTED_NORM]
        mod_pivot_on_year_df = self.pivot_on_year_dfs[subdir].rename(
            columns={COL_VOTES_COUNTED: 'Votes counted: Actual', COL_VOTES_COUNTED_NORM: 'Votes counted: Adjusted for weight'})

        melted_vote_count_pivot_df = pd.melt(
            mod_pivot_on_year_df, 
            id_vars=cols,
            var_name='Actual vs Adjusted Vote count^',
            value_name='Vote count^'
        )

        # assign df to melted_vote_count_pivot_dfs at subdir 
        self.melted_vote_count_pivot_dfs[subdir] = melted_vote_count_pivot_df


    def load_group_aggs_by_year(self, subdir=None, update=False):
        if not subdir:
            subdir = GEN_DATA_DIR
        group_aggs_by_year_csv_path = f"{BASE_DATA_DIR}/{subdir}/{GROUP_AGGS_BY_YEAR_CSV}"

        # if df for subdir is already loaded and we're not updating, then we're done
        if subdir in self.group_aggs_by_year_dfs and not update:
            return

        # load df from csv, make modifications to be shared by all downstream users
        print(f'loading {group_aggs_by_year_csv_path}')
        group_aggs_by_year_df = pd.read_csv(group_aggs_by_year_csv_path)
        group_aggs_by_year_df.drop('Unnamed: 0', axis=1, inplace=True)
        # rename pop per EC vote
        group_aggs_by_year_df.rename(columns={COL_POP_PER_EC: COL_POP_PER_EC_SHORT}, inplace=True)

        # assign df to pivot_on_year_dfs at subdir 
        self.group_aggs_by_year_dfs[subdir] = group_aggs_by_year_df


    def load_swallowed_vote_sampler(self):
        print(f'loading {SWALLOWED_VOTE_2020_CSV}')
        self.swallowed_vote_df = pd.read_csv(SWALLOWED_VOTE_2020_CSV)
