import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash_pages.components import navbar, form_input_vw_over_time_line_chart


content = html.Div([
    navbar,
    dbc.Card(className="bg-success", children=[
        dbc.CardBody([
            html.Div(children=[
                html.Ul(className="pagination pagination-lg justify-content-center", children=[
                    html.Li(className="page-item flex", style={"width": "50%"}, children=[
                        html.A(className="page-link", href="/voter-weight-calculation", children=[
                            "← Appendix 1: Calculating “Voter Weight” Per State"
                        ])
                    ]),
                    html.Li(className="page-item flex", style={"width": "20%"}),
                    html.Li(className="page-item flex", style={"width": "50%", "text-align": "right"}, children=[
                        html.A(className="page-link", href="/explanation-of-groupings", children=[
                            "Appendix 3: Explanation of State Aggregate Groupings →"
                        ])
                    ]),
                ])
            ]),
            html.Hr(className="border-light"),
            html.Br(),
            dbc.Row(className="text-white", justify="center", align="center", children=[
                html.H3("Appendix 2: Annotated Timeline Charting Voter Weight Trends: 1800 - 2020"),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=12, children=[
                    form_input_vw_over_time_line_chart,
                    dcc.Graph(id="fig-line-vote-weight-by-state-group"),
                ])
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=5, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.H4("Using the Annotated Voter Weight timeline chart", className="card-title"),
                            html.P(className="card-text", children=[
                                "The line chart above shows Voter Weight trends as a function of time, spanning every US presidential election between 1800 and \
                                2020.",
                            ]),
                            html.P(className="card-text", children=[
                                "When you first load the page, it displays aggregate/average data at the state-group level (with “Civil War” grouping selected). \
                                Using the legend to the right you can hide group-level trend lines one at a time, and using the “Show / Hide State Groups” \
                                dropdown menu above you can hide the group-level trend lines en masse."
                            ]),
                            html.P(className="card-text", children=[
                                "Using the dropdown menu above the chart, you can select individual states to compare. These can be overlaid onto group-level \
                                data or viewed separately."
                            ]),
                            html.P(className="card-text", children=[
                                "Background colors, markers, and text annotations denoting significant events and eras are there to add context, relating to \
                                African American rights and to voting rights generally. These can also be hidden using the checkboxes above the chart.",                            
                            ]),
                            html.P(className="card-text", children=[
                                "If things get too cluttered, you can assemble a comparison from scratch by hitting the “Clear canvas” button to start fresh. \
                                Toggling from “linear” to “log” scale for Vote Weight (Y axis) can help de-clutter trend lines in the lower registers as well.",                              
                            ]),
                            html.P(className="card-text", children=[
                                "As with most other charts and maps on the site, you can toggle between grouping states by their Civil War affiliations or their \
                                Regional Census designation, and you can specify the Electoral College vote threshold at which states are extracted into the “Small” \
                                group to reduce the effects of small-state bias in the trend lines.",                              
                            ]),
                        ])
                    ])
                ]),
                dbc.Col(md=7, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.H4("Election year range; quirks in the early years", className="card-title"),
                            html.P(className="card-text", children=[
                                "Where’s 1788-1796? And what’s with the zig-zaggy lines in the early 1800s?"
                            ]),
                            html.P(className="card-text", children=[
                                "So, I’d actually forgotten this detail about US history, but for the first 40-odd years after its founding there wasn’t a whole lot \
                                of actual ", html.I("voting"), " for president in this country. I don’t mean among women and racial minorities specifically, I mean \
                                among ", html.I("people"), ". Before phrases like “populism,” “democratic,” and the “politics of the common man” gained cachet in the \
                                1820s, a majority of presidential electors were chosen by state legislatures, or in states holding a so-called “popular” vote this \
                                voting was the exclusive purview of a tiny sliver of property-owning white males.",                              
                            ]),
                            html.P(className="card-text", children=[
                                "As a result, fewer than 2% of people voted in each of these first 10 US presidential elections, hitting a 30-year low in 1820 \
                                at 1.11% of the total population (see figure below)."
                            ]),
                            html.P(className="card-text", children=[
                                "Popular vote data before 1800 is too scant to really work with, then from 1800 to 1824 the amount of data increases - but it’s \
                                erratic. Several states switch back and forth between elector selection (a) by legislature, (b) by very limited popular vote, \
                                and (c) by significantly wider popular vote.",
                            ]),
                            html.P(className="card-text", children=[
                                "My presentation of these earliest years doesn't account for the on-again/off-again use of Popular Vote very well. My aggregate \
                                tallies (at the state-group level) exclude states that don’t even hold a popular presidential vote in a given year. This means \
                                states like North Carolina and Kentucky that did hold popular votes - albeit very restrictive ones - in those earliest years end \
                                up being “penalized” more than states like New York and South Carolina where ", html.I("nobody"), " was permitted to vote.",                              
                            ]),
                            html.P(className="card-text", children=[
                                "Between 1820 and 1828 the popular vote increased 10-fold, marking the dawn of “populism” and “Jacksonian democracy,” and from 1828 \
                                onward some form of popular vote has been the norm in every state (except South Carolina, which didn’t switch to popular vote until \
                                Reconstruction)."
                            ]),
                            html.P(className="card-text", children=[
                                "I considered excluding the years prior to 1828 from analysis altogether, since those years tell a much different story than what \
                                emerges from the late 1820s onward, but in the end I held onto them - less for the trend analysis than for the novelty and intrigue.",                              
                            ]),
                            html.P(className="card-text", children=[
                                "The “Votes cast as a percentage of population” chart below shows this overall increase (and decrease) in national popular vote over \
                                time.",                              
                            ]),
                        ])
                    ])
                ])
            ]),
            html.Br(),html.Br(),
            dbc.Row([
                dbc.Col(md=2, className="text-white", style={'textAlign': 'left'}, children=[
                    dbc.FormGroup([
                        html.H4("Y axis:"),
                        dcc.RadioItems(
                            id="y-axis-input-2",
                            className="text-white", 
                            options=[
                                {'label': 'Linear', 'value': 'linear'},
                                {'label': 'Log', 'value': 'log'}
                            ],
                            value='linear',
                            inputStyle={"margin-left": "4px", "margin-right": "4px"}
                        )
                    ])
                ]),
                dbc.Col(md=8, className="text-white", style={'textAlign': 'center'}, children=[
                    html.H3("Voter Participation Nationally Over Time"),
                ]),
                dbc.Col(md=2)
            ]),
            dbc.Row([
                dbc.Col(md=12, children=[
                    dcc.Graph(id="fig-line-total-vote-over-time")
                ])
            ]),
            html.Br(),
            html.Hr(className="border-light"),
            html.Div(children=[
                html.Ul(className="pagination pagination-lg justify-content-center", children=[
                    html.Li(className="page-item flex", style={"width": "50%"}, children=[
                        html.A(className="page-link", href="/voter-weight-calculation", children=[
                            "← Appendix 1: Calculating “Voter Weight” Per State"
                        ])
                    ]),
                    html.Li(className="page-item flex", style={"width": "20%"}),
                    html.Li(className="page-item flex", style={"width": "50%", "text-align": "right"}, children=[
                        html.A(className="page-link", href="/explanation-of-groupings", children=[
                            "Appendix 3: Explanation of State Aggregate Groupings →"
                        ])
                    ]),
                ])
            ]),
        ])
    ])
])