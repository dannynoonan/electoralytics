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
            dbc.DropdownMenuItem([html.I(className="fa"), "Inter-State Voter Impact Comparison"], href='/vote-weight-comparison', target="_blank"), 
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
        dbc.Col(md=9, children=[
            html.H4("Election Year")
        ]),
        dbc.Col(md=3, children=[
            html.H4("Grouping Options")
        ])
    ]),
    dbc.Row([
        dbc.Col(md=9, children=[
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
                    {'label': 'Civil War', 'value': 'Civil War'},
                    {'label': 'Regional Census', 'value': 'Regional Census'}
                ], 
                value="Civil War"
            )
        ]),
        dbc.Col(md=1, children=[
            dcc.Checklist(
                id="small-group-input", 
                options=[
                    {'label': ' Extract Small', 'value': 'Extract Small'},
                ],
                value=['Extract Small']
            )
        ])
    ])
])


swallowed_vote_view_dropdown = dbc.FormGroup([
    html.H4("Swallowed vote view"),
    dcc.Dropdown(id="display-type", options=[{"label": "2020", "value": "2020"}], value="2020")
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
                            dcc.Graph(id="vote-weight-comparison-by-state-map-1"),
                            html.Br(),
                            dcc.Graph(id="vote-weight-comparison-by-state-scatter-dots"),
                            html.Br(),
                            dcc.Graph(id="vote-weight-comparison-by-state-bar-1"),
                            html.Br(),
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="vote-weight-comparison-by-state-scatter-bubbles"),
                            html.Br(), 
                            dcc.Graph(id="vote-weight-comparison-by-state-scatter-abbrevs"),
                            html.Br(),
                            dcc.Graph(id="vote-weight-comparison-by-state-bar-2"),
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
                            dcc.Graph(id="vote-weight-comparison-by-state-group-box-1"),
                            html.Br(),
                            dcc.Graph(id="vote-weight-comparison-by-state-group-map-1"),
                            html.Br(),
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="vote-weight-comparison-by-state-group-scatter-bubbles"),
                            html.Br(),
                            dcc.Graph(id="vote-weight-comparison-by-state-group-scatter-dots"),
                            html.Br(),
                        ])
                    ])
                ]),

                dbc.Tab(label="State-Level Comparisons - Slider/Animations", tab_style={"font-size": "20px"}, children=[
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

                dbc.Tab(label="Regional Aggregate Comparisons - Slider/Animations", tab_style={"font-size": "20px"}, children=[
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


# layout 2
layout_2 = html.Div([
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
    empty_layout,
])



# Index callbacks
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/vote-weight-comparison":
        return layout_1
    elif pathname == "/swallowed-vote-sampler":
        return layout_2
    else:
        return empty_layout



# Layout 1 callbacks
@app.callback(
    Output('vote-weight-comparison-by-state-map-1', 'figure'),
    Output('vote-weight-comparison-by-state-bar-1', 'figure'),
    Output('vote-weight-comparison-by-state-bar-2', 'figure'),
    Output('vote-weight-comparison-by-state-scatter-dots', 'figure'),
    Output('vote-weight-comparison-by-state-scatter-abbrevs', 'figure'),
    Output('vote-weight-comparison-by-state-scatter-bubbles', 'figure'),
    Input('year-input', 'value'),
    Input('groupings-input', 'value'),
    Input('small-group-input', 'value'),
)
def display_state_level_figs(year_input, groupings_input, small_group_input):
    # process input
    year = int(year_input)
    subdir = map_to_subdir(groupings_input, small_group_input)
    data_obj.load_dfs_for_subdir(subdir)
    # generate figs
    fig_map_1 = fig_builder.build_ivw_by_state_map(data_obj, frame=year, subdir=subdir)
    fig_bar_1 = fig_builder.build_ivw_by_state_bar(data_obj, frame=year, subdir=subdir)
    fig_bar_2 = fig_builder.build_actual_vs_adjusted_ec_bar(data_obj, frame=year, subdir=subdir)
    fig_scatter_dots = fig_builder.build_ivw_by_state_scatter_dots(data_obj, frame=year, subdir=subdir)
    fig_scatter_abbrevs = fig_builder.build_ivw_by_state_scatter_abbrevs(data_obj, frame=year, subdir=subdir)
    fig_scatter_bubbles = fig_builder.build_ivw_by_state_scatter_bubbles(data_obj, frame=year, subdir=subdir)
    return fig_map_1, fig_bar_1, fig_bar_2, fig_scatter_dots, fig_scatter_abbrevs, fig_scatter_bubbles

@app.callback(
    Output('vote-weight-comparison-by-state-group-map-1', 'figure'),
    Output('vote-weight-comparison-by-state-group-line-1', 'figure'),
    Output('vote-weight-comparison-by-state-group-box-1', 'figure'),
    Output('vote-weight-comparison-by-state-group-scatter-dots', 'figure'),
    Output('vote-weight-comparison-by-state-group-scatter-bubbles', 'figure'),
    Input('year-input', 'value'),
    Input('groupings-input', 'value'),
    Input('small-group-input', 'value'),
)
def display_regional_aggregate_figs(year_input, groupings_input, small_group_input):
    # process input
    year = int(year_input)
    subdir = map_to_subdir(groupings_input, small_group_input)
    data_obj.load_dfs_for_subdir(subdir)
    # generate figs
    fig_map_1 = fig_builder.build_state_groups_map(data_obj, frame=year, subdir=subdir)
    fig_line_1 = fig_builder.build_ivw_by_state_group_line_chart(data_obj, frame=year, subdir=subdir)
    fig_box_1 = fig_builder.build_ivw_by_state_group_box_plot(data_obj, frame=year, subdir=subdir)
    fig_scatter_dots = fig_builder.build_ivw_by_state_group_scatter_dots(data_obj, frame=year, subdir=subdir)
    fig_scatter_bubbles = fig_builder.build_ivw_by_state_group_scatter_bubbles(data_obj, frame=year, subdir=subdir)
    return fig_map_1, fig_line_1, fig_box_1, fig_scatter_dots, fig_scatter_bubbles

@app.callback(
    Output('vote-weight-comparison-by-state-map-1-anim', 'figure'),
    # Output('vote-weight-comparison-by-state-bar-1-anim', 'figure'),
    # Output('vote-weight-comparison-by-state-bar-2-anim', 'figure'),
    Output('vote-weight-comparison-by-state-scatter-dots-anim', 'figure'),
    Output('vote-weight-comparison-by-state-scatter-abbrevs-anim', 'figure'),
    Output('vote-weight-comparison-by-state-scatter-bubbles-anim', 'figure'),
    Input('groupings-input', 'value'),
    Input('small-group-input', 'value'),
)
def display_state_level_anims(groupings_input, small_group_input):
    # process input
    subdir = map_to_subdir(groupings_input, small_group_input)
    data_obj.load_dfs_for_subdir(subdir)
    # generate figs
    anim_map_1 = fig_builder.build_ivw_by_state_map(data_obj, subdir=subdir)
    # anim_bar_1 = fig_builder.build_ivw_by_state_bar(data_obj, subdir=subdir)
    # anim_bar_2 = fig_builder.build_actual_vs_adjusted_ec_bar(data_obj, subdir=subdir)
    anim_scatter_dots = fig_builder.build_ivw_by_state_scatter_dots(data_obj, subdir=subdir)
    anim_scatter_abbrevs = fig_builder.build_ivw_by_state_scatter_abbrevs(data_obj, subdir=subdir)
    anim_scatter_bubbles = fig_builder.build_ivw_by_state_scatter_bubbles(data_obj, subdir=subdir)
    return anim_map_1, anim_scatter_dots, anim_scatter_abbrevs, anim_scatter_bubbles


@app.callback(
    Output('vote-weight-comparison-by-state-group-map-1-anim', 'figure'),
    Output('vote-weight-comparison-by-state-group-scatter-dots-anim', 'figure'),
    Output('vote-weight-comparison-by-state-group-scatter-bubbles-anim', 'figure'),
    Input('groupings-input', 'value'),
    Input('small-group-input', 'value'),
)
def display_regional_aggregate_anims(groupings_input, small_group_input):
    # process input
    subdir = map_to_subdir(groupings_input, small_group_input)
    data_obj.load_dfs_for_subdir(subdir)
    # generate figs
    anim_map_1 = fig_builder.build_state_groups_map(data_obj, subdir=subdir)
    anim_scatter_dots = fig_builder.build_ivw_by_state_group_scatter_dots(data_obj, subdir=subdir)
    anim_scatter_bubbles = fig_builder.build_ivw_by_state_group_scatter_bubbles(data_obj, subdir=subdir)
    return anim_map_1, anim_scatter_dots, anim_scatter_bubbles



# Layout 2 callbacks
@app.callback(
    Output('swallowed-vote-sampler-1', 'figure'),
    Input('display-type', 'value'),
)
def display_swallowed_vote_fig_1(display_type):
    fig = fig_builder.build_swallowed_vote_fig_1(data_obj)
    return fig

@app.callback(
    Output('swallowed-vote-sampler-2', 'figure'),
    Input('display-type', 'value'),
)
def display_swallowed_vote_fig_2(display_type):
    fig = fig_builder.build_swallowed_vote_fig_2(data_obj)
    return fig

@app.callback(
    Output('swallowed-vote-sampler-3', 'figure'),
    Input('display-type', 'value'),
)
def display_swallowed_vote_fig_3(display_type):
    fig = fig_builder.build_swallowed_vote_fig_3(data_obj)
    return fig

@app.callback(
    Output('swallowed-vote-sampler-4', 'figure'),
    Input('display-type', 'value'),
)
def display_swallowed_vote_fig_4(display_type):
    fig = fig_builder.build_swallowed_vote_fig_4(data_obj)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)