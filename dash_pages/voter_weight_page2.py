import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash_pages.components import navbar, data_obj


content = html.Div([
    navbar,
    dbc.Card(className="bg-success", children=[
        dbc.CardBody([
            html.Div(children=[
                html.Ul(className="pagination pagination-lg justify-content-center", children=[
                    html.Li(className="page-item flex", style={"width": "50%"}, children=[
                        html.A(className="page-link", href="/voter-weight-electoral-college-bias-page1", children=[
                            "← Part 1: Electoral College bias: Equality for states, not for voters"
                        ])
                    ]),
                    html.Li(className="page-item flex", style={"width": "20%"}),
                    html.Li(className="page-item flex", style={"width": "50%", "text-align": "right"}, children=[
                        html.A(className="page-link", href="/voter-weight-electoral-college-bias-page3", children=[
                            "Part 3: Reconstruction and Black voting rights →"
                        ])
                    ]),
                ])
            ]),
            html.Hr(className="border-light"),
            html.Br(),
            dbc.Row(className="text-white", justify="center", align="center", children=[
                html.H3("Part 2: Small-state bias and slave-state bias: As the framers intended"),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.Div(className="card-text lead", style={"margin-left": "50px", "margin-right": "50px", "font-size": "13pt"}, children=[
                                html.P(style={"font-style": "italic"}, children=[
                                    "The Electoral College was not grounded in the principle that the votes of all individuals should count equally. The \
                                    framers, acting out of perceived political necessity, chose to give extra weight to the votes of two groups of citizens: \
                                    inhabitants of small states and white residents of states that had slavery.",
                                    dcc.Link(href="/sources-notes", children=[html.Sup("4")]),
                                ]),
                                html.P(children=["—Alexander Keyssar, ", html.I("“Why Do We Still Have the Electoral College?”")])
                            ]),
                            html.Br(),
                            html.H4("Small-state bias"),
                            html.P(className="card-text", children=[
                                "In the 21st century, the idea that voters in smaller states have greater influence on national elections than voters in more \
                                populous states has drawn its share of ire."
                            ]),
                            html.Img(src="/static/stockImages/ec-vote-1836.jpg", style={"float": "left", "padding-right": "10px", "padding-top": "5px"}, 
                                width="45%"),
                            html.P(className="card-text", children=[
                                "Quick review: each state’s Electoral College votes equal the sum of its Congressional Representatives (based on population) \
                                + Senators (2 per state regardless of population), the same bicameral balance that was part of the Constitutional Convention’s ", 
                                dcc.Link("Great Compromise", href="https://en.wikipedia.org/wiki/Connecticut_Compromise", target="_blank"), ". And just as every \
                                state sends the same number of Senators to DC, even the smallest states receive the same +2 Senator “bicameral boost” in their \
                                Electoral College vote count, hence the “3-vote-minimum” for even the least populous states (see ", html.B("Figure 1"), "). The \
                                hyper-enfranchisement effect of the +2 boost tapers off as states increase in population and Electoral College apportionment, but \
                                if a state’s population garners it only 1 or 2 Congressional Representatives then that +2 Senator boost easily doubles or triples \
                                the relative impact of the voters in that state."
                            ]),
                            html.P(className="card-text", children=[
                                "This “small-state bias” is often calculated by comparing the ratio of each state’s ", html.I("population"), " to its Electoral \
                                College votes. The same effect is evident—and arguably more precise—if we compare the ratio of each state’s voter ", 
                                html.I("participation"), " (turnout) to its Electoral College votes. This ratio is the basis of “Voter Weight,” the core metric \
                                I'll be using throughout my analysis (explained in detail ", dcc.Link("here", href="/voter-weight-calculation"), ").",
                            ]),
                            html.P(className="card-text", children=[
                                "In ", html.B("Figure 2"), ", each state is listed in descending order by Voter Weight, and color shading indicates its number \
                                of votes in the Electoral College. If, in this most recent election, Voter Weight was 3.19 in Wyoming compared with 0.81 in \
                                neighboring Colorado, that means a vote cast in Cheyenne counted for 4X a vote cast 45 minutes south in Fort Collins. Want to \
                                make your voice heard in Washington? Move to Wyoming!"
                            ]), 
                        ])
                    ]),                               
                ]),
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.H4("A note about swing states and “winner-take-all”"),
                            html.P(className="card-text", children=[
                                "Astute critics of this crude voter influence metric will be quick to point out that it completely ignores the reality of \
                                “battleground states,” which Wyoming isn't but Colorado arguably is. The Electoral College's “winner take all” implementation, \
                                and the safe-state vs swing-state electioneering it engenders, tends to overshadow nibbling irritatants like small-state bias, \
                                but stick with me — the applications of this relatively simple Voter Weight metric might surprise you."
                            ]),
                            html.Br(),
                            html.H4("As the framers intended"),
                            html.P(className="card-text", children=[
                                "In the present-day political balance, rural states (like Wyoming) benefitting from small-state bias tend to lean conservative, adding \
                                an air of political urgency to recent grievances against this electoral wrinkle. But the influence boost for states with smaller \
                                populations has been part of the Electoral College since its inception — and suffice to say this was not its most controversial piece. \
                                From its genesis during the Constitutional Convention, each state’s apportionment in the Electoral College was based on two things:",
                                html.Ol(children=[
                                    html.Li("The same hybrid of flat (Senate) + proportional (House) representation that was the basis of the bicameral Great \
                                        Compromise - aka “small-state bias”"),
                                    html.Li("The infamous “Three-fifths Compromise” that rewarded white property-owning male voters in slave states with increased \
                                        congressional representation (and electoral vote allocation) in direct proportion to the size of their enslaved populations \
                                        - aka “slave-state bias”")
                                ]),
                            ]),
                            html.Img(src="/static/stockImages/constitution.jpg", style={"float": "right", "padding-left": "10px", "padding-top": "5px"}, width="50%"),
                            html.P(className="card-text", children=[
                                "Antiquated though it may be, many still argue that small-state bias has a functional role to play as a bulwark against big-state tyranny, \
                                protecting smaller populations (often spread across large swaths of territory) from being drowned out by those living in larger \
                                population centers. And as patently objectionable as the three-fifths compromise is, the fact that it and the heinous institution it \
                                bolstered were rendered obsolete by the Reconstruction amendments following the Civil War 150+ years ago has presumably limited its \
                                relevance with respect to the Electoral College since then."
                            ]),
                            html.P(className="card-text", children=[
                                "Presumably..."
                            ]), 
                        ])
                    ]), 
                ]),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=12, children=[
                    html.H4("Select year:", className="text-white"),
                    dcc.Slider(
                        id="small-state-bias-year-input",
                        className="text-white",
                        min=1980,
                        max=2020,
                        step=None,
                        marks={
                            int(y): {'label': str(y), 'style': {'transform': 'rotate(45deg)', 'color': 'white'}}
                            for y in data_obj.all_years if y >= 1980
                        },
                        value=2020,
                    ),
                ])                   
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=6, children=[
                    dcc.Graph(id="fig-bar-small-state-bias"),
                    html.P(className="card-text", style={"padding": "5px"}, children=[
                        html.Small("Figure 2: Small-state bias, shown by color shading states according to Electoral College votes, then listing them in \
                            descending order by Voter Weight."),
                    ]),
                ]),
                dbc.Col(md=6, children=[
                    dcc.Graph(id="fig-map-color-by-ecv"),
                    html.P(className="card-text", style={"padding": "5px"}, children=[
                        html.Small("Figure 1: States shaded by Electoral College votes, derived by adding the state's number of Congressional Representatives \
                            (as determined by decennial population census) to its number of Senators (2 per state, regardless of population)"),
                    ]),
                    html.Br(), 
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.P(className="card-text", style={"font-style": "italic"}, children=[
                                "The figures above, the figures below, and every other figure in this publication are interactive. Move the “Select year” slider \
                                to bring a different election year into focus. Highlight a portion of the figure to zoom in, then double-click to reset to the original \
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
                ]), 
            ]),
            html.Br(),
            html.Hr(className="border-light"),
            html.Br(),
            dbc.Row([
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.H4("Slave-state bias"),
                            html.P(className="card-text", children=[
                                "Sticking with the same “Voter Weight” calculation above, but turning the clock back 160 years, we encounter the infamous slave-state \
                                bias in ", html.B("Figure 3"), ". I’ve added new color shading to states in this second bar plot, using each state’s relationship to \
                                slavery as a grouping heuristic. For small states I’ve also carried forward color shading based on state size."
                            ]),
                            html.P(className="card-text", children=[
                                "Highlighting an example: If Voter Weight in 1852 was 2.24 in Alabama (9 Electoral College votes) compared with 0.78 in Illinois \
                                (11 Electoral College votes), that means pound-for-pound it would take ~3 votes cast in Illinois to equal the influence of a \
                                single vote cast in Alabama. This same trend applies to each slave state (shaded in pink) compared to each free state (shaded in \
                                purple) in Figure 3. This chart makes it easy to see how, aided by the three-fifths compromise, the “Slave Power” of the South \
                                was able to retain the political representation needed to assert and perpetuate slaveholder interests, despite a voting \
                                population much smaller than that in the North."
                            ]),
                            html.P(className="card-text", children=[
                                "States benefitting from the small-state boost, whether free states or slave states, still rise to the top of the Voter Weight \
                                rankings, but since the larger slave states send more electors to the Electoral College the magnitude of slave-state bias has \
                                measurably greater impact overall."
                            ]),
                            html.P(className="card-text", children=[
                                html.B("Figure 5"), " rearranges the data from Figure 3 into a scatter plot, crossing each state's voter turnout (x axis) with its \
                                Electoral College votes (y axis). The intersection between the axes where the Voter Weight ratio is 1.0 is plotted as a diagonal line \
                                signifying the nationwide mean. ", html.I("If every vote in every state counted equally, every state’s dot would be directly on top of \
                                that nationwide mean line."),
                            ]),
                            html.P(className="card-text", children=[
                                "To the extent that some state’s voters have greater impact than others (through favorable Electoral College apportionment, depressed \
                                turnout, etc), those whose dots appear above and to the left of the median line have more weight, while states whose dots appear below \
                                and to the right of the median line have less."
                            ]),
                            html.P(className="card-text", children=[
                                html.B("Figure 4"), " anchors us geographically by displaying each state's group affiliation on a map. All three figures are controlled \
                                using the same Year selection slider below and to the right."
                            ]),
                        ])
                    ]),
                ]),
                dbc.Col(md=6, children=[    
                    dcc.Graph(id="fig-scatter-dots-slave-state-bias"),
                    html.P(className="card-text", style={"padding": "5px"}, children=[
                        html.Small("Figure 5: Slave-state bias, shown by color shading states into Free, Slave, and Small groupings, and plotting voter turnout \
                            on the x axis against Electoral College Votes on the y axis. The average voter turnout per Electoral College vote — that is, the \
                            intersection between the axes where the Voter Weight ratio is 1.0 — is plotted as a diagonal line signifying the nationwide mean. \
                            States whose dots appear above and to the left of the nationwide mean line have Voter Weights greater than 1, those whose dots are \
                            below and to the right have Voter Weights less than 1."),
                    ]),
                ])
            ]),
            dbc.Row([
                dbc.Col(md=12, children=[
                    html.H4("Select year:", className="text-white"),
                    dcc.Slider(
                        id="slave-state-bias-year-input",
                        min=1820,
                        max=1860,
                        step=None,
                        marks={
                            int(y): {'label': str(y), 'style': {'transform': 'rotate(45deg)', 'color': 'white'}}
                            for y in data_obj.all_years if y >= 1820 and y <= 1860
                        },
                        value=1852,
                    ),
                ]),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=6, children=[
                    dcc.Graph(id="fig-bar-slave-state-bias"),
                    html.P(className="card-text", style={"padding": "5px"}, children=[
                        html.Small("Figure 3: Slave-state bias, shown by color shading states into Free, Slave, and Small groupings, then listing them in \
                            descending order by Voter Weight. Voter Weights are higher in slave states than free states, with small states still having some \
                            of the highest weights."),
                    ]),
                ]),
                dbc.Col(md=6, children=[
                    dcc.Graph(id="fig-map-slave-state-bias"),
                    html.P(className="card-text", style={"padding": "5px"}, children=[
                        html.Small("Figure 4: Reference map illustrating which states fit into which group. Areas lacking color shading or hover data \
                            are states that haven’t been admitted to the Union yet."),
                    ]),
                ])
            ]),
            html.Br(),
            html.Hr(className="border-light"),
            html.Div(children=[
                html.Ul(className="pagination pagination-lg justify-content-center", children=[
                    html.Li(className="page-item flex", style={"width": "50%"}, children=[
                        html.A(className="page-link", href="/voter-weight-electoral-college-bias-page1", children=[
                            "← Part 1: Electoral College bias: Equality for states, not for voters"
                        ])
                    ]),
                    html.Li(className="page-item flex", style={"width": "20%"}),
                    html.Li(className="page-item flex", style={"width": "50%", "text-align": "right"}, children=[
                        html.A(className="page-link", href="/voter-weight-electoral-college-bias-page3", children=[
                            "Part 3: Reconstruction and Black voting rights →"
                        ])
                    ]),
                ])
            ]),
        ])
    ])
])