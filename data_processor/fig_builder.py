import math
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from data_processor.functions import get_era_for_year, apply_animation_settings, map_to_subdir, get_description_for_group_key
from metadata import (
    ACW_GROUPS, CENSUS_GROUPS, GROUPS_FOR_DIR, GROUP_COLORS, PARTIES, PARTY_COLORS, FRAME_RATE, Columns, DataDirs
)


WIDTH_FULL_PAGE = 1640
WIDTH_HALF_PAGE = 800
HEIGHT_HALF_PAGE_SQUARE = WIDTH_HALF_PAGE
HEIGHT_HALF_PAGE_CRT = WIDTH_HALF_PAGE * .75

cols = Columns()
ddirs = DataDirs()


def build_ivw_by_state_bar(data_obj, groups_dir, max_small, frame=None, color_col=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    pivot_on_year_df = data_obj.pivot_on_year_dfs[subdir]
    groups = GROUPS_FOR_DIR[groups_dir]

    if not color_col:
        color_col = cols.GROUP

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] == frame]

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
    fig = px.bar(pivot_on_year_df, x=cols.VOTE_WEIGHT, y=cols.STATE, color=color_col, hover_name=cols.STATE, hover_data=hover_data,
                color_continuous_scale=color_continuous_scale, color_continuous_midpoint=color_continuous_midpoint,
                color_discrete_map=color_discrete_map, category_orders=category_orders,
                animation_frame=cols.YEAR, # ignored if df is for single year
                labels={cols.VOTE_WEIGHT: 'Relative impact per voter'}, title=fig_title,
                width=WIDTH_HALF_PAGE, height=HEIGHT_HALF_PAGE_SQUARE)

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
def build_actual_vs_adjusted_ec_bar(data_obj, groups_dir, max_small, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    melted_ec_votes_pivot_df = data_obj.melted_ec_votes_pivot_dfs[subdir].sort_values('EC votes^', ascending=True)

    # if frame is set, extract single-year data
    if frame:
        melted_ec_votes_pivot_df = melted_ec_votes_pivot_df[melted_ec_votes_pivot_df[cols.YEAR] == frame]

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

    fig = px.bar(melted_ec_votes_pivot_df, x='EC votes^', y=cols.STATE,  
                color='Actual vs Adjusted EC votes^', barmode='group', hover_name=cols.STATE, hover_data=hover_data,
                animation_frame=cols.YEAR, # ignored if df is for single year
                color_discrete_sequence=color_discrete_sequence, 
                title=fig_title, width=WIDTH_HALF_PAGE, height=HEIGHT_HALF_PAGE_SQUARE)

    fig.update_layout(
        yaxis={'tickangle': 35, 'showticklabels': True, 'type': 'category', 'tickfont_size': 8},
        yaxis_categoryorder='total descending'
    )
    fig.update_xaxes(title_text='Actual EC votes / EC Votes If Adjusted For Popular Vote Turnout')

    return fig


def build_actual_vs_adjusted_vw_bar(data_obj, groups_dir, max_small, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    melted_vote_count_pivot_df = data_obj.melted_vote_count_pivot_dfs[subdir].sort_values('Vote count^', ascending=True)

    # if frame is set, extract single-year data
    if frame:
        melted_vote_count_pivot_df = melted_vote_count_pivot_df[melted_vote_count_pivot_df[cols.YEAR] == frame]

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

    fig = px.bar(melted_vote_count_pivot_df, x='Vote count^', y=cols.STATE,  
                color='Actual vs Adjusted Vote count^', barmode='group', hover_name=cols.STATE, hover_data=hover_data,
                animation_frame=cols.YEAR, # ignored if df is for single year
                color_discrete_sequence=color_discrete_sequence, 
                title=fig_title, width=WIDTH_HALF_PAGE, height=HEIGHT_HALF_PAGE_SQUARE)

    fig.update_layout(
        yaxis={'tickangle': 35, 'showticklabels': True, 'type': 'category', 'tickfont_size': 8},
        yaxis_categoryorder='total descending'
    )
    fig.update_xaxes(title_text='Actual Vote Count / Vote Count If Adjusted For Individual Vote Weight')

    return fig


def build_ivw_by_state_map(data_obj, groups_dir, max_small, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    pivot_on_year_df = data_obj.pivot_on_year_dfs[subdir]

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] == frame]

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
        fig_title = f'{base_fig_title}: 1828 - 2020'

    fig = px.choropleth(pivot_on_year_df, locations=cols.ABBREV, color=cols.LOG_VOTE_WEIGHT,
                        locationmode='USA-states', scope="usa", hover_name=cols.STATE, hover_data=hover_data, 
                        color_continuous_scale=px.colors.diverging.BrBG[::-1], color_continuous_midpoint=0,
                        # range_color=[-1.0, pivot_on_single_year[cols.LOG_VOTE_WEIGHT].max()],
                        # range_color=[log_vote_weight_min, log_vote_weight_max],  
                        animation_frame=cols.YEAR, # ignored if df is for single year
                        title=fig_title, width=WIDTH_HALF_PAGE, height=HEIGHT_HALF_PAGE_CRT)

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


def build_ivw_by_state_scatter_dots(data_obj, groups_dir, max_small, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    pivot_on_year_df = data_obj.pivot_on_year_dfs[subdir]
    groups = GROUPS_FOR_DIR[groups_dir]

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] == frame].sort_values(cols.GROUP, ascending=True)
    
    # calculate axis range boundaries 
    ec_max = round(pivot_on_year_df[cols.EC_VOTES].max() * 1.05)
    norm_max = round(pivot_on_year_df[cols.EC_VOTES_NORM].max() * 1.05)

    # display metadata
    hover_data = {cols.VOTES_COUNTED: True, cols.VOTE_WEIGHT: True, cols.POP_PER_EC_SHORT: True}
    base_fig_title = 'Vote Weight Per Person Per State'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        fig_title = f'{base_fig_title}: 1828 - 2020'

    # init figure with core properties
    fig = px.scatter(pivot_on_year_df, x=cols.EC_VOTES_NORM, y=cols.EC_VOTES, color=cols.GROUP,  
                    animation_frame=cols.YEAR, # ignored if df is for single year
                    hover_name=cols.STATE, hover_data=hover_data,
                    color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                    title=fig_title, width=WIDTH_HALF_PAGE, height=HEIGHT_HALF_PAGE_CRT, 
    #                  log_x=True, log_y=True, range_x=[.4,norm_max], range_y=[2,ec_max],
                    opacity=0.7, range_x=[0,norm_max], range_y=[0,ec_max])
    
    # scatterplot dot formatting
    fig.update_traces(marker=dict(size=24, line=dict(width=1, color='white')), 
                    selector=dict(mode='markers'))

    # reference mean / quazi-linear regression line
    fig.add_trace(go.Scatter(x=[0,ec_max], y=[0,ec_max], mode='lines', 
                            name='Nationwide mean', line=dict(color='black', width=1)))

    # axis labels
    fig.update_xaxes(title_text='State EC votes if adjusted for popular vote turnout')
    fig.update_yaxes(title_text='Electoral college votes per state')

    fig.update_layout(title_x=0.45)

    return fig


