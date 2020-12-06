# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

# from .metadata import PIVOT_ON_YEAR_CSV

BASE_DATA_DIR = 'data'
PIVOT_ON_YEAR_CSV = f'{BASE_DATA_DIR}/pivotOnYear.csv'
print(f"PIVOT_ON_YEAR_CSV: {PIVOT_ON_YEAR_CSV}")


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
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
        children='Ahoy',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Where does this appear?', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='does-this-matter',
        figure=fig
    ),
])



if __name__ == '__main__':
    # hot-reload: automatically reload page when source is edited
    app.run_server(debug=True)
    # app.run_server(dev_tools_hot_reload=False)