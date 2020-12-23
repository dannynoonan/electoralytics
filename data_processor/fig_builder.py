import math
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from data_processor.functions import get_era_for_year, apply_animation_settings
from metadata import (
    GEN_DATA_DIR, GEN_ALT_GROUP_DIR, GEN_NO_SMALL_DIR, GEN_ALT_GROUP_NO_SMALL_DIR, 
    ACW_GROUPS, CENSUS_GROUPS, GROUP_COLORS, PARTIES, PARTY_COLORS, FRAME_RATE,
    COL_ABBREV, COL_STATE, COL_GROUP, COL_YEAR, COL_EC_VOTES, COL_EC_VOTES_NORM, 
    COL_VOTES_COUNTED, COL_VOTES_COUNTED_PCT, COL_VOTE_WEIGHT, COL_LOG_VOTE_WEIGHT, COL_AVG_WEIGHT, 
    COL_POP_PER_EC, COL_POP_PER_EC_SHORT, COL_PARTY, COL_STATE_COUNT, COL_STATES_IN_GROUP
)


BAR_WIDTH=800
BAR_HEIGHT=800
SCATTER_WIDTH=800
SCATTER_HEIGHT=600
MAP_WIDTH=800
MAP_HEIGHT=600
BOX_WIDTH=800
BOX_HEIGHT=600
LINE_WIDTH=1640
LINE_HEIGHT=500


def build_ivw_by_state_bar(data_obj, frame=None, subdir=None):
    if not subdir:
        subdir = GEN_DATA_DIR
    pivot_on_year_df = data_obj.pivot_on_year_dfs[subdir]

    # shift to altGroup if specified by subdir 
    groups = ACW_GROUPS
    if subdir in [GEN_ALT_GROUP_DIR, GEN_ALT_GROUP_NO_SMALL_DIR]:
        groups = CENSUS_GROUPS

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[COL_YEAR] == frame]

    # remove placeholder rows for state groups that lack actual state data
    pivot_on_year_df = pivot_on_year_df[pd.notnull(pivot_on_year_df[COL_STATE])]

    # display metadata
    hover_data = {COL_PARTY: False, COL_VOTES_COUNTED: True, COL_EC_VOTES: True, COL_POP_PER_EC_SHORT: True, COL_EC_VOTES_NORM: True,
                COL_STATE: False}
    # category_orders = {COL_PARTY: PARTIES}
    # color_discrete_sequence = [PARTY_COLORS[p] for p in PARTIES]
    category_orders = {COL_GROUP: groups}
    color_discrete_sequence = [GROUP_COLORS[g] for g in groups]
    # fig_title = f'{year} Presidential Election: Comparative Vote Weight Per Ballot Cast Per State'
    base_fig_title = 'Vote Weight Per Ballot Cast Per State'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        base_fig_title = 'Voter impact by state'
        fig_title = f'{base_fig_title}: 1828 - 2020'
    
    # declare fig
    fig = px.bar(pivot_on_year_df, x=COL_VOTE_WEIGHT, y=COL_STATE, color=COL_GROUP, hover_name=COL_STATE, hover_data=hover_data,
                # category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
                animation_frame=COL_YEAR, # ignored if df is for single year
                labels={COL_VOTE_WEIGHT: 'Relative impact per voter'}, width=BAR_WIDTH, height=BAR_HEIGHT, title=fig_title)

    fig.update_layout(
        yaxis={'tickangle': 35, 'showticklabels': True, 'type': 'category', 'tickfont_size': 8},
        yaxis_categoryorder='total ascending',
    )

    return fig


