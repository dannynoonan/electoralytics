import numpy as np
import pandas as pd

from metadata import Columns, DataDirs, DataFiles, DATA_DIR_TO_SMALL_GROUP_LABELS


cols = Columns()
ddirs = DataDirs()
dfiles = DataFiles()


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
            subdir = f"{ddirs.GEN}/{ddirs.ACW}/{ddirs.SMALL_4}"
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
            subdir = f"{ddirs.GEN}/{ddirs.ACW}/{ddirs.SMALL_4}"
        pivot_on_year_csv_path = f"{ddirs.BASE}/{subdir}/{dfiles.PIVOT_ON_YEAR}"
        small_subdir = subdir.split('/')[-1]

        # if df for subdir is already loaded and we're not updating, then we're done
        if subdir in self.pivot_on_year_dfs and not update:
            return

        # load df from csv, make modifications to be shared by all downstream users
        print(f"loading {pivot_on_year_csv_path}")
        df = pd.read_csv(pivot_on_year_csv_path)
        df.drop('Unnamed: 0', axis=1, inplace=True)
        # rename specific columns and column values
        if small_subdir in DATA_DIR_TO_SMALL_GROUP_LABELS.keys():
            small_col_name = DATA_DIR_TO_SMALL_GROUP_LABELS[small_subdir]
            df.loc[df[cols.GROUP] == 'Small', cols.GROUP] = small_col_name
        df.rename(columns={cols.POP_PER_EC: cols.POP_PER_EC_SHORT}, inplace=True)
        # generate Vote Weight (log) column, workaround to choropleth lacking log color scale option
        df[cols.LOG_VOTE_WEIGHT] = np.log2(df[cols.VOTE_WEIGHT])

        # extract valid election years (for request validation)
        self.all_years = df[cols.YEAR].unique()
        # assign df to pivot_on_year_dfs at subdir 
        self.pivot_on_year_dfs[subdir] = df


    def melt_pivot_on_year(self, subdir=None, update=False):
        if not subdir:
            subdir = f"{ddirs.GEN}/{ddirs.ACW}/{ddirs.SMALL_4}"

        # if df for subdir is already loaded and we're not updating, then we're done
        if subdir in self.melted_ec_votes_pivot_dfs and not update:
            return

        # if source pivot_on_year_df is empty, we don't have a df to melt 
        if not subdir in self.pivot_on_year_dfs:
            print(f"failure to melt pivot_on_year_df for subdir '{subdir}', source df self.pivot_on_year_dfs[{subdir}] is empty")
            return

        print(f"melting self.pivot_on_year_dfs[{subdir}] into melted_ec_votes_pivot_dfs and melted_vote_count_pivot_dfs")

        # melt EC votes and EC votes normalized into the same column to create melted_ec_votes_pivot_dfs
        col_names = self.pivot_on_year_dfs[subdir].columns.values
        col_names = col_names[col_names != cols.EC_VOTES]
        col_names = col_names[col_names != cols.EC_VOTES_NORM]
        mod_pivot_on_year_df = self.pivot_on_year_dfs[subdir].rename(
            columns={cols.EC_VOTES: 'EC votes: Actual', cols.EC_VOTES_NORM: 'ECV: Adjusted for turnout'})
        
        melted_ec_votes_pivot_df = pd.melt(
            mod_pivot_on_year_df, 
            id_vars=col_names,
            var_name='Actual vs Adjusted EC votes^',
            value_name='EC votes^'
        )

        # assign df to melted_ec_votes_pivot_dfs at subdir 
        self.melted_ec_votes_pivot_dfs[subdir] = melted_ec_votes_pivot_df

        # melt Vote count and Vote count normalized into the same column to create melted_vote_count_pivot_dfs
        col_names = self.pivot_on_year_dfs[subdir].columns.values
        col_names = col_names[col_names != cols.VOTES_COUNTED]
        col_names = col_names[col_names != cols.VOTES_COUNTED_NORM]
        mod_pivot_on_year_df = self.pivot_on_year_dfs[subdir].rename(
            columns={cols.VOTES_COUNTED: 'Votes counted: Actual', cols.VOTES_COUNTED_NORM: 'Votes counted: Adjusted for weight'})

        melted_vote_count_pivot_df = pd.melt(
            mod_pivot_on_year_df, 
            id_vars=col_names,
            var_name='Actual vs Adjusted Vote count^',
            value_name='Vote count^'
        )

        # assign df to melted_vote_count_pivot_dfs at subdir 
        self.melted_vote_count_pivot_dfs[subdir] = melted_vote_count_pivot_df


    def load_group_aggs_by_year(self, subdir=None, update=False):
        if not subdir:
            subdir = f"{ddirs.GEN}/{ddirs.ACW}/{ddirs.SMALL_4}"
        group_aggs_by_year_csv_path = f"{ddirs.BASE}/{subdir}/{dfiles.GROUP_AGGS_BY_YEAR}"
        small_subdir = subdir.split('/')[-1]

        # if df for subdir is already loaded and we're not updating, then we're done
        if subdir in self.group_aggs_by_year_dfs and not update:
            return

        # load df from csv, make modifications to be shared by all downstream users
        print(f'loading {group_aggs_by_year_csv_path}')
        df = pd.read_csv(group_aggs_by_year_csv_path)
        df.drop('Unnamed: 0', axis=1, inplace=True)
        # rename specific columns and column values
        if small_subdir in DATA_DIR_TO_SMALL_GROUP_LABELS.keys():
            small_col_name = DATA_DIR_TO_SMALL_GROUP_LABELS[small_subdir]
            df.loc[df[cols.GROUP] == 'Small', cols.GROUP] = small_col_name
        df.rename(columns={cols.POP_PER_EC: cols.POP_PER_EC_SHORT}, inplace=True)

        # assign df to pivot_on_year_dfs at subdir 
        self.group_aggs_by_year_dfs[subdir] = df


    def load_swallowed_vote_sampler(self):
        print(f'loading {dfiles.SWALLOWED_VOTE_2020}')
        self.swallowed_vote_df = pd.read_csv(dfiles.SWALLOWED_VOTE_2020)
