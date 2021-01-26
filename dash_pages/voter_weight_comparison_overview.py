import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash_pages.components import navbar, form_input_vw_over_time_line_chart, form_input_y_axis


content = html.Div([
    navbar,
    dbc.Card(className="bg-success", children=[
        dbc.CardBody([
            html.Br(),
            dbc.Row(className="text-white", justify="center", align="center", children=[
                html.H3("Comparing Voter Weight Per State/Per Grouping"),
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
                            html.H4("Using the Voter Weight timeline chart", className="card-title"),
                            html.P(className="card-text", children=[
                                "The line chart above shows Voter Weight trends as a function of time, spanning every US presidential election between 1800 and \
                                2020. When you first load the page, it displays aggregate/average data at the state group level, but using the dropdown menu above \
                                you can select individual states to compare, and using the legend to the right or the checkbox above you can hide the group-level \
                                trend lines one at a time or en masse."
                            ]),
                            html.P(className="card-text", children=[
                                "Background colors, markers, and text annotations denoting significant events and eras are there to add context, relating to \
                                African American rights and to voting rights generally. These can also be hidden using the checkboxes above the chart.",                            
                            ]),
                            html.P(className="card-text", children=[
                                "If things get too cluttered and you decide to assemble a comparison from scratch, hit the “Clear canvas” button to start fresh. \
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
                                at 1.11% of the total population. Popular vote data before 1800 is too scant to really work with, then from 1800 to 1824 the amount \
                                of data increases but it’s erratic, as several states switch back and forth between elector selection by legislature, by very limited \
                                popular vote, and by significantly wider popular vote. My regional tallies exclude states that don’t even hold popular presidential \
                                elections in a given year, meaning states like North Carolina and Kentucky that have very ", html.I("restrictive"), " voting end up \
                                being “penalized” more than states like New York, South Carolina, occasionally Massachusetts, and other states in years when ",
                                html.I("nobody"), " ends up voting.",                              
                            ]),
                            html.P(className="card-text", children=[
                                "Between 1820 and 1828 the popular vote increased 10-fold, marking the dawn of “populism” and “Jacksonian democracy,” and from 1828 \
                                onward some form of popular vote has been the norm in every state (except South Carolina, which didn’t switch to popular vote until \
                                Reconstruction). I considered excluding the years prior to 1828 altogether, since those years tell a much different story than what \
                                emerges from the late 1820s onward, but in the end I held onto them - less for the trend analysis than for the novelty and intrigue.",                              
                            ]),
                            html.P(className="card-text", children=[
                                "The “Votes cast as a percentage of population” chart below shows the increase (and decrease) in national popular vote over time.",                              
                            ]),
                        ])
                    ])
                ])
            ]),
            html.Br(),
            # dbc.Row([
            #     html.H2("Voter Participation Nationally Over Time"),
            # ], justify="center", align="center"),
            dbc.Row([
                dbc.Col(md=12, children=[
                    form_input_y_axis,
                    dcc.Graph(id="fig-line-total-vote-over-time")
                ])
            ]),
        ])
    ])
])