# ref: https://towardsdatascience.com/how-to-create-a-grouped-bar-chart-with-plotly-express-in-python-e2b64ed4abd7
def build_actual_vs_adjusted_ec_bar(data_obj, frame=None, subdir=None):
    if not subdir:
        subdir = GEN_DATA_DIR
    melted_pivot_on_year_df = data_obj.melted_pivot_on_year_dfs[subdir]

    # if frame is set, extract single-year data
    if frame:
        melted_pivot_on_year_df = melted_pivot_on_year_df[melted_pivot_on_year_df[COL_YEAR] == frame]

    # remove placeholder rows for state groups that lack actual state data
    melted_pivot_on_year_df = melted_pivot_on_year_df[pd.notnull(melted_pivot_on_year_df[COL_STATE])]

    # display metadata
    hover_data = {COL_PARTY: False, 'Actual vs Adjusted EC votes^': False, COL_VOTES_COUNTED: True, COL_POP_PER_EC_SHORT: True,
                COL_STATE: False}
    color_discrete_sequence = ['LimeGreen','DarkGreen']
    base_fig_title = 'Actual EC Votes vs EC Votes Adjusted For Turnout'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        base_fig_title = 'Voter impact by state'
        fig_title = f'{base_fig_title}: 1828 - 2020'

    fig = px.bar(melted_pivot_on_year_df, x='EC votes^', y=COL_STATE,  
                color='Actual vs Adjusted EC votes^', barmode='group', hover_name=COL_STATE, hover_data=hover_data,
                animation_frame=COL_YEAR, # ignored if df is for single year
                color_discrete_sequence=color_discrete_sequence, width=BAR_WIDTH, height=BAR_HEIGHT, title=fig_title)

    fig.update_layout(
        yaxis={'tickangle': 35, 'showticklabels': True, 'type': 'category', 'tickfont_size': 8},
        yaxis_categoryorder='total descending'
    )
    fig.update_xaxes(title_text='Actual EC votes / EC Votes If Adjusted For Popular Vote Turnout')

    return fig


def build_ivw_by_state_map(data_obj, frame=None, subdir=None):
    if not subdir:
        subdir = GEN_DATA_DIR
    pivot_on_year_df = data_obj.pivot_on_year_dfs[subdir]

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[COL_YEAR] == frame]

    # generate COL_LOG_VOTE_WEIGHT column, workaround to manually create log color scale
    # pivot_on_single_year[COL_LOG_VOTE_WEIGHT] = np.log2(pivot_on_single_year[COL_VOTE_WEIGHT])

    # log_vote_weight_ser = pivot_on_year_df[COL_LOG_VOTE_WEIGHT].replace([np.inf, -np.inf], np.nan).dropna()
    # log_vote_weight_min = log_vote_weight_ser.min()
    # log_vote_weight_max = log_vote_weight_ser.max()
    # vote_weight_ser = pivot_on_year_df[COL_VOTE_WEIGHT].replace([np.inf, -np.inf], np.nan).dropna()
    # vote_weight_min = vote_weight_ser.min()
    # vote_weight_max = vote_weight_ser.max()

    # display metadata
    hover_data = {COL_YEAR: False, COL_ABBREV: False, COL_LOG_VOTE_WEIGHT: False, COL_GROUP: True,
                COL_VOTES_COUNTED: True, COL_EC_VOTES: True, COL_VOTE_WEIGHT: True, COL_POP_PER_EC_SHORT: True, 
                COL_EC_VOTES_NORM: True}
    # map_title = f'{year} presidential election: Vote weight per person per state'
    base_fig_title = 'Vote Weight Per Person Per State'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        base_fig_title = 'Voter impact by state'
        fig_title = f'{base_fig_title}: 1828 - 2020'

    fig = px.choropleth(pivot_on_year_df, locations=COL_ABBREV, color=COL_LOG_VOTE_WEIGHT,
                        locationmode='USA-states', scope="usa", hover_name=COL_STATE, hover_data=hover_data, 
                        color_continuous_scale=px.colors.diverging.BrBG[::-1], color_continuous_midpoint=0,
                        # range_color=[-1.0, pivot_on_single_year[COL_LOG_VOTE_WEIGHT].max()],
                        # range_color=[log_vote_weight_min, log_vote_weight_max],  
                        animation_frame=COL_YEAR, # ignored if df is for single year
                        title=fig_title, width=MAP_WIDTH, height=MAP_HEIGHT)

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


