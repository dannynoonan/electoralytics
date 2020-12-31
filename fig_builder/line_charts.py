import plotly.express as px
import plotly.graph_objects as go

from data_processor.functions import map_to_subdir
from metadata import Columns, FigDimensions, GROUPS_FOR_DIR, GROUP_COLORS, COLORS_PLOTLY, YEAR_0, YEAR_N, EVENTS, ERAS


cols = Columns()
fig_dims = FigDimensions()


def build_ivw_by_state_group_line_chart(data_obj, groups_dir, max_small, frame, fig_width=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    group_aggs_by_year_df = data_obj.group_agg_weights_pivot_dfs[subdir]
    groups = GROUPS_FOR_DIR[groups_dir]

    # hackish way to remove years where Average Weight is 0 from Postbellum and West Groups without removing it for Confederate or South Groups
    group_aggs_by_year_df = group_aggs_by_year_df.loc[~((group_aggs_by_year_df[cols.AVG_WEIGHT] == 0) & (group_aggs_by_year_df[cols.GROUP] == 'Postbellum'))]
    group_aggs_by_year_df = group_aggs_by_year_df.loc[~((group_aggs_by_year_df[cols.AVG_WEIGHT] == 0) & (group_aggs_by_year_df[cols.GROUP] == 'West'))]

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = 700

    # display metadata
    hover_data = {cols.GROUP: False, cols.STATES_IN_GROUP: True, cols.EC_VOTES: True}
    avg_weight_min = group_aggs_by_year_df[group_aggs_by_year_df[cols.AVG_WEIGHT] > 0][cols.AVG_WEIGHT].min() * 0.8
    avg_weight_max = group_aggs_by_year_df[group_aggs_by_year_df[cols.AVG_WEIGHT] > 0][cols.AVG_WEIGHT].max() * 1.05
    fig_title = 'Average Vote Weight Per Ballot Cast For Each Election, Grouped By Region'
    # fig_title = f'{base_fig_title}: (Highlighting {frame})'

    fig = px.line(group_aggs_by_year_df, x=cols.YEAR, y=cols.AVG_WEIGHT, color=cols.GROUP, 
                    hover_name=cols.GROUP, hover_data=hover_data, 
                    color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                    title=fig_title, width=fig_width, height=fig_height, 
                    line_shape='spline',
    #               log_y=True
                )
    
    for i in range(len(fig.data)):
        fig.data[i].update(mode='markers+lines')

    fig.update_layout(xaxis_range=[YEAR_0, YEAR_N])
    fig.update_layout(yaxis_range=[avg_weight_min, avg_weight_max])

    # axis labels
    fig.update_xaxes(title_text='Election Year')
    fig.update_yaxes(title_text='Average Vote Weight Per Ballot Cast')

    # add vertical line highlighting selected year (frame)
    # fig.add_trace(go.Scatter(x=[frame, frame], y=[avg_weight_min, avg_weight_max], 
    #                         mode='lines', name=frame, line=dict(color='pink', width=1)))

    # build markers and labels marking events 
    event_markers = build_and_annotate_event_markers(fig, EVENTS, avg_weight_min, avg_weight_max)

    # build shaded blocks designating eras
    era_blocks = build_and_annotate_era_blocks(fig, ERAS, avg_weight_max)

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
    fig_title = 'Ballots Cast as a Percentage of Total Population In Each Election'

    fig = px.line(totals_by_year_df, x=cols.YEAR, y=cols.VOTES_COUNTED_PCT_TOTAL_POP, 
                    hover_name=cols.YEAR, hover_data=hover_data, 
                    title=fig_title, width=fig_width, height=fig_height, 
                    line_shape='spline', 
                    # log_y=True
                    )

    for i in range(len(fig.data)):
        fig.data[i].update(mode='markers+lines')

    fig.update_layout(xaxis_range=[1785, YEAR_N])
    fig.update_layout(yaxis_range=[0, vote_pct_max])

    # build markers and labels marking events 
    event_markers = build_and_annotate_event_markers(fig, EVENTS, 0, vote_pct_max)

    # build shaded blocks designating eras
    era_blocks = build_and_annotate_era_blocks(fig, ERAS, vote_pct_max)

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
        event_name = f"{event['name']} ({event['year']})"
        fig.add_annotation(x=event['year'], y=y_max, text=event_name, showarrow=False, 
            yshift=-2, xshift=-7, textangle=-90, align='right', yanchor='top')
        if event.get('desc'):
            event_desc = f"<i>{event['desc']}</i>"
            fig.add_annotation(x=event['year'], y=y_min, text=event_desc, showarrow=False, 
                yshift=2, xshift=6, textangle=-90, align='left', yanchor='bottom')

    return event_markers


def build_and_annotate_era_blocks(fig, eras, y_max):
    # build shaded blocks designating eras
    era_blocks = []
    for era in eras:
        # add rectangle for each era date range
        block = dict(type='rect', line_width=0, x0=era['begin'], x1=era['end'], y0=0, y1=y_max, 
                    fillcolor=era['color'], opacity=0.1)
        era_blocks.append(block) 
        # add annotation for each era
        era_len = era['end'] - era['begin']
        era_mid = (era['end'] + era['begin']) / 2
        showarrow = False
        yshift = 7
        if era_len < 12:
            showarrow = True
            yshift = 0
        
        fig.add_annotation(x=era_mid, y=y_max, text=era['name'], showarrow=showarrow, yshift=yshift, 
            # align='left', textangle=-90, yanchor='top'
        )

    return era_blocks