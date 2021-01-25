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
GRID_COLOR = '#DDDDDD'


def build_ivw_by_state_group_line_chart(data_obj, groups_dir, max_small, fig_width=None, fig_height=None, state_abbrevs=None, log_y=False, 
                                        display_groups=True, display_eras=True, display_events=True):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    data_obj.load_totals_by_year
    group_aggs_by_year_df = data_obj.group_agg_weights_pivot_dfs[subdir].copy()
    groups = GROUPS_FOR_DIR[groups_dir].copy()
    group_col = GROUPS_COL_FOR_DIR[groups_dir]

    # assign GROUP_COLORS to local var so it can be modified if states are added
    group_colors = GROUP_COLORS

    if not fig_width:
        fig_width = fig_dims.MD6
    if not fig_height:
        fig_height = 700

    # if we're hiding groups, drop everything from df except Nat'l Average data
    if not display_groups:
        group_aggs_by_year_df = group_aggs_by_year_df[group_aggs_by_year_df[cols.GROUP] == "Nat'l Average"]
    else:
        # hackish way to remove years where Average Weight is 0 from Postbellum and West Groups without removing it for Confederate or South Groups
        group_aggs_by_year_df = group_aggs_by_year_df.loc[~((group_aggs_by_year_df[cols.AVG_WEIGHT] == 0) & (group_aggs_by_year_df[cols.GROUP] == 'Postbellum'))]
        group_aggs_by_year_df = group_aggs_by_year_df.loc[~((group_aggs_by_year_df[cols.AVG_WEIGHT] == 0) & (group_aggs_by_year_df[cols.GROUP] == 'West'))]

    # drop rows with 0 EC votes (e.g. Union when no states had pop vote, Confed states during Civil War, etc)
    group_aggs_by_year_df = group_aggs_by_year_df[group_aggs_by_year_df[cols.EC_VOTES] > 0]

    # track the number of traces displayed, hovermode type and hovertemplate format are altered to maximize info while fitting to screen
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

    # if any states are selected, merge their data into group aggs df
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
    fig_title = 'Average Voter Weight Per Ballot Cast For Each Presidential Election'
    if display_groups:
        fig_title = f"{fig_title}, Grouped By Region"
    if trace_count >= MAX_TRACE_COUNT:
        fig_title = f"{fig_title} [** MAXES OUT AT 22 LINES **]"
    x_axis_title = 'Election Year'
    y_axis_title = 'Voter Weight'
    # y_axis_title = 'Vote Weight Per Ballot Cast'
    if log_y:
        y_axis_title = f"{y_axis_title} (log)"
    # custom_data enables dynamic variable substitution in hovertemplates for static frames
    custom_data = [cols.GROUP, cols.STATES_IN_GROUP, cols.EC_VOTES, cols.VOTES_COUNTED, cols.POP_PER_EC]
    
    # calculate axis range boundaries 
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

    # init figure with core properties
    fig = px.line(group_aggs_by_year_df, x=cols.YEAR, y=cols.AVG_WEIGHT, color=cols.GROUP, title=fig_title, 
                    color_discrete_map=group_colors, category_orders={cols.GROUP: groups}, custom_data=custom_data,
                    width=fig_width, height=fig_height, line_shape='spline', log_y=log_y)
    
    # include dots marking data points in each trace
    for i in range(len(fig.data)):
        fig.data[i].update(mode='markers+lines')

    # axis metadata
    fig.update_xaxes(title_text=x_axis_title, gridcolor=GRID_COLOR)
    fig.update_yaxes(title_text=y_axis_title, gridcolor=GRID_COLOR)
    # have x axis ticks every 20 years from YEAR_0-YEAR_N, inclusive of YEAR_N
    tick_span = 20
    x_axis_ticks = dict(tickmode='array', tickvals=[x for x in range(YEAR_0, YEAR_N+tick_span, tick_span)])
    fig.update_layout(xaxis_range=[YEAR_0, YEAR_N], yaxis_range=[avg_weight_min, avg_weight_max], plot_bgcolor='white', xaxis=x_axis_ticks)
    if trace_count <= TRACE_MAX_FOR_HOVERMODE_X:
        fig.update_layout(hovermode="x")

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

    # center title
    fig.update_layout(title_x=0.5)

    # hovertemplate formatting and variable substitution using customdata
    # if trace_count < TRACE_MAX_FOR_EXPANDED_HOVERDATA <= TRACE_MAX_FOR_HOVERMODE_X:
    if trace_count <= TRACE_MAX_FOR_EXPANDED_HOVERDATA or trace_count > TRACE_MAX_FOR_HOVERMODE_X:
        fig.update_traces(
            hovertemplate="<br>".join([
                "<b>%{customdata[0]}</b> (%{x})<br></b>",
                "Popular Vote: <b>%{customdata[3]:,}</b>",
                "Electoral College Votes: <b>%{customdata[2]:,}</b>",
                "Average Voter weight: <b>%{y:.2f}</b>",
                "Avg Pop Vote Per Elector: <b>%{customdata[4]:,}</b>",
                "State(s): <b>%{customdata[1]}</b>",
            ])
        )
    else:
        fig.update_traces(
            hovertemplate="<br>".join([
                "<b>%{customdata[0]}</b> (%{x})<br></b>",
                "Combined EC Votes: <b>%{customdata[2]:,}</b>",
                "Combined Popular Vote: <b>%{customdata[3]:,}</b>",
                "Average Voter Weight: <b>%{y:.2f}</b>",
                "States in Group: <b>%{customdata[1]}</b>",
            ])
        )

    return fig


