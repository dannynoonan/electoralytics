import math
import plotly.express as px
import plotly.graph_objects as go

from data_processor.functions import map_to_subdir, append_state_vw_pivot_to_groups_aggs_df
from metadata import (
    Columns, FigDimensions, GROUPS_FOR_DIR, GROUP_COLORS, COLORS_PLOTLY, GROUP_ALT_COLORS, GROUPS_COL_FOR_DIR,
    YEAR_0, YEAR_N, EVENTS, ERAS)


cols = Columns()
fig_dims = FigDimensions()


def build_ivw_by_state_group_line_chart(data_obj, groups_dir, max_small, fig_width=None, state_abbrevs=None, log_y=False):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    group_aggs_by_year_df = data_obj.group_agg_weights_pivot_dfs[subdir]
    groups = GROUPS_FOR_DIR[groups_dir]
    group_col = GROUPS_COL_FOR_DIR[groups_dir]

    # assign GROUP_COLORS to local var so it can be modified if states are added
    group_colors = GROUP_COLORS

    # hackish way to remove years where Average Weight is 0 from Postbellum and West Groups without removing it for Confederate or South Groups
    group_aggs_by_year_df = group_aggs_by_year_df.loc[~((group_aggs_by_year_df[cols.AVG_WEIGHT] == 0) & (group_aggs_by_year_df[cols.GROUP] == 'Postbellum'))]
    group_aggs_by_year_df = group_aggs_by_year_df.loc[~((group_aggs_by_year_df[cols.AVG_WEIGHT] == 0) & (group_aggs_by_year_df[cols.GROUP] == 'West'))]

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = 700

    # merge selected states into group aggs df
    if state_abbrevs:
        all_states_meta = data_obj.all_states_meta_df
        for state_abbrev in state_abbrevs:
            # extract state and group info for state_abbrev from all_states_meta df
            state = all_states_meta.loc[all_states_meta[cols.ABBREV] == state_abbrev][cols.STATE].item()
            state_group = all_states_meta.loc[all_states_meta[cols.ABBREV] == state_abbrev][group_col].item()
            # extract single-state data from vote weight pivot df
            state_vw_pivot_df = data_obj.get_single_state_vote_weight_pivot(state_abbrev, subdir=subdir)
            # append single-state df to group aggs df after transformation to sync their column names
            group_aggs_by_year_df = append_state_vw_pivot_to_groups_aggs_df(state_vw_pivot_df, group_aggs_by_year_df, group_colors)
            # update group_colors with additional color for state for line chart based on state's group mapping
            group_colors[state] = GROUP_ALT_COLORS[state_group]

    # display metadata
    hover_data = {cols.GROUP: False, cols.STATES_IN_GROUP: True, cols.EC_VOTES: True}
    avg_weight_min = group_aggs_by_year_df[group_aggs_by_year_df[cols.AVG_WEIGHT] > 0][cols.AVG_WEIGHT].min() * 0.8
    avg_weight_max = group_aggs_by_year_df[group_aggs_by_year_df[cols.AVG_WEIGHT] > 0][cols.AVG_WEIGHT].max() * 1.05
    print(f"avg_weight_min: {avg_weight_min}, avg_weight_max: {avg_weight_max}")
    if log_y:
        # log2_avg_weight_min = math.log(avg_weight_min, 2)
        # log2_avg_weight_max = math.log(avg_weight_max, 2)
        # print(f"log2_avg_weight_min: {log2_avg_weight_min}, log2_avg_weight_max: {log2_avg_weight_max}")
        avg_weight_min = math.log(avg_weight_min, 10)
        avg_weight_max = math.log(avg_weight_max, 10)
        print(f"log10 avg_weight_min: {avg_weight_min}, log10 avg_weight_max: {avg_weight_max}")
        # pow_avg_weight_min = math.pow(2, avg_weight_min)
        # pow_avg_weight_max = math.pow(2, avg_weight_max)
        # print(f"pow_avg_weight_min: {pow_avg_weight_min}, pow_avg_weight_max: {pow_avg_weight_max}")
        # sqrt_avg_weight_min = math.sqrt(avg_weight_min)
        # sqrt_avg_weight_max = math.sqrt(avg_weight_max)
        # print(f"sqrt_avg_weight_min: {sqrt_avg_weight_min}, sqrt_avg_weight_max: {sqrt_avg_weight_max}")

    fig_title = 'Average Vote Weight Per Ballot Cast For Each Election, Grouped By Region'

    fig = px.line(group_aggs_by_year_df, x=cols.YEAR, y=cols.AVG_WEIGHT, color=cols.GROUP, 
                    hover_name=cols.GROUP, hover_data=hover_data, 
                    color_discrete_map=group_colors, category_orders={cols.GROUP: groups},
                    title=fig_title, width=fig_width, height=fig_height, 
                    line_shape='spline', log_y=log_y)
    
    for i in range(len(fig.data)):
        fig.data[i].update(mode='markers+lines')

    fig.update_layout(xaxis_range=[YEAR_0, YEAR_N])
    fig.update_layout(yaxis_range=[avg_weight_min, avg_weight_max])

    # if not log_y:
    #     fig.update_layout(yaxis_range=[avg_weight_min, avg_weight_max])
    # else:
    #     fig.update_layout(yaxis_range=[-.3, .5])

    # axis labels
    fig.update_xaxes(title_text='Election Year')
    y_axis_text = 'Average Vote Weight Per Ballot Cast'
    if log_y:
        y_axis_text = f"{y_axis_text} (log)"
    fig.update_yaxes(title_text=y_axis_text)

    # add vertical line highlighting selected year (frame)
    # fig.add_trace(go.Scatter(x=[frame, frame], y=[avg_weight_min, avg_weight_max], 
    #                         mode='lines', name=frame, line=dict(color='pink', width=1)))

    # if not log_y:
    # build markers and labels marking events 
    event_markers = build_and_annotate_event_markers(fig, EVENTS, avg_weight_min, avg_weight_max)

    # build shaded blocks designating eras
    era_blocks = build_and_annotate_era_blocks(fig, ERAS, YEAR_0, avg_weight_max)

    # update layout with era_blocks and event_markers
    fig.update_layout(shapes=era_blocks + event_markers)

    return fig


