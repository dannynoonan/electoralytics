import math
import numpy as np
import pandas as pd
import plotly.express as px

from data_processor.functions import get_era_for_year, map_to_subdir, get_description_for_group_key, apply_animation_settings
from metadata import Columns, DataDirs, FigDimensions, GROUPS_FOR_DIR, GROUP_COLORS, YEAR_0, YEAR_N


cols = Columns()
ddirs = DataDirs()
fig_dims = FigDimensions()


def build_ivw_by_state_map(data_obj, groups_dir, max_small, color_field, fig_width=None, frame=None):
    print(f"in build_ivw_by_state_map, groups_dir {groups_dir}, max_small {max_small}")

    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    pivot_on_year_df = data_obj.state_vote_weights_pivot_dfs[subdir].copy()
    groups = GROUPS_FOR_DIR[groups_dir]

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] == frame]

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.crt(fig_width)

    # display metadata common to (or that doesn't interfere with) all display types
    base_fig_title = 'Impact Per Voter Per State'
    # base_fig_title = 'Vote Weight Per Person Per State'
    # custom_data enables dynamic variable substitution in hovertemplates for static frames
    custom_data = [cols.STATE, cols.GROUP, cols.YEAR, cols.VOTES_COUNTED, cols.EC_VOTES, cols.VOTE_WEIGHT, cols.POP_PER_EC, cols.EC_VOTES_NORM, 
                    cols.VOTES_COUNTED_NORM]
    # hover_data is the fallback plan for animations where custom_data doesn't work
    hover_data = {cols.ABBREV: False, cols.LOG_VOTE_WEIGHT: False, cols.GROUP: True, cols.YEAR: True, cols.VOTES_COUNTED: True, cols.EC_VOTES: True, 
                    cols.VOTE_WEIGHT: True, cols.POP_PER_EC: True, cols.EC_VOTES_NORM: True, cols.VOTES_COUNTED_NORM: True}
    
    # set fields and values that differ for static years (frame) vs animations (!frame)
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        fig_title = f'{base_fig_title}: {YEAR_0} - {YEAR_N}'

    # init figure with core properties
    if color_field == cols.LOG_VOTE_WEIGHT:
        # init figure where state color is determined by its vote weight (log value)
        fig = px.choropleth(pivot_on_year_df, locations=cols.ABBREV, color=color_field, title=fig_title, 
                            locationmode='USA-states', scope="usa", custom_data=custom_data,
                            hover_name=cols.STATE, hover_data=hover_data, animation_frame=cols.YEAR, # ignored if df is for single year
                            color_continuous_scale=px.colors.diverging.BrBG[::-1], color_continuous_midpoint=0,
                            width=fig_width, height=fig_height)
        # colorbar labels: calculate log values for weights so I can plot the familiar linear numbers on the color bar
        # TODO pretty sure this works around a plotly choropleth bug, open ticket or post to stackoverflow
        colorbar_labels = ['0.1', '0.2', '0.33', '0.5', '0.7', '1.0', '1.5', '2.5', '4', '6', '9']
        linear_vals = [float(x) for x in colorbar_labels]
        log_vals = [math.log(t, 2) for t in linear_vals]
        fig.update_layout(
            coloraxis_colorbar=dict(tickvals=log_vals, ticktext=colorbar_labels, title='IPV (log)'))

    elif color_field == cols.GROUP:
        # init figure where state is determined by its state group
        fig = px.choropleth(pivot_on_year_df, locations=cols.ABBREV, color=cols.GROUP, title=fig_title,
                            locationmode='USA-states', scope="usa", custom_data=custom_data,
                            hover_name=cols.STATE, hover_data=hover_data, animation_frame=cols.YEAR, animation_group=cols.GROUP, # ignored if df is for single year
                            color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                            width=fig_width, height=fig_height)

    # center title
    fig.update_layout(title_x=0.5)

    # apply animation settings
    if not frame:
        apply_animation_settings(fig, base_fig_title)

    # hovertemplate formatting and variable substitution using customdata
    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>%{customdata[0]}</b> (%{customdata[2]})<br>",
            "Popular vote: <b>%{customdata[3]:,}</b>",
            "Electoral College votes: <b>%{customdata[4]}</b>",
            "Impact per voter: <b>%{customdata[5]:.2f}</b>",
            "Population per EC vote: <b>%{customdata[6]:,}</b>",
            "Group: <b>%{customdata[1]}</b>",
            "<br><b>Normalized to nat'l average:</b>",
            "%{customdata[3]:,} pop votes => %{customdata[7]:.2f} EC votes",
            "%{customdata[4]} EC votes => %{customdata[8]:,} pop votes",
        ])
    )

    return fig
