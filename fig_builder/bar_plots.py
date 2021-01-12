import math
import pandas as pd
import plotly.express as px

from data_processor.functions import get_era_for_year, map_to_subdir
from metadata import Columns, DataDirs, FigDimensions, GROUPS_FOR_DIR, GROUP_COLORS, PARTIES, PARTY_COLORS, YEAR_0, YEAR_N


cols = Columns()
ddirs = DataDirs()
fig_dims = FigDimensions()


def build_ivw_by_state_bar(data_obj, groups_dir, max_small, fig_width=None, frame=None, color_col=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    pivot_on_year_df = data_obj.state_vote_weights_pivot_dfs[subdir].copy()
    groups = GROUPS_FOR_DIR[groups_dir]

    if not color_col:
        color_col = cols.GROUP

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] == frame]

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.wide_door(fig_width)

    # remove placeholder rows for state groups that lack actual state data
    pivot_on_year_df = pivot_on_year_df[pd.notnull(pivot_on_year_df[cols.STATE])]
    pivot_on_year_df = pivot_on_year_df[pd.notnull(pivot_on_year_df[cols.VOTE_WEIGHT])]
    # pivot_on_year_df.loc[pd.isnull(pivot_on_year_df[cols.VOTE_WEIGHT]), cols.VOTE_WEIGHT] = -0.1

    # display metadata
    base_fig_title = 'Impact Per Voter Per State'
    # base_fig_title = 'Vote Weight Per Ballot Cast Per State'
    # fig_title = f'{year} Presidential Election: Comparative Vote Weight Per Ballot Cast Per State'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        fig_title = f'{base_fig_title}: {YEAR_0} - {YEAR_N}'
    x_axis_title = 'Impact per voter'
    # custom_data enables dynamic variable substitution in hovertemplates for static frames    
    custom_data = [cols.VOTES_COUNTED, cols.EC_VOTES, cols.POP_PER_EC, cols.VOTES_COUNTED_NORM, cols.EC_VOTES_NORM, cols.GROUP]

    # set color sequence based on color_col
    category_orders = {}
    color_discrete_map = []
    color_continuous_scale = []
    color_continuous_midpoint = None
    if color_col == cols.PARTY:
        category_orders = {cols.PARTY: PARTIES}
        color_discrete_map = PARTY_COLORS
    elif color_col == cols.LOG_VOTE_WEIGHT:
        color_continuous_scale = px.colors.diverging.BrBG[::-1]
        color_continuous_midpoint = 0
    elif color_col == cols.GROUP:
        category_orders = {cols.GROUP: groups}
        color_discrete_map = GROUP_COLORS
    
    # init figure with core properties
    fig = px.bar(pivot_on_year_df, x=cols.VOTE_WEIGHT, y=cols.STATE, color=color_col, title=fig_title, 
                custom_data=custom_data, animation_frame=cols.YEAR, # ignored if df is for single year
                color_continuous_scale=color_continuous_scale, color_continuous_midpoint=color_continuous_midpoint,
                color_discrete_map=color_discrete_map, category_orders=category_orders,
                # labels={cols.VOTE_WEIGHT: 'Relative impact per voter'}, 
                width=fig_width, height=fig_height)

    # axis titles, ticks, labels, and ordering
    fig.update_xaxes(title_text=x_axis_title)
    fig.update_yaxes(title_text='')
    fig.update_layout(
        yaxis={'tickangle': 35, 'showticklabels': True, 'type': 'category', 'tickfont_size': 8},
        yaxis_categoryorder='total ascending')
    if color_col == cols.LOG_VOTE_WEIGHT:
        # calculate log values for weights so I can plot the familiar linear numbers on the color bar
        # TODO pretty sure this works around a plotly bug, also present in choropleth, open ticket or post to stackoverflow
        tick_text = ['0.5', '0.7', '1.0', '1.5', '2.5', '4', '6', '9']
        lin_ticks = [float(x) for x in tick_text]
        log_ticks = [math.log(t, 2) for t in lin_ticks]
        fig.update_layout(
            coloraxis_colorbar=dict(tickvals=log_ticks, ticktext=tick_text))

    # center title
    fig.update_layout(title_x=0.5)

    # TODO where are x, y, and customdata actually defined, in fig? I'd like to avoid these redundant key-value mappings and use an f-string for this but not sure how
    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>%{x}</b> (%{y})<br>",
            "Popular vote: <b>%{customdata[0]:,}</b>",
            "Electoral College votes: <b>%{customdata[1]}</b>",
            "Population per EC vote: <b>%{customdata[2]:,}</b>",
            # "Group: %{customdata[5]}",
            "<br><b>Normalized to nat'l average:</b>",
            "%{customdata[0]:,} pop votes => %{customdata[4]:.2f} EC votes",
            "%{customdata[1]} EC votes => %{customdata[3]:,} pop votes",
        ])
    )

    return fig


