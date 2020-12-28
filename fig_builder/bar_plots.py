import pandas as pd
import plotly.express as px

from data_processor.functions import get_era_for_year, map_to_subdir
from metadata import Columns, FigDimensions, GROUPS_FOR_DIR, GROUP_COLORS, PARTIES, PARTY_COLORS


cols = Columns()
fig_dims = FigDimensions()


def build_ivw_by_state_bar(data_obj, groups_dir, max_small, fig_width=None, frame=None, color_col=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    pivot_on_year_df = data_obj.pivot_on_year_dfs[subdir]
    groups = GROUPS_FOR_DIR[groups_dir]

    if not color_col:
        color_col = cols.GROUP

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] == frame]

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.fat_door(fig_width)

    # remove placeholder rows for state groups that lack actual state data
    pivot_on_year_df = pivot_on_year_df[pd.notnull(pivot_on_year_df[cols.STATE])]

    # display metadata
    hover_data = {cols.PARTY: False, cols.VOTES_COUNTED: True, cols.EC_VOTES: True, cols.POP_PER_EC_SHORT: True, 
                cols.VOTES_COUNTED_NORM: True, cols.EC_VOTES_NORM: True, cols.STATE: False}

    # set color sequence
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
    
    
    # fig_title = f'{year} Presidential Election: Comparative Vote Weight Per Ballot Cast Per State'
    base_fig_title = 'Vote Weight Per Ballot Cast Per State'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        fig_title = f'{base_fig_title}: 1828 - 2020'
    
    # declare fig
    fig = px.bar(pivot_on_year_df, x=cols.VOTE_WEIGHT, y=cols.STATE, color=color_col, 
                hover_name=cols.STATE, hover_data=hover_data,
                animation_frame=cols.YEAR, # ignored if df is for single year
                color_continuous_scale=color_continuous_scale, color_continuous_midpoint=color_continuous_midpoint,
                color_discrete_map=color_discrete_map, category_orders=category_orders,
                labels={cols.VOTE_WEIGHT: 'Relative impact per voter'}, 
                title=fig_title, width=fig_width, height=fig_height)

    fig.update_layout(
        yaxis={'tickangle': 35, 'showticklabels': True, 'type': 'category', 'tickfont_size': 8},
        yaxis_categoryorder='total ascending',
    )

    if color_col == cols.LOG_VOTE_WEIGHT:
        fig.update_layout(
            coloraxis_colorbar=dict(tickvals=[-0.693, -0.357, 0, 0.405, 0.916, 1.386, 1.792, 2.197],
                                    ticktext=['0.5', '0.7', '1.0', '1.5', '2.5', '4', '6', '9']))

    return fig


