import math
import numpy as np
import pandas as pd
import plotly.express as px

from data_processor.functions import get_era_for_year, map_to_subdir, get_description_for_group_key
from metadata import Columns, DataDirs, FigDimensions, GROUPS_FOR_DIR, GROUP_COLORS, YEAR_0, YEAR_N


cols = Columns()
ddirs = DataDirs()
fig_dims = FigDimensions()


def build_ivw_by_state_map(data_obj, groups_dir, max_small, color_field, fig_width=None, frame=None):
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

    # log_vote_weight_ser = pivot_on_year_df[cols.LOG_VOTE_WEIGHT].replace([np.inf, -np.inf], np.nan).dropna()
    # log_vote_weight_min = log_vote_weight_ser.min()
    # log_vote_weight_max = log_vote_weight_ser.max()
    # vote_weight_ser = pivot_on_year_df[cols.VOTE_WEIGHT].replace([np.inf, -np.inf], np.nan).dropna()
    # vote_weight_min = vote_weight_ser.min()
    # vote_weight_max = vote_weight_ser.max()

    # display metadata
    custom_data = [cols.STATE, cols.GROUP, cols.YEAR, cols.VOTES_COUNTED, cols.EC_VOTES, cols.VOTE_WEIGHT, cols.POP_PER_EC_SHORT, cols.EC_VOTES_NORM, 
                    cols.VOTES_COUNTED_NORM]
    # map_title = f'{year} presidential election: Vote weight per person per state'
    base_fig_title = 'Vote Weight Per Person Per State'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        fig_title = f'{base_fig_title}: {YEAR_0} - {YEAR_N}'

    if color_field == cols.LOG_VOTE_WEIGHT:
        fig = px.choropleth(pivot_on_year_df, locations=cols.ABBREV, color=color_field, title=fig_title, 
                            locationmode='USA-states', scope="usa", custom_data=custom_data,
                            animation_frame=cols.YEAR, # ignored if df is for single year
                            color_continuous_scale=px.colors.diverging.BrBG[::-1], color_continuous_midpoint=0,
                            # range_color=[-1.0, pivot_on_single_year[cols.LOG_VOTE_WEIGHT].max()],
                            # range_color=[log_vote_weight_min, log_vote_weight_max],  
                            width=fig_width, height=fig_height)
        # TODO apply what I learned doing log_y line charts here
        fig.update_layout(
            coloraxis_colorbar=dict(tickvals=[-2.303, -1.609, -1.109, -0.693, -0.357, 0, 0.405, 0.916, 1.386, 1.792, 2.197],
                                    ticktext=['0.1', '0.2', '0.33', '0.5', '0.7', '1.0', '1.5', '2.5', '4', '6', '9']))
    elif color_field == cols.GROUP:
        fig = px.choropleth(pivot_on_year_df, locations=cols.ABBREV, color=cols.GROUP, 
                            locationmode='USA-states', scope="usa", custom_data=custom_data,
                            animation_frame=cols.YEAR, animation_group=cols.GROUP, # ignored if df is for single year
                            color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                            width=fig_width, height=fig_height)

    # TODO where are x, y, and customdata actually defined, in fig? I'd like to avoid these redundant key-value mappings and use an f-string for this but not sure how
    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>%{customdata[0]}</b> (%{customdata[2]})<br>",
            "Popular vote: <b>%{customdata[3]:,}</b>",
            "Electoral College votes: <b>%{customdata[4]}</b>",
            "Vote Weight: <b>%{customdata[5]:.2f}</b>",
            "Population per EC vote: <b>%{customdata[6]:,}</b>",
            "Group: <b>%{customdata[1]}</b>",
            "<br><b>Normalized to nat'l average:</b>",
            "%{customdata[3]:,} pop votes => %{customdata[7]:.2f} EC votes",
            "%{customdata[4]} EC votes => %{customdata[8]:,} pop votes",
        ])
    )

    return fig
