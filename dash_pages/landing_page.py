import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


from dash_pages.components import navbar


content = html.Div([
    navbar,
    html.Br(),html.Br(),
    dbc.Row([
        dbc.Col(md=1),
        dbc.Col(md=5, children=[
            dbc.Card([
                dbc.CardBody([
                    html.H4("Landing Page", className="card-title"),
                    html.P(
                        "Landing content",
                        className="card-text",
                    ),
                ]),
            ])
        ]),
        dbc.Col(md=6),
    ]),
    html.Br(),
])