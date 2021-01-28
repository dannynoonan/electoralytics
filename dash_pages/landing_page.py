import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash_pages.components import navbar


content = html.Div([
    navbar,
    html.Div(className="jumbotron bg-success text-white", children=[
        html.H3(children=[
            "Visualizing Jim Crow Voter Suppression: Population, Participation, and Electoral College Bias"
        ]),
        html.Br(),
        html.Div(className="list-group", children=[
            html.A(className="list-group-item list-group-item-action flex-column align-items-start bg-primary", 
                href="/voter-weight-electoral-college-bias-overview", children=[
                html.H4(className="mb-1 text-success", children=[
                    "Visualizing Jim Crow Voter Suppression: Population, Participation, and “Voter Weight” (main article)"
                ]),
                html.Img(src="/static/screenshots/barFreeSlaveSmall1852.png", height="250", style={"padding": "5px", "padding-top": "10px"}),
                html.Img(src="/static/screenshots/mapFreeSlaveSmall1852.png", height="250", style={"padding": "5px", "padding-top": "10px"}),
                html.Img(src="/static/screenshots/scatterDotsAcw1920.png", height="250", style={"padding": "5px", "padding-top": "10px"}),
                html.Img(src="/static/screenshots/scatterBubblesAcw1940.png", height="250", style={"padding": "5px", "padding-top": "10px"}),
            ]),
            html.A(className="list-group-item list-group-item-action flex-column align-items-start bg-primary", 
                href="/voter-weight-timeline-visualization", children=[
                html.H4(className="mb-1 text-success", children=[
                    "Annotated Timeline Charting Voter Weight Trends: 1800 - 2020",
                ]),
                html.Img(src="/static/screenshots/lineChartGroupVwSince1800.png", height="250", style={"padding": "5px", "padding-top": "10px"}),
                html.Img(src="/static/screenshots/lineChartWIvsGAsince1800.png", height="250", style={"padding": "5px", "padding-top": "10px"}),
            ]),
            html.A(className="list-group-item list-group-item-action flex-column align-items-start bg-primary", 
                href="/voter-weight-figure-vault", children=[
                html.H4(className="mb-1 text-success", children=[
                    "The Vault: 220 Years of Maps, Bar Charts, Scatter Plots, and Box Plots",
                ]),
                html.Img(src="/static/screenshots/scatterBubblesAcw1900.png", height="250", style={"padding": "5px", "padding-top": "10px"}),
                html.Img(src="/static/screenshots/boxAcw1920.png", height="250", style={"padding": "5px", "padding-top": "10px"}),
                html.Img(src="/static/screenshots/scatterAbbrevsAcw1920.png", height="250", style={"padding": "5px", "padding-top": "10px"}),
                html.Img(src="/static/screenshots/mapVoteWeights1880.png", height="250", style={"padding": "5px", "padding-top": "10px"}),
            ]),
            html.A(className="list-group-item list-group-item-action flex-column align-items-start bg-primary", 
                href="/voter-weight-calculation", children=[
                html.H4(className="mb-1 text-success", children=[
                    "Calculating Voter Weight",
                ]),
                html.Img(src="/static/vwMath/derivingPvpeVw.png", height="150", style={"padding": "5px", "padding-top": "10px"}),
                html.Img(src="/static/vwMath/vwEcSummQuotEquation.png", height="150", style={"padding": "5px", "padding-top": "10px"}),
                html.Img(src="/static/vwMath/vwMathSampler/popToEcWIGA1900.png", height="150", style={"padding": "5px", "padding-top": "10px"}),
            ]),
            html.A(className="list-group-item list-group-item-action flex-column align-items-start bg-primary", 
                href="/explanation-of-groupings", children=[
                html.H4(className="mb-1 text-success", children=[
                    "Explanation of State Groupings",
                ]),
                html.Img(src="/static/screenshots/mapAcw1880.png", height="250", style={"padding": "5px", "padding-top": "10px"}),
                html.Img(src="/static/screenshots/mapCensus1960.png", height="250", style={"padding": "5px", "padding-top": "10px"}),
            ]),
            html.A(className="list-group-item list-group-item-action flex-column align-items-start bg-primary", 
                href="/voter-weight-conclusions", children=[
                html.H4(className="mb-1 text-success", children=[
                    "Discussion and Conclusions", 
                ])
            ]),
        ])
    ]),
    html.Br(),
])