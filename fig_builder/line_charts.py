import plotly.express as px
import plotly.graph_objects as go

from data_processor.functions import map_to_subdir
from metadata import Columns, FigDimensions, GROUPS_FOR_DIR, GROUP_COLORS, COLORS_PLOTLY


cols = Columns()
fig_dims = FigDimensions()


def build_ivw_by_state_group_line_chart(data_obj, groups_dir, max_small, frame, fig_width=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    group_aggs_by_year_df = data_obj.group_aggs_by_year_dfs[subdir]
    groups = GROUPS_FOR_DIR[groups_dir]

    # hackish way to remove years where Average Weight is 0 from Postbellum and West Groups without removing it for Confederate or South Groups
    group_aggs_by_year_df = group_aggs_by_year_df.loc[~((group_aggs_by_year_df[cols.AVG_WEIGHT] == 0) & (group_aggs_by_year_df[cols.GROUP] == 'Postbellum'))]
    group_aggs_by_year_df = group_aggs_by_year_df.loc[~((group_aggs_by_year_df[cols.AVG_WEIGHT] == 0) & (group_aggs_by_year_df[cols.GROUP] == 'West'))]

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = 500

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

    fig.update_layout(xaxis_range=[1828, 2020])
    fig.update_layout(yaxis_range=[avg_weight_min, avg_weight_max])

    # axis labels
    fig.update_xaxes(title_text='Election Year')
    fig.update_yaxes(title_text='Average Vote Weight Per Ballot Cast')

    # add vertical line highlighting selected year (frame)
    # fig.add_trace(go.Scatter(x=[frame, frame], y=[avg_weight_min, avg_weight_max], 
    #                         mode='lines', name=frame, line=dict(color='pink', width=1)))


    events = [
        # {'year': 1857, 'name': 'Dred Scott v Sandford'},
        {'year': 1861, 'name': 'Civil War begins'},
        # {'year': 1863, 'name': 'Emancipation Proclamation'},
        {'year': 1865, 'name': 'Civil War ends, 13th Amendment'},
        # {'year': 1868, 'name': '14th Amendment'},
        {'year': 1870, 'name': '15th Amendment'},
        {'year': 1877, 'name': 'Compromise of 1877'},
        {'year': 1896, 'name': 'Plessy v Ferguson'},
        {'year': 1920, 'name': '19th Amendment'},
        # {'year': 1921, 'name': 'Tulsa race massacre'},
        {'year': 1924, 'name': 'KKK peak membership'},
        # {'year': 1932, 'name': 'Tuskegee Syphilis Study'},
        {'year': 1954, 'name': 'Brown v Board of Education'},
        # {'year': 1955, 'name': 'Emmett Till lynching, Montgomery bus boycott'},
        {'year': 1960, 'name': 'Sit-ins'},
        # {'year': 1964, 'name': 'Civil Rights Act, 24th Amendment'}, 
        {'year': 1965, 'name': 'Voting Rights Act'},
        {'year': 1971, 'name': '26th Amendment'},
        {'year': 2013, 'name': 'Shelby County v. Holder'},
    ]

    eras = [
        {'begin': 1828, 'end': 1861, 'name': 'Antebellum Period', 'color': '#636EFA'},
        {'begin': 1861, 'end': 1865, 'name': 'Civil War', 'color': '#FECB52'},
        {'begin': 1865, 'end': 1877, 'name': 'Reconstruction', 'color': '#00CC96'},
        {'begin': 1877, 'end': 1896, 'name': 'Redemption', 'color': '#AB63FA'},
        {'begin': 1896, 'end': 1954, 'name': 'Jim Crow', 'color': '#FFA15A'},
        {'begin': 1954, 'end': 1965, 'name': 'Civil Rights Era', 'color': '#19D3F3'},
        {'begin': 1965, 'end': 2020, 'name': 'Post Voting Rights Act', 'color': '#FF6692'},
    ]

    # build markers and labels marking events 
    event_markers = []
    for event in events:
        # add vertical line for each event date
        marker = dict(type='line', line_width=1, x0=event['year'], x1=event['year'], y0=avg_weight_min, y1=avg_weight_max)
        event_markers.append(marker)
        # add annotation for each event
        fig.add_annotation(x=event['year']-1, y=avg_weight_max, text=event['name'], showarrow=False, 
            yshift=-2, xshift=-1, 
            textangle=-90, align='right', yanchor='top')

    # build shaded blocks designating eras
    era_blocks = []
    for era in eras:
        # add rectangle for each era date range
        block = dict(type='rect', line_width=0, x0=era['begin'], x1=era['end'], y0=avg_weight_min, y1=avg_weight_max, 
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
        
        fig.add_annotation(x=era_mid, y=avg_weight_max, text=era['name'], showarrow=showarrow, yshift=yshift, 
            # align='left', textangle=-90, yanchor='top'
        )

    # update layout with era_blocks and event_markers
    fig.update_layout(shapes=era_blocks + event_markers)

    return fig
    