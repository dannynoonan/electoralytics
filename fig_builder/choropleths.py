import math
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from data_processor.functions import get_era_for_year, map_to_subdir, apply_animation_settings
from metadata import Columns, DataDirs, FigDimensions, GROUPS_FOR_DIR, GROUP_COLORS, YEAR_0, YEAR_N


cols = Columns()
ddirs = DataDirs()
fig_dims = FigDimensions()


def build_vw_by_state_map(data_obj, groups_dir, max_small, color_col=None, fig_width=None, frame=None, alt_groups=[],
                          base_fig_title=None, show_era=True, show_year=True, display_ecv=False, groups_label=None, alt_data=None):
    """
    swiss army knife function for generating a px.choropleth map, color-shading states by group or along a data spectrum.
    supports static single-year plots or animations. 
    """
    subdir = map_to_subdir(groups_dir, max_small)
    groups = GROUPS_FOR_DIR[groups_dir].copy()

    # hackish hijack to support custom census comparison logic 
    census_diff_hilites = False
    diff_positive_df = None
    diff_negative_df = None
    if alt_data and alt_data == 'census_diff_2020':
        data_obj.load_census_diff_2020()
        pivot_on_year_df = data_obj.census_diff_2020_df.copy()
        if frame in [2020.2, 2020.3]:
            census_diff_hilites = True
        if frame in [2020.1, 2020.2]:
            frame = '2020'
        if frame in [2020.3, 2020.4]:
            frame = '2020 retrofit'
        range_color = [-1.5,1.5]
    else:
        data_obj.load_dfs_for_subdir(subdir)
        pivot_on_year_df = data_obj.state_vote_weights_pivot_dfs[subdir].copy()
        range_color = None

    if not color_col:
        color_col = cols.LOG_VOTE_WEIGHT

    # done in haste, this should probably be integrated into conditionals below
    if not groups_label:
        groups_label = color_col
        if groups_label == 'Group':
            groups_label = 'State Grouping'

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.crt(fig_width)

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] == frame]
        # extract subset of states to display for custom census comparison data
        if alt_data and alt_data == 'census_diff_2020':
            if census_diff_hilites:
                if color_col == cols.PARTY:
                    diff_positive_col = 'EC diff positive'
                    diff_negative_col = 'EC diff negative'
                else:
                    diff_positive_col = 'VW diff positive'
                    diff_negative_col = 'VW diff negative'
                diff_positive_df = pivot_on_year_df[pivot_on_year_df[diff_positive_col].notna()]
                diff_negative_df = pivot_on_year_df[pivot_on_year_df[diff_negative_col].notna()]
                pivot_on_year_df = diff_positive_df.append(diff_negative_df, ignore_index=True)

    if alt_groups:
        if 'slave_free' in alt_groups:
            pivot_on_year_df.loc[pivot_on_year_df[cols.GROUP] == 'Union', cols.GROUP] = 'Free'
            pivot_on_year_df.loc[pivot_on_year_df[cols.GROUP] == 'Confederate', cols.GROUP] = 'Slave'
            pivot_on_year_df.loc[pivot_on_year_df[cols.GROUP] == 'Border', cols.GROUP] = 'Slave'
            # groups = ['Free', 'Slave', 'Small']
            groups = ['Free', 'Slave', 'Small', 'Small (3-5 ECV)']
            # remove any rows added by other processes
            pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.GROUP].isin(groups)]
        if 'split_small' in alt_groups:
            pivot_on_year_df.loc[pivot_on_year_df[cols.EC_VOTES] <= 5, cols.GROUP] = '4-5 ECV'
            pivot_on_year_df.loc[pivot_on_year_df[cols.EC_VOTES] == 3, cols.GROUP] = '3 ECV'
            groups.extend(['3 ECV', '4-5 ECV'])
        if 'ecv_only' in alt_groups:
            pivot_on_year_df.loc[pivot_on_year_df[cols.EC_VOTES] == 3, cols.GROUP] = '3 ECV'
            pivot_on_year_df.loc[pivot_on_year_df[cols.EC_VOTES] >= 4, cols.GROUP] = '4-5 ECV'
            pivot_on_year_df.loc[pivot_on_year_df[cols.EC_VOTES] >= 6, cols.GROUP] = '6-8 ECV'
            pivot_on_year_df.loc[pivot_on_year_df[cols.EC_VOTES] >= 9, cols.GROUP] = '9-13 ECV'
            pivot_on_year_df.loc[pivot_on_year_df[cols.EC_VOTES] >= 14, cols.GROUP] = '14-19 ECV'
            pivot_on_year_df.loc[pivot_on_year_df[cols.EC_VOTES] >= 20, cols.GROUP] = '20+ ECV'
            groups = ['3 ECV', '4-5 ECV', '6-8 ECV', '9-13 ECV', '14-19 ECV', '20+ ECV']
            groups_label = 'EC Votes (Size)'

    # figure title depends on which field the color scale is based on
    if not base_fig_title:
        if color_col == cols.GROUP:
            if groups_dir == ddirs.ACW:
                base_fig_title = 'States Grouped By Civil War Alignment'
            else:
                base_fig_title = 'States Grouped By Regional Census'
        else:
            base_fig_title = 'States Color Shaded According to Voter Weight'
        
    # set fields and values that differ for static years (frame) vs animations (!frame)
    if frame:
        fig_title = base_fig_title
        if show_year:
            fig_title = f'{fig_title} ({frame})'
        if show_era:
            era = get_era_for_year(frame)
            fig_title = f'{fig_title}<br>{era}'
    else:
        fig_title = f'{base_fig_title} ({YEAR_0} - {YEAR_N})'

    # display metadata common to (or that doesn't interfere with) all display types
    # custom_data enables dynamic variable substitution in hovertemplates for static frames
    custom_data = [cols.STATE, cols.GROUP, cols.YEAR, cols.VOTES_COUNTED, cols.EC_VOTES, cols.VOTE_WEIGHT, cols.POP_PER_EC, cols.EC_VOTES_NORM, 
                    cols.VOTES_COUNTED_NORM]
    # hover_data is the fallback plan for animations where custom_data doesn't work
    hover_data = {cols.ABBREV: False, cols.LOG_VOTE_WEIGHT: False, cols.GROUP: True, cols.YEAR: True, cols.VOTES_COUNTED: True, cols.EC_VOTES: True, 
                    cols.VOTE_WEIGHT: True, cols.POP_PER_EC: True, cols.EC_VOTES_NORM: True, cols.VOTES_COUNTED_NORM: True}

    # init figure with core properties
    if color_col == cols.LOG_VOTE_WEIGHT:
        # init figure where state color is determined by its vote weight (log value)
        fig = px.choropleth(pivot_on_year_df, locations=cols.ABBREV, color=color_col, title=fig_title, 
                            locationmode='USA-states', scope="usa", custom_data=custom_data,
                            hover_name=cols.STATE, hover_data=hover_data, animation_frame=cols.YEAR, # ignored if df is for single year
                            color_continuous_scale=px.colors.diverging.BrBG[::-1], color_continuous_midpoint=0,
                            range_color=range_color, labels={cols.GROUP: groups_label}, height=fig_height)
        # colorbar labels: calculate log values for weights so I can plot the familiar linear numbers on the color bar
        # TODO pretty sure this works around a plotly choropleth bug, open ticket or post to stackoverflow
        colorbar_labels = ['0.1', '0.2', '0.33', '0.5', '0.7', '1.0', '1.5', '2.5', '4', '6', '9']
        linear_vals = [float(x) for x in colorbar_labels]
        log_vals = [math.log(t, 2) for t in linear_vals]
        fig.update_layout(
            coloraxis_colorbar=dict(tickvals=log_vals, ticktext=colorbar_labels, title='Voter<br>Weight'))

    elif color_col == cols.GROUP:
        # while I would prefer the NaNs to declare themselves as such, they don't render nicely as customdata params in hovertemplates
        pivot_on_year_df.fillna(-1, inplace=True)
        # init figure where state is determined by its state group
        fig = px.choropleth(pivot_on_year_df, locations=cols.ABBREV, color=color_col, title=fig_title,
                            locationmode='USA-states', scope="usa", custom_data=custom_data,
                            hover_name=cols.STATE, hover_data=hover_data, animation_frame=cols.YEAR, animation_group=cols.GROUP, # ignored if df is for single year
                            color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                            labels={cols.GROUP: groups_label}, height=fig_height)

    elif color_col == cols.PARTY:
        color_discrete_sequence = ['Blue', 'Red']
        category_orders = {cols.PARTY: ['Biden', 'Trump']}
        fig = px.choropleth(pivot_on_year_df, locations=cols.ABBREV, color=color_col, title=fig_title, 
                            locationmode='USA-states', scope="usa", custom_data=custom_data,
                            hover_name=cols.STATE, hover_data=hover_data, 
                            color_discrete_sequence=color_discrete_sequence, category_orders=category_orders,
                            labels={cols.PARTY: groups_label}, height=fig_height)
        # originally had add_scattergeo traces here, had to move them to end of function after hovertemplate traces, otherwise hovertemplates are imposed on them

    # display formatting
    fig.update_layout(title_x=0.5, dragmode=False, margin=go.layout.Margin(l=0, r=0, b=20, t=100))

    # apply animation settings
    if not frame:
        apply_animation_settings(fig, base_fig_title)

    # hovertemplate formatting and variable substitution using customdata
    if color_col == cols.LOG_VOTE_WEIGHT:
        fig.update_traces(
            hovertemplate="<br>".join([
                "<b>%{customdata[0]}</b> (%{customdata[2]})",
                "<b>→ Voter Weight: %{customdata[5]:.2f}</b><br>",
                "Popular Vote (Turnout): <b>%{customdata[3]:,}</b>",
                "Electoral College Votes: <b>%{customdata[4]}</b>",
                "Popular Vote Per Elector: <b>%{customdata[6]:,}</b>",
                "Group: <b>%{customdata[1]}</b>",
                "<br><b>Normalized to Nat'l Average:</b>",
                "%{customdata[3]:,} Pop Votes → %{customdata[7]:.2f} EC Votes",
                "%{customdata[4]} EC Votes → %{customdata[8]:,} Pop Votes",
            ])
        )
    elif alt_groups and ('ecv_only' in alt_groups):
        fig.update_traces(
            hovertemplate="<br>".join([
                "%{customdata[0]} (%{customdata[2]}): <b>%{customdata[4]} EC Votes</b><br>",
                "Popular Vote (Turnout): <b>%{customdata[3]:,}</b>",
                "Popular Vote Per Elector: <b>%{customdata[6]:,}</b>",
                "Voter Weight: <b>%{customdata[5]:.2f}</b>",
                "Group: <b>%{customdata[1]}</b>",
                "<br><b>Normalized to Nat'l Average:</b>",
                "%{customdata[3]:,} Pop Votes → %{customdata[7]:.2f} EC Votes",
                "%{customdata[4]} EC Votes → %{customdata[8]:,} Pop Votes",
            ])
        )
    # elif color_col == cols.PARTY and alt_data and alt_data == 'census_diff_2020':
    #     fig.update_traces(
    #         hovertemplate="<br>".join([
    #             "<b>%{customdata[0]}</b><br>",
    #             "Popular Vote (Turnout): <b>%{customdata[3]:,}</b>",
    #             "Electoral College Votes: <b>%{customdata[4]}</b>",
    #             "Popular Vote Per Elector: <b>%{customdata[6]:,}</b>",
    #             "Voter Weight: <b>%{customdata[5]:.2f}</b>",
    #             "Group: <b>%{customdata[1]}</b>",
    #             "<br><b>Normalized to Nat'l Average:</b>",
    #             "%{customdata[3]:,} Pop Votes → %{customdata[7]:.2f} EC Votes",
    #             "%{customdata[4]} EC Votes → %{customdata[8]:,} Pop Votes",
    #         ])
    #     )
    else:
        fig.update_traces(
            hovertemplate="<br>".join([
                "<b>%{customdata[0]}</b> (%{customdata[2]})<br>",
                "Popular Vote (Turnout): <b>%{customdata[3]:,}</b>",
                "Electoral College Votes: <b>%{customdata[4]}</b>",
                "Popular Vote Per Elector: <b>%{customdata[6]:,}</b>",
                "Voter Weight: <b>%{customdata[5]:.2f}</b>",
                "Group: <b>%{customdata[1]}</b>",
                "<br><b>Normalized to Nat'l Average:</b>",
                "%{customdata[3]:,} Pop Votes → %{customdata[7]:.2f} EC Votes",
                "%{customdata[4]} EC Votes → %{customdata[8]:,} Pop Votes",
            ])
        )

    if alt_data and alt_data == 'census_diff_2020' and census_diff_hilites:
        if color_col == cols.PARTY:
            pos_color = "lime"
            neg_color = "black" 
            diff_positive_col = 'EC diff positive'
            diff_negative_col = 'EC diff negative'
        else:
            pos_color = "#22DD22"
            neg_color = "black" 
            diff_positive_col = 'VW diff positive'
            diff_negative_col = 'VW diff negative'
        fig.add_scattergeo(locationmode='USA-states', text=diff_positive_df[diff_positive_col],
                            hoverinfo='skip', locations=diff_positive_df[cols.ABBREV], 
                            mode='text', textfont=dict(size=10, color=pos_color), showlegend=False)
        fig.add_scattergeo(locationmode='USA-states', text=diff_negative_df[diff_negative_col],
                            hoverinfo='skip', locations=diff_negative_df[cols.ABBREV],
                            mode='text', textfont=dict(size=10, color=neg_color), showlegend=False)
    else:
        if color_col == cols.LOG_VOTE_WEIGHT:
            abbrev_color = "black"
            text_col = cols.VOTE_WEIGHT
        else:
            abbrev_color = "white" 
            text_col = cols.EC_VOTES
        fig.add_scattergeo(locationmode='USA-states', text=pivot_on_year_df[text_col],
                            hoverinfo='skip', locations=pivot_on_year_df[cols.ABBREV], 
                            mode='text', textfont=dict(size=10, color=abbrev_color), showlegend=False)

    return fig