def build_total_vote_line_chart(data_obj, fig_width=None):
    data_obj.load_totals_by_year()
    totals_by_year_df = data_obj.totals_by_year_df

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = 700

    # display metadata
    hover_data = {cols.YEAR: False, cols.VOTES_COUNTED: True, cols.TOTAL_POP: True, cols.EC_VOTES: True, cols.POP_PER_EC: True}
    vote_pct_max = totals_by_year_df[cols.VOTES_COUNTED_PCT_TOTAL_POP].max() * 1.1
    x_min = 1785
    fig_title = 'Ballots Cast as a Percentage of Total Population In Each Election'

    fig = px.line(totals_by_year_df, x=cols.YEAR, y=cols.VOTES_COUNTED_PCT_TOTAL_POP, 
                    hover_name=cols.YEAR, hover_data=hover_data, 
                    title=fig_title, width=fig_width, height=fig_height, 
                    line_shape='spline', 
                    # log_y=True
                    )

    for i in range(len(fig.data)):
        fig.data[i].update(mode='markers+lines')

    fig.update_layout(xaxis_range=[x_min, YEAR_N])
    fig.update_layout(yaxis_range=[0, vote_pct_max])

    # build markers and labels marking events 
    event_markers = build_and_annotate_event_markers(fig, EVENTS, 0, vote_pct_max)

    # build shaded blocks designating eras
    era_blocks = build_and_annotate_era_blocks(fig, ERAS, x_min, vote_pct_max)

    # update layout with era_blocks and event_markers
    fig.update_layout(shapes=era_blocks + event_markers)

    return fig


def build_and_annotate_event_markers(fig, events, y_min, y_max):
    # build markers and labels marking events 
    event_markers = []
    for event in events:
        # add vertical line for each event date
        marker = dict(type='line', line_width=1, x0=event['year'], x1=event['year'], y0=0, y1=y_max)
        event_markers.append(marker)
        # add annotation for each event name and description
        event_name = event['name']
        if str(event['year']) not in event['name']: 
            event_name = f"{event_name} ({event['year']})"
        fig.add_annotation(x=event['year'], y=y_max, text=event_name, showarrow=False, 
            yshift=-2, xshift=-7, textangle=-90, align='right', yanchor='top')
        if event.get('desc'):
            event_desc = f"<i>{event['desc']}</i>"
            fig.add_annotation(x=event['year'], y=y_min, text=event_desc, showarrow=False, 
                yshift=2, xshift=6, textangle=-90, align='left', yanchor='bottom')

    return event_markers


def build_and_annotate_era_blocks(fig, eras, x_min, y_max):
    # build shaded blocks designating eras
    era_blocks = []
    for era in eras:
        # add rectangle for each era date range
        block = dict(type='rect', line_width=0, x0=era['begin'], x1=era['end'], y0=0, y1=y_max, 
                    fillcolor=era['color'], opacity=0.1)
        era_blocks.append(block) 
        # add annotation for each era
        era_begin = era['begin']
        if era_begin < x_min:
            era_begin = x_min
        era_len = era['end'] - era_begin
        era_mid = (era['end'] + era_begin) / 2
        showarrow = False
        yshift = 8
        if era_len < 10:
            showarrow = True
            yshift = 0
        
        era_name = f"<b>{era['name']}</b>"
        fig.add_annotation(x=era_mid, y=y_max, text=era_name, showarrow=showarrow, yshift=yshift)

    return era_blocks