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
year_dropdown = dbc.FormGroup([
    html.H4("Election Year"),
    dcc.Dropdown(
        id="year-input", 
        options=[{"label": y, "value": y} for y in data_obj.all_years], 
        value="2020"
    ),
    html.Br(),
    html.H4("Grouping Options"),
    dcc.Dropdown(
        id="groupings-input", 
        options=[
            {'label': 'Original', 'value': 'Original'},
            {'label': 'Alternate', 'value': 'Alternate'}
        ], 
        value="Original"
    ), 
    html.Br(),
    dcc.Checklist(
        id="small-group-input", 
        options=[
            {'label': 'Extract Small', 'value': 'Extract Small'},
        ],
        value=['Extract Small']
    )
])


swallowed_vote_view_dropdown = dbc.FormGroup([
    html.H4("Swallowed vote view"),
    dcc.Dropdown(id="display-type", options=[{"label": "2020", "value": "2020"}], value="2020")
])


layout_1 = html.Div([
    ## Top
    navbar,
    html.Br(),

    dbc.Row([
        ### input + panel
        dbc.Col(md=2, children=[
            year_dropdown,
            html.Br(),html.Br(),
            html.Div(id="year-summary")
        ]),
        dbc.Col(md=10, children=[
            dbc.Col(html.H4("Inter-State Voter Impact Comparison"), width={"size": 6, "offset": 3}), 
            html.Br(),
            dbc.Tabs(className="nav nav-pills", children=[
                dbc.Tab(label="Comparing States", children=[
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="vote-weight-comparison-by-state-map-1"),
                            html.Br(),
                            dcc.Graph(id="vote-weight-comparison-by-state-bar-1"),
                            html.Br(),
                            dcc.Graph(id="vote-weight-comparison-by-state-bar-2")
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="vote-weight-comparison-by-state-scatter-1"),
                            html.Br(),
                            dcc.Graph(id="vote-weight-comparison-by-state-scatter-2"),
                            html.Br(),
                            dcc.Graph(id="vote-weight-comparison-by-state-scatter-3")
                        ])
                    ])
                ]),

                dbc.Tab(label="Comparing Historical Regions", children=[
                    dbc.Row([
                        dbc.Col(md=12, children=[
                            dcc.Graph(id="vote-weight-comparison-by-state-group-line-1")
                        ])
                    ]),
                    html.Br(),
                    dbc.Row([
                        ### input + panel
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="vote-weight-comparison-by-state-group-map-1"),
                            html.Br(),
                            dcc.Graph(id="vote-weight-comparison-by-state-group-box-1")
                        ]),
                        ### map
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="vote-weight-comparison-by-state-group-scatter-1"),
                            html.Br(),
                            dcc.Graph(id="vote-weight-comparison-by-state-group-scatter-2")
                        ])
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
    Output('vote-weight-comparison-by-state-scatter-1', 'figure'),
    Output('vote-weight-comparison-by-state-scatter-2', 'figure'),
    Output('vote-weight-comparison-by-state-scatter-3', 'figure'),
    Input('year-input', 'value'),
    Input('groupings-input', 'value'),
    Input('small-group-input', 'value'),
)
def update_figure(year_input, groupings_input, small_group_input):
    # process input
    year = int(year_input)
    subdir = map_to_subdir(groupings_input, small_group_input)
    data_obj.load_dfs_for_subdir(subdir)
    # generate figs
    fig_map_1 = fig_builder.build_ivw_by_state_map(data_obj, year, subdir=subdir)
    fig_bar_1 = fig_builder.build_fig_for_year(data_obj, year, subdir=subdir)
    fig_bar_2 = fig_builder.build_actual_vs_adjusted_ec_fig(data_obj, year, subdir=subdir)
    fig_scatter_1 = fig_builder.build_ivw_by_state_scatter_1(data_obj, year, subdir=subdir)
    fig_scatter_2 = fig_builder.build_ivw_by_state_scatter_2(data_obj, year, subdir=subdir)
    fig_scatter_3 = fig_builder.build_ivw_by_state_scatter_3(data_obj, year, subdir=subdir)
    return fig_map_1, fig_bar_1, fig_bar_2, fig_scatter_1, fig_scatter_2, fig_scatter_3

@app.callback(
    Output('vote-weight-comparison-by-state-group-map-1', 'figure'),
    Output('vote-weight-comparison-by-state-group-line-1', 'figure'),
    Output('vote-weight-comparison-by-state-group-box-1', 'figure'),
    Output('vote-weight-comparison-by-state-group-scatter-1', 'figure'),
    Output('vote-weight-comparison-by-state-group-scatter-2', 'figure'),
    Input('year-input', 'value'),
    Input('groupings-input', 'value'),
    Input('small-group-input', 'value'),
)
def update_overlay_figure(year_input, groupings_input, small_group_input):
    # process input
    year = int(year_input)
    subdir = map_to_subdir(groupings_input, small_group_input)
    data_obj.load_dfs_for_subdir(subdir)
    # generate figs
    fig_map_1 = fig_builder.build_state_groups_map(data_obj, year, subdir=subdir)
    fig_line_1 = fig_builder.build_ivw_by_state_group_line_chart(data_obj, year, subdir=subdir)
    fig_box_1 = fig_builder.build_ivw_by_state_group_box_plot(data_obj, year, subdir=subdir)
    fig_scatter_1 = fig_builder.build_ivw_by_state_group_scatter_1(data_obj, year, subdir=subdir)
    fig_scatter_2 = fig_builder.build_ivw_by_state_group_scatter_2(data_obj, year, subdir=subdir)
    return fig_map_1, fig_line_1, fig_box_1, fig_scatter_1, fig_scatter_2


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