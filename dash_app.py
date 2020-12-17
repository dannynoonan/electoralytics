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
from data_processor.functions import validate_input


# base config
app = dash.Dash(external_stylesheets=[dbc.themes.SOLAR])
# server is needed for heroku deployment
server = app.server


# load source data 
do = DataObject()
do.load_pivot_on_year()
do.melt_pivot_on_year()
do.load_swallowed_vote_sampler()



url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# navbar
navbar = html.Div([
    html.H1('Electoralytics', id="nav-pills"),
    dbc.Nav(className="nav nav-pills", children=[
        dbc.DropdownMenu(label="Pages / Graphs", nav=True, children=[
            dbc.DropdownMenuItem([html.I(className="fa"), "Voter impact per state"], href='/page-1', target="_blank"), 
            dbc.DropdownMenuItem([html.I(className="fa"), "Swallowed vote sampler"], href='/page-2', target="_blank")
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
    dcc.Dropdown(id="year-input", options=[{"label": y, "value": y} for y in do.all_years], value="2020")
])

swallowed_vote_view_dropdown = dbc.FormGroup([
    html.H4("Swallowed vote view"),
    dcc.Dropdown(id="display-type", options=[{"label": "2020", "value": "2020"}], value="2020")
])


# page 1
layout_page_1 = html.Div([
    ## Top
    # html.H1('Electoralytics', id="nav-pills"),
    navbar,
    html.Br(),html.Br(),

    dbc.Row([
        ### input + panel
        dbc.Col(md=3, children=[
            year_dropdown, 
            html.Br(),html.Br(),html.Br(),
            html.Div(id="year-summary")
        ]),
        ### figures
        dbc.Col(md=9, children=[
            dbc.Col(html.H4("States where votes count the most"), width={"size": 6, "offset": 3}), 
            dbc.Tabs(className="nav nav-pills", children=[
                dbc.Tab(dcc.Graph(id="voter-impact-per-state"), label="Voter impact per state"),
                dbc.Tab(dcc.Graph(id="adjusted-ec-votes-per-state"), label="Actual vs Adjusted EC votes"),
            ])
        ])
    ])
])


# page 2
layout_page_2 = html.Div([
    ## Top
    # html.H1('Electoralytics', id="nav-pills"),
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
    layout_page_1,
    layout_page_2,
    empty_layout,
])



# Index callbacks
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/page-1":
        return layout_page_1
    elif pathname == "/page-2":
        return layout_page_2
    else:
        return empty_layout


# Page 1 callbacks
@app.callback(
    Output('voter-impact-per-state', 'figure'),
    Input('year-input', 'value'),
)
def update_figure(year_input):
    year = int(year_input)
    fig = fig_builder.build_fig_for_year(year, do.pivot_on_year_df)
    return fig


@app.callback(
    Output('adjusted-ec-votes-per-state', 'figure'),
    Input('year-input', 'value'),
)
def update_overlay_figure(year_input):
    year = int(year_input)
    fig = fig_builder.build_actual_vs_adjusted_ec_fig(year, do.melted_pivot_on_year_df)
    return fig


# Page 2 callbacks
@app.callback(
    Output('swallowed-vote-sampler-1', 'figure'),
    Input('display-type', 'value'),
)
def display_swallowed_vote_fig_1(display_type):
    fig = fig_builder.build_swallowed_vote_fig_1(do.swallowed_vote_df)
    return fig

@app.callback(
    Output('swallowed-vote-sampler-2', 'figure'),
    Input('display-type', 'value'),
)
def display_swallowed_vote_fig_2(display_type):
    fig = fig_builder.build_swallowed_vote_fig_2(do.swallowed_vote_df)
    return fig

@app.callback(
    Output('swallowed-vote-sampler-3', 'figure'),
    Input('display-type', 'value'),
)
def display_swallowed_vote_fig_3(display_type):
    fig = fig_builder.build_swallowed_vote_fig_3(do.swallowed_vote_df)
    return fig

@app.callback(
    Output('swallowed-vote-sampler-4', 'figure'),
    Input('display-type', 'value'),
)
def display_swallowed_vote_fig_4(display_type):
    fig = fig_builder.build_swallowed_vote_fig_4(do.swallowed_vote_df)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)