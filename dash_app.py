import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import flask

import pandas as pd
import plotly.express as px

from data_processor.data_objects import DataObject
from data_processor import fig_builder 
from data_processor.functions import validate_input, map_to_subdir
from metadata import GEN_DATA_DIR, COL_LOG_VOTE_WEIGHT, GEN_DATA_ACW_DIR, GEN_DATA_CENSUS_DIR


# base config
app = dash.Dash(external_stylesheets=[dbc.themes.SOLAR])
# server is needed for heroku deployment
server = app.server


# load source data for default subdir
data_obj = DataObject()
data_obj.load_dfs_for_subdir()
data_obj.load_swallowed_vote_sampler()


### BOOTSTRAP COMPONENTS ###
# url / page  
url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# navbar
navbar = html.Div([
    html.Br(),
    html.H1('Electoralytics', id="nav-pills"),
    dbc.Nav(className="nav nav-pills", children=[
        dbc.DropdownMenu(label="Pages / Graphs", nav=True, children=[
            dbc.DropdownMenuItem([html.I(className="fa"), "Vote Weight Comparison Between States"], href='/vote-weight-comparison', target="_blank"), 
            dbc.DropdownMenuItem([html.I(className="fa"), "Explanation of Regional State Groupings"], href='/explanation-of-groupings', target="_blank"), 
            dbc.DropdownMenuItem([html.I(className="fa"), "Sampler of Swallowed Votes"], href='/swallowed-vote-sampler', target="_blank"),
        ]),
        dbc.DropdownMenu(label="References / Resources", nav=True, children=[
            dbc.DropdownMenuItem([html.I(className="fa"), "Source code"], href='https://github.com/dannynoonan/electoralytics', target="_blank"), 
            dbc.DropdownMenuItem([html.I(className="fa"), "Articles"], href='/resources/articles'),
            dbc.DropdownMenuItem([html.I(className="fa"), "Podcasts"], href='/resources/podcasts'),
            dbc.DropdownMenuItem([html.I(className="fa"), "Books"], href='/resources/books'),
        ])
    ])
])


# inputs
year_slider = dbc.FormGroup([
    dbc.Row([
        dbc.Col(md=8, children=[
            html.H4("Election Year")
        ]),
        dbc.Col(md=2, children=[
            html.H4("State Grouping")
        ]),
        dbc.Col(md=2, children=[
            html.H4("Extract Small Group?")
        ])
    ]),
    dbc.Row([
        dbc.Col(md=8, children=[
            dcc.Slider(
                id="year-input",
                min=1828,
                max=2020,
                marks={
                    int(y): {'label': str(y), 'style': {'transform': 'rotate(45deg)'}}
                    for y in data_obj.all_years
                },
                value=1960,
            )
        ]),
        dbc.Col(md=2, children=[
            dcc.Dropdown(
                id="groupings-input", 
                options=[
                    {'label': 'Civil War', 'value': GEN_DATA_ACW_DIR},
                    {'label': 'Regional Census', 'value': GEN_DATA_CENSUS_DIR}
                ], 
                value=GEN_DATA_ACW_DIR
            )
        ]),
        dbc.Col(md=2, children=[
            dcc.Dropdown(
                id="max-small-input", 
                options=[
                    {'label': 'No Small Group', 'value': '0'},
                    {'label': '3 EC Votes', 'value': '3'},
                    {'label': '3 or 4 EC Votes', 'value': '4'},
                    {'label': '3 - 5 EC Votes', 'value': '5'},
                ], 
                value="4"
            )
        ])
    ])
])


swallowed_vote_view_dropdown = dbc.FormGroup([
    html.H4("Swallowed vote view"),
    dcc.Dropdown(id="display-type", options=[{"label": "2020", "value": "2020"}], value="2020")
])


groupings_explanation_dropdown = dbc.FormGroup([
    html.H4("Groupings explanation"),
    dcc.Dropdown(id="year-input", options=[{"label": "2020", "value": "2020"}], value="2020")
])