def build_total_vote_line_chart(data_obj, fig_width=None, log_y=False,):
    data_obj.load_totals_by_year()
    totals_by_year_df = data_obj.totals_by_year_df.copy()

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = 700

    # display metadata
    fig_title = 'Votes Cast For President as a Percentage of Total Population'
    x_axis_title = 'Election Year'
    y_axis_title = 'Percentage of national population who voted'
    if log_y:
        y_axis_title = f"{y_axis_title} (log)"
    # custom_data enables dynamic variable substitution in hovertemplates for static frames
    custom_data = [cols.VOTES_COUNTED, cols.TOTAL_POP, cols.EC_VOTES, cols.POP_PER_EC, cols.STATE_COUNT, cols.STATES_USING_POP]

    # calculate axis range boundaries 
    x_min = 1785
    vote_pct_min = totals_by_year_df[cols.VOTES_COUNTED_PCT_TOTAL_POP].min() * 0.8
    vote_pct_max = totals_by_year_df[cols.VOTES_COUNTED_PCT_TOTAL_POP].max() * 1.05
    orig_vote_pct_max = vote_pct_max
    orig_vote_pct_min = vote_pct_min
    if log_y:
        vote_pct_min = math.log(vote_pct_min, 10) 
        vote_pct_max = math.log(vote_pct_max, 10) * 1.05
        orig_vote_pct_max = orig_vote_pct_max * 1.05 

    # init figure with core properties
    fig = px.line(totals_by_year_df, x=cols.YEAR, y=cols.VOTES_COUNTED_PCT_TOTAL_POP, title=fig_title, 
                    custom_data=custom_data, width=fig_width, height=fig_height, line_shape='spline', log_y=log_y)

    # include dots marking data points in each trace
    for i in range(len(fig.data)):
        fig.data[i].update(mode='markers+lines')

    # build markers and labels marking events 
    event_markers = build_and_annotate_event_markers(fig, EVENTS, vote_pct_min, vote_pct_max, y_min2=orig_vote_pct_min, y_max2=orig_vote_pct_max)
    # build shaded blocks designating eras
    era_blocks = build_and_annotate_era_blocks(fig, ERAS, x_min, orig_vote_pct_min, orig_vote_pct_max, y_max2=vote_pct_max)
    shapes = event_markers + era_blocks

    # axis metadata
    fig.update_xaxes(title_text=x_axis_title, gridcolor=GRID_COLOR)
    fig.update_yaxes(title_text=y_axis_title, gridcolor=GRID_COLOR)
    # have x axis ticks every 20 years from YEAR_0-YEAR_N, inclusive of YEAR_N
    tick_span = 20
    x_axis_ticks = dict(tickmode='array', tickvals=[x for x in range(YEAR_0, YEAR_N+tick_span, tick_span)])
    fig.update_layout(xaxis_range=[x_min, YEAR_N], yaxis_range=[vote_pct_min, vote_pct_max], xaxis=x_axis_ticks,
                    plot_bgcolor='white', shapes=shapes)
    
    # center title
    fig.update_layout(title_x=0.5)

    # hovertemplate formatting and variable substitution using customdata
    # hover text format solution from https://stackoverflow.com/questions/59057881/python-plotly-how-to-customize-hover-template-on-with-what-information-to-show
    # TODO where are x, y, and customdata actually defined, in fig? I'd like to avoid these redundant key-value mappings and use an f-string for this but not sure how
    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>%{y:.2f}%</b> (%{x})<br>",
            "Popular Vote: <b>%{customdata[0]:,}</b>",
            "Total Population: <b>%{customdata[1]:,}</b>",
            "Total EC Votes: <b>%{customdata[2]}</b>",
            "Avg Pop Vote Per Elector: <b>%{customdata[3]:,}</b>",
            "State Count: <b>%{customdata[4]}</b> (%{customdata[5]} using Pop Vote)</b>",
        ])
    )

    return fig