import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash_pages.components import navbar, data_obj


content = html.Div([
    navbar,
    dbc.Card(className="bg-success", children=[
        dbc.CardBody([
            html.Br(),
            dbc.Row(className="text-white", justify="center", align="center", children=[
                html.H3("Visualizing the “Jim Crow Power” through Electoral College data"),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=3, children=[
                    html.Div(className="list-group sticky-top", children=[
                        html.A(href="/voter-weight-electoral-college-bias-intro", className="list-group-item list-group-item-action active", children=[
                            "→ Intro: American voter enfranchisement"]),
                        html.A(href="/voter-weight-electoral-college-bias-page1", className="list-group-item list-group-item-action", children=[
                            "Part 1: Equality for states, not for voters"]),
                        html.A(href="/voter-weight-electoral-college-bias-page2", className="list-group-item list-group-item-action", children=[
                            "Part 2: Small-state bias and slave-state bias"]),
                        html.A(href="/voter-weight-electoral-college-bias-page3", className="list-group-item list-group-item-action", children=[
                            "Part 3: Reconstruction and Black voting rights"]),
                        html.A(href="/voter-weight-electoral-college-bias-page4", className="list-group-item list-group-item-action", children=[
                            "Part 4: Suppression-state bias"]),
                        html.A(href="/voter-weight-results", className="list-group-item list-group-item-action", children=[
                            "Part 5: Results and observations"]),
                        html.A(href="/voter-weight-conclusions", className="list-group-item list-group-item-action", children=[
                            "Part 6: Conclusions and interpretation"]),
                        html.A(href="/voter-weight-calculation", className="list-group-item list-group-item-action", children=[
                            "Appx 1: Calculating Voter Weight"]),
                        html.A(href="/voter-weight-timeline-visualization", className="list-group-item list-group-item-action", children=[
                            "Appx 2: Annotated timeline"]),
                        html.A(href="/explanation-of-groupings", className="list-group-item list-group-item-action", children=[
                            "Appx 3: Explanation of state groupings"]),
                        html.A(href="/voter-weight-figure-vault", className="list-group-item list-group-item-action", children=[
                            "The Vault: 220 years of maps, charts, & figures"]),
                    ])
                ]),
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success lead", style={"font-family": "times-new-roman"}, children=[
                        dbc.CardBody([
                            html.H3("American voter enfranchisement: A zero-sum game"),
                            html.P("April 2, 2021", style={"font-family": "arial", "font-size": "10pt"}),
                            html.Img(src="/static/stockImages/the_first_vote_loc.jpg", style={"float": "right", "padding-left": "10px"}, width="40%"),
                            html.P(children=[
                                "Apart from a brief hopeful period between the Civil War and the end of Reconstruction, the disenfranchisement of Southern Blacks in the \
                                US’s first 190 years was nearly absolute. Before emancipation, enslaved Blacks were prevented from voting entirely, while during the Jim \
                                Crow era, “Southern Blacks were made electorally invisible, whether through restrictive voting practices like poll taxes and literacy \
                                tests or by campaigns of terrorism and state-sanctioned murder.”", dcc.Link(href="/sources-notes", children=[html.Sup("1")]), " Because \
                                the Electoral College grants voting influence based on population rather than participation, the disenfranchisement of Southern Blacks \
                                fed directly into the “hyper-enfranchisement” of Southern whites in both periods. As a result, for most of America’s first two centuries, ", 
                                html.Span(style={"font-weight":"bold"}, children=["Southern whites held significantly more power, per voter, than any other demographic \
                                anywhere else in the US."])
                            ]),
                            html.P(children=[
                                "The augmented pre-war influence of Southern white voters became known as the “Slave Power,” notorious for its focus on protecting and \
                                expanding the institution from which it derived its power, and for the infamous “three-fifths clause” that padded its influence. Similarly \
                                during Jim Crow, the collective influence of Southern whites became known as the “Solid South,” also notorious for obstructing Civil \
                                Rights legislation and perpetuating its racially suppressive hold on power - but not as well known for any mathematical bias playing to \
                                its advantage."
                            ]),
                            html.P(children=[
                                "I first became interested in comparing disenfranchisement in relation to hyper-enfranchisement during these two periods \
                                after an ", dcc.Link("October 2020 episode", href="https://www.npr.org/2020/09/30/918717270/the-electoral-college", 
                                target="_blank"), " of NPR’s ", html.I("Throughline"), ", which framed Jim Crow voter suppression as a “five-fifths” \
                                variation on the three-fifths compromise.", dcc.Link(href="/sources-notes", children=[html.Sup("2")]), " The suggestion that \
                                the two eras might be quantified side-by-side prompted me to work out a generic formula for comparing them, by measuring the \
                                relative influence of voters in any given state, in any given year, using the ratio of each state’s voter turnout to its \
                                Electoral College votes. The resulting ", html.Span(style={"font-weight":"bold"}, children=["“", dcc.Link("Voter Weight", 
                                href="/voter-weight-calculation"), "” metric measures the degree of hyper-enfranchisement experienced by voters in a given \
                                state"]), ", which (absent other factors) is inversely proportional to the degree of voter disenfranchisement in that state."
                            ]),
                            html.H3("Visualizing Voter Weight by state / by year"),
                            html.P(children=[
                                "The first figure below illustrates the hyper-enfranchisement of voters in certain states relative to others by displaying them in \
                                descending order by Voter Weight, shading them in terms of their Civil War grouping (more info about state groupings ", 
                                dcc.Link("here", href="/explanation-of-groupings"), "). This figure, as with all figures on the site, is interactive. ", 
                                html.Span(style={"font-style":"italic", "text-decoration":"underline"}, children=["Move the “Select year” slider to bring a different \
                                election year into focus"]), ". Highlight a portion of the figure to zoom in, then double-click to reset to the original scale. Roll \
                                over any bar in the chart to see the factors that contribute to its Voter Weight calculation. ", html.Span(style={"font-weight":"bold"}, 
                                children=["Note that if every vote in every state counted equally, all of the Voter Weights would be 1.0 and each bar in the chart \
                                would be the same length."])
                            ]),
                        ])
                    ]),
                    html.Br(),
                    html.H4("Select year:", className="text-white"),
                    dcc.Slider(
                        id="year-input-slavery-jimcrow-vw-bias-bar",
                        min=1832,
                        max=1964,
                        step=None,
                        marks={
                            int(y): {'label': str(y), 'style': {'transform': 'rotate(45deg)', 'color': 'white'}}
                            for y in data_obj.all_years if y >= 1832 and y <= 1964
                        },
                        value=1920,
                    ),
                    html.Br(),
                    dcc.Graph(id="fig-bar-slavery-jimcrow-vw-bias"),
                    html.Br(),
                    dbc.Card(className="border-success lead", style={"font-family": "times-new-roman"}, children=[
                        dbc.CardBody([
                            html.P(children=[
                                "In the next figure you can see the relationship between voter turnout (x axis) and Electoral College votes (y axis) in determining \
                                Voter Weight. The diagonal line cutting from the lower left to upper right indicates the national mean, where the Voter Weight ratio \
                                is 1.0. ", html.Span(style={"font-weight":"bold"}, children=["If every vote in every state counted equally, every state’s dot would \
                                fall on the diagonal nationwide mean line."])
                            ]),
                         ])
                    ]),
                    html.Br(),  
                    html.H4("Select year:", className="text-white"),
                    dcc.Slider(
                        id="year-input-slavery-jimcrow-vw-bias-scatter-dots",
                        min=1832,
                        max=1964,
                        step=None,
                        marks={
                            int(y): {'label': str(y), 'style': {'transform': 'rotate(45deg)', 'color': 'white'}}
                            for y in data_obj.all_years if y >= 1832 and y <= 1964
                        },
                        value=1920,
                    ),
                    html.Br(),
                    dcc.Graph(id="fig-scatter-dots-slavery-jimcrow-vw-bias"),
                    html.Br(),
                    dbc.Card(className="border-success lead", style={"font-family": "times-new-roman"}, children=[
                        dbc.CardBody([
                            html.P(children=[
                                "The rest of the site, beginning with ", dcc.Link("Part 1: Equality for states, not for voters", 
                                href="/voter-weight-electoral-college-bias-page1"), ", further explores the biases and vulnerabilities built into our \
                                electoral apportionment system, aided by interactive maps, figures, and animations."
                            ]),
                            html.H3("A note on methods"),
                            html.P(children=[
                                "All presidential election data was compiled from this ", 
                                dcc.Link("Wikipedia portal", href="https://en.wikipedia.org/wiki/List_of_United_States_presidential_election_results_by_state", 
                                target="_blank"), " and is managed in csv files ", dcc.Link(" here", 
                                href="https://github.com/dannynoonan/electoralytics/tree/master/data", target="_blank"), ". The data transformations lean \
                                heavily on python's ", dcc.Link("pandas", target="_blank", 
                                href="https://towardsdatascience.com/a-quick-introduction-to-the-pandas-python-library-f1b678f34673"), " library, while \
                                visualizations leverage pandas integration with ", dcc.Link("plotly express", target="_blank", 
                                href="https://medium.com/plotly/introducing-plotly-express-808df010143d"), " and the ", dcc.Link("dash", 
                                href="https://medium.com/plotly/introducing-dash-5ecf7191b503", target="_blank"), " framework. The calculations behind \
                                these data transformations are explored in depth on the ", dcc.Link("Voter Weight calculation", 
                                href="/voter-weight-calculation"), " page, and source code for the overall project is available in the ",
                                dcc.Link("electoralytics repo", href="https://github.com/dannynoonan/electoralytics", target="_blank"), " on github."
                            ]),
                            html.H3("Want to dig deeper?"),
                            html.P(children=[
                                dcc.Link("→ Continue to Part 1: Equality for states, not for voters", href="/voter-weight-electoral-college-bias-page1"),
                                html.Br(),
                                dcc.Link("→ Skip to Part 2: Small-state bias and slave-state bias", href="/voter-weight-electoral-college-bias-page2"),
                                html.Br(),
                                dcc.Link("→ Skip to Part 3: Reconstruction and Black voting rights", href="/voter-weight-electoral-college-bias-page3"),
                                html.Br(),
                                dcc.Link("→ Skip to Part 4: Suppression-state bias", href="/voter-weight-electoral-college-bias-page4"),
                                html.Br(),
                                dcc.Link("→ Learn about the math behind “Voter weight”", href="/voter-weight-calculation"),
                                html.Br(),
                                dcc.Link("→ Reveal Electoral College bias through interactive maps, charts and more", href="/voter-weight-figure-vault"),
                            ]),
                        ]),
                    ]),
                ]),
                dbc.Col(md=3),
            ]),
            html.Br(),
            html.Hr(className="border-light"),
            html.Div(children=[
                html.Ul(className="pagination pagination-lg justify-content-center", children=[
                    html.Li(className="page-item flex", style={"width": "60%"}),
                    html.Li(className="page-item flex", style={"width": "40%", "text-align": "right"}, children=[
                        html.A(className="page-link", href="/voter-weight-electoral-college-bias-page1", children=[
                            "Part 1: Electoral College basics: Equality for states, not for voters →"
                        ])
                    ]),
                ])
            ]),
        ]),
    ]),
])