layout_1 = html.Div([
    navbar,
    html.Br(),
    dbc.Row([
        # html.H3("Comparing Individual Voter Impact Per State"),
        # html.H3("Comparing Vote Weight Per Ballot Cast Per State"),
        html.H3("Comparing Vote Weight Per Ballot Cast (Per State/Per Region)"),
    ], justify="center", align="center"),
    dbc.Row([
        dbc.Col(md=12, children=[
            year_slider,
            # group_select,
        ])
    ]),
    dbc.Row([
        dbc.Col(md=12, children=[
            # dbc.Col(html.H4("Inter-State Voter Impact Comparison"), width={"size": 6, "offset": 3}), 
            # html.Br(),
            dbc.Tabs(className="nav nav-pills", children=[
                dbc.Tab(label="State-Level Comparisons", tab_style={"font-size": "20px"}, children=[
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-color-by-state-vw"),
                            html.Br(),
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-bar-state-vw-color-by-vw"),
                            html.Br(),
                        ])
                    ]),
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-color-by-group"),
                            html.Br(),
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-bar-state-vw-color-by-group"),
                            html.Br(),
                        ])
                    ]),
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="vote-weight-comparison-by-state-scatter-dots"),
                            html.Br(),
                            dcc.Graph(id="vote-weight-comparison-by-state-scatter-abbrevs"),
                            html.Br(),
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="vote-weight-comparison-by-state-scatter-bubbles"),
                            html.Br(), 
                        ])
                    ]),
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-bar-actual-vs-adj-ec"),
                            html.Br(),
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-bar-actual-vs-adj-vw"),
                            html.Br(),
                        ])
                    ])
                ]),

                dbc.Tab(label="Regional Aggregate Comparisons", tab_style={"font-size": "20px"}, children=[
                    dbc.Row([
                        dbc.Col(md=12, children=[
                            dcc.Graph(id="vote-weight-comparison-by-state-group-line-1")
                        ])
                    ]),
                    html.Br(),
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="vote-weight-comparison-by-state-group-scatter-dots"),
                            html.Br(),
                            dcc.Graph(id="vote-weight-comparison-by-state-group-box-1"),
                            html.Br(),
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="vote-weight-comparison-by-state-group-scatter-bubbles"),
                            html.Br(),
                        ])
                    ])
                ]),

                dbc.Tab(label="State-Level Comparison Animations", tab_style={"font-size": "20px"}, children=[
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="vote-weight-comparison-by-state-map-1-anim"),
                            html.Br(),
                            dcc.Graph(id="vote-weight-comparison-by-state-scatter-dots-anim"),
                            html.Br(),
                            # dcc.Graph(id="vote-weight-comparison-by-state-bar-1-anim"),
                            # html.Br(),
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="vote-weight-comparison-by-state-scatter-bubbles-anim"),
                            html.Br(), 
                            dcc.Graph(id="vote-weight-comparison-by-state-scatter-abbrevs-anim"),
                            html.Br(),
                            # dcc.Graph(id="vote-weight-comparison-by-state-bar-2-anim"),
                            # html.Br(),
                        ])
                    ])
                ]),

                dbc.Tab(label="Regional Aggregate Comparison Animations", tab_style={"font-size": "20px"}, children=[
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="vote-weight-comparison-by-state-group-scatter-bubbles-anim"),
                            html.Br(),
                            dcc.Graph(id="vote-weight-comparison-by-state-group-map-1-anim"),
                            html.Br(),
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="vote-weight-comparison-by-state-group-scatter-dots-anim"),
                            html.Br(),
                        ]),
                    ])
                ]),

            ])
        ])
    ])
])


layout_2 = html.Div([
    ## Top
    navbar,
    html.Br(),html.Br(),

    dbc.Row([
        html.H3("Explanation of Regional State Groupings"),
    ], justify="center", align="center"),

    dbc.Row([
        dbc.Col(md=3, children=[
            groupings_explanation_dropdown,
            html.Br(),
        ])
    ]),

    dbc.Row([
        dbc.Col(md=6, children=[
            dcc.Graph(id="state-groupings-anim-civil-war-no-small"),
            html.Br(),
            dcc.Graph(id="state-groupings-anim-civil-war-small-3"),
            html.Br(),
            dcc.Graph(id="state-groupings-anim-civil-war-small-4"),
            html.Br(),
            dcc.Graph(id="state-groupings-anim-civil-war-small-5"),
            html.Br(),
        ]),
        dbc.Col(md=6, children=[
            dcc.Graph(id="state-groupings-anim-regional-census-no-small"),
            html.Br(),
            dcc.Graph(id="state-groupings-anim-regional-census-small-3"),
            html.Br(),
            dcc.Graph(id="state-groupings-anim-regional-census-small-4"),
            html.Br(),
            dcc.Graph(id="state-groupings-anim-regional-census-small-5"),
            html.Br(),
        ])
    ])    
])


