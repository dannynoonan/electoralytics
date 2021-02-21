import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash_pages.components import navbar, data_obj


content = html.Div([
    navbar,
    dbc.Card(className="border-primary bg-dark", children=[
        dbc.CardBody([
            html.Br(),
            dbc.Row([
                # dbc.Col(md=1),
                dbc.Col(md=8, children=[
                    dbc.Card(className="border-success lead", style={"font-family": "times-new-roman"}, children=[
                        dbc.CardBody([
                            html.H3("Welcome to Electoralytics"),
                            html.P(children=[
                                "Inside you’ll find an exploration of the imbalances built into the US electoral system, described through \
                                simple equations and illustrated through data visualizations. The first project, of what I hope will be many, is \
                                a deep dive into Electoral College data to illustrate the effects of disenfranchisement in the Jim Crow South as \
                                compared to the pre-Civil War era of slavery."
                            ]),
                            html.H4(children=[
                                dcc.Link("[2/12/2021] American voter enfranchisement: A zero-sum game", href="/voter-weight-landing")
                            ]),
                        ]),
                    ]),
                ]),
                # dbc.Col(md=1),
            ]),
            dbc.Row([
                html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),
                html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),
            ]),
        ]),
    ]),
])