def build_ivw_by_state_scatter_abbrevs(data_obj, groups_dir, max_small, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    pivot_on_year_df = data_obj.pivot_on_year_dfs[subdir]
    groups = GROUPS_FOR_DIR[groups_dir]

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] == frame]

    # calculate axis range boundaries 
    ec_max = round(pivot_on_year_df[cols.EC_VOTES].max() * 1.05)
    norm_max = round(pivot_on_year_df[cols.EC_VOTES_NORM].max() * 1.05)

    # display metadata
    hover_data = {cols.VOTES_COUNTED: True, cols.VOTE_WEIGHT: True, cols.POP_PER_EC_SHORT: True}
    base_fig_title = 'Vote Weight Per Person Per State'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        fig_title = f'{base_fig_title}: 1828 - 2020'

    # init figure with core properties
    fig = px.scatter(pivot_on_year_df, x=cols.EC_VOTES_NORM, y=cols.EC_VOTES, color=cols.GROUP,  
                    animation_frame=cols.YEAR, # ignored if df is for single year
                    hover_name=cols.STATE, hover_data=hover_data, text=cols.ABBREV,
                    color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                    title=fig_title, width=WIDTH_HALF_PAGE, height=HEIGHT_HALF_PAGE_CRT,
                    opacity=0.7, log_x=True, log_y=True, range_x=[.4,norm_max], range_y=[2.5,ec_max])
        
    # scatterplot dot formatting
    fig.update_traces(marker=dict(size=24, line=dict(width=1, color='DarkSlateGrey')), 
                    selector=dict(mode='markers'))

    # reference mean / quazi-linear regression line
    fig.add_trace(go.Scatter(x=[0,ec_max], y=[0,ec_max], mode='lines', 
                            name='Nationwide mean', line=dict(color='black', width=1)))

    # axis labels
    fig.update_xaxes(title_text='State EC votes if adjusted for popular vote turnout (log)')
    fig.update_yaxes(title_text='Electoral college votes per state (log)')

    # axis tick overrides
    layout = dict(
        yaxis=dict(tickmode='array', tickvals=[3,4,5,6,7,8,9,10,12,15,20,25,30,40,50]),
        xaxis=dict(tickmode='array', tickvals=[.5,.75,1,1.5,2,3,4,5,6,7,8,10,12,15,20,25,30,40,50,60])
    )
    fig.update_layout(layout)

    fig.update_layout(title_x=0.45)

    return fig