# ref: https://towardsdatascience.com/how-to-create-a-grouped-bar-chart-with-plotly-express-in-python-e2b64ed4abd7
def build_actual_vs_adjusted_ec_bar(data_obj, groups_dir, max_small, fig_width=None, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    melted_ec_votes_pivot_df = data_obj.melted_ec_votes_pivot_dfs[subdir].sort_values('EC votes^', ascending=True)

    # if frame is set, extract single-year data
    if frame:
        melted_ec_votes_pivot_df = melted_ec_votes_pivot_df[melted_ec_votes_pivot_df[cols.YEAR] == frame]

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.square(fig_width)

    # remove placeholder rows for state groups that lack actual state data
    melted_ec_votes_pivot_df = melted_ec_votes_pivot_df[pd.notnull(melted_ec_votes_pivot_df[cols.STATE])]

    # display metadata
    hover_data = {cols.PARTY: False, 'Actual vs Adjusted EC votes^': False, cols.VOTE_WEIGHT: True, cols.VOTES_COUNTED: True, 
                cols.VOTES_COUNTED_NORM: True, cols.POP_PER_EC_SHORT: True, cols.STATE: False}
    color_discrete_sequence = ['DarkGreen', 'LimeGreen']
    base_fig_title = 'Actual EC Votes vs EC Votes Adjusted For Turnout'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        fig_title = f'{base_fig_title}: 1828 - 2020'

    fig = px.bar(melted_ec_votes_pivot_df, x='EC votes^', y=cols.STATE, color='Actual vs Adjusted EC votes^', 
                barmode='group', hover_name=cols.STATE, hover_data=hover_data,
                animation_frame=cols.YEAR, # ignored if df is for single year
                color_discrete_sequence=color_discrete_sequence, 
                title=fig_title, width=fig_width, height=fig_height)

    fig.update_layout(
        yaxis={'tickangle': 35, 'showticklabels': True, 'type': 'category', 'tickfont_size': 8},
        yaxis_categoryorder='total descending'
    )
    fig.update_xaxes(title_text='Actual EC votes / EC Votes If Adjusted For Popular Vote Turnout')

    return fig


def build_actual_vs_adjusted_vw_bar(data_obj, groups_dir, max_small, fig_width=None, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    melted_vote_count_pivot_df = data_obj.melted_vote_count_pivot_dfs[subdir].sort_values('Vote count^', ascending=True)

    # if frame is set, extract single-year data
    if frame:
        melted_vote_count_pivot_df = melted_vote_count_pivot_df[melted_vote_count_pivot_df[cols.YEAR] == frame]

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.square(fig_width)

    # remove placeholder rows for state groups that lack actual state data
    melted_vote_count_pivot_df = melted_vote_count_pivot_df[pd.notnull(melted_vote_count_pivot_df[cols.STATE])]

    # display metadata
    hover_data = {cols.PARTY: False, 'Actual vs Adjusted Vote count^': False, cols.VOTE_WEIGHT: True, cols.EC_VOTES: True,
                cols.EC_VOTES_NORM: True, cols.POP_PER_EC_SHORT: True, cols.STATE: False}
    color_discrete_sequence = ['DarkBlue', 'DodgerBlue']
    base_fig_title = 'Actual Vote Count vs Vote Count Adjusted For Vote Weight'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        fig_title = f'{base_fig_title}: 1828 - 2020'

    fig = px.bar(melted_vote_count_pivot_df, x='Vote count^', y=cols.STATE, color='Actual vs Adjusted Vote count^', 
                barmode='group', hover_name=cols.STATE, hover_data=hover_data,
                animation_frame=cols.YEAR, # ignored if df is for single year
                color_discrete_sequence=color_discrete_sequence, 
                title=fig_title, width=fig_width, height=fig_height)

    fig.update_layout(
        yaxis={'tickangle': 35, 'showticklabels': True, 'type': 'category', 'tickfont_size': 8},
        yaxis_categoryorder='total descending'
    )
    fig.update_xaxes(title_text='Actual Vote Count / Vote Count If Adjusted For Individual Vote Weight')

    return fig


def build_swallowed_vote_fig_1(data_obj):
    # display metadata
    hover_data = {'State': True, 'Candidate': True, 'EC Votes for Candidate': True, 'State: Candidate': False,
                'Candidate: Outcome': False}
    category_orders = {'Candidate': ['Biden','Trump']}
    color_discrete_sequence = ['Blue','Red']

    fig = px.bar(data_obj.swallowed_vote_df, x="Popular Vote", y="State: Candidate", 
                color='Candidate', hover_data=hover_data, width=1000, height=800,
                category_orders=category_orders, color_discrete_sequence=color_discrete_sequence)

    fig.update_layout(yaxis_categoryorder='total ascending')
    fig.update_xaxes(range=[0,10000000])

    return fig
    

def build_swallowed_vote_fig_2(data_obj):
    # display metadata
    hover_data = {'State': True, 'Candidate': True, 'EC Votes for Candidate': True, 'State: Candidate': False, 
                'Candidate: Outcome': False}
    category_orders = {'Candidate: Outcome': ['Biden: Win','Trump: Win','Biden: Loss','Trump: Loss']}
    color_discrete_sequence = ['Blue','Red','Gray','Gray']

    fig = px.bar(data_obj.swallowed_vote_df, x="Popular Vote", y="State: Candidate", 
                color='Candidate: Outcome', hover_data=hover_data, width=1000, height=800,
                category_orders=category_orders, color_discrete_sequence=color_discrete_sequence)

    fig.update_layout(yaxis_categoryorder='total ascending')
    fig.update_xaxes(range=[0,10000000])

    return fig


def build_swallowed_vote_fig_3(data_obj):
    # display metadata
    hover_data = {'State': True, 'Candidate': True, 'EC Votes for Candidate': True, 'State: Candidate': False, 
                'Candidate: Outcome': False}
    category_orders = {'Candidate: Outcome': ['Biden: Win','Trump: Win','Biden: Loss','Trump: Loss']}
    color_discrete_sequence = ['Blue','Red','Gray','Gray']

    fig = px.bar(data_obj.swallowed_vote_df, x="Popular Vote", y="State", 
                color='Candidate: Outcome', barmode='relative', hover_data=hover_data, width=1000, height=800,
                category_orders=category_orders, color_discrete_sequence=color_discrete_sequence)

    fig.update_layout(yaxis_categoryorder='total ascending')
    fig.update_xaxes(range=[0,18000000])

    return fig


def build_swallowed_vote_fig_4(data_obj):
    distilled_svs = data_obj.swallowed_vote_df.sort_values('EC Votes for Candidate', ascending=False)
    distilled_svs = distilled_svs[distilled_svs['EC Votes for Candidate'] != 0]
    
    # display metadata
    hover_data = {'State': True, 'EC Votes for Candidate': True, 'State: Candidate': False}
    category_orders = {'Candidate': ['Biden','Trump']}
    color_discrete_sequence = ['Blue','Red']

    fig = px.bar(distilled_svs, x="EC Votes for Candidate", y="State", 
                color='Candidate', hover_data=hover_data, width=1000, height=800,
                category_orders=category_orders, color_discrete_sequence=color_discrete_sequence)

    fig.update_layout(yaxis_categoryorder='total ascending')

    return fig
