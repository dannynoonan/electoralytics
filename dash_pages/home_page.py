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
                                simple equations and illustrated through data visualizations."
                            ]),
                            html.A(className="list-group-item list-group-item-action flex-column align-items-start bg-primary", 
                                href="/census-2020-retrofit", children=[
                                html.H4(className="mb-1 text-success", children=[
                                    "[May 5, 2021] Retrofitting the 2020 Census to 2020 Election data (", html.I("Click to read article"), ")",
                                ]),
                                html.Img(src="/static/screenshots/census2020Retrofit/ecVotesBarRetrofit.png", width="31.83%", style={"padding": "5px", "padding-top": "10px"}),
                                html.Img(src="/static/screenshots/census2020Retrofit/voterWeightMapRetrofit.png", width="36.33%", style={"padding": "5px", "padding-top": "10px"}),
                                html.Img(src="/static/screenshots/census2020Retrofit/voterWeightBarRetrofit.png", width="31.83%", style={"padding": "5px", "padding-top": "10px"}),
                            ]),
                            html.A(className="list-group-item list-group-item-action flex-column align-items-start bg-primary", 
                                href="/voter-weight-electoral-college-bias-intro", children=[
                                html.H4(className="mb-1 text-success", children=[
                                    "[April 2, 2021] Visualizing the “Jim Crow Power” through Electoral College data (", html.I("Click to read article"), ")",
                                ]),
                                html.Img(src="/static/screenshots/barFreeSlaveSmall1852.png", width="27.7%", style={"padding": "5px", "padding-top": "10px"}),
                                html.Img(src="/static/screenshots/mapFreeSlaveSmall1852.png", width="37.22%", style={"padding": "5px", "padding-top": "10px"}),
                                html.Img(src="/static/screenshots/scatterDotsFreeSlaveSmall1852.png", width="35.08%", style={"padding": "5px", "padding-top": "10px"}),
                                html.Br(),
                                html.Img(src="/static/screenshots/barAcw1920.png", width="25.46%", style={"padding": "5px", "padding-top": "10px"}),
                                html.Img(src="/static/screenshots/scatterBubblesAcw1920.png", width="36.21%", style={"padding": "5px", "padding-top": "10px"}),
                                html.Img(src="/static/screenshots/boxAcw1920.png", width="38.33%", style={"padding": "5px", "padding-top": "10px"}),
                                html.Br(),
                                html.Img(src="/static/screenshots/lineChartGroupVwSince1800.png", width="100%", style={"padding": "5px", "padding-top": "10px"}),
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