def build_ivw_by_state_scatter_bubbles(data_obj, groups_dir, max_small, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    pivot_on_year_df = data_obj.pivot_on_year_dfs[subdir]
    groups = GROUPS_FOR_DIR[groups_dir]

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] == frame]

    # calculate axis range boundaries 
    ec_max = round(pivot_on_year_df[cols.EC_VOTES].max())
    weight_min = pivot_on_year_df[pivot_on_year_df[cols.VOTE_WEIGHT] > 0][cols.VOTE_WEIGHT].min() * 0.9
    weight_max = pivot_on_year_df[cols.VOTE_WEIGHT].max()

    # display metadata
    hover_data = {cols.VOTES_COUNTED: True, cols.POP_PER_EC_SHORT: True}
    base_fig_title = 'Vote Weight Per Person Per State'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        fig_title = f'{base_fig_title}: 1828 - 2020'

    # init figure with core properties
    fig = px.scatter(pivot_on_year_df, x=cols.EC_VOTES, y=cols.VOTE_WEIGHT, color=cols.GROUP, 
                    hover_name=cols.STATE, hover_data=hover_data, size=cols.VOTES_COUNTED_PCT, size_max=80, 
                    animation_frame=cols.YEAR, # ignored if df is for single year
                    color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                    title=fig_title, width=WIDTH_HALF_PAGE, height=HEIGHT_HALF_PAGE_CRT,
                    opacity=0.5, log_y=True, range_x=[0,ec_max], range_y=[weight_min,weight_max])

    # scatterplot dot formatting
    fig.update_traces(marker=dict(line=dict(width=1, color='white')), 
                    selector=dict(mode='markers'))

    # reference mean / quazi-linear regression line
    fig.add_trace(go.Scatter(x=[0,ec_max], y=[1,1], mode='lines', 
                            name='Nationwide mean', line=dict(color='black', width=1)))

    # axis labels
    fig.update_xaxes(title_text='Electoral college votes per state')
    fig.update_yaxes(title_text='Individual voter impact per state (log)')

    # axis tick overrides
    layout = dict(yaxis=dict(tickmode='array', tickvals=[0.4,0.5,.6,.8,1,1.5,2,3,5,8]))
    fig.update_layout(layout)

    fig.update_layout(title_x=0.45)

    return fig


