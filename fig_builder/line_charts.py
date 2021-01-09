import math
import plotly.express as px
import plotly.graph_objects as go

from data_processor.functions import map_to_subdir, append_state_vw_pivot_to_groups_aggs_df
from fig_builder.line_charts_helper import build_and_annotate_event_markers, build_and_annotate_era_blocks
from metadata import (
    Columns, FigDimensions, GROUPS_FOR_DIR, GROUP_COLORS, GROUP_ALT_COLORS, GROUPS_COL_FOR_DIR,
    YEAR_0, YEAR_N, EVENTS, ERAS)


cols = Columns()
fig_dims = FigDimensions()


TRACE_MAX_FOR_EXPANDED_HOVERDATA = 5
TRACE_MAX_FOR_HOVERMODE_X = 7
MAX_TRACE_COUNT = 22


def build_ivw_by_state_group_line_chart(data_obj, groups_dir, max_small, fig_width=None, fig_height=None, state_abbrevs=None, log_y=False, 
                                        display_groups=True, display_eras=True, display_events=True):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    data_obj.load_totals_by_year
    group_aggs_by_year_df = data_obj.group_agg_weights_pivot_dfs[subdir]
    groups = GROUPS_FOR_DIR[groups_dir]
    group_col = GROUPS_COL_FOR_DIR[groups_dir]

    # assign GROUP_COLORS to local var so it can be modified if states are added
    group_colors = GROUP_COLORS

    # if we're hiding groups, drop everything from df except Nat'l Average data
    if not display_groups:
        group_aggs_by_year_df = group_aggs_by_year_df[group_aggs_by_year_df[cols.GROUP] == "Nat'l Average"]
    else:
        # hackish way to remove years where Average Weight is 0 from Postbellum and West Groups without removing it for Confederate or South Groups
        group_aggs_by_year_df = group_aggs_by_year_df.loc[~((group_aggs_by_year_df[cols.AVG_WEIGHT] == 0) & (group_aggs_by_year_df[cols.GROUP] == 'Postbellum'))]
        group_aggs_by_year_df = group_aggs_by_year_df.loc[~((group_aggs_by_year_df[cols.AVG_WEIGHT] == 0) & (group_aggs_by_year_df[cols.GROUP] == 'West'))]

    if not fig_width:
        fig_width = fig_dims.MD6
    if not fig_height:
        fig_height = 700

    # trace_count
    trace_count = 1  # 1 for Nat'l Avg
    if display_groups:
        trace_count = trace_count + 4  # 4 for groups
        if max_small > 0:
            trace_count = trace_count + 1  # 1 for small group
    if state_abbrevs:
        trace_count = trace_count + len(state_abbrevs)  # 1 for each state
    # secretly throttle trace_count shhhh... TODO handle this on front end
    while trace_count > MAX_TRACE_COUNT:
        state_abbrevs.pop()
        trace_count = trace_count-1

    # merge selected states into group aggs df
    if state_abbrevs:
        all_states_meta = data_obj.all_states_meta_df
        group_counters = {}
        for state_abbrev in state_abbrevs:
            # extract state and group info for state_abbrev from all_states_meta df
            state = all_states_meta.loc[all_states_meta[cols.ABBREV] == state_abbrev][cols.STATE].item()
            state_group = all_states_meta.loc[all_states_meta[cols.ABBREV] == state_abbrev][group_col].item()
            # extract single-state data from vote weight pivot df
            state_vw_pivot_df = data_obj.get_single_state_vote_weight_pivot(state_abbrev, subdir=subdir)
            # append single-state df to group aggs df after transformation to sync their column names
            group_aggs_by_year_df = append_state_vw_pivot_to_groups_aggs_df(state_vw_pivot_df, group_aggs_by_year_df, group_colors)
            # update group_colors with additional color for state for line chart based on state's group mapping
            # funky logic to assign a potentially endless number of states to one of three color variants for any given group
            if state_group in group_counters:
                grp_ctr = group_counters[state_group] % 3
            else:
                grp_ctr = 0
            alt_group_label = f"{state_group}{grp_ctr}"
            group_colors[state] = GROUP_ALT_COLORS[alt_group_label]
            group_counters[state_group] = grp_ctr+1    

    # display metadata
    custom_data = [cols.GROUP, cols.STATES_IN_GROUP, cols.EC_VOTES, cols.VOTES_COUNTED, cols.POP_PER_EC_SHORT]
    fig_title = 'Average Vote Weight Per Ballot Cast For Each Election'
    if display_groups:
        fig_title = f"{fig_title}, Grouped By Region"
    if trace_count >= MAX_TRACE_COUNT:
        fig_title = f"{fig_title} [** MAXES OUT AT 22 LINES **]"
    # TODO not sure the best way to organize this. I think it's only necessary because of inconsistencies in how plotly 
    # translates log values for y0 and y1. When I have time I'll file a bug or post to stackoverflow. 
    avg_weight_min = group_aggs_by_year_df[group_aggs_by_year_df[cols.AVG_WEIGHT] > 0][cols.AVG_WEIGHT].min() * 0.9
    avg_weight_max = group_aggs_by_year_df[group_aggs_by_year_df[cols.AVG_WEIGHT] > 0][cols.AVG_WEIGHT].max() * 1.05
    orig_avg_weight_min = avg_weight_min
    orig_avg_weight_max = avg_weight_max
    if log_y:
        avg_weight_min = math.log(avg_weight_min, 10)
        avg_weight_max = math.log(avg_weight_max, 10) * 1.05
        orig_avg_weight_max = orig_avg_weight_max * 1.05 

    fig = px.line(group_aggs_by_year_df, x=cols.YEAR, y=cols.AVG_WEIGHT, color=cols.GROUP, title=fig_title, 
                    color_discrete_map=group_colors, category_orders={cols.GROUP: groups}, custom_data=custom_data,
                    width=fig_width, height=fig_height, line_shape='spline', log_y=log_y)
    
    for i in range(len(fig.data)):
        fig.data[i].update(mode='markers+lines')

    # axis labels
    fig.update_xaxes(title_text='Election Year')
    y_axis_text = 'Average Vote Weight Per Ballot Cast'
    if log_y:
        y_axis_text = f"{y_axis_text} (log)"
    fig.update_yaxes(title_text=y_axis_text)

    # have x axis ticks every 20 years from 1840-2020
    x_axis_ticks = dict(tickmode='array', tickvals=[x*20 for x in range(92, 102)])

    # update layout and axes
    fig.update_layout(xaxis_range=[YEAR_0, YEAR_N], yaxis_range=[avg_weight_min, avg_weight_max], plot_bgcolor='white', xaxis=x_axis_ticks)
    if trace_count <= TRACE_MAX_FOR_HOVERMODE_X:
        fig.update_layout(hovermode="x")
    fig.update_xaxes(gridcolor='#DDDDDD')
    fig.update_yaxes(gridcolor='#DDDDDD')

    shapes = []
    # if display_events, add markers and labels designating events 
    if display_events:
        event_markers = build_and_annotate_event_markers(fig, EVENTS, avg_weight_min, avg_weight_max, y_min2=orig_avg_weight_min, y_max2=orig_avg_weight_max)
        shapes.extend(event_markers)
    # if display_eras, add shaded blocks and labels designating eras
    if display_eras:
        era_blocks = build_and_annotate_era_blocks(fig, ERAS, YEAR_0, orig_avg_weight_min, orig_avg_weight_max, y_max2=avg_weight_max)
        shapes.extend(era_blocks)
    fig.update_layout(shapes=shapes)

    # TODO where are x, y, and customdata actually defined, in fig? I'd like to avoid these redundant key-value mappings and use an f-string for this but not sure how
    # if trace_count < TRACE_MAX_FOR_EXPANDED_HOVERDATA <= TRACE_MAX_FOR_HOVERMODE_X:
    if trace_count <= TRACE_MAX_FOR_EXPANDED_HOVERDATA or trace_count > TRACE_MAX_FOR_HOVERMODE_X:
        fig.update_traces(
            hovertemplate="<br>".join([
                "<b>%{customdata[0]}</b> (%{x})<br></b>",
                "Average weight: <b>%{y:.2f}</b>",
                "States in group: <b>%{customdata[1]}</b>",
                "Combined EC votes: <b>%{customdata[2]:,}</b>",
                "Votes counted: <b>%{customdata[3]:,}</b>",
                "Avg pop per EC vote: <b>%{customdata[4]:,}</b>",
            ])
        )
    else:
        fig.update_traces(
            hovertemplate="<br>".join([
                "<b>%{customdata[0]}</b> (%{x})<br></b>",
                "Average weight: <b>%{y:.2f}</b>",
                "States in group: <b>%{customdata[1]}</b>",
                "Combined EC votes: <b>%{customdata[2]:,}</b>",
            ])
        )

    return fig