# layout 3
layout_3 = html.Div([
    ## Top
    navbar,
    html.Br(),html.Br(),

    dbc.Row([
        ### input + panel
        dbc.Col(md=3, children=[
            swallowed_vote_view_dropdown,
            html.Br(),html.Br(),html.Br(),
            html.Div(id="todo")
        ]),
        ### figures
        dbc.Col(md=9, children=[
            dbc.Col(html.H4("2020 sampler of votes 'flipped' by the Electoral College"), width={"size": 6, "offset": 3}), 
            dbc.Tabs(className="nav nav-pills", children=[
                dbc.Tab(dcc.Graph(id="swallowed-vote-sampler-1"), label="Raw popular vote"),
                dbc.Tab(dcc.Graph(id="swallowed-vote-sampler-2"), label="Muted popular vote"),
                dbc.Tab(dcc.Graph(id="swallowed-vote-sampler-3"), label="Stacked popular vote"),
                dbc.Tab(dcc.Graph(id="swallowed-vote-sampler-4"), label="Converted to EC vote"),
            ])
        ])
    ])
])


empty_layout = html.Div([
    navbar,
])



# app layout
app.layout = dbc.Container(fluid=True, children=[
    url_bar_and_content_div,
])

# app layout
app.validation_layout = dbc.Container(fluid=True, children=[
    url_bar_and_content_div,

    ## Body
    layout_1,
    layout_2,
    layout_3,
    empty_layout,
])



# Index callbacks
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/vote-weight-comparison":
        return layout_1
    elif pathname == "/explanation-of-groupings":
        return layout_2
    elif pathname == "/swallowed-vote-sampler":
        return layout_3
    else:
        return empty_layout



# Layout 1 callbacks
@app.callback(
    Output('fig-map-color-by-state-vw', 'figure'),
    Output('fig-map-color-by-group', 'figure'),
    Output('fig-bar-state-vw-color-by-group', 'figure'),
    Output('fig-bar-state-vw-color-by-vw', 'figure'),
    Output('fig-bar-actual-vs-adj-ec', 'figure'),
    Output('fig-bar-actual-vs-adj-vw', 'figure'),
    Output('vote-weight-comparison-by-state-scatter-dots', 'figure'),
    Output('vote-weight-comparison-by-state-scatter-abbrevs', 'figure'),
    Output('vote-weight-comparison-by-state-scatter-bubbles', 'figure'),
    Input('year-input', 'value'),
    Input('groupings-input', 'value'),
    Input('max-small-input', 'value'),
)
def display_state_level_figs(year_input, groupings_input, max_small_input):
    print(f"#### in display_state_level_figs")
    # process input
    year = int(year_input)
    max_small = int(max_small_input)
    # generate figs
    fig_map_color_by_state_vw = fig_builder.build_ivw_by_state_map(data_obj, groupings_input, max_small, frame=year)
    fig_map_color_by_group = fig_builder.build_state_groups_map(data_obj, groupings_input, max_small, frame=year)
    fig_bar_state_vw_color_by_group = fig_builder.build_ivw_by_state_bar(data_obj, groupings_input, max_small, frame=year)
    fig_bar_state_vw_color_by_vw = fig_builder.build_ivw_by_state_bar(data_obj, groupings_input, max_small, frame=year, color_col=COL_LOG_VOTE_WEIGHT)
    fig_bar_actual_vs_adj_ec = fig_builder.build_actual_vs_adjusted_ec_bar(data_obj, groupings_input, max_small, frame=year)
    fig_bar_actual_vs_adj_vw = fig_builder.build_actual_vs_adjusted_vw_bar(data_obj, groupings_input, max_small, frame=year)
    fig_scatter_dots = fig_builder.build_ivw_by_state_scatter_dots(data_obj, groupings_input, max_small, frame=year)
    fig_scatter_abbrevs = fig_builder.build_ivw_by_state_scatter_abbrevs(data_obj, groupings_input, max_small, frame=year)
    fig_scatter_bubbles = fig_builder.build_ivw_by_state_scatter_bubbles(data_obj, groupings_input, max_small, frame=year)
    return (fig_map_color_by_state_vw, fig_map_color_by_group, fig_bar_state_vw_color_by_group, fig_bar_state_vw_color_by_vw, 
        fig_bar_actual_vs_adj_ec, fig_bar_actual_vs_adj_vw, fig_scatter_dots, fig_scatter_abbrevs, fig_scatter_bubbles)

