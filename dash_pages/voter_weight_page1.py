import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash_pages.components import navbar, data_obj, form_input_line_vw_timeline_short


content = html.Div([
    navbar,
    dbc.Card(className="bg-success", children=[
        dbc.CardBody([
            html.Div(children=[
                html.Ul(className="pagination pagination-lg justify-content-center", children=[
                    html.Li(className="page-item flex", style={"width": "50%"}, children=[
                        html.A(className="page-link", href="/voter-weight-electoral-college-bias-intro", children=[
                            "← Intro: American voter enfranchisement: A zero-sum game"
                        ])
                    ]),
                    html.Li(className="page-item flex", style={"width": "20%"}),
                    html.Li(className="page-item flex", style={"width": "50%", "text-align": "right"}, children=[
                        html.A(className="page-link", href="/voter-weight-electoral-college-bias-page2", children=[
                            "Part 2: Small-state bias and slave-state bias: As the framers intended →"
                        ])
                    ]),
                ])
            ]),
            html.Hr(className="border-light"),
            html.Br(),
            dbc.Row(className="text-white", justify="center", align="center", children=[
                html.H3("Part 1: Electoral College bias: Equality for states, not for voters"),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.Div(className="card-text lead", style={"margin-left": "50px", "margin-right": "50px", "font-size": "13pt"}, children=[
                                html.P(style={"font-style": "italic"}, children=[
                                    "The Electoral College was neither an exercise in applied Platonism nor an experiment in indirect government based on \
                                    elitist distrust of the masses. It was merely a jerry-rigged improvisation which has subsequently been endowed with a high \
                                    theoretical content… The future was left to cope with the problem of what to do with this Rube Goldberg mechanism.",
                                    dcc.Link(href="/sources-notes", children=[html.Sup("3")]),
                                ]),
                                html.P(children=["—John Roche, ", html.I("“The Founding Fathers: A Reform Caucus in Action”")])
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
                                "Pre-allocating representational influence to states, rather than simply tallying the ballots of individual citizens who turn \
                                out to vote, originated in part from an effort to balance out the influence of each state.", dcc.Link(href="/sources-notes", 
                                children=[html.Sup("4")]), " And to a certain extent this goal of balancing state-level influence was achieved, but with the \
                                side-effect of creating imbalances between the influence of individual voters. In the coming sections I explore three types of \
                                Electoral College imbalance, rooted in the push and pull between state apportionment and voter participation, that are emergent \
                                in historical election data:",
                                html.Ul([
                                    html.Li(children=[html.B("Small-state bias"), ": Every state, regardless of population, gets two Electoral College votes for \
                                        its two Senators, proportionally favoring smaller states with fewer Representatives"]),
                                    html.Li(children=[html.B("Slave-state bias"), ": Although slaves couldn't vote, the “three-fifths compromise” included them \
                                        in the basis for Congressional and Electoral College representation, thereby amplifying the influence of Southern whites \
                                        who effectively voted on their slaves' behalf"]),
                                    html.Li(children=[html.B("Suppression-state bias"), ": The increased influence of voters in states that actively prevent \
                                        legally eligible and census tabulated citizens from voting, as took place for many decades in the Jim Crow South"])
                                ]),
                            ]),
                        ]),
                    ]),
                ]),
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.Img(src="/static/stockImages/census-1790.jpg", style={"float": "right", "padding-left": "10px", "padding-top": "5px"}, width="45%"),
                            html.P(className="card-text", children=[
                                "Each of these biases directly amplify the influence of one state's (or region's) voters over another's, resulting in the \
                                “hyper-enfranchisement” of certain voters relative to others. The small-state and slave-state biases are well-known, baked into \
                                the Constitution from the get-go, the type of simple quantifiable anecdotes you'd expect on an American History exam or in a \
                                game of Trivial Pursuit. By contrast, the bias amplifying Southern white voters as a direct result of their suppression of \
                                Black voters in the Jim Crow South is not as widely discussed."
                            ]),
                            html.P(className="card-text", children=[
                                "In a certain respect, historical disinterest in suppression-state bias makes sense: Compared to the direct and devastating \
                                effects of Jim Crow voter suppression on the Black population, the amplified national influence Southern whites experienced as \
                                a result of that suppression barely registers as a corollary anecdote. But on the other hand, to the extent that it may have \
                                contributed to the longevity and totality of Jim Crow voter suppression, any connection between this amplified national \
                                influence and the perpetuation of Southern white regional dominance is worth examining."
                            ]),
                            html.P(className="card-text", children=[
                                "Moreover, while slavery survived fewer than 80 years after ratification of the Constitution, Black voter suppression in the Jim \
                                Crow South endured for nearly 90 years after the end of Reconstruction. And this may not be the only metric by which the Jim \
                                Crow Era eclipsed the antebellum period. By quantitatively comparing these biases head-to-head, this project explores the idea \
                                that Jim Crow voter suppression may paradoxically have conferred ", html.I("greater"), " influence to Southern whites ", 
                                html.I("after"), " the abolition of slavery than the three-fifths compromise did before the Civil War and emancipation."
                            ]),
                        ]),                      
                    ]),
                ]),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=12, children=[
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
                ]),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=6, children=[
                    dcc.Graph(id="fig-bar-color-by-vw"),
                    html.P(className="card-text", style={"padding": "5px"}, children=[
                        html.Small(children=["Figure 1: States color shaded by Voter Weight, or degree of hyper-enfranchisement, over the course of 56 presidential \
                            elections between 1800 and 2020. Control the year using the slider above, or open an ", dcc.Link("intractive slideshow animation", 
                            className="text-white", target="_blank",
                            href="https://htmlpreview.github.io/?https://github.com/dannynoonan/electoralytics/blob/master/html_figures/anim_bar_state_vw_color_by_vw_acw4_900.html"), 
                            " illustrating the full history."]),
                    ]),
                    html.Br(),
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.H4("Voter Weight"),
                            html.Img(style={"float": "right", "padding-right": "10px"}, src="/static/vwMath/derivingPvpeVw.png", width="55%"),
                            html.P(className="card-text", children=[
                                "Although each Electoral College bias derives from distinct legal statutes and census formulas, in the pages ahead I’ll be \
                                applying the same “Voter Weight” calculation to illustrate each bias side by side. Check out the ", dcc.Link("Calculating \
                                Voter Weight", href="/voter-weight-calculation"), " section for a detailed breakdown of the math behind this metric."
                            ]),
                            html.P(className="card-text", children=[
                                "A couple of top-line observations for now:",
                                html.Ul(children=[
                                    html.Li("Voter Weight is a zero sum game: in aggregate all weights average out to 1.0, so an increase in one state must be \
                                        offset by a decrease in another"),
                                    html.Li("While a higher Voter Weight benefits those to whom it directly applies, it is ultimately a marker of anti-democratic \
                                        outcomes that favor one population over another"),
                                    html.Li("Regardless of which factors of apportionment or participation are responsible for shifts or distortions in Voter \
                                        Weight, the resulting comparison is apples-to-apples — that is, the same calculation can be applied regardless of \
                                        underlying bias / combination of biases")
                                ]),
                            ]),
                        ])
                    ])
                ]),
                dbc.Col(md=6, children=[
                    dcc.Graph(id="fig-map-color-by-vw2"),
                    html.P(className="card-text", style={"padding": "5px"}, children=[
                        html.Small(children=["Figure 2: States color shaded by Voter Weight, or degree of hyper-enfranchisement, over the course of 56 presidential \
                            elections between 1800 and 2020. Control the year using the slider above, or open an ", dcc.Link("intractive slideshow animation", 
                            className="text-white", target="_blank",
                            href="https://htmlpreview.github.io/?https://github.com/dannynoonan/electoralytics/blob/master/html_figures/anim_map_state_vw_acw4_1000.html"), 
                            " illustrating the full history."]),
                    ]),
                    html.Br(),
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.P(className="card-text", style={"font-style": "italic"}, children=[
                                "The figures above, the figures below, and every other figure in this publication are interactive. Move the “Select year” slider to \
                                bring a different election year into focus. Highlight a portion of the figure to zoom in, then double-click to reset to the original \
                                scale. Roll over any bar in the chart to see the factors that contribute to its Voter Weight calculation."
                            ]),
                            html.P(className="card-text", style={"font-style": "italic"}, children=[ 
                                "All figures use presidential election data accessible via this ", dcc.Link("Wikipedia portal", 
                                href="https://en.wikipedia.org/wiki/List_of_United_States_presidential_election_results_by_state", target="_blank"), ". A consolidated \
                                version of that data (what I’m using to power this website) is available in csv format in the ", dcc.Link("data/ directory", 
                                href="https://github.com/dannynoonan/electoralytics/tree/master/data", target="_blank"), " of the ", dcc.Link("electoralytics repo", 
                                href="https://github.com/dannynoonan/electoralytics", target="_blank"), " on github."
                            ]),
                        ]),
                    ]),
                    html.Br(),
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.Img(src="/static/stockImages/ballot-box-game.jpg", style={"float": "right", "padding-left": "10px", "padding-top": "5px"}, width="45%"),
                            html.P(className="card-text", children=[
                                "The color shading for each state in ", html.B("Figure 1"), " and ", html.B("Figure 2"), " corresponds to that state's Voter Weight in a given presidential \
                                election. Adjust the 'Select Year' slider above the figure to toggle between different election years."
                            ]),
                            html.P(className="card-text", children=[
                                html.B("Figure 3"), " below provides an interactive overview of Voter Weight measurements over time, with states grouped by Civil \
                                War alliance or census region (use the pulldown menu to choose). You may also select individual states for direct comparison, \
                                superimposing each of their Voter Weight trend lines simultaneously. This figure jumps ahead a bit in terms of what's been \
                                discussed so far, but gives a preview of patterns and trends we'll be exploring in the coming pages."
                            ])
                        ])
                    ])
                ]),
            ]),
            html.Br(),
            html.Hr(className="border-light"),
            html.Br(),
            dbc.Row(className="text-white", justify="center", align="center", children=[
                html.H3("Hyper-enfranchisement trends over time: Regional Voter Weight averages per election"),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=12, children=[
                    form_input_line_vw_timeline_short,
                    dcc.Graph(id="fig-line-vw-timeline-short"),
                    html.P(className="card-text", style={"padding": "5px", "font-size":"10pt"}, children=[
                        "Figure 3: Voter Weight trends as a function of time, spanning every US presidential election between 1840 and 2000.",
                        html.Ul([
                            html.Li("Using the legend to the right you can hide group-level trend lines one at a time, and using the “Show / Hide State Groups” \
                            dropdown menu above you can hide the group-level trend lines en masse."),
                            html.Li("Using the dropdown menu above the chart, you can select individual states to compare. These can be overlaid onto group-level data \
                            or viewed separately."),
                            html.Li("Background colors, markers, and text annotations denoting significant events and eras are there to add context, relating to African \
                            American rights and to voting rights generally. These can also be hidden using the checkboxes above the chart."),
                            html.Li("If things get too cluttered, you can assemble a comparison from scratch by hitting the “Clear canvas” button to start fresh. \
                            Toggling from “linear” to “log” scale for Vote Weight (Y axis) can help de-clutter trend lines in the lower registers as well."),
                            html.Li("When you first load the page, it displays aggregate/average data at the state-group level (with “Civil War” grouping selected), but \
                            you can toggle between grouping states by their Civil War affiliations or their Regional Census designation."),
                            html.Li("You can also specify the Electoral College vote threshold at which states are extracted into the “Small” group to reduce the \
                            effects of small-state bias in the trend lines.")
                        ]),
                    ]),
                ])
            ]),
            html.Hr(className="border-light"),
            html.Div(children=[
                html.Ul(className="pagination pagination-lg justify-content-center", children=[
                    html.Li(className="page-item flex", style={"width": "50%"}, children=[
                        html.A(className="page-link", href="/voter-weight-electoral-college-bias-intro", children=[
                            "← Intro: Hyper-enfranchisement and the Electoral College"
                        ])
                    ]),
                    html.Li(className="page-item flex", style={"width": "20%"}),
                    html.Li(className="page-item flex", style={"width": "50%", "text-align": "right"}, children=[
                        html.A(className="page-link", href="/voter-weight-electoral-college-bias-page2", children=[
                            "Part 2: Small-state bias and slave-state bias: As the framers intended →"
                        ])
                    ]),
                ])
            ]),
        ]),
    ]),
])