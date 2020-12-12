import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import flask

import pandas as pd
import plotly.express as px

from data_processor.data_objects import DataObject
from data_processor.fig_builder import build_actual_vs_adjusted_ec_fig, build_fig_for_year
from data_processor.functions import validate_input


# base config
app = dash.Dash(external_stylesheets=[dbc.themes.SOLAR])
# server is needed for heroku deployment
server = app.server


# load source data 
do = DataObject()
do.load_pivot_on_year()
do.melt_pivot_on_year()



# navbar
navbar = dbc.Nav(className="nav nav-pills", children=[
    dbc.DropdownMenu(label="Pages / Graphs", nav=True, children=[
        dbc.DropdownMenuItem([html.I(className="fa"), "Voter impact per state"], href='/page-1', target="_blank"), 
        dbc.DropdownMenuItem([html.I(className="fa"), "Another page"], href='/page-2', target="_blank")
    ]),
    dbc.DropdownMenu(label="References / Resources", nav=True, children=[
        dbc.DropdownMenuItem([html.I(className="fa"), "Source code"], href='https://github.com/dannynoonan/electoralytics', target="_blank"), 
        dbc.DropdownMenuItem([html.I(className="fa"), "Articles"], href='/resources/articles'),
        dbc.DropdownMenuItem([html.I(className="fa"), "Podcasts"], href='/resources/podcasts'),
        dbc.DropdownMenuItem([html.I(className="fa"), "Books"], href='/resources/books'),
    ])
])

# inputs
inputs = dbc.FormGroup([
    html.H4("Election Year"),
    dcc.Dropdown(id="year-input", options=[{"label": y, "value": y} for y in do.all_years], value="2020")
])

# app layout
app.layout = dbc.Container(fluid=True, children=[
    ## Top
    html.H1('Electoralytics', id="nav-pills"),
    navbar,
    html.Br(),html.Br(),html.Br(),
    ## Body
    dbc.Row([
        ### input + panel
        dbc.Col(md=3, children=[
            inputs, 
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



# Page 1 callbacks
@app.callback(
    Output('voter-impact-per-state', 'figure'),
    Input('year-input', 'value'),
)
def update_figure(year_input):
    year = int(year_input)
    fig = build_fig_for_year(year, do.pivot_on_year_df)
    return fig


@app.callback(
    Output('adjusted-ec-votes-per-state', 'figure'),
    Input('year-input', 'value'),
)
def update_overlay_figure(year_input):
    year = int(year_input)
    fig = build_actual_vs_adjusted_ec_fig(year, do.melted_pivot_on_year_df)
    return fig


# Page 2 callbacks
# @app.callback(Output('page-2-display-value', 'children'),
#               Input('page-2-dropdown', 'value'))
# def display_value(value):
#     print('display_value')
#     return 'You have selected "{}"'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)