@app.callback(
    # Output('vote-weight-comparison-by-state-group-map-1', 'figure'),
    Output('vote-weight-comparison-by-state-group-line-1', 'figure'),
    Output('vote-weight-comparison-by-state-group-box-1', 'figure'),
    Output('vote-weight-comparison-by-state-group-scatter-dots', 'figure'),
    Output('vote-weight-comparison-by-state-group-scatter-bubbles', 'figure'),
    Input('year-input', 'value'),
    Input('groupings-input', 'value'),
    Input('max-small-input', 'value'),
)
def display_regional_aggregate_figs(year_input, groupings_input, max_small_input):
    print(f"#### in display_regional_aggregate_figs")
    # process input
    year = int(year_input)
    max_small = int(max_small_input)
    # generate figs
    # fig_map_1 = fig_builder.build_state_groups_map(data_obj, groupings_input, max_small_input, frame=year)
    fig_line_1 = fig_builder.build_ivw_by_state_group_line_chart(data_obj, groupings_input, max_small, frame=year)
    fig_box_1 = fig_builder.build_ivw_by_state_group_box_plot(data_obj, groupings_input, max_small, frame=year)
    fig_scatter_dots = fig_builder.build_ivw_by_state_group_scatter_dots(data_obj, groupings_input, max_small, frame=year)
    fig_scatter_bubbles = fig_builder.build_ivw_by_state_group_scatter_bubbles(data_obj, groupings_input, max_small, frame=year)
    return fig_line_1, fig_box_1, fig_scatter_dots, fig_scatter_bubbles

@app.callback(
    Output('vote-weight-comparison-by-state-map-1-anim', 'figure'),
    # Output('vote-weight-comparison-by-state-bar-1-anim', 'figure'),
    # Output('vote-weight-comparison-by-state-bar-2-anim', 'figure'),
    Output('vote-weight-comparison-by-state-scatter-dots-anim', 'figure'),
    Output('vote-weight-comparison-by-state-scatter-abbrevs-anim', 'figure'),
    Output('vote-weight-comparison-by-state-scatter-bubbles-anim', 'figure'),
    Input('groupings-input', 'value'),
    Input('max-small-input', 'value'),
)
def display_state_level_anims(groupings_input, max_small_input):
    print(f"#### in display_state_level_anims")
    # process input
    max_small = int(max_small_input)
    # generate figs
    anim_map_1 = fig_builder.build_ivw_by_state_map(data_obj, groupings_input, max_small)
    # anim_bar_1 = fig_builder.build_ivw_by_state_bar(data_obj, groupings_input, max_small_input)
    # anim_bar_2 = fig_builder.build_actual_vs_adjusted_ec_bar(data_obj, groupings_input, max_small_input)
    anim_scatter_dots = fig_builder.build_ivw_by_state_scatter_dots(data_obj, groupings_input, max_small)
    anim_scatter_abbrevs = fig_builder.build_ivw_by_state_scatter_abbrevs(data_obj, groupings_input, max_small)
    anim_scatter_bubbles = fig_builder.build_ivw_by_state_scatter_bubbles(data_obj, groupings_input, max_small)
    return anim_map_1, anim_scatter_dots, anim_scatter_abbrevs, anim_scatter_bubbles

