import pandas as pd

from metadata import Columns, DataDirs, YEAR_0, YEAR_N, FRAME_RATE, GROUP_COLORS, GROUP_ALT_COLORS, GROUPS_COL_FOR_DIR


# disable unhelpful 'SettingWithCopyWarnings'
pd.options.mode.chained_assignment = None


cols = Columns()
ddirs = DataDirs()


def validate_input(year_input, all_years):
    year = int(year_input)
    if year in all_years:
        return year
    else:
        return -1


def map_to_subdir(groups_dir, max_small):
    subdir = f"{ddirs.GEN}/{groups_dir}"
    if max_small == 3:
        subdir = f"{subdir}/{ddirs.SMALL_3}"
    elif max_small == 4:
        subdir = f"{subdir}/{ddirs.SMALL_4}"
    elif max_small == 5:
        subdir = f"{subdir}/{ddirs.SMALL_5}"
    else:
        # if max_small not explicitly set, assume it is 0
        subdir = f"{subdir}/{ddirs.NO_SMALL}"
    return subdir


def flatten_state_color_map(all_states_meta_df, groups_dir):
    group_col = GROUPS_COL_FOR_DIR[groups_dir]

    state_color_map = {}
    for index, meta_row in all_states_meta_df.iterrows():
        state_color_map[meta_row[cols.STATE]] = GROUP_COLORS[meta_row[group_col]]

    return state_color_map



def get_era_for_year(year):
    if year <= 1860:
        return 'Antebellum Period'
    elif year == 1864:
        return 'Civil War'
    elif year <= 1876:
        return 'Reconstruction'
    elif year <= 1892:
        return 'Redemption / Early Jim Crow'
    elif year <= 1948:
        return 'Jim Crow Era'
    elif year <= 1964:
        return 'Late Jim Crow / Civil Rights Era'
    else:
        return 'Post Voting Rights Act'


def apply_animation_settings(fig, base_fig_title, frame_rate=None):
    if not frame_rate:
        frame_rate = FRAME_RATE

    fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = frame_rate
        
    for button in fig.layout.updatemenus[0].buttons:
        button["args"][1]["frame"]["redraw"] = True
        
    for step in fig.layout.sliders[0].steps:
        step["args"][1]["frame"]["redraw"] = True

    for k in range(len(fig.frames)):
        year = YEAR_0 + (k*4)
        era = get_era_for_year(year)
        fig.frames[k]['layout'].update(title_text=f'{base_fig_title}: {year} ({era})')

    # return fig


def append_state_vw_pivot_to_groups_aggs_df(state_vw_pivot_df, group_aggs_by_year_df, group_colors):
    # drop columns not being merged
    state_vw_pivot_df.drop([cols.GROUP, cols.PARTY, cols.LOG_VOTE_WEIGHT], axis=1, inplace=True)
    # rename columns to be consistent with group aggs cols
    state_vw_pivot_df.rename(columns={cols.ABBREV: cols.STATES_IN_GROUP, cols.STATE: cols.GROUP, cols.VOTE_WEIGHT: cols.AVG_WEIGHT},
                            inplace=True)
    state_vw_pivot_df[cols.STATE_COUNT] = 1  

    # concat single-state df to group aggs df
    group_aggs_by_year_df = pd.concat([group_aggs_by_year_df, state_vw_pivot_df], ignore_index=True, sort=False)

    return group_aggs_by_year_df


def fill_out_state_year_matrix(pivot_on_year_df, all_states_meta_df, groups_dir):
    group_col = GROUPS_COL_FOR_DIR[groups_dir]

    year = YEAR_0
    while year <= YEAR_N:
        # extract year into separate dataframe
        pivot_on_single_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] == year]

        # iterate thru each of the (eventual) 51 states, check if row exists yet
        for index, meta_row in all_states_meta_df.iterrows():
            state_in_year = pivot_on_single_year_df[pivot_on_single_year_df[cols.ABBREV] == meta_row[cols.ABBREV]]
            if len(state_in_year) == 0:
                # if no match for state in year, add row to pivot_on_year_df using state metadata, 0s, and blank spaces
                df = pd.DataFrame([[meta_row[cols.ABBREV], meta_row[cols.STATE], meta_row[group_col], year, 0, 0, 0, 0, 0, 0, 0, '']],
                            columns=[cols.ABBREV, cols.STATE, cols.GROUP, cols.YEAR, cols.EC_VOTES, cols.VOTES_COUNTED, cols.VOTES_COUNTED_NORM,
                                    cols.VOTES_COUNTED_PCT, cols.EC_VOTES_NORM, cols.POP_PER_EC, cols.VOTE_WEIGHT, cols.PARTY])
                pivot_on_year_df = pd.concat([pivot_on_year_df, df], ignore_index=True, sort=False)
        
        year = year + 4

    return pivot_on_year_df
