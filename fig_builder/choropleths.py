import math
import numpy as np
import pandas as pd
import plotly.express as px

from data_processor.functions import get_era_for_year, map_to_subdir, get_description_for_group_key
from metadata import Columns, FigDimensions, GROUPS_FOR_DIR, GROUP_COLORS, YEAR_0, YEAR_N


cols = Columns()
fig_dims = FigDimensions()


def build_ivw_by_state_map(data_obj, groups_dir, max_small, fig_width=None, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    pivot_on_year_df = data_obj.state_vote_weights_pivot_dfs[subdir]

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] == frame]

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.crt(fig_width)

    # log_vote_weight_ser = pivot_on_year_df[cols.LOG_VOTE_WEIGHT].replace([np.inf, -np.inf], np.nan).dropna()
    # log_vote_weight_min = log_vote_weight_ser.min()
    # log_vote_weight_max = log_vote_weight_ser.max()
    # vote_weight_ser = pivot_on_year_df[cols.VOTE_WEIGHT].replace([np.inf, -np.inf], np.nan).dropna()
    # vote_weight_min = vote_weight_ser.min()
    # vote_weight_max = vote_weight_ser.max()

    # display metadata
    hover_data = {cols.YEAR: False, cols.ABBREV: False, cols.LOG_VOTE_WEIGHT: False, cols.GROUP: True,
                cols.VOTES_COUNTED: True, cols.EC_VOTES: True, cols.VOTE_WEIGHT: True, cols.POP_PER_EC_SHORT: True, 
                cols.EC_VOTES_NORM: True}
    # map_title = f'{year} presidential election: Vote weight per person per state'
    base_fig_title = 'Vote Weight Per Person Per State'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        fig_title = f'{base_fig_title}: {YEAR_0} - {YEAR_N}'

    fig = px.choropleth(pivot_on_year_df, locations=cols.ABBREV, color=cols.LOG_VOTE_WEIGHT,
                        locationmode='USA-states', scope="usa", hover_name=cols.STATE, hover_data=hover_data, 
                        animation_frame=cols.YEAR, # ignored if df is for single year
                        color_continuous_scale=px.colors.diverging.BrBG[::-1], color_continuous_midpoint=0,
                        # range_color=[-1.0, pivot_on_single_year[cols.LOG_VOTE_WEIGHT].max()],
                        # range_color=[log_vote_weight_min, log_vote_weight_max],  
                        title=fig_title, width=fig_width, height=fig_height)

    fig.update_layout(
        coloraxis_colorbar=dict(tickvals=[-2.303, -1.609, -1.109, -0.693, -0.357, 0, 0.405, 0.916, 1.386, 1.792, 2.197],
                                ticktext=['0.1', '0.2', '0.33', '0.5', '0.7', '1.0', '1.5', '2.5', '4', '6', '9']))

    # if write_html:
    #     # apply_animation_settings(fig, base_fig_title=base_fig_title)

    #     fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = FRAME_RATE
    #     fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 500
            
    #     for button in fig.layout.updatemenus[0].buttons:
    #         button["args"][1]["frame"]["redraw"] = True
            
    #     for step in fig.layout.sliders[0].steps:
    #         step["args"][1]["frame"]["redraw"] = True

    #     for k in range(len(fig.frames)):
    #         year = 1828 + (k*4)
    #         era = get_era_for_year(year)
    #         fig.frames[k]['layout'].update(title_text=f'{base_fig_title}: {year} ({era})')

    #     fig.write_html('ivw_by_state_map_anim.html')

    return fig


def build_state_groups_map(data_obj, groups_dir, max_small, fig_width=None, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    pivot_on_year_df = data_obj.state_vote_weights_pivot_dfs[subdir]
    groups = GROUPS_FOR_DIR[groups_dir]

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] == frame]

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.crt(fig_width)

    # generate cols.LOG_VOTE_WEIGHT column, workaround to manually create log color scale
    # pivot_on_single_year[cols.LOG_VOTE_WEIGHT] = np.log2(pivot_on_single_year[cols.VOTE_WEIGHT])

    # display metadata
    hover_data = {cols.YEAR: False, cols.ABBREV: False, cols.GROUP: True, cols.VOTES_COUNTED: True, 
              cols.EC_VOTES: True, cols.VOTE_WEIGHT: True, cols.POP_PER_EC_SHORT: True, cols.EC_VOTES_NORM: True}
    base_fig_title = get_description_for_group_key(groups_dir)
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        fig_title = f'{base_fig_title}: {YEAR_0} - {YEAR_N}'

    fig = px.choropleth(pivot_on_year_df, locations=cols.ABBREV, color=cols.GROUP, 
                        locationmode='USA-states', scope="usa", hover_name=cols.STATE, hover_data=hover_data, 
                        animation_frame=cols.YEAR, animation_group=cols.GROUP, # ignored if df is for single year
                        color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                        title=fig_title, width=fig_width, height=fig_height)

    return fig