import pandas as pd

from metadata import Columns, DataDirs, YEAR_0, FRAME_RATE, GROUP_ALT_COLORS


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
        # max_small should be explicitly set to 0, but catch-all just in case
        subdir = f"{subdir}/{ddirs.NO_SMALL}"
    return subdir


def get_description_for_group_key(group_key):
    if group_key == ddirs.ACW:
        return 'Civil War Groupings'
    if group_key == ddirs.CENSUS:
        return 'Regional Census Groupings'


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
