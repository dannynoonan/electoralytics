import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash_pages.components import navbar


content = html.Div([
    navbar,
    dbc.Card(className="bg-success", children=[
        dbc.CardBody([
            html.Br(),
            # dbc.Row(className="text-white", justify="center", align="center", children=[
            #     html.H3("Visualizing Jim Crow Voter Suppression: Population, Participation, and Electoral College Bias"),
            # ]),
            # html.Br(),
            dbc.Card(className="bg-success border-primary", children=[
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            html.H4(children=[
                                dcc.Link("2/10/2021: Visualizing Jim Crow Voter Suppression: Population, Participation, and Electoral College Bias", 
                                href="/voter-weight-electoral-college-bias-overview", className="text-white")
                            ]),
                            html.Br(),
                            html.P(className="text-white", children=[
                                "The Electoral College is known for its quirks and imbalances. It allocates greater influence to voters in smaller states. \
                                It originally tabulated slaves as three-fifths of a person, then handed that three-fifths boost to slave-owners. And where \
                                it does meter out influence based purely on population, it does so with no regard to voter participation, leaving it \
                                vulnerable to legalistic manipulation while incentivizing voter suppression."
                            ]),
                            html.P(className="text-white", children=[
                                "A ", html.U(children=[dcc.Link("recent episode", href="https://www.npr.org/2020/09/30/918717270/the-electoral-college", 
                                target="_blank", className="text-white")]),
                                " of ", html.I("NPR’s Throughline"), " delved into one way this disconnect between Electoral College representation and \
                                voter participation has been manipulated, framing voter suppression in the Jim Crow South in terms of the Constitution’s \
                                original three-fifths slave-tabulating logic. The podcast pointed out that while the Reconstruction amendments gave full \
                                citizenship and voting rights to former slaves, the trampling of these rights at the state level was selective: Blacks were \
                                dropped from voter rolls, but recorded as full citizens in the population census. In doing so, Southern Redeemer governments \
                                effectively replaced the antebellum three-fifths status quo with a new “five-fifths” boost to the Southern white vote."
                            ]),
                            html.P(className="text-white", children=[
                                "2020 was a year of fresh perspectives on racial justice history, and quantifying slavery’s apportionment logic side-by-side \
                                with the suppression effects of Jim Crow was fresh perspective for me. Not only did this thrust the remote, anachronistic \
                                history of the three-fifths compromise onto the doorstep of the very recent past, it also prompted me to wonder: is there a \
                                uniform way to quantify the relative fairness, inequity, or bias enjoyed/exploited by any given state, in any given election?"
                            ]),
                            html.P(className="text-white", children=[
                                "I took a stab at unearthing any scholarly metrics on the topic and came up empty, so I forged ahead with my own amateur \
                                mathing. Using a simple, generic formula, aided by python data processing and visualization tools, I’ve attempted an \
                                apples-to-apples comparison of voter influence per state over time. The slavery vs Jim Crow comparison is at the heart of my \
                                exploration, but a number of other twists, turns, and trends popped up along the way."
                            ]),
                            html.P(className="text-white", children=[
                                "Continue to the ", html.U(children=[dcc.Link("Main article...", href="/voter-weight-electoral-college-bias-overview", 
                                className="text-white")])
                            ]),
                            dcc.Link(href="/voter-weight-electoral-college-bias-overview", children=[
                                html.Img(src="/static/screenshots/barFreeSlaveSmall1852.png", height="300", style={"padding": "5px", "padding-top": "10px"}),
                                html.Img(src="/static/screenshots/mapFreeSlaveSmall1852.png", height="300", style={"padding": "5px", "padding-top": "10px"}),
                                html.Img(src="/static/screenshots/scatterDotsAcw1920.png", height="272", style={"padding": "5px", "padding-top": "10px"}),
                                html.Img(src="/static/screenshots/scatterBubblesAcw1940.png", height="272", style={"padding": "5px", "padding-top": "10px"}),
                            ]),
                        ]),
                        dbc.Col(md=6, children=[
                            # html.H4(className="text-white", children=[
                            #     "Supplemental material:"
                            # ]),
                            html.Div(className="list-group", children=[
                                html.A(className="list-group-item list-group-item-action flex-column align-items-start bg-primary", children=[
                                    html.H4(className="mb-1 text-white", children=[
                                        "Supplemental sections",
                                    ]),
                                ]),
                                html.A(className="list-group-item list-group-item-action flex-column align-items-start bg-primary", 
                                    href="/voter-weight-timeline-visualization", children=[
                                    html.H4(className="mb-1 text-success", children=[
                                        "Annotated Timeline Charting Voter Weight Trends: 1800 - 2020",
                                    ]),
                                    html.Img(src="/static/screenshots/lineChartGroupVwSince1800.png", height="250", style={"padding": "5px", "padding-top": "10px"}),
                                    # html.Img(src="/static/screenshots/lineChartWIvsGAsince1800.png", height="250", style={"padding": "5px", "padding-top": "10px"}),
                                ]),
                                html.A(className="list-group-item list-group-item-action flex-column align-items-start bg-primary", 
                                    href="/voter-weight-figure-vault", children=[
                                    html.H4(className="mb-1 text-success", children=[
                                        "The Vault: 220 Years of Maps, Bar Charts, Scatter Plots, and Box Plots",
                                    ]),
                                    html.Img(src="/static/screenshots/scatterBubblesAcw1900.png", height="250", style={"padding": "5px", "padding-top": "10px"}),
                                    html.Img(src="/static/screenshots/boxAcw1920.png", height="250", style={"padding": "5px", "padding-top": "10px"}),
                                    # html.Img(src="/static/screenshots/scatterAbbrevsAcw1920.png", height="250", style={"padding": "5px", "padding-top": "10px"}),
                                    # html.Img(src="/static/screenshots/mapVoteWeights1880.png", height="250", style={"padding": "5px", "padding-top": "10px"}),
                                ]),
                                html.A(className="list-group-item list-group-item-action flex-column align-items-start bg-primary", 
                                    href="/voter-weight-calculation", children=[
                                    html.H4(className="mb-1 text-success", children=[
                                        "Calculating Voter Weight",
                                    ]),
                                    html.Img(src="/static/vwMath/derivingPvpeVw.png", height="150", style={"padding": "5px", "padding-top": "10px"}),
                                    html.Img(src="/static/vwMath/vwEcSummQuotEquation.png", height="150", style={"padding": "5px", "padding-top": "10px"}),
                                    # html.Img(src="/static/vwMath/vwMathSampler/popToEcWIGA1900.png", height="150", style={"padding": "5px", "padding-top": "10px"}),
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
                            ]),
                        ]),
                    ]),
                ]),
            ]),
        ])
    ]),
    html.Br(),
])