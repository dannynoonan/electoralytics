# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
#import flask

import pandas as pd
import plotly.express as px

from functions import validate_input, build_fig_for_year
from metadata import BASE_DATA_DIR, PIVOT_ON_YEAR_CSV


# # override hover_data
# hover_data = {'Party': False, 'Votes counted': True, 'EC votes': True, 'Pop. per EC vote': True, 
#               'EC votes normalized': True}


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# server is needed for heroku deployment
server = app.server


colors = {
    'background': '#111111',
    'text': '#000000'
}



# load source data 
pivot_on_year_df = pd.read_csv(PIVOT_ON_YEAR_CSV)
pivot_on_year_df.drop('Unnamed: 0', axis=1, inplace=True)
# rename pop per EC vote
pivot_on_year_df.rename(columns={'Population per EC vote': 'Pop. per EC vote'}, inplace=True)
# extract valid election years (for request validation)
all_years = pivot_on_year_df['Year'].unique()

# init default fig
fig = build_fig_for_year(2016, pivot_on_year_df)



# render fig via app layout
app.layout = html.Div(children=[
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
])


@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('year-input', 'value'))
def update_graph(year_input):
    year = validate_input(year_input, all_years)
    if year == -1:
        year = 2016

    fig = build_fig_for_year(year, pivot_on_year_df)

    return fig


if __name__ == '__main__':
    # hot-reload: automatically reload page when source is edited
    app.run_server(debug=True)
    # app.run_server(dev_tools_hot_reload=False)