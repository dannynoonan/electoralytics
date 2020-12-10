import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import flask

import pandas as pd
import plotly.express as px

from data_processor.data_objects import DataObject
from data_processor.fig_builder import build_fig_for_year
from data_processor.functions import validate_input


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# server is needed for heroku deployment
server = app.server


colors = {
    'background': '#111111',
    'text': '#000000'
}


# load source data 
do = DataObject()
do.load_pivot_on_year()

# init default fig
fig = build_fig_for_year(2016, do.pivot_on_year_df)



url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

layout_index = html.Div([
    dcc.Link('Voter impact by state', href='/page-1'),
    html.Br(),
    dcc.Link('Some other page', href='/page-2'),
])

layout_page_1 = html.Div([
    html.H1(
        children='Where votes count the most',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(
        children='Individual voter impact per state in Presidential elections',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(["Election Year: ",
              dcc.Input(id='year-input', value='2016', type='text', debounce=True)]),

    dcc.Graph(
        id='indicator-graphic',
        figure=fig
    ),


    html.Br(),
    dcc.Link('Home', href='/'),
    html.Br(),
    dcc.Link('Some other page', href='/page-2'),
])

layout_page_2 = html.Div([
    html.H2('Some other page'),
    dcc.Dropdown(
        id='page-2-dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='page-2-display-value'),
    html.Br(),
    dcc.Link('Home', href='/'),
    html.Br(),
    dcc.Link('Voter impact by state', href='/page-1'),
])

# index layout
app.layout = url_bar_and_content_div

# "complete" layout
app.validation_layout = html.Div([
    url_bar_and_content_div,
    layout_index,
    layout_page_1,
    layout_page_2,
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
        return layout_index


# Page 1 callbacks
@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('year-input', 'value'))
def update_figure(year_input):
    year = validate_input(year_input, do.all_years)
    if year == -1:
        year = 2016

    fig = build_fig_for_year(year, do.pivot_on_year_df)

    return fig


# Page 2 callbacks
@app.callback(Output('page-2-display-value', 'children'),
              Input('page-2-dropdown', 'value'))
def display_value(value):
    print('display_value')
    return 'You have selected "{}"'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)