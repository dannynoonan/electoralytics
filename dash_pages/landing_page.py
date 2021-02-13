import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash_pages.components import navbar, data_obj


content = html.Div([
    navbar,
    dbc.Card(className="border-primary bg-success", children=[
        dbc.CardBody([
            html.Br(),
            dbc.Card(className="bg-primary", children=[
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            html.H4(children=[
                                dcc.Link("[2/12/2021] Visualizing Jim Crow Voter Suppression: Apportionment, Participation, and Electoral College Bias", 
                                href="/voter-weight-electoral-college-bias-overview")
                            ]),
                            html.Br(),
                            html.P(className="text-white", children=[
                                "The Electoral College is known for its quirks and imbalances. It allocates greater influence to voters in smaller states. \
                                It originally tabulated slaves as three-fifths of a person, giving that three-fifths boost to slave-owners. And where \
                                it does meter out influence based purely on population, it does so with no regard to voter participation, leaving it \
                                vulnerable to legalistic manipulation while incentivizing voter suppression."
                            ]),
                            html.P(className="text-white", children=[
                                "An ", dcc.Link("October 2020 episode", href="https://www.npr.org/2020/09/30/918717270/the-electoral-college", 
                                target="_blank"), " of ", html.I("NPR’s Throughline"), " delved into one such manipulation, framing disenfranchisement \
                                efforts in the Jim Crow South as a “five-fifths” variation on the Constitution’s original three-fifths slave-tabulating \
                                logic. In a year of fresh perspectives on racial justice history, not only did this thrust the remote, anachronistic \
                                history of the three-fifths compromise onto the doorstep of the very recent past, it also prompted me to wonder: is \
                                there a uniform way to quantify the relative fairness, inequity, or bias enjoyed/exploited by any given state, in any \
                                given election?"
                            ]),
                            html.P(className="text-white", children=[
                                "I took a stab at unearthing any scholarly metrics on the topic and didn't find any publications with the same objective, \
                                so I forged ahead with my own amateur data wrangling. Using a simple, generic formula, aided by python data processing and \
                                visualization tools, I’ve attempted an apples-to-apples comparison of voter influence per state over time. The slavery vs \
                                Jim Crow comparison is at the heart of my exploration, but a number of other twists, turns, and trends popped up along the way."
                            ]),
                            html.H5(className="text-white", children=[
                                "» Continue to the ", dcc.Link("main article...", href="/voter-weight-electoral-college-bias-overview")
                            ]),
                            html.Br(),

                            # dbc.Card(className="bg-primary", children=[
                            #     dbc.CardBody([
                                    html.H4(className="text-white", children=[
                                        "Supplemental sections:"
                                    ]),
                                    html.Div(className="accordion list-group", children=[
                                        html.A(className="list-group-item list-group-item-action flex-column align-items-start bg-success", children=[
                                            html.H5(className="mb-1 text-white", id="group-1-toggle", children=[
                                                "» Annotated Timeline Charting Voter Weight Trends",
                                            ]),
                                            dbc.Collapse(id="collapse-1", children=[
                                                dcc.Link(href="/voter-weight-timeline-visualization", children=[
                                                    html.Br(),
                                                    html.P(className="text-white", children=[
                                                        "Explore an interactive line chart plotting Voter Weight as a function of time from 1800 to 2020 »"
                                                    ]),
                                                    html.Img(src="/static/screenshots/lineChartGroupVwSince1800.png", width="100%", style={"padding": "5px", "padding-top": "0px"}),
                                                ]),       
                                            ]),
                                        ]),
                                        html.A(className="list-group-item list-group-item-action flex-column align-items-start bg-success", children=[
                                            html.H5(className="mb-1 text-white", id="group-2-toggle", children=[
                                                "» Calculating Voter Weight",
                                            ]),
                                            dbc.Collapse(id="collapse-2", children=[
                                                dcc.Link(href="/voter-weight-calculation", children=[
                                                    html.Br(),
                                                    html.P(className="text-white", children=[
                                                        "The math behind the metric being used to compare states over time »"
                                                    ]),
                                                    html.Img(src="/static/vwMath/derivingPvpeVw.png", width="48%", style={"padding": "5px", "padding-top": "0px"}),
                                                    html.Img(src="/static/vwMath/vwEcSummQuotEquation.png", width="51%", style={"padding": "5px", "padding-top": "0px"}),
                                                ]),       
                                            ]),
                                        ]),
                                        html.A(className="list-group-item list-group-item-action flex-column align-items-start bg-success", children=[
                                            html.H5(className="mb-1 text-white", id="group-3-toggle", children=[
                                                "» Explanation of State Groupings",
                                            ]),
                                            dbc.Collapse(id="collapse-3", children=[
                                                dcc.Link(href="/explanation-of-groupings", children=[
                                                    html.Br(),
                                                    html.P(className="text-white", children=[
                                                        "Backstory and breakdown of state grouping heuristics used throughout this site »"
                                                    ]),
                                                    html.Img(src="/static/screenshots/mapAcw1880.png", width="50%", style={"padding": "5px", "padding-top": "0px"}),
                                                    html.Img(src="/static/screenshots/mapCensus1960.png", width="50%", style={"padding": "5px", "padding-top": "0px"}),
                                                ]),       
                                            ]),
                                        ]),
                                        html.A(className="list-group-item list-group-item-action flex-column align-items-start bg-success", children=[
                                            html.H5(className="mb-1 text-white", id="group-4-toggle", children=[
                                                "» The Vault: 220 Years of Maps, Bar Charts, Scatter Plots, and Box Plots",
                                            ]),
                                            dbc.Collapse(id="collapse-4", children=[
                                                dcc.Link(href="/voter-weight-figure-vault", children=[
                                                    html.Br(),
                                                    html.P(className="text-white", children=[
                                                        "Less talk, more figures »"
                                                    ]),
                                                    html.Img(src="/static/screenshots/scatterBubblesAcw1900.png", width="50%", style={"padding": "5px", "padding-top": "0px"}),
                                                    html.Img(src="/static/screenshots/boxAcw1920.png", width="50%", style={"padding": "5px", "padding-top": "0px"}),
                                                ]),       
                                            ]),
                                        ]),
                                        html.A(className="list-group-item list-group-item-action flex-column align-items-start bg-success", children=[
                                            html.H5(className="mb-1 text-white", id="group-5-toggle", children=[
                                                "» Discussion and Conclusions",
                                            ]),
                                            dbc.Collapse(id="collapse-5", children=[
                                                dcc.Link(href="/voter-weight-conclusions", children=[
                                                    html.Br(),
                                                    html.P(className="text-white", children=[
                                                        "Interpretation of results, humbly expressed by a non-historian / non-mathematician »"
                                                    ]),
                                                ]),       
                                            ]),
                                        ]),
                                        
                                        # html.Br(),
                                        # dcc.Graph(id="fig-map-color-by-vw-landing")
                                #     ])
                                # ]),


                                # dbc.Card(className="bg-success text-white", children=[
                                #     dbc.CardHeader(
                                #         html.H2(
                                #             dbc.Button("The Vault: 220 Years of Maps, Bar Charts, Scatter Plots, and Box Plots", 
                                #                 className="text-white btn-lg", color="link", id="group-2-toggle")
                                #         )
                                #     ),
                                #     dbc.Collapse(
                                #         dbc.CardBody([
                                #             html.Img(src="/static/screenshots/scatterBubblesAcw1900.png", height="250", 
                                #                 style={"padding": "5px", "padding-top": "10px"}),
                                #             html.Img(src="/static/screenshots/boxAcw1920.png", height="250", 
                                #                 style={"padding": "5px", "padding-top": "10px"})
                                #         ]),
                                #         id="collapse-2",
                                #     ),
                                # ]),
                                # make_accordion_item(1, "Annotated Timeline Charting Voter Weight Trends: 1800 - 2020", 
                                #     ["/static/screenshots/lineChartGroupVwSince1800.png"], 250),
                                # make_accordion_item(2, "The Vault: 220 Years of Maps, Bar Charts, Scatter Plots, and Box Plots", 
                                #     ["/static/screenshots/scatterBubblesAcw1900.png", "/static/screenshots/boxAcw1920.png"], 250),
                                # make_accordion_item(3, "Calculating Voter Weight", 
                                #     ["/static/vwMath/derivingPvpeVw.png", "/static/vwMath/vwEcSummQuotEquation.png"], 150),
                                # make_accordion_item(4, "Explanation of State Groupings", 
                                #     ["/static/screenshots/mapAcw1880.png", "/static/screenshots/mapCensus1960.png"], 250),
                                # dbc.Card(className="bg-success text-white", children=[
                                #     dbc.CardHeader(
                                #         html.H2(
                                #             dbc.Button("Discussion and Conclusions", className="text-white btn-lg", color="link")
                                #         )
                                #     )
                                # ])
                            ])
                        ]),
                        dbc.Col(md=6, children=[
                            # dbc.Card(className="bg-primary", children=[
                            #     dbc.CardBody([
                                    # dcc.Graph(id="fig-scatter-dots-ec-bias"),
                                    # html.Br(),
                                    html.H4("Select year:", className="text-white"),
                                    dcc.Slider(
                                        id="ec-bias-year-input",
                                        min=1880,
                                        max=1960,
                                        step=None,
                                        marks={
                                            int(y): {'label': str(y), 'style': {'transform': 'rotate(45deg)', 'color': 'white'}}
                                            for y in data_obj.all_years if y >= 1880 and y <= 1960
                                        },
                                        value=1920,
                                    ),
                                    html.Br(),
                                    dcc.Graph(id="fig-bar-ec-bias"),
                                ])
                        #     ])
                        # ]),
                    ]),
                ]),
            ]),
            html.Br(),
        ])
    ]),
])