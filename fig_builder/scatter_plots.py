import plotly.express as px
import plotly.graph_objects as go

from data_processor.functions import get_era_for_year, map_to_subdir
from metadata import Columns, FigDimensions, GROUPS_FOR_DIR, GROUP_COLORS, YEAR_0, YEAR_N


cols = Columns()
fig_dims = FigDimensions()


def build_ivw_by_state_scatter_dots(data_obj, groups_dir, max_small, fig_width=None, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    pivot_on_year_df = data_obj.state_vote_weights_pivot_dfs[subdir]
    groups = GROUPS_FOR_DIR[groups_dir]

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] == frame].sort_values(cols.GROUP, ascending=True)

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.crt(fig_width)
    
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
        fig_title = f'{base_fig_title}: {YEAR_0} - {YEAR_N}'

    # init figure with core properties
    fig = px.scatter(pivot_on_year_df, x=cols.EC_VOTES_NORM, y=cols.EC_VOTES, color=cols.GROUP,  
                    animation_frame=cols.YEAR, # ignored if df is for single year
                    hover_name=cols.STATE, hover_data=hover_data,
                    color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                    title=fig_title, width=fig_width, height=fig_height, 
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


def build_ivw_by_state_scatter_abbrevs(data_obj, groups_dir, max_small, fig_width=None, frame=None):
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
        fig_title = f'{base_fig_title}: {YEAR_0} - {YEAR_N}'

    # init figure with core properties
    fig = px.scatter(pivot_on_year_df, x=cols.EC_VOTES_NORM, y=cols.EC_VOTES, color=cols.GROUP,  
                    animation_frame=cols.YEAR, # ignored if df is for single year
                    hover_name=cols.STATE, hover_data=hover_data, text=cols.ABBREV,
                    color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                    title=fig_title, width=fig_width, height=fig_height,
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


def build_ivw_by_state_scatter_bubbles(data_obj, groups_dir, max_small, fig_width=None, frame=None):
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
        fig_title = f'{base_fig_title}: {YEAR_0} - {YEAR_N}'

    # init figure with core properties
    fig = px.scatter(pivot_on_year_df, x=cols.EC_VOTES, y=cols.VOTE_WEIGHT, color=cols.GROUP, 
                    hover_name=cols.STATE, hover_data=hover_data, size=cols.VOTES_COUNTED_PCT, size_max=80, 
                    animation_frame=cols.YEAR, # ignored if df is for single year
                    color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                    title=fig_title, width=fig_width, height=fig_height,
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


def build_ivw_by_state_group_scatter_dots(data_obj, groups_dir, max_small, fig_width=None, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    group_aggs_by_year_df = data_obj.group_agg_weights_pivot_dfs[subdir]
    groups = GROUPS_FOR_DIR[groups_dir]

    # if frame is set, extract single-year data
    if frame:
        group_aggs_by_year_df = group_aggs_by_year_df[group_aggs_by_year_df[cols.YEAR] == frame]

    # remove the Nat'l Average data
    group_aggs_by_year_df = group_aggs_by_year_df.loc[~(group_aggs_by_year_df[cols.GROUP] == "Nat'l Average")]

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.crt(fig_width)

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
        fig_title = f'{base_fig_title}: {YEAR_0} - {YEAR_N}'

    # init figure with core properties
    fig = px.scatter(group_aggs_by_year_df, x=cols.EC_VOTES_NORM, y=cols.EC_VOTES, color=cols.GROUP, 
                    hover_name=cols.GROUP, hover_data=hover_data,
                    animation_frame=cols.YEAR, animation_group=cols.GROUP, # ignored if df is for single year
                    color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                    title=fig_title, width=fig_width, height=fig_height, 
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


def build_ivw_by_state_group_scatter_bubbles(data_obj, groups_dir, max_small, fig_width=None, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    group_aggs_by_year_df = data_obj.group_agg_weights_pivot_dfs[subdir]
    groups = GROUPS_FOR_DIR[groups_dir]

    # if frame is set, extract single-year data
    if frame:
        group_aggs_by_year_df = group_aggs_by_year_df[group_aggs_by_year_df[cols.YEAR] == frame]

    # remove the Nat'l Average data
    group_aggs_by_year_df = group_aggs_by_year_df.loc[~(group_aggs_by_year_df[cols.GROUP] == "Nat'l Average")]

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.crt(fig_width)

    # calculate axis range boundaries
    ec_max = round(group_aggs_by_year_df[cols.EC_VOTES].max() * 1.1)
    weight_min = group_aggs_by_year_df[group_aggs_by_year_df[cols.AVG_WEIGHT] > 0][cols.AVG_WEIGHT].min() * 0.9
    weight_max = group_aggs_by_year_df[cols.AVG_WEIGHT].max() * 1.1

    # display metadata
    hover_data = {cols.GROUP: False, cols.VOTES_COUNTED: True, cols.STATE_COUNT: True, cols.STATES_IN_GROUP: True, cols.POP_PER_EC_SHORT: True}
    base_fig_title = 'Average Vote Weight Per Person Per Region'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        fig_title = f'{base_fig_title}: {YEAR_0} - {YEAR_N}'

    # init figure with core properties
    fig = px.scatter(group_aggs_by_year_df, x=cols.EC_VOTES, y=cols.AVG_WEIGHT, color=cols.GROUP, 
                    size=cols.VOTES_COUNTED_PCT, size_max=80, hover_name=cols.GROUP, hover_data=hover_data, 
                    animation_frame=cols.YEAR, animation_group=cols.GROUP, # ignored if df is for single year
                    color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                    title=fig_title, width=fig_width, height=fig_height, 
                    opacity=0.5, log_y=True, range_x=[0, ec_max], range_y=[weight_min, weight_max])

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
