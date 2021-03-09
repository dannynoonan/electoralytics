import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash_pages.components import navbar, data_obj, form_input_line_vw_timeline_short


content = html.Div([
    navbar,
    dbc.Card(className="bg-success", children=[
        dbc.CardBody([
            html.Br(),
            dbc.Row(className="text-white", justify="center", align="center", children=[
                html.H3("Visualizing Jim Crow Voter Suppression: Apportionment, Participation, and Electoral College Bias"),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.Div(className="card-text lead", style={"margin-left": "50px", "margin-right": "50px", "font-style": "italic"}, children=[
                                html.P("“From the nature of man we may be sure, that those who have power in their hands will not give it up while they can retain \
                                    it. On the contrary we know they will always when they can rather increase it.”"),
                                html.P("—George Mason, during the Consitutional Convention in 1787")
                            ]),
                            html.Br(),
                            html.H4("Different states, different weights"),
                            html.P(className="card-text", children=[
                                "There’s some funny math built into the way we elect the US president."
                            ]),
                            html.P(className="card-text", children=[
                                "Unlike more run-of-the-mill democratic contests where every vote is tallied and the candidate with the most votes wins (", 
                                html.I("BOHHH"), "-ring), here the weight of each individual vote depends on the state from which it is cast. Specifically: (a) \
                                the Electoral College apportionment granted to that state, and (b) how many people turn out to vote in that state."
                            ]),
                            html.P(className="card-text", children=[
                                "These factors originated in an effort to balance out the influence of each state, but one of their effects has been to create \
                                imbalances between the influence of individual voters. In the coming sections I explore three types of Electoral College \
                                imbalance, rooted in the push and pull between state apportionment and voter participation, that are emergent in historical \
                                election data:",
                                html.Ul([
                                    html.Li(children=[html.B("Small-state bias"), ": Every state, regardless of population, gets two Electoral College votes for \
                                        its two Senators, proportionally favoring smaller states with fewer Representatives"]),
                                    html.Li(children=[html.B("Slave-state bias"), ": Although slaves couldn't vote, the “three-fifths compromise” included them \
                                        in the basis for Congressional and Electoral College representation, thereby amplifying the influence of Southern whites \
                                        who effectively voted on their behalf"]),
                                    html.Li(children=[html.B("Suppression-state bias"), ": The increased influence of voters in states that actively prevent \
                                        legally eligible and census tabulated citizens from voting, as took place for many decades in the Jim Crow South"])
                                ]),
                            ]),
                            html.P(className="card-text", children=[
                                "Each of these biases directly amplify the influence of one state's (or region's) voters over another's, resulting in the \
                                “hyper-enfranchisement” of certain voters relative to others. The small-state and slave-state biases are well-known, baked into \
                                the Constitution from the get-go, the type of simple quantifiable anecdotes you'd expect on an American History exam or in a \
                                game of Trivial Pursuit. By contrast, the bias amplifying Southern white voters as a direct result of their suppression of \
                                Black voters in the Jim Crow South is not as widely discussed."
                            ]),
                            html.P(className="card-text", children=[
                                "In a certain respect, historical disinterest in suppression-state bias makes sense: Compared to the direct and devastating \
                                effects of Jim Crow voter suppression on the Black population, the hyper-enfranchisement of the Southern whites who perpetrated \
                                that suppression (that is, the amplified national influence Southern whites experienced by suppressing regional Black voter \
                                turnout) hardly registers as a corollary anecdote. However, the role that the inflated national influence of Southern whites \
                                had in perpetuating its own regional dominance feels like a critical component—if not ", html.I("the"), " principal \
                                factor—contributing to the longevity and totality of Jim Crow voter suppression."
                            ]),
                            html.P(className="card-text", children=[
                                "Indeed, while slavery survived fewer than 80 years after ratification of the Constitution, Black voter suppression in the Jim \
                                Crow South endured for nearly 90 years after the end of Reconstruction. And this may not be the only metric by which the Jim \
                                Crow Era eclipsed the antebellum period. By quantitatively comparing these biases head-to-head, this project explores the idea \
                                that Jim Crow voter suppression may paradoxically have conferred ", html.I("greater"), " influence to Southern whites ", 
                                html.I("after"), " the abolition of slavery than the three-fifths compromise did before the Civil War and emancipation."
                            ]),
                        ])
                    ]),
                    html.Br(),
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([                           
                            html.H4("Voter Weight"),
                            html.Img(style={"float": "right", "padding-right": "10px"}, src="/static/vwMath/derivingPvpeVw.png", width="55%"),
                            html.P(className="card-text", children=[
                                "Despite small-state bias and slave-state bias deriving from different legal statutes and census formulas, I’m applying the same \
                                “Voter Weight” calculation to illustrate each in the figures above. Check out the ", dcc.Link("Calculating Voter Weight",
                                href="/voter-weight-calculation"), " section for a detailed breakdown of the math behind this metric."
                            ]),
                            html.P(className="card-text", children=[
                                "A couple of top line observations for now:",
                                html.Ul(children=[
                                    html.Li("Voter Weight is a zero sum game: in aggregate all weights average out to 1.0, so an increase in one state must be offset \
                                        by a decrease in another"),
                                    html.Li("While a higher Voter Weight benefits those to whom it directly applies, it is ultimately a marker of anti-democratic \
                                        outcomes that favor one population over another"),
                                    html.Li("Regardless of which factors of apportionment or participation are responsible for shifts or distortions in Voter Weight, \
                                        the resulting comparison is apples-to-apples — that is, the same calculation can be applied regardless of underlying bias / \
                                        combination of biases")
                                ]),
                            ]),
                            html.P(className="card-text", children=[
                                "An interactive map shading each state according to Voter Weight in every presidential election since 1800 is shown at the bottom of \
                                the ", dcc.Link("Calculating Voter Weight", href="/voter-weight-calculation"), " page."
                            ])
                        ])
                    ]),
                    html.Br(),
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.P(className="card-text", children=[
                                html.B("Next section >> "), dcc.Link("Part 2: Small-state bias and slave-state bias: As the founders intended", 
                                href="/voter-weight-electoral-college-bias-page2")
                            ]),
                            html.P(children=[
                                html.Ul(children=[
                                    html.Li(
                                        dcc.Link("Intro: Hyper-enfranchisement and the Electoral College", href="/voter-weight-electoral-college-bias-intro")
                                    ),
                                    html.Li("Part 1: Electoral College bias breakdown"),
                                    html.Li(
                                        dcc.Link("Part 2: Small-state bias and slave-state bias: As the framers intended", href="/voter-weight-electoral-college-bias-page2")
                                    ),
                                    html.Li(
                                        dcc.Link("Part 3: Reconstruction, Redemption, and suppression-state bias", href="/voter-weight-electoral-college-bias-page3")
                                    ),
                                    html.Li(
                                        dcc.Link("Part 4: Conclusions and Discussion", href="/voter-weight-conclusions")
                                    ),
                                    html.Li(
                                        dcc.Link("Deep dive into calculating Voter Weight", href="/voter-weight-calculation")
                                    ),
                                    html.Li(
                                        dcc.Link("Deep dive into state grouping heuristics", href="/explanation-of-groupings")
                                    ),
                                    html.Li(
                                        dcc.Link("Roll-up of interactive maps, figures, and charts", href="/voter-weight-figure-vault")
                                    ),
                                ])
                            ]),
                        ]),
                    ]),
                ]),
                dbc.Col(md=6, children=[
                    dcc.Graph(id="fig-map-color-by-ecv"),
                    html.P(className="card-text", style={"padding": "5px"}, children=[
                        html.Small("Figure 1: States shaded by Electoral College votes, derived by adding the state's number of Congressional Representatives \
                            (as determined by decennial population census) to its number of Senators (2 per state, regardless of population)"),
                    ]),
                    html.H4("Select year:", className="text-white"),
                    dcc.Slider(
                        id="map-year-input",
                        min=1832,
                        max=2020,
                        step=None,
                        marks={
                            int(y): {'label': str(y), 'style': {'transform': 'rotate(45deg)', 'color': 'white', 'font-size': '10px'}}
                            for y in data_obj.all_years if y >= 1832
                        },
                        value=1960,
                    ),
                    html.Br(),
                    dcc.Graph(id="fig-map-color-by-vw2"),
                    html.P(className="card-text", style={"padding": "5px"}, children=[
                        html.Small(children=["Figure 2: States color shaded by Voter Weight, or degree of hyper-enfranchisement, over the course of 56 presidential \
                            elections between 1800 and 2020. Control the year using the slider above, or open an ", dcc.Link("intractive slideshow animation", 
                            className="text-white", target="_blank",
                            href="https://htmlpreview.github.io/?https://github.com/dannynoonan/electoralytics/blob/master/html_figures/anim_map_state_vw_acw4_1000.html"), 
                            " illustrating the full history."]),
                    ]),
                ]),
            ]),
            html.Br(),
            html.Hr(className="border-light"),
            html.Br(),
            dbc.Row(className="text-white", justify="center", align="center", children=[
                html.H3("Regional hyper-enfranchisement trends over time"),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=12, children=[
                    form_input_line_vw_timeline_short,
                    dcc.Graph(id="fig-line-vw-timeline-short"),
                ])
            ]),
            html.Br(),
        ]),
    ]),
])