def build_total_vote_line_chart(data_obj, fig_width=None, log_y=False,):
    data_obj.load_totals_by_year()
    totals_by_year_df = data_obj.totals_by_year_df

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = 700

    # display metadata
    custom_data = [cols.VOTES_COUNTED, cols.TOTAL_POP, cols.EC_VOTES, cols.POP_PER_EC, cols.STATE_COUNT, cols.STATES_USING_POP]
    fig_title = 'Votes Cast For President as a Percentage of Total Population'

    x_min = 1785
    vote_pct_min = totals_by_year_df[cols.VOTES_COUNTED_PCT_TOTAL_POP].min() * 0.8
    vote_pct_max = totals_by_year_df[cols.VOTES_COUNTED_PCT_TOTAL_POP].max() * 1.05
    orig_vote_pct_max = vote_pct_max
    orig_vote_pct_min = vote_pct_min
    if log_y:
        vote_pct_min = math.log(vote_pct_min, 10) 
        vote_pct_max = math.log(vote_pct_max, 10) * 1.05
        orig_vote_pct_max = orig_vote_pct_max * 1.05 

    fig = px.line(totals_by_year_df, x=cols.YEAR, y=cols.VOTES_COUNTED_PCT_TOTAL_POP, title=fig_title, 
                    custom_data=custom_data, width=fig_width, height=fig_height, line_shape='spline', log_y=log_y)

    for i in range(len(fig.data)):
        fig.data[i].update(mode='markers+lines')

    # axis labels
    fig.update_xaxes(title_text='Election Year')
    y_axis_text = 'Percentage of National Population Who Voted'
    if log_y:
        y_axis_text = f"{y_axis_text} (log)"
    fig.update_yaxes(title_text=y_axis_text)

    # build markers and labels marking events 
    event_markers = build_and_annotate_event_markers(fig, EVENTS, vote_pct_min, vote_pct_max, y_min2=orig_vote_pct_min, y_max2=orig_vote_pct_max)
    # build shaded blocks designating eras
    era_blocks = build_and_annotate_era_blocks(fig, ERAS, x_min, orig_vote_pct_min, orig_vote_pct_max, y_max2=vote_pct_max)
    shapes = event_markers + era_blocks

    # have x axis ticks every 20 years from 1800-2020
    x_axis_ticks = dict(tickmode='array', tickvals=[x*20 for x in range(90, 102)])

    # update layout and axes 
    fig.update_layout(xaxis_range=[x_min, YEAR_N], yaxis_range=[vote_pct_min, vote_pct_max], xaxis=x_axis_ticks,
                    plot_bgcolor='white', shapes=shapes)
    fig.update_xaxes(gridcolor='#DDDDDD')
    fig.update_yaxes(gridcolor='#DDDDDD')

    # hover text format solution from https://stackoverflow.com/questions/59057881/python-plotly-how-to-customize-hover-template-on-with-what-information-to-show
    # TODO where are x, y, and customdata actually defined, in fig? I'd like to avoid these redundant key-value mappings and use an f-string for this but not sure how
    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>%{y:.2f}%</b> (%{x})<br>",
            "Votes counted: <b>%{customdata[0]:,}</b>",
            "Total population: <b>%{customdata[1]:,}</b>",
            "Total EC votes: <b>%{customdata[2]}</b>",
            "Avg pop per EC vote: <b>%{customdata[3]:,}</b>",
            "State count: <b>%{customdata[4]}</b> (%{customdata[5]} using pop vote)</b>",
        ])
    )

    return fig