def build_ivw_by_state_scatter_dots(data_obj, frame=None, subdir=None):
    if not subdir:
        subdir = GEN_DATA_DIR
    pivot_on_year_df = data_obj.pivot_on_year_dfs[subdir]

    # shift to altGroup if specified by subdir 
    groups = ACW_GROUPS
    if subdir in [GEN_ALT_GROUP_DIR, GEN_ALT_GROUP_NO_SMALL_DIR]:
        groups = CENSUS_GROUPS

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[COL_YEAR] == frame]
    
    # calculate axis range boundaries 
    ec_max = round(pivot_on_year_df[COL_EC_VOTES].max() * 1.05)
    norm_max = round(pivot_on_year_df[COL_EC_VOTES_NORM].max() * 1.05)

    # display metadata
    hover_data = {COL_VOTES_COUNTED: True, COL_VOTE_WEIGHT: True, COL_POP_PER_EC_SHORT: True}
    category_orders = {COL_GROUP: groups}
    color_discrete_sequence = [GROUP_COLORS[g] for g in groups]
    base_fig_title = 'Vote Weight Per Person Per State'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        base_fig_title = 'Voter impact by state'
        fig_title = f'{base_fig_title}: 1828 - 2020'

    # init figure with core properties
    fig = px.scatter(pivot_on_year_df, x=COL_EC_VOTES_NORM, y=COL_EC_VOTES, 
                    animation_frame=COL_YEAR, # ignored if df is for single year
                    color=COL_GROUP, title=fig_title, 
                    hover_name=COL_STATE, hover_data=hover_data,
                    # category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
    #                  log_x=True, log_y=True, range_x=[.4,norm_max], range_y=[2,ec_max],
                    width=SCATTER_WIDTH, height=SCATTER_HEIGHT, opacity=0.7, range_x=[0,norm_max], range_y=[0,ec_max])
    
    # scatterplot dot formatting
    fig.update_traces(marker=dict(size=24, line=dict(width=1, color='DarkSlateGrey')), 
                    selector=dict(mode='markers'))

    # reference mean / quazi-linear regression line
    fig.add_trace(go.Scatter(x=[0,ec_max], y=[0,ec_max], mode='lines', 
                            name='Nationwide mean', line=dict(color='black', width=1)))

    # axis labels
    fig.update_xaxes(title_text='State EC votes if adjusted for popular vote turnout')
    fig.update_yaxes(title_text='Electoral college votes per state')

    fig.update_layout(title_x=0.45)

    return fig


def build_ivw_by_state_scatter_abbrevs(data_obj, frame=None, subdir=None):
    if not subdir:
        subdir = GEN_DATA_DIR
    pivot_on_year_df = data_obj.pivot_on_year_dfs[subdir]

    # shift to altGroup if specified by subdir 
    groups = ACW_GROUPS
    if subdir in [GEN_ALT_GROUP_DIR, GEN_ALT_GROUP_NO_SMALL_DIR]:
        groups = CENSUS_GROUPS

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[COL_YEAR] == frame]

    # calculate axis range boundaries 
    ec_max = round(pivot_on_year_df[COL_EC_VOTES].max() * 1.05)
    norm_max = round(pivot_on_year_df[COL_EC_VOTES_NORM].max() * 1.05)

    # display metadata
    hover_data = {COL_VOTES_COUNTED: True, COL_VOTE_WEIGHT: True, COL_POP_PER_EC_SHORT: True}
    category_orders = {COL_GROUP: groups}
    color_discrete_sequence = [GROUP_COLORS[g] for g in groups]
    base_fig_title = 'Vote Weight Per Person Per State'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        base_fig_title = 'Voter impact by state'
        fig_title = f'{base_fig_title}: 1828 - 2020'

    # init figure with core properties
    fig = px.scatter(pivot_on_year_df, x=COL_EC_VOTES_NORM, y=COL_EC_VOTES, 
                    color=COL_GROUP, title=fig_title, 
                    animation_frame=COL_YEAR, # ignored if df is for single year
                    hover_name=COL_STATE, hover_data=hover_data, text=COL_ABBREV,
                    # category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
                    log_x=True, log_y=True, range_x=[.4,norm_max], range_y=[2.5,ec_max],
                    width=SCATTER_WIDTH, height=SCATTER_HEIGHT, opacity=0.7)
        
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


def build_ivw_by_state_scatter_bubbles(data_obj, frame=None, subdir=None):
    if not subdir:
        subdir = GEN_DATA_DIR
    pivot_on_year_df = data_obj.pivot_on_year_dfs[subdir]

    # shift to altGroup if specified by subdir 
    groups = ACW_GROUPS
    if subdir in [GEN_ALT_GROUP_DIR, GEN_ALT_GROUP_NO_SMALL_DIR]:
        groups = CENSUS_GROUPS

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[COL_YEAR] == frame]

    # calculate axis range boundaries 
    ec_max = round(pivot_on_year_df[COL_EC_VOTES].max())
    weight_min = pivot_on_year_df[pivot_on_year_df[COL_VOTE_WEIGHT] > 0][COL_VOTE_WEIGHT].min() * 0.9
    weight_max = pivot_on_year_df[COL_VOTE_WEIGHT].max()

    # display metadata
    hover_data = {COL_VOTES_COUNTED: True, COL_POP_PER_EC_SHORT: True}
    category_orders = {COL_GROUP: groups}
    color_discrete_sequence = [GROUP_COLORS[g] for g in groups]
    base_fig_title = 'Vote Weight Per Person Per State'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        base_fig_title = 'Voter impact by state'
        fig_title = f'{base_fig_title}: 1828 - 2020'

    # init figure with core properties
    fig = px.scatter(pivot_on_year_df, x=COL_EC_VOTES, y=COL_VOTE_WEIGHT, 
                    size=COL_VOTES_COUNTED_PCT, color=COL_GROUP, hover_name=COL_STATE, hover_data=hover_data, 
                    animation_frame=COL_YEAR, # ignored if df is for single year
                    # category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
                    title=fig_title, width=SCATTER_WIDTH, height=SCATTER_HEIGHT, opacity=0.5,
                    log_y=True, size_max=80, range_x=[0,ec_max], range_y=[weight_min,weight_max])

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


