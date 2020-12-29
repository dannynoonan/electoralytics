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
    #               log_y=True
                )

    fig.update_layout(yaxis_range=[avg_weight_min, avg_weight_max])

    # axis labels
    fig.update_xaxes(title_text='Election Year')
    fig.update_yaxes(title_text='Average Vote Weight Per Ballot Cast')

    # add vertical line highlighting selected year (frame)
    # fig.add_trace(go.Scatter(x=[frame, frame], y=[avg_weight_min, avg_weight_max], 
    #                         mode='lines', name=frame, line=dict(color='pink', width=1)))


    events = {
        # '1857': 'Dred Scott v Sandford',
        '1861': 'Civil War begins', 
        # '1863': ['Emancipation Proclamation',
        '1865': 'Civil War ends, 13th Amendment ratified',
        # '1868': '14th Amendment ratified',
        '1870': '15th Amendment ratified',
        '1877': 'Compromise of 1877 ends Reconstruction',
        '1896': 'Plessy v Ferguson',
        '1920': '19th Amendment ratified',
        # '1921': 'Tulsa race massacre',
        '1924': 'KKK peak membership',
        # '1932': 'Tuskegee Syphilis Study',
        '1954': 'Brown v Board of Education',
        # '1955': 'Emmett Till lynching, Montgomery bus boycott',
        '1960': 'Sit-ins',
        # '1964': 'Civil Rights Act, 24th Amendment ratified', 
        '1965': 'Voting Rights Act',
        '1971': '26th Amendment ratified',
        '2013': 'Shelby County v. Holder',
    }

    eras = [
        {'begin': 1828, 'end': 1861, 'name': 'Antebellum Period'},
        {'begin': 1861, 'end': 1865, 'name': 'Civil War'},
        {'begin': 1865, 'end': 1877, 'name': 'Reconstruction'},
        {'begin': 1877, 'end': 1896, 'name': 'Redemption / Early Jim Crow'},
        {'begin': 1896, 'end': 1954, 'name': 'Jim Crow'},
        {'begin': 1954, 'end': 1965, 'name': 'Late Jim Crow / Civil Rights Era'},
        {'begin': 1965, 'end': 2020, 'name': 'Post Voting Rights Act'},
    ]

    # build markers and labels marking events 
    event_markers = []
    for year, event in events.items():
        year = int(year)
        # add vertical line for each event date
        marker = dict(type='line', line_width=1, x0=year, x1=year, y0=avg_weight_min, y1=avg_weight_max)
        event_markers.append(marker)
        # add annotation for each event
        fig.add_annotation(x=year-1, y=avg_weight_max, text=event, showarrow=False, 
            yshift=-2, xshift=-1, 
            textangle=-90, align='right', yanchor='top')

    # build shaded blocks designating eras
    era_blocks = []
    for i in range(len(eras)):
        block = dict(type='rect', line_width=0, x0=eras[i]['begin'], x1=eras[i]['end'], y0=avg_weight_min, y1=avg_weight_max, 
                    fillcolor=COLORS_PLOTLY[i], opacity=0.1)
        era_blocks.append(block) 

    # update layout with era_blocks and event_markers
    fig.update_layout(shapes=era_blocks + event_markers)

    return fig
    