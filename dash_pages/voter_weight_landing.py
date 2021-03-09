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
                dbc.Col(md=3),
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success lead", style={"font-family": "times-new-roman"}, children=[
                        dbc.CardBody([
                            html.H3("American voter enfranchisement: A zero-sum game"),
                            html.P("Feb 12, 2021", style={"font-family": "arial", "font-size": "10pt"}),
                            html.P(children=[
                                "Apart from a brief hopeful period between the Civil War and the end of Reconstruction, the disenfranchisement of \
                                Southern Blacks in the US’s first 190 years was nearly absolute. During slavery, Blacks were unable to vote entirely, \
                                while during the Jim Crow era, “Southern Blacks were made electorally invisible, whether through restrictive \
                                practices like poll taxes and literacy tests or by campaigns of terrorism and state-sanctioned murder.”", 
                                html.Sup("1"), " Because the Electoral College grants voting influence based on population rather than \
                                participation, the disenfranchisement of Southern Blacks fed directly into the “hyper-enfranchisement” of Southern \
                                whites in both periods. This resulted in Southern whites holding significantly more power, per voter, than any other \
                                demographic anywhere else in the US."
                            ]),
                            html.P(children=[
                                "I first became interested in quantifying disenfranchisement in relation to hyper-enfranchisement after an ",
                                dcc.Link("October 2020 episode", href="https://www.npr.org/2020/09/30/918717270/the-electoral-college", 
                                target="_blank"), " of NPR’s ", html.I("Throughline"), ". The podcast framed Jim Crow voter suppression as a \
                                “five-fifths” variation on the three-fifths compromise, that infamous slave-tabulation ratio etched into the \
                                Constitution. The suggestion that the two eras might be quantified side by side prompted me to work out a generic \
                                formula for comparing them, by measuring the relative influence of voters in any given state, in any given year, \
                                using the ratio of each state’s voter turnout to its Electoral College votes. The resulting “", dcc.Link("Voter Weight", 
                                href="/voter-weight-calculation"), "” metric measures the degree of hyper-enfranchisement experienced by voters in a \
                                given state, which (absent other factors) is inversely proportional to the degree of voter disenfranchisement in that \
                                state."
                            ]),
                            html.H3("Visualizing Voter Weight by state / by year"),
                            html.P(children=[
                                "The first figure below illustrates the hyper-enfranchisement of voters in certain states relative to others by \
                                displaying them in descending order by Voter Weight, shading them in terms of their Civil War grouping (more info \
                                about state groupings ", dcc.Link("here", href="/explanation-of-groupings"), "). This figure, as with all figures on \
                                the site, is interactive. Move the “Select year” slider to bring a different election year into focus. Highlight a \
                                portion of the figure to zoom in, then double-click to reset to the original scale. Roll over any bar in the chart to \
                                see the factors that contribute to its Voter Weight calculation. Note that if every vote in every state counted \
                                equally, all of the Voter Weights would be 1.0 and each bar in the chart would be the same length."
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
                                "In the next figure you can see the relationship between voter turnout (x axis) and Electoral College votes (y axis) in \
                                determining Voter Weight. The diagonal line indicates the national mean, where the Voter Weight ratio is 1.0. If every \
                                vote in every state counted equally, every state’s dot would fall on this nationwide mean line."
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
                                "The rest of the site, beginning with the ", dcc.Link("complete article", 
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
                                html.Ul(children=[
                                    html.Li(
                                        dcc.Link("Read the full article", href="/voter-weight-electoral-college-bias-page1")
                                    ),
                                    html.Li(
                                        dcc.Link("See an annotated timeline of voter weight trends", href="/voter-weight-timeline-visualization")
                                    ),
                                    html.Li(
                                        dcc.Link("Learn about the math behind voter weight", href="/voter-weight-calculation")
                                    ),
                                    html.Li(
                                        dcc.Link("Get the breakdown of state grouping heuristics used throughout the site", href="/explanation-of-groupings")
                                    ),
                                    html.Li(
                                        dcc.Link("Reveal Electoral College bias through interactive maps, charts and more", href="/voter-weight-figure-vault")
                                    ),
                                ])
                            ]),
                        ]),
                    ]),
                ]),
                dbc.Col(md=3),
            ]),
            html.Br(),
        ])
    ]),
])