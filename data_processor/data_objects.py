import numpy as np
import pandas as pd

from metadata import Columns, DataDirs, DataFiles, DATA_DIR_TO_SMALL_GROUP_LABELS


cols = Columns()
ddirs = DataDirs()
dfiles = DataFiles()


class DataObject():

    def __init__(self):
        self.subdirs_loaded = []
        self.state_vote_weights_pivot_dfs = {}
        self.melted_ec_votes_pivot_dfs = {}
        self.melted_vote_count_pivot_dfs = {}
        self.group_agg_weights_pivot_dfs = {}
        self.all_years = None
        self.all_states_meta_df = None
        self.abbrevs_to_states = None
        self.totals_by_year_df = None
        self.census_diff_2020_df = None
        self.swallowed_vote_df = None


    def load_dfs_for_subdir(self, subdir=None):
        """
        kicks off the loading of several csv files into df memory based on subdir
        """
        if not subdir:
            subdir = f"{ddirs.GEN}/{ddirs.ACW}/{ddirs.SMALL_4}"
        if not subdir in self.subdirs_loaded:
            print(f"subdirs_loaded: '{self.subdirs_loaded}' does not include requested sudbdir '{subdir}', loading it now...")
            self.load_state_vote_weights_pivot(subdir=subdir)
            self.melt_state_vote_weights_pivot(subdir=subdir)
            self.load_group_agg_weights_pivot(subdir=subdir)
            self.subdirs_loaded.append(subdir)
            print(f"finished loading sudbdir '{subdir}'")


    def load_state_vote_weights_pivot(self, subdir=None):
        """
        load state_vote_weights_pivot data for subdir from csv into df, also set all_years
        """
        if not subdir:
            subdir = f"{ddirs.GEN}/{ddirs.ACW}/{ddirs.SMALL_4}"
        state_vote_weights_pivot_csv_path = f"{ddirs.BASE}/{subdir}/{dfiles.STATE_VOTE_WEIGHTS_PIVOT}"
        small_subdir = subdir.split('/')[-1]

        # if df for subdir is already loaded then we're done
        if subdir in self.state_vote_weights_pivot_dfs:
            return

        # load df from csv, make modifications to be shared by all downstream users
        print(f"loading {state_vote_weights_pivot_csv_path}")
        df = pd.read_csv(state_vote_weights_pivot_csv_path)
        df.drop('Unnamed: 0', axis=1, inplace=True)
        # rename specific columns and column values
        if small_subdir in DATA_DIR_TO_SMALL_GROUP_LABELS.keys():
            small_col_name = DATA_DIR_TO_SMALL_GROUP_LABELS[small_subdir]
            df.loc[df[cols.GROUP] == 'Small', cols.GROUP] = small_col_name
        # df.rename(columns={cols.POP_PER_EC: cols.POP_PER_EC_SHORT}, inplace=True)
        # generate log columns, workaround to colorscales lacking log option
        df[cols.LOG_VOTE_WEIGHT] = np.log2(df[cols.VOTE_WEIGHT])
        df[cols.LOG_EC_VOTES] = np.log10((df[cols.EC_VOTES]))

        # extract valid election years (for request validation)
        self.all_years = df[cols.YEAR].unique()
        # assign df to state_vote_weights_pivot_dfs at subdir 
        self.state_vote_weights_pivot_dfs[subdir] = df


    def get_single_state_vote_weight_pivot(self, state_abbrev, subdir=None):
        """
        extract single_state_vw_pivot df for state_abbrev from state_vote_weights_pivot_df 
        """
        if not subdir:
            subdir = f"{ddirs.GEN}/{ddirs.ACW}/{ddirs.SMALL_4}"
        if not subdir in self.state_vote_weights_pivot_dfs:
            self.load_state_vote_weights_pivot(subdir=subdir)

        state_vote_weights_pivot_df = self.state_vote_weights_pivot_dfs[subdir]
        single_state_vw_pivot_df = state_vote_weights_pivot_df.loc[state_vote_weights_pivot_df[cols.ABBREV] == state_abbrev]

        return single_state_vw_pivot_df


    def load_census_diff_2020(self):
        """
        load census_diff_2020 data from csv into df and transform each in same fashion as normal election years
        """
        # only load if not already set
        if self.census_diff_2020_df is not None:
            return

        census_diff_2020_pivot_csv_path = f"{ddirs.BASE}/{dfiles.CENSUS_DIFF_2020_PIVOT}"

        # load df from csv, make modifications to be shared by all downstream users
        print(f"loading {census_diff_2020_pivot_csv_path}")
        df = pd.read_csv(census_diff_2020_pivot_csv_path)
        # generate log columns, workaround to colorscales lacking log option
        df[cols.LOG_VOTE_WEIGHT] = np.log2(df[cols.VOTE_WEIGHT])
        df[cols.LOG_EC_VOTES] = np.log10((df[cols.EC_VOTES]))

        # assign df to census_diff_2020_df 
        self.census_diff_2020_df = df


    def melt_state_vote_weights_pivot(self, subdir=None):
        """
        transform single_state_vw_pivot for subdir into two new versions where columns are melted on (1) ec votes and (2) vote count
        """
        if not subdir:
            subdir = f"{ddirs.GEN}/{ddirs.ACW}/{ddirs.SMALL_4}"

        # if df for subdir is already loaded then we're done
        if subdir in self.melted_ec_votes_pivot_dfs:
            return

        # if source state_vote_weights_pivot_df is empty, we don't have a df to melt 
        if not subdir in self.state_vote_weights_pivot_dfs:
            print(f"failure to melt state_vote_weights_pivot_df for subdir '{subdir}', source df self.state_vote_weights_pivot_dfs[{subdir}] is empty")
            return

        print(f"melting self.state_vote_weights_pivot_dfs[{subdir}] into melted_ec_votes_pivot_dfs and melted_vote_count_pivot_dfs")

        # melt EC votes and EC votes normalized into the same column to create melted_ec_votes_pivot_dfs
        col_names = self.state_vote_weights_pivot_dfs[subdir].columns.values
        ec_mod_df = self.state_vote_weights_pivot_dfs[subdir].copy()
        ec_mod_df['EC Votes: Actual'] = ec_mod_df[cols.EC_VOTES]
        ec_mod_df['ECV: Adjusted for Turnout'] = ec_mod_df[cols.EC_VOTES_NORM]
        melted_ec_votes_pivot_df = pd.melt(
            ec_mod_df, 
            id_vars=col_names,
            var_name='Actual vs Adjusted EC Votes*',
            value_name='EC Votes*'
        )
        # assign df to melted_ec_votes_pivot_dfs at subdir 
        self.melted_ec_votes_pivot_dfs[subdir] = melted_ec_votes_pivot_df

        # melt Vote count and Vote count normalized into the same column to create melted_vote_count_pivot_dfs
        col_names = self.state_vote_weights_pivot_dfs[subdir].columns.values
        vc_mod_df = self.state_vote_weights_pivot_dfs[subdir].copy()
        vc_mod_df['Popular Vote: Actual'] = vc_mod_df[cols.VOTES_COUNTED]
        vc_mod_df['Pop Vote: Adjusted for Voter Weight'] = vc_mod_df[cols.VOTES_COUNTED_NORM]
        melted_vote_count_pivot_df = pd.melt(
            vc_mod_df, 
            id_vars=col_names,
            var_name='Actual vs Adjusted Popular Vote*',
            value_name='Popular Vote*'
            # var_name='Actual vs Adjusted Vote count*',
            # value_name='Vote count*'
        )
        # assign df to melted_vote_count_pivot_dfs at subdir 
        self.melted_vote_count_pivot_dfs[subdir] = melted_vote_count_pivot_df


    def load_group_agg_weights_pivot(self, subdir=None):
        """
        load group_agg_weights_pivot data for subdir from csv into df
        """
        if not subdir:
            subdir = f"{ddirs.GEN}/{ddirs.ACW}/{ddirs.SMALL_4}"
        group_agg_weights_pivot_csv_path = f"{ddirs.BASE}/{subdir}/{dfiles.GROUP_AGG_WEIGHTS_PIVOT}"
        small_subdir = subdir.split('/')[-1]

        # if df for subdir is already loaded and we're not updating, then we're done
        if subdir in self.group_agg_weights_pivot_dfs:
            return

        # load df from csv, make modifications to be shared by all downstream users
        print(f'loading {group_agg_weights_pivot_csv_path}')
        df = pd.read_csv(group_agg_weights_pivot_csv_path)
        df.drop('Unnamed: 0', axis=1, inplace=True)
        # rename specific columns and column values
        if small_subdir in DATA_DIR_TO_SMALL_GROUP_LABELS.keys():
            small_col_name = DATA_DIR_TO_SMALL_GROUP_LABELS[small_subdir]
            df.loc[df[cols.GROUP] == 'Small', cols.GROUP] = small_col_name
        # df.rename(columns={cols.POP_PER_EC: cols.POP_PER_EC_SHORT}, inplace=True)

        # assign df to group_agg_weights_pivot_dfs at subdir 
        self.group_agg_weights_pivot_dfs[subdir] = df


    def load_all_states_meta(self):
        """
        load the_one_ring csv into df and extract all_states_meta into df
        """
        # TODO all_states_meta should be a separate csv generated by multi_ring_filebuilder
        print(f'loading {dfiles.THE_ONE_RING} to extract all_states_meta')
        the_one_ring = pd.read_csv(dfiles.THE_ONE_RING)
        all_states_meta_df = the_one_ring[[cols.ABBREV, cols.STATE, cols.ACW_GROUP, cols.CENSUS_GROUP]]
        self.all_states_meta_df = all_states_meta_df.loc[~(all_states_meta_df[cols.STATE] == 'United States')]


    def load_abbrevs_to_states(self):
        """
        extract abbrevs_to_states from all_states_meta 
        """
        if self.all_states_meta_df is None:
            self.load_all_states_meta()
        abbrevs_to_states_df = self.all_states_meta_df[[cols.ABBREV, cols.STATE]]
        self.abbrevs_to_states = {row[0]: row[1] for row in abbrevs_to_states_df.values}


    def load_totals_by_year(self):
        """
        load totals_by_year data from csv into df
        """
        print(f'loading {dfiles.TOTALS_BY_YEAR}')
        self.totals_by_year_df = pd.read_csv(dfiles.TOTALS_BY_YEAR)


    def load_swallowed_vote_sampler(self):
        """
        load swallowed_vote_sampler data from csv into df
        """
        print(f'loading {dfiles.SWALLOWED_VOTE_2020}')
        self.swallowed_vote_df = pd.read_csv(dfiles.SWALLOWED_VOTE_2020)