def build_ivw_by_state_group_box_plot(data_obj, year, subdir=None):
    if not subdir:
        subdir = GEN_DATA_DIR
    pivot_on_year_df = data_obj.pivot_on_year_dfs[subdir]

    # shift to altGroup if specified by subdir 
    groups = ACW_GROUPS
    if subdir in [GEN_ALT_GROUP_DIR, GEN_ALT_GROUP_NO_SMALL_DIR]:
        groups = CENSUS_GROUPS

    # extract single-year data
    pivot_on_single_year = pivot_on_year_df[pivot_on_year_df[COL_YEAR] == year].sort_values(COL_PARTY, ascending=True)

    # display metadata
    category_orders = {COL_GROUP: groups}
    color_discrete_sequence = [GROUP_COLORS[g] for g in groups]
    # box_title = f'{year} presidential election: voter impact by state grouping'
    era = get_era_for_year(year)
    fig_title = f'Ranges of Vote Weight Per Person Per Regional Grouping: {year} ({era})'

    # box plot
    box_data = pivot_on_single_year[[COL_GROUP, COL_VOTE_WEIGHT]]
    pivot = box_data.pivot(columns=COL_GROUP, values=COL_VOTE_WEIGHT)

    fig = px.box(pivot, color=COL_GROUP, 
                # category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
                width=BOX_WIDTH, height=BOX_HEIGHT, log_y=True, title=fig_title)

    # fig.add_trace(go.Scatter(x=flat_data['EC votes'], y=flat_data['Mean vote weight'], 
    #                          mode='lines', name=trace_name_natl_avg, line=dict(color='black', width=1)))

    fig.update_xaxes(title_text='')
    fig.update_yaxes(title_text='Range of Vote Weight Per Person Within Regional Grouping')
    fig.update_layout(title_x=0.46)
    return fig


def build_state_groups_map(data_obj, year, subdir=None):
    if not subdir:
        subdir = GEN_DATA_DIR
    pivot_on_year_df = data_obj.pivot_on_year_dfs[subdir]

    # shift to altGroup if specified by subdir 
    groups = ACW_GROUPS
    if subdir in [GEN_ALT_GROUP_DIR, GEN_ALT_GROUP_NO_SMALL_DIR]:
        groups = CENSUS_GROUPS

    # extract single-year data
    pivot_on_single_year = pivot_on_year_df[pivot_on_year_df[COL_YEAR] == year]

    # generate COL_LOG_VOTE_WEIGHT column, workaround to manually create log color scale
    # pivot_on_single_year[COL_LOG_VOTE_WEIGHT] = np.log2(pivot_on_single_year[COL_VOTE_WEIGHT])

    # display metadata
    hover_data = {COL_YEAR: False, COL_ABBREV: False, COL_GROUP: True, COL_VOTES_COUNTED: True, 
              COL_EC_VOTES: True, COL_VOTE_WEIGHT: True, COL_POP_PER_EC_SHORT: True, COL_EC_VOTES_NORM: True}
    category_orders = {COL_GROUP: groups}
    color_discrete_sequence = [GROUP_COLORS[g] for g in groups]
    era = get_era_for_year(year)
    fig_title = f'Regional Groupings During {year} Presidential Election ({era})'

    fig = px.choropleth(pivot_on_single_year, locations=COL_ABBREV, color=COL_GROUP, 
                        locationmode='USA-states', scope="usa", hover_name=COL_STATE, hover_data=hover_data, 
                        # category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
                        title=fig_title, width=MAP_WIDTH, height=MAP_HEIGHT)

    return fig