@app.callback(
    Output('vote-weight-comparison-by-state-group-map-1-anim', 'figure'),
    Output('vote-weight-comparison-by-state-group-scatter-dots-anim', 'figure'),
    Output('vote-weight-comparison-by-state-group-scatter-bubbles-anim', 'figure'),
    Input('groupings-input', 'value'),
    Input('max-small-input', 'value'),
)
def display_regional_aggregate_anims(groupings_input, max_small_input):
    print(f"#### in display_regional_aggregate_anims")
    # process input
    max_small = int(max_small_input)
    # generate figs
    anim_map_1 = fig_builder.build_state_groups_map(data_obj, groupings_input, max_small)
    anim_scatter_dots = fig_builder.build_ivw_by_state_group_scatter_dots(data_obj, groupings_input, max_small)
    anim_scatter_bubbles = fig_builder.build_ivw_by_state_group_scatter_bubbles(data_obj, groupings_input, max_small)
    return anim_map_1, anim_scatter_dots, anim_scatter_bubbles


# Layout 2 callbacks
@app.callback(
    Output('state-groupings-anim-civil-war-no-small', 'figure'),
    Output('state-groupings-anim-regional-census-no-small', 'figure'),
    Output('state-groupings-anim-civil-war-small-3', 'figure'),
    Output('state-groupings-anim-regional-census-small-3', 'figure'),
    Output('state-groupings-anim-civil-war-small-4', 'figure'),
    Output('state-groupings-anim-regional-census-small-4', 'figure'),
    Output('state-groupings-anim-civil-war-small-5', 'figure'),
    Output('state-groupings-anim-regional-census-small-5', 'figure'),
    Input('year-input', 'value'),
)
def display_all_state_grouping_map_anims(year_input):
    print(f"#### in display_all_state_grouping_map_anims")
    # process input
    year = int(year_input) # TODO probably access different small variants here, EC=3 vs EC=4 vs EC=5
    # generate figs
    anim_map_acw_no_small = fig_builder.build_state_groups_map(data_obj, GEN_DATA_ACW_DIR, 0)
    anim_map_census_no_small = fig_builder.build_state_groups_map(data_obj, GEN_DATA_CENSUS_DIR, 0)
    anim_map_acw_small_3 = fig_builder.build_state_groups_map(data_obj, GEN_DATA_ACW_DIR, 3)
    anim_map_census_small_3 = fig_builder.build_state_groups_map(data_obj, GEN_DATA_CENSUS_DIR, 3)
    anim_map_acw_small_4 = fig_builder.build_state_groups_map(data_obj, GEN_DATA_ACW_DIR, 4)
    anim_map_census_small_4 = fig_builder.build_state_groups_map(data_obj, GEN_DATA_CENSUS_DIR, 4)
    anim_map_acw_small_5 = fig_builder.build_state_groups_map(data_obj, GEN_DATA_ACW_DIR, 5)
    anim_map_census_small_5 = fig_builder.build_state_groups_map(data_obj, GEN_DATA_CENSUS_DIR, 5)
    return (anim_map_acw_no_small, anim_map_census_no_small, anim_map_acw_small_3, anim_map_census_small_3,
        anim_map_acw_small_4, anim_map_census_small_4, anim_map_acw_small_5, anim_map_census_small_5)


# Layout 3 callbacks
@app.callback(
    Output('swallowed-vote-sampler-1', 'figure'),
    Input('display-type', 'value'),
)
def display_swallowed_vote_fig_1(display_type):
    print(f"#### in display_swallowed_vote_fig_1")
    fig = fig_builder.build_swallowed_vote_fig_1(data_obj)
    return fig

@app.callback(
    Output('swallowed-vote-sampler-2', 'figure'),
    Input('display-type', 'value'),
)
def display_swallowed_vote_fig_2(display_type):
    print(f"#### in display_swallowed_vote_fig_2")
    fig = fig_builder.build_swallowed_vote_fig_2(data_obj)
    return fig

@app.callback(
    Output('swallowed-vote-sampler-3', 'figure'),
    Input('display-type', 'value'),
)
def display_swallowed_vote_fig_3(display_type):
    print(f"#### in display_swallowed_vote_fig_3")
    fig = fig_builder.build_swallowed_vote_fig_3(data_obj)
    return fig

@app.callback(
    Output('swallowed-vote-sampler-4', 'figure'),
    Input('display-type', 'value'),
)
def display_swallowed_vote_fig_4(display_type):
    print(f"#### in display_swallowed_vote_fig_4")
    fig = fig_builder.build_swallowed_vote_fig_4(data_obj)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)