def build_ivw_by_state_group_box_plot(data_obj, groups_dir, max_small, frame):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    pivot_on_year_df = data_obj.pivot_on_year_dfs[subdir]
    groups = GROUPS_FOR_DIR[groups_dir]

    # extract single-year data
    pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] == frame]

    # display metadata
    base_fig_title = 'Range of Vote Weight Per Person Per Region'
    era = get_era_for_year(frame)
    fig_title = f'{base_fig_title}: {frame} ({era})'

    # box plot
    box_data = pivot_on_year_df[[cols.GROUP, cols.VOTE_WEIGHT]]
    pivot = box_data.pivot(columns=cols.GROUP, values=cols.VOTE_WEIGHT)

    fig = px.box(pivot, color=cols.GROUP, 
                color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                title=fig_title, width=WIDTH_HALF_PAGE, height=HEIGHT_HALF_PAGE_CRT, 
                log_y=True)

    # fig.add_trace(go.Scatter(x=flat_data['EC votes'], y=flat_data['Mean vote weight'], 
    #                          mode='lines', name=trace_name_natl_avg, line=dict(color='black', width=1)))

    fig.update_xaxes(title_text='')
    fig.update_yaxes(title_text='Range of Vote Weight Per Person Within Regional Grouping')
    fig.update_layout(title_x=0.46)
    return fig


def build_state_groups_map(data_obj, groups_dir, max_small, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    pivot_on_year_df = data_obj.pivot_on_year_dfs[subdir]
    groups = GROUPS_FOR_DIR[groups_dir]

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] == frame]

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
        fig_title = f'{base_fig_title}: 1828 - 2020'

    fig = px.choropleth(pivot_on_year_df, locations=cols.ABBREV, color=cols.GROUP, 
                        locationmode='USA-states', scope="usa", hover_name=cols.STATE, hover_data=hover_data, 
                        animation_frame=cols.YEAR, animation_group=cols.GROUP, # ignored if df is for single year
                        color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                        title=fig_title, width=WIDTH_HALF_PAGE, height=HEIGHT_HALF_PAGE_CRT)

    return fig