def build_ivw_by_state_group_scatter_dots(data_obj, year, subdir=None):
    if not subdir:
        subdir = GEN_DATA_DIR
    group_aggs_by_year_df = data_obj.group_aggs_by_year_dfs[subdir]

    # shift to altGroup if specified by subdir 
    groups = ACW_GROUPS
    if subdir in [GEN_ALT_GROUP_DIR, GEN_ALT_GROUP_NO_SMALL_DIR]:
        groups = CENSUS_GROUPS

    # extract single-year data
    group_aggs_by_single_year = group_aggs_by_year_df[group_aggs_by_year_df[COL_YEAR] == year]

    # calculate axis range boundaries
    ec_max = round(group_aggs_by_single_year[COL_EC_VOTES].max() * 1.05)
    #pop_max = round(group_aggs_by_year[COL_VOTES_COUNTED].max() * 1.05)
    norm_max = round(group_aggs_by_single_year[COL_EC_VOTES_NORM].max() * 1.05)

    # display metadata
    hover_data = {COL_VOTES_COUNTED: True, COL_AVG_WEIGHT: True, COL_POP_PER_EC_SHORT: True,
                COL_STATE_COUNT: True, COL_STATES_IN_GROUP: True}
    category_orders = {COL_GROUP: groups}
    color_discrete_sequence = [GROUP_COLORS[g] for g in groups]
    era = get_era_for_year(year)
    fig_title = f'Average Vote Weight Per Person Per Regional Grouping: {year} ({era})'

    # init figure with core properties
    fig = px.scatter(group_aggs_by_single_year, x=COL_EC_VOTES_NORM, y=COL_EC_VOTES, 
                    # animation_frame=COL_YEAR, animation_group=COL_GROUP, 
                    color=COL_GROUP, title=fig_title, hover_name=COL_GROUP, hover_data=hover_data,
                    # category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
    #                  log_x=True, log_y=True, range_x=[.4,norm_max], range_y=[2,ec_max],
                    width=SCATTER_WIDTH, height=SCATTER_HEIGHT, opacity=0.7, range_x=[0, norm_max], range_y=[0, ec_max])
        
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


