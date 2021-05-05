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
            html.Br(),html.Br(),
            dbc.Row([
                dbc.Col(md=3, children=[
                    html.H4("Drag slider to see change:", className="text-white", style={'text-align': 'center'}),
                ]),
                dbc.Col(md=6, children=[
                    dcc.Slider(
                        id="year-input-census-2020-color-by-party",
                        min=2020.1,
                        max=2020.4,
                        step=None,
                        marks={
                            2020.1: {'label': '2020 election, before census', 'style': {'color': 'white'}},
                            2020.2: {'label': 'Pre-census highlights', 'style': {'text-align': 'left', 'color': 'white'}},
                            2020.3: {'label': 'Post-census highlights', 'style': {'color': 'white'}},
                            2020.4: {'label': '2020 election, retrofitted to census', 'style': {'white-space': 'nowrap', 'color': 'white'}},
                        },
                        value=2020.1,
                    ),
                ]),
                dbc.Col(md=3)
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=6, children=[
                    dcc.Graph(id="fig-bar-census-2020-color-by-party"),
                ]),
                dbc.Col(md=6, children=[
                    dcc.Graph(id="fig-map-census-2020-color-by-party"),
                ])
            ]),
            html.Br(),html.Br(),
            dbc.Row([
                dbc.Col(md=3, children=[
                    html.H4("Drag slider to see change:", className="text-white", style={'text-align': 'center'}),
                ]),
                dbc.Col(md=6, children=[
                    dcc.Slider(
                        id="year-input-census-2020-color-by-vw",
                        min=2020.1,
                        max=2020.4,
                        step=None,
                        marks={
                            2020.1: {'label': '2020 election, before census', 'style': {'color': 'white'}},
                            2020.2: {'label': 'Pre-census highlights', 'style': {'text-align': 'left', 'color': 'white'}},
                            2020.3: {'label': 'Post-census highlights', 'style': {'color': 'white'}},
                            2020.4: {'label': '2020 election, retrofitted to census', 'style': {'white-space': 'nowrap', 'color': 'white'}},
                        },
                        value=2020.1,
                    ),
                ]),
                dbc.Col(md=3)
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=6, children=[
                    dcc.Graph(id="fig-bar-census-2020-color-by-vw"),
                ]),
                dbc.Col(md=6, children=[
                    dcc.Graph(id="fig-map-census-2020-color-by-vw"),
                ])
            ]),
        ])
    ])
])