# ref: https://towardsdatascience.com/how-to-create-a-grouped-bar-chart-with-plotly-express-in-python-e2b64ed4abd7
def build_actual_vs_adjusted_ec_bar(data_obj, groups_dir, max_small, fig_width=None, frame=None):
    # TODO does this need groups_dir and max_small or can it use defaults 100% of time?
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    melted_ec_votes_pivot_df = data_obj.melted_ec_votes_pivot_dfs[subdir].sort_values('EC votes*', ascending=True)

    # if frame is set, extract single-year data
    if frame:
        melted_ec_votes_pivot_df = melted_ec_votes_pivot_df[melted_ec_votes_pivot_df[cols.YEAR] == frame]

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.square(fig_width)

    # remove placeholder rows for state groups that lack actual state data
    melted_ec_votes_pivot_df = melted_ec_votes_pivot_df[pd.notnull(melted_ec_votes_pivot_df[cols.STATE])]

    # display metadata
    base_fig_title = 'Actual EC Votes vs EC Votes Adjusted For Turnout'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        fig_title = f'{base_fig_title}: {YEAR_0} - {YEAR_N}'
    x_axis_title = 'Actual EC votes / EC Votes If Adjusted For Popular Vote Turnout'
    # custom_data enables dynamic variable substitution in hovertemplates for static frames
    custom_data = [cols.YEAR, cols.EC_VOTES, cols.VOTES_COUNTED, cols.VOTE_WEIGHT, cols.POP_PER_EC, cols.VOTES_COUNTED_NORM, cols.EC_VOTES_NORM]
    # set color sequence
    color_discrete_sequence = ['DarkGreen', 'LimeGreen']

    # init figure with core properties
    fig = px.bar(melted_ec_votes_pivot_df, x='EC votes*', y=cols.STATE, color='Actual vs Adjusted EC votes*', title=fig_title, 
                custom_data=custom_data, barmode='group', animation_frame=cols.YEAR, # ignored if df is for single year
                color_discrete_sequence=color_discrete_sequence, width=fig_width, height=fig_height)

    # axis titles, ticks, labels, and ordering
    fig.update_xaxes(title_text=x_axis_title)
    fig.update_yaxes(title_text='')
    fig.update_layout(
        yaxis={'tickangle': 35, 'showticklabels': True, 'type': 'category', 'tickfont_size': 8},
        yaxis_categoryorder='total descending')

    # center title
    fig.update_layout(title_x=0.5)

    # TODO where are x, y, and customdata actually defined, in fig? I'd like to avoid these redundant key-value mappings and use an f-string for this but not sure how
    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>%{x}</b>*<br>",
            "<b>%{y}</b> (%{customdata[0]}):",
            "Popular vote: <b>%{customdata[2]:,}</b>",
            "Vote Weight: <b>%{customdata[3]:.2f}</b>",
            "Population per EC vote: <b>%{customdata[4]:,}</b>",
            "<br><b>Normalized to nat'l average:</b>",
            "%{customdata[2]:,} pop votes => %{customdata[6]:.2f} EC votes",
            "%{customdata[1]} EC votes => %{customdata[5]:,} pop votes",
        ])
    )

    return fig


def build_actual_vs_adjusted_vw_bar(data_obj, groups_dir, max_small, fig_width=None, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    melted_vote_count_pivot_df = data_obj.melted_vote_count_pivot_dfs[subdir].sort_values('Vote count*', ascending=True)

    # if frame is set, extract single-year data
    if frame:
        melted_vote_count_pivot_df = melted_vote_count_pivot_df[melted_vote_count_pivot_df[cols.YEAR] == frame]

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.square(fig_width)

    # remove placeholder rows for state groups that lack actual state data
    melted_vote_count_pivot_df = melted_vote_count_pivot_df[pd.notnull(melted_vote_count_pivot_df[cols.STATE])]

    # display metadata
    base_fig_title = 'Actual Vote Count vs Vote Count Adjusted For Vote Weight'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        fig_title = f'{base_fig_title}: {YEAR_0} - {YEAR_N}'
    x_axis_title = 'Actual Vote Count / Vote Count If Adjusted For Individual Vote Weight'
    # custom_data enables dynamic variable substitution in hovertemplates for static frames
    custom_data = [cols.YEAR, cols.EC_VOTES, cols.VOTES_COUNTED, cols.VOTE_WEIGHT, cols.POP_PER_EC, cols.VOTES_COUNTED_NORM, cols.EC_VOTES_NORM]
    color_discrete_sequence = ['DarkBlue', 'DodgerBlue']
    
    # init figure with core properties
    fig = px.bar(melted_vote_count_pivot_df, x='Vote count*', y=cols.STATE, color='Actual vs Adjusted Vote count*', title=fig_title, 
                custom_data=custom_data, barmode='group', animation_frame=cols.YEAR, # ignored if df is for single year
                color_discrete_sequence=color_discrete_sequence, width=fig_width, height=fig_height)

    # axis titles, ticks, labels, and ordering
    fig.update_xaxes(title_text=x_axis_title)
    fig.update_yaxes(title_text='')
    fig.update_layout(
        yaxis={'tickangle': 35, 'showticklabels': True, 'type': 'category', 'tickfont_size': 8},
        yaxis_categoryorder='total descending')

    # center title
    fig.update_layout(title_x=0.5)

    # TODO where are x, y, and customdata actually defined, in fig? I'd like to avoid these redundant key-value mappings and use an f-string for this but not sure how
    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>%{x:,}</b>*<br>",
            "<b>%{y}</b> (%{customdata[0]}):",
            "Popular vote: <b>%{customdata[2]:,}</b>",
            "Vote Weight: <b>%{customdata[3]:.2f}</b>",
            "Population per EC vote: <b>%{customdata[4]:,}</b>",
            "<br><b>Normalized to nat'l average:</b>",
            "%{customdata[2]:,} pop votes => %{customdata[6]:.2f} EC votes",
            "%{customdata[1]} EC votes => %{customdata[5]:,} pop votes",
        ])
    )

    return fig


