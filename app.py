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
print(f"PIVOT_ON_YEAR_CSV: {PIVOT_ON_YEAR_CSV}")


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server


colors = {
    'background': '#111111',
    'text': '#000000'
}


# load source data 
pivot_on_year = pd.read_csv(PIVOT_ON_YEAR_CSV)
pivot_on_year.drop('Unnamed: 0', axis=1, inplace=True)

# extract single-year data
pivot_on_year_2016 = pivot_on_year[pivot_on_year['Year'] == 2016].sort_values('Party', ascending=True)

# create fig
fig = px.bar(pivot_on_year_2016, x="Vote weight", y="State", color='Party', 
             width=1000, height=800)

fig.update_layout(
    yaxis={'tickangle':35, 'showticklabels':True, 'type':'category', 'tickfont_size':8},
    yaxis_categoryorder = 'total ascending'
)

# show fig via app layout
app.layout = html.Div(children=[
    html.H1(
        children='Individual voter impact per state',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(["Select Year: ",
              dcc.Input(id='year-input', value='2016', type='text')]),

    dcc.Graph(
        id='indicator-graphic',
        figure=fig
    ),
])


@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('year-input', 'value'))
def update_graph(year_input):
    year = int(year_input)
    #print(f"Accessing pivot_on_year with len: {len(pivot_on_year)} for year_value: {year}")
    pivot_on_single_year = pivot_on_year[pivot_on_year['Year'] == year].sort_values('Party', ascending=True)
    #print(f"Sorted pivot_on_single_year with len: {len(pivot_on_single_year)}")
    
    # update fig
    fig = px.bar(pivot_on_single_year, x='Vote weight', y='State', color='Party', 
                width=1000, height=800)

    fig.update_layout(
        yaxis={'tickangle':35, 'showticklabels':True, 'type':'category', 'tickfont_size':8},
        yaxis_categoryorder = 'total ascending'
    )

    return fig


if __name__ == '__main__':
    # hot-reload: automatically reload page when source is edited
    app.run_server(debug=True)
    # app.run_server(dev_tools_hot_reload=False)