# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
#import flask

import pandas as pd
import plotly
import plotly.express as px

# from .metadata import PIVOT_ON_YEAR_CSV


BASE_DATA_DIR = 'data'
PIVOT_ON_YEAR_CSV = f'{BASE_DATA_DIR}/pivotOnYear.csv'


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#server = app.server


colors = {
    'background': '#111111',
    'text': '#000000'
}



def validate_input(year_input):
    year = int(year_input)
    if year in all_years:
        return year
    else:
        return -1

def build_fig_for_year(year):
    # extract single-year data
    pivot_on_single_year = pivot_on_year[pivot_on_year['Year'] == year].sort_values('Party', ascending=True)
    
    # update fig
    fig = px.bar(pivot_on_single_year, x='Vote weight', y='State', color='Party', 
                width=1000, height=800)

    fig.update_layout(
        yaxis={'tickangle':35, 'showticklabels':True, 'type':'category', 'tickfont_size':8},
        yaxis_categoryorder = 'total ascending'
    )

    return fig



# load source data 
pivot_on_year = pd.read_csv(PIVOT_ON_YEAR_CSV)
pivot_on_year.drop('Unnamed: 0', axis=1, inplace=True)
all_years = pivot_on_year['Year'].unique()

# init default fig
fig = build_fig_for_year(2016)



# show fig via app layout
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
    year = validate_input(year_input)
    if year == -1:
        year = 2016

    fig = build_fig_for_year(year)

    return fig


if __name__ == '__main__':
    # hot-reload: automatically reload page when source is edited
    app.run_server(debug=True)
    # app.run_server(dev_tools_hot_reload=False)