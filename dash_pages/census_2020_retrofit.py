import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash_pages.components import navbar, data_obj


content = html.Div([
    navbar,
    dbc.Card(className="bg-success", children=[
        dbc.CardBody([
            html.Br(),
            dbc.Row(className="text-white", justify="center", align="center", children=[
                html.H3("Applying 2020 Census data to the 2020 Presidential election"),
                # html.H3("Retrofitting the 2020 Presidential election to 2020 Census data"),
            ]),
            html.Br(),
            html.Div(children=[
                dcc.Dropdown(
                    id="fake-input",
                    options=[
                        {'label': 'Bar chart', 'value': 'bar_chart'},
                        {'label': 'Map', 'value': 'map'},
                        {'label': 'Scatter plot: dots', 'value': 'scatter_dots'},
                        {'label': 'Scatter plot: abbrevs', 'value': 'scatter_abbrevs'},
                    ], 
                    value='bar_chart',
                )
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=6, children=[
                    dcc.Graph(id="fig-bar-2020"),
                    html.Br(),
                    dcc.Graph(id="fig-map-2020"),
                    html.Br(),
                    dcc.Graph(id="fig-scatter-dots-2020"),
                    html.Br(),
                    dcc.Graph(id="fig-scatter-bubbles-2020"),
                ]),
                dbc.Col(md=6, children=[
                    dcc.Graph(id="fig-bar-2020-retrofit"),
                    html.Br(),
                    dcc.Graph(id="fig-map-2020-retrofit"),
                    html.Br(),
                    dcc.Graph(id="fig-scatter-dots-2020-retrofit"),
                    html.Br(),
                    dcc.Graph(id="fig-scatter-bubbles-2020-retrofit"),
                ])
            ]),
        ])
    ])
])