def build_ivw_by_state_group_scatter_bubbles(data_obj, year, subdir=None):
    if not subdir:
        subdir = GEN_DATA_DIR
    group_aggs_by_year_df = data_obj.group_aggs_by_year_dfs[subdir]

    # shift to altGroup if specified by subdir 
    groups = ACW_GROUPS
    if subdir in [GEN_ALT_GROUP_DIR, GEN_ALT_GROUP_NO_SMALL_DIR]:
        groups = CENSUS_GROUPS

    # extract single-year data
    group_aggs_by_single_year = group_aggs_by_year_df[group_aggs_by_year_df[COL_YEAR] == year]

    # calculate axis range boundaries
    ec_max = round(group_aggs_by_single_year[COL_EC_VOTES].max() * 1.1)
    weight_min = group_aggs_by_single_year[group_aggs_by_single_year[COL_AVG_WEIGHT] > 0][COL_AVG_WEIGHT].min() * 0.9
    weight_max = group_aggs_by_single_year[COL_AVG_WEIGHT].max() * 1.1

    # display metadata
    hover_data = {COL_VOTES_COUNTED: True, COL_STATE_COUNT: True, COL_STATES_IN_GROUP: True, COL_POP_PER_EC_SHORT: True}
    category_orders = {COL_GROUP: groups}
    color_discrete_sequence = [GROUP_COLORS[g] for g in groups]
    era = get_era_for_year(year)
    fig_title = f'Average Vote Weight Per Person Per Regional Grouping: {year} ({era})'

    # init figure with core properties
    fig = px.scatter(group_aggs_by_single_year, x=COL_EC_VOTES, y=COL_AVG_WEIGHT, 
                    # animation_frame=COL_YEAR, animation_group=COL_GROUP, 
                    size=COL_VOTES_COUNTED_PCT, color=COL_GROUP, hover_name=COL_GROUP, hover_data=hover_data, 
                    # category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
                    title=fig_title, width=SCATTER_WIDTH, height=SCATTER_HEIGHT, opacity=0.5,
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


def build_ivw_by_state_group_line_chart(data_obj, year, subdir=None):
    if not subdir:
        subdir = GEN_DATA_DIR
    group_aggs_by_year_df = data_obj.group_aggs_by_year_dfs[subdir]

    # shift to altGroup if specified by subdir 
    groups = ACW_GROUPS
    if subdir in [GEN_ALT_GROUP_DIR, GEN_ALT_GROUP_NO_SMALL_DIR]:
        groups = CENSUS_GROUPS

    # display metadata
    hover_data = {COL_STATES_IN_GROUP: True, COL_EC_VOTES: True}
    category_orders = {COL_GROUP: groups}
    color_discrete_sequence = [GROUP_COLORS[g] for g in groups]
    avg_weight_min = group_aggs_by_year_df[group_aggs_by_year_df[COL_AVG_WEIGHT] > 0][COL_AVG_WEIGHT].min() * 0.8
    avg_weight_max = group_aggs_by_year_df[group_aggs_by_year_df[COL_AVG_WEIGHT] > 0][COL_AVG_WEIGHT].max() * 1.05
    fig_title = f'Average Vote Weight Per Ballot Cast For Each Election, Grouped By Region (Highlighting {year})'

    fig = px.line(group_aggs_by_year_df, x=COL_YEAR, y=COL_AVG_WEIGHT, color=COL_GROUP, hover_data=hover_data, 
                    width=LINE_WIDTH, height=LINE_HEIGHT, title=fig_title, 
    #               log_y=True
                )

    fig.update_layout(yaxis_range=[avg_weight_min, avg_weight_max])

    # axis labels
    fig.update_xaxes(title_text='Election Year')
    fig.update_yaxes(title_text='Average Vote Weight Per Ballot Cast')

    fig.add_trace(go.Scatter(x=[year, year], y=[avg_weight_min, avg_weight_max], 
                            # category_orders=category_orders, color_discrete_sequence=color_discrete_sequence, 
                            mode='lines', name=year, line=dict(color='black', width=1)))

    return fig


# def build_ivw_by_state_map_anim(data_obj, subdir=None):
#     if not subdir:
#         subdir = GEN_DATA_DIR
#     pivot_on_year_df = data_obj.pivot_on_year_dfs[subdir]

#     # generate COL_LOG_VOTE_WEIGHT column, workaround to manually create log color scale
#     # pivot_on_single_year[COL_LOG_VOTE_WEIGHT] = np.log2(pivot_on_single_year[COL_VOTE_WEIGHT])

#     # log_vote_weight_ser = pivot_on_year_df[COL_LOG_VOTE_WEIGHT].replace([np.inf, -np.inf], np.nan).dropna()
#     # log_vote_weight_min = log_vote_weight_ser.min()
#     # log_vote_weight_max = log_vote_weight_ser.max()
#     # vote_weight_ser = pivot_on_year_df[COL_VOTE_WEIGHT].replace([np.inf, -np.inf], np.nan).dropna()
#     # vote_weight_min = vote_weight_ser.min()
#     # vote_weight_max = vote_weight_ser.max()

#     # display metadata
#     hover_data = {COL_YEAR: False, COL_ABBREV: False, COL_LOG_VOTE_WEIGHT: False, COL_GROUP: True,
#                 COL_VOTES_COUNTED: True, COL_EC_VOTES: True, COL_VOTE_WEIGHT: True, COL_POP_PER_EC_SHORT: True, 
#                 COL_EC_VOTES_NORM: True}
#     fig_title = 'Vote Weight Per Person Per State'

#     fig = px.choropleth(pivot_on_year_df, locations=COL_ABBREV, color=COL_LOG_VOTE_WEIGHT,
#                         locationmode='USA-states', scope="usa", hover_name=COL_STATE, hover_data=hover_data, 
#                         color_continuous_scale=px.colors.diverging.BrBG[::-1], animation_frame=COL_YEAR,
#                         # range_color=[-1.0, pivot_on_single_year[COL_LOG_VOTE_WEIGHT].max()],
#                         # range_color=[log_vote_weight_min, log_vote_weight_max],
#                         color_continuous_midpoint=0,
#                         title=fig_title, width=MAP_WIDTH, height=MAP_HEIGHT)

#     fig.update_layout(
#         coloraxis_colorbar=dict(tickvals=[-2.303, -1.609, -1.109, -0.693, -0.357, 0, 0.405, 0.916, 1.386, 1.792, 2.197],
#                                 ticktext=['0.1', '0.2', '0.33', '0.5', '0.7', '1.0', '1.5', '2.5', '4', '6', '9']))

#     return fig


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