def build_swallowed_vote_fig_1(data_obj):
    # display metadata
    hover_data = {'State': True, 'Candidate': True, 'EC Votes for Candidate': True, 'State: Candidate': False,
                'Candidate: Outcome': False}
    category_orders = {'Candidate': ['Biden','Trump']}
    color_discrete_sequence = ['Blue','Red']

    # init figure with core properties
    fig = px.bar(data_obj.swallowed_vote_df, x="Popular Vote", y="State: Candidate", 
                color='Candidate', hover_data=hover_data, width=1000, height=800,
                category_orders=category_orders, color_discrete_sequence=color_discrete_sequence)

    fig.update_layout(yaxis_categoryorder='total ascending')
    fig.update_xaxes(range=[0,10000000])

    # center title
    fig.update_layout(title_x=0.5)

    return fig
    

def build_swallowed_vote_fig_2(data_obj):
    # display metadata
    hover_data = {'State': True, 'Candidate': True, 'EC Votes for Candidate': True, 'State: Candidate': False, 
                'Candidate: Outcome': False}
    category_orders = {'Candidate: Outcome': ['Biden: Win','Trump: Win','Biden: Loss','Trump: Loss']}
    color_discrete_sequence = ['Blue','Red','Gray','Gray']

    # init figure with core properties
    fig = px.bar(data_obj.swallowed_vote_df, x="Popular Vote", y="State: Candidate", 
                color='Candidate: Outcome', hover_data=hover_data, width=1000, height=800,
                category_orders=category_orders, color_discrete_sequence=color_discrete_sequence)

    fig.update_layout(yaxis_categoryorder='total ascending')
    fig.update_xaxes(range=[0,10000000])

    # center title
    fig.update_layout(title_x=0.5)

    return fig


def build_swallowed_vote_fig_3(data_obj):
    # display metadata
    hover_data = {'State': True, 'Candidate': True, 'EC Votes for Candidate': True, 'State: Candidate': False, 
                'Candidate: Outcome': False}
    category_orders = {'Candidate: Outcome': ['Biden: Win','Trump: Win','Biden: Loss','Trump: Loss']}
    color_discrete_sequence = ['Blue','Red','Gray','Gray']

    # init figure with core properties
    fig = px.bar(data_obj.swallowed_vote_df, x="Popular Vote", y="State", 
                color='Candidate: Outcome', barmode='relative', hover_data=hover_data, width=1000, height=800,
                category_orders=category_orders, color_discrete_sequence=color_discrete_sequence)

    fig.update_layout(yaxis_categoryorder='total ascending')
    fig.update_xaxes(range=[0,18000000])

    # center title
    fig.update_layout(title_x=0.5)

    return fig


def build_swallowed_vote_fig_4(data_obj):
    distilled_svs = data_obj.swallowed_vote_df.sort_values('EC Votes for Candidate', ascending=False)
    distilled_svs = distilled_svs[distilled_svs['EC Votes for Candidate'] != 0]
    
    # display metadata
    hover_data = {'State': True, 'EC Votes for Candidate': True, 'State: Candidate': False}
    category_orders = {'Candidate': ['Biden','Trump']}
    color_discrete_sequence = ['Blue','Red']

    # init figure with core properties
    fig = px.bar(distilled_svs, x="EC Votes for Candidate", y="State", 
                color='Candidate', hover_data=hover_data, width=1000, height=800,
                category_orders=category_orders, color_discrete_sequence=color_discrete_sequence)

    fig.update_layout(yaxis_categoryorder='total ascending')

    # center title
    fig.update_layout(title_x=0.5)

    return fig