def build_ivw_by_state_group_scatter_dots(data_obj, groups_dir, max_small, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    group_aggs_by_year_df = data_obj.group_aggs_by_year_dfs[subdir]
    groups = GROUPS_FOR_DIR[groups_dir]

    # if frame is set, extract single-year data
    if frame:
        group_aggs_by_year_df = group_aggs_by_year_df[group_aggs_by_year_df[cols.YEAR] == frame]

    # calculate axis range boundaries
    ec_max = round(group_aggs_by_year_df[cols.EC_VOTES].max() * 1.05)
    #pop_max = round(group_aggs_by_year[cols.VOTES_COUNTED].max() * 1.05)
    norm_max = round(group_aggs_by_year_df[cols.EC_VOTES_NORM].max() * 1.05)

    # display metadata
    hover_data = {cols.VOTES_COUNTED: True, cols.AVG_WEIGHT: True, cols.POP_PER_EC_SHORT: True,
                cols.STATE_COUNT: True, cols.STATES_IN_GROUP: True}
    base_fig_title = 'Average Vote Weight Per Person Per Region'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        fig_title = f'{base_fig_title}: 1828 - 2020'

    # init figure with core properties
    fig = px.scatter(group_aggs_by_year_df, x=cols.EC_VOTES_NORM, y=cols.EC_VOTES, color=cols.GROUP, 
                    hover_name=cols.GROUP, hover_data=hover_data,
                    animation_frame=cols.YEAR, animation_group=cols.GROUP, # ignored if df is for single year
                    color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                    title=fig_title, width=WIDTH_HALF_PAGE, height=HEIGHT_HALF_PAGE_CRT, 
    #                  log_x=True, log_y=True, range_x=[.4,norm_max], range_y=[2,ec_max],
                    opacity=0.7, range_x=[0, norm_max], range_y=[0, ec_max])
        
    # scatterplot dot formatting
    fig.update_traces(marker=dict(size=24, line=dict(width=1, color='DarkSlateGrey')), selector=dict(mode='markers'))

    # reference mean / quazi-linear regression line
    fig.add_trace(go.Scatter(x=[0,ec_max], y=[0,ec_max], mode='lines', 
                            name='Nationwide mean', line=dict(color='black', width=1)))

    # axis labels
    fig.update_xaxes(title_text='State group EC votes if adjusted for popular vote turnout')
    fig.update_yaxes(title_text='Electoral college votes per state group')

    # axis tick overrides
    num_xticks = round(norm_max / 50) + 1
    layout = dict(xaxis=dict(tickmode='array', tickvals=[t*50 for t in range(num_xticks)]))
    fig.update_layout(layout)

    fig.update_layout(title_x=0.45)

    return fig


def build_ivw_by_state_group_scatter_bubbles(data_obj, groups_dir, max_small, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    group_aggs_by_year_df = data_obj.group_aggs_by_year_dfs[subdir]
    groups = GROUPS_FOR_DIR[groups_dir]

    # if frame is set, extract single-year data
    if frame:
        group_aggs_by_year_df = group_aggs_by_year_df[group_aggs_by_year_df[cols.YEAR] == frame]

    # calculate axis range boundaries
    ec_max = round(group_aggs_by_year_df[cols.EC_VOTES].max() * 1.1)
    weight_min = group_aggs_by_year_df[group_aggs_by_year_df[cols.AVG_WEIGHT] > 0][cols.AVG_WEIGHT].min() * 0.9
    weight_max = group_aggs_by_year_df[cols.AVG_WEIGHT].max() * 1.1

    # display metadata
    hover_data = {cols.VOTES_COUNTED: True, cols.STATE_COUNT: True, cols.STATES_IN_GROUP: True, cols.POP_PER_EC_SHORT: True}
    base_fig_title = 'Average Vote Weight Per Person Per Region'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        fig_title = f'{base_fig_title}: 1828 - 2020'

    # init figure with core properties
    fig = px.scatter(group_aggs_by_year_df, x=cols.EC_VOTES, y=cols.AVG_WEIGHT, 
                    size=cols.VOTES_COUNTED_PCT, color=cols.GROUP, hover_name=cols.GROUP, hover_data=hover_data, 
                    animation_frame=cols.YEAR, animation_group=cols.GROUP, # ignored if df is for single year
                    color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                    title=fig_title, width=WIDTH_HALF_PAGE, height=HEIGHT_HALF_PAGE_CRT, opacity=0.5,
                    log_y=True, size_max=80, range_x=[0, ec_max], range_y=[weight_min, weight_max])

    # scatterplot dot formatting
    fig.update_traces(marker=dict(line=dict(width=1, color='white')),
                    selector=dict(mode='markers'))

    # reference mean / quazi-linear regression line
    fig.add_trace(go.Scatter(x=[0,ec_max], y=[1,1], mode='lines', name='Nationwide mean', line=dict(color='black', width=1)))

    # axis labels
    fig.update_xaxes(title_text='Electoral college votes per group')
    fig.update_yaxes(title_text='Impact per individual voter per group')

    fig.update_layout(title_x=0.45)

    return fig


def build_ivw_by_state_group_line_chart(data_obj, groups_dir, max_small, frame):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    group_aggs_by_year_df = data_obj.group_aggs_by_year_dfs[subdir]
    groups = GROUPS_FOR_DIR[groups_dir]

    # display metadata
    hover_data = {cols.STATES_IN_GROUP: True, cols.EC_VOTES: True}
    avg_weight_min = group_aggs_by_year_df[group_aggs_by_year_df[cols.AVG_WEIGHT] > 0][cols.AVG_WEIGHT].min() * 0.8
    avg_weight_max = group_aggs_by_year_df[group_aggs_by_year_df[cols.AVG_WEIGHT] > 0][cols.AVG_WEIGHT].max() * 1.05
    base_fig_title = 'Average Vote Weight Per Ballot Cast For Each Election, Grouped By Region'
    fig_title = f'{base_fig_title}: (Highlighting {frame})'

    fig = px.line(group_aggs_by_year_df, x=cols.YEAR, y=cols.AVG_WEIGHT, color=cols.GROUP, hover_data=hover_data, 
                    color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                    width=WIDTH_FULL_PAGE, height=500, title=fig_title, 
    #               log_y=True
                )

    fig.update_layout(yaxis_range=[avg_weight_min, avg_weight_max])

    # axis labels
    fig.update_xaxes(title_text='Election Year')
    fig.update_yaxes(title_text='Average Vote Weight Per Ballot Cast')

    fig.add_trace(go.Scatter(x=[frame, frame], y=[avg_weight_min, avg_weight_max], 
                            mode='lines', name=frame, line=dict(color='black', width=1)))

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
