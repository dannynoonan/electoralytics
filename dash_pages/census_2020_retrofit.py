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
                # html.H3("Applying 2020 Census data to the 2020 Presidential election"),
                html.H3("Retrofitting the 2020 Presidential election to 2020 Census data"),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=3, children=[
                    html.Div(className="list-group sticky-top", children=[
                        html.A(href="/census-2020-retrofit", className="list-group-item list-group-item-action active", children=[
                            "→ [5/5/2021] Retrofitting the 2020 Presidential election to 2020 Census data"]),
                        html.A(href="/voter-weight-electoral-college-bias-intro", className="list-group-item list-group-item-action", children=[
                            "[4/2/2021] Visualizing the “Jim Crow Power”"]),
                        html.A(href="/voter-weight-calculation", className="list-group-item list-group-item-action", children=[
                            "Calculating Voter Weight"]),
                        html.A(href="/voter-weight-figure-vault", className="list-group-item list-group-item-action", children=[
                            "The Vault: 220 years of maps, charts, & figures"]),
                    ])
                ]),
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success lead", style={"font-family": "times-new-roman"}, children=[
                        dbc.CardBody([
                            html.P("May 5, 2021", style={"font-family": "arial", "font-size": "10pt"}),
                            html.P(className="card-text", children=[
                                "Last week, the US Census Bureau released its first round of results from the 2020 Census, including state-level reapportionment of \
                                Congressional seats and Electoral College votes. The changes were ", dcc.Link("less dramatic than predicted", target="_blank",
                                href="https://www.washingtonpost.com/politics/2021/04/27/trailer-big-census-small-changes-next-decade-political-map-explained/"), 
                                ", with the biggest headlines being about the ", dcc.Link("slow overall rate of population growth", target="_blank",
                                href="https://www.washingtonpost.com/dc-md-va/interactive/2021/2020-census-us-population-results/"), " rather than the redistribution \
                                of population, representation, and political influence. The fact that New York lost a Congressional seat and an Electoral College \
                                vote by a ", dcc.Link("whisker-thin margin of 89 respondents", target="_blank",
                                href="https://www.businessinsider.com/new-york-lost-house-seat-by-89-people-census-bureau-2021-4"), " has induced some Empire state \
                                facepalming, but by and large the repportionment conversation seems to reduce to the age old question: does a population influx change \
                                the politics of a place, or does a place change the politics of a population influx?"
                            ]),
                            html.P(className="card-text", children=[
                                "It remains to be seen whether migrating Californians turn Texas into California, or whether Texas turns Californians Texan. Not in \
                                dispute: traditionally Red states will be gaining more political headcount than they’re losing, while traditionally Blue states are \
                                losing more than they’re gaining."
                            ]),
                            html.H4(className="lead", style={"font-size": "20pt"}, children=["When the Census and a Presidential election overlap"]),
                            html.P(className="card-text", children=[
                                "Every 10 years the US conducts a Census, and every 20 years that Census happens to occur in the same year as a Presidential election. \
                                When the two overlap, as they did in 2020, it gives an opportunity to immediately apply the updated Census apportionment data to the \
                                recent election. In fact, mathematically speaking, 2020 Census data provides a “truer” filter through which to interpet the 2020 \
                                election than the crusty old 2010 Census apportionment data it replaces."
                            ]),
                            html.P(className="card-text", children=[
                                "13 states are having their Congressional headcounts and Electoral College allocation changed due to 2020 Census results, and none of \
                                these changes go into effect until 2022. But, for experimentation’s sake, if we retroactively apply these changes to the 2020 \
                                Presidential election, we see that states Biden won are losing 3 Electoral College votes overall, compared to states Trump won gaining \
                                3 Electoral College votes. Recalculating 2020’s election results through the filter of 2020 Census data, Biden’s 306-232 Electoral \
                                College victory narrows slightly, from a 74-vote margin down to a 68-vote margin."
                            ])
                        ]),
                    ]),
                ]),
                dbc.Col(md=3),
            ]),
            html.Br(),html.Br(),
            dbc.Row([
                dbc.Col(md=3, children=[
                    html.H4("Drag slider to see change →", className="text-white", style={'text-align': 'center'}),
                ]),
                dbc.Col(md=6, children=[
                    dcc.Slider(
                        id="year-input-census-2020-color-by-party",
                        min=2020.1,
                        max=2020.4,
                        step=None,
                        marks={
                            2020.1: {'label': '2020 election, before census', 'style': {'color': 'white'}},
                            2020.2: {'label': 'Pre-census highlights', 'style': {'text-align': 'left', 'color': 'white'}},
                            2020.3: {'label': 'Post-census highlights', 'style': {'color': 'white'}},
                            2020.4: {'label': '2020 election, retrofitted to census', 'style': {'white-space': 'nowrap', 'color': 'white'}},
                        },
                        value=2020.1,
                    ),
                ]),
                dbc.Col(md=3)
            ]),
            html.Br(),html.Br(),
            dbc.Row([
                dbc.Col(md=6, children=[
                    dcc.Graph(id="fig-bar-census-2020-color-by-party"),
                ]),
                dbc.Col(md=6, children=[
                    dcc.Graph(id="fig-map-census-2020-color-by-party"),
                    html.Br(),
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.Div(style={"text-align": "center"}, children=[
                                html.P(className="card-text", children=[
                                    "Map and bar chart of states color shaded by Voter Weight. States in bar chart are also ordered by Voter Weight."
                                ]),
                            ]),
                            html.Small(children=[
                                "↑ Open an ", dcc.Link("intractive slideshow animation", target="_blank",
                                href="https://htmlpreview.github.io/?https://github.com/dannynoonan/electoralytics/blob/master/html_figures/anim_map_state_vw_acw4_1000.html"),
                                " illustrating every year for the map above",
                            ]),
                            html.Br(),
                            html.Small(className="card-text", style={"float": "right"}, children=[
                                "Open an ", dcc.Link("intractive slideshow animation", target="_blank",
                                href="https://htmlpreview.github.io/?https://github.com/dannynoonan/electoralytics/blob/master/html_figures/anim_bar_state_vw_color_by_vw_acw4_900.html"),
                                " illustrating every year for the chart to the right →",
                            ]),
                        ]),
                    ])
                ]),
            ]),
            html.Br(),html.Br(),
            dbc.Row([
                dbc.Col(md=3),
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success lead", style={"font-family": "times-new-roman"}, children=[
                        dbc.CardBody([
                            html.P(className="card-text", children=[
                                "That 6-vote difference isn't exactly headline-grabbing, but it’s easy to imagine a world where a razor-thin Presidential election \
                                outcome could be thrown into further chaos by contemporaneous Census updates, particularly if the fresh Census data favors the loser \
                                and tightens (or reverses) any Electoral College advantage. For example, if Biden had lost Georgia (16 EC votes) and Pennsylvania (20 \
                                EC votes), bringing the November 2020 Electoral College scoreboard to a nail-biting 270-268, then the retrofitted application of 2020 \
                                Census data to the 2020 election would have actually put Biden a couple Electoral College votes behind. Not in a legal sense, since \
                                there’s nothing remotely legal about the retroactive application of 2020 Census data to already-certified 2020 election results. But \
                                questions of legality haven’t exactly hindered the GOP’s more fanatical “stop the steal” propagandists in recent months."                          
                            ]),
                            html.P(className="card-text", children=[
                                "Historically, Presidential elections that happen to coincide with the Census have largely been Electoral College blowouts, so the \
                                idea of re-assessing a recent election using an updated apportionment filter has never had any reason to gain traction. Even the 1860 \
                                election, where Lincoln only captured 40% of the popular vote, was still a 100-vote Electoral College landslide, as was Kennedy’s \
                                84-vote Electoral College cushion over Nixon in 1960, despite Kennedy’s razor-thin 0.02% lead in the popular vote."
                            ]),                
                            html.P(className="card-text", children=[
                                "The elections of 1800 and 2000 are the exceptions, but in both cases the year’s fresh Census data ended up favoring the winner, thus \
                                adding to their legitimacy rather than igniting further controversy. The 1800 rematch between Jefferson and Adams was an 8-vote \
                                Electoral College squeaker, but Jefferson’s edge would have expanded to 21 had the 1800 Census data been applied to the 1800 election \
                                (none of which would have affected the dead-heat Jefferson found himself in with his slippery “running mate” Aaron Burr). And the \
                                tinder was certainly in place to spark a fresh round of controversy after Bush-Gore 2000, where months of legal wrangling had delivered \
                                Bush a 4-vote Electoral College victory by the time the Census data was released. But the reapportionment changes resulting from the \
                                2000 Census almost universally favored the victor: retroactive application of 2020 Census data to the 2020 Presidential election would \
                                have widened Bush's Electoral College lead from 4 votes to 18."
                            ]),
                            html.H4(className="lead", style={"font-size": "20pt"}, children=["Before vs after: Whose votes count the most?"]),
                            html.P(className="card-text", children=[
                                "“Voter Weight” calculates the relative impact of a vote cast in one state vs a vote cast in another, given the total number of votes \
                                cast in each state and the number of Electoral College votes allocated to each state respectively. Very high and very low Voter Weights \
                                speak to imbalances in the system, anti-Democratic forces that tend to favor one population over another. It sounds ominous—and at \
                                points in American history it certainly has been—but in recent decades Voter Weight disparities have been almost entirely tied to the \
                                size of a state’s population, with the +2 Electoral College votes each state receives for its 2 Senators conferring a greater \
                                proportional boost to small states than it does for larger, more populous states (visit the ", dcc.Link("Voter Weight calculation page", 
                                href="/voter-weight-calculation"), " for more details). It’s a crude and simple metric, devoid of nuance with respect to the contextual \
                                importance of a given state in a given election (i.e. whether it’s a “swing state” or a “safe state”), but it remains one of the \
                                emergent quirks of the Electoral College worth keeping tabs on - and a potential canary in the coal mine should state-level voter \
                                suppression reach levels that would register nationally."
                            ]),                
                            html.P(className="card-text", children=[
                                "The charts below spell out how 2020 Census data, if retroactively applied to 2020 election results, would affect Voter Weight \
                                calculations and rankings. Not surprisingly, the smallest states are the ones most affected by their apportionment changes, with West \
                                Virginia voters shaving 20% off their national influence and dropping from 9th place to the 13th spot, and Montana voters moving in \
                                the opposite direction, trading up to 9th place from 13th and adding 33% to their national influence. Colorado expands their stake by \
                                11% and leaps 7 spots from 49th to 42nd, while Oregon voters leap 18 spots from 44th place to 32nd, expanding their national influence \
                                by 14% and cozying up alongside Texans (who, despite gaining the most electoral influence in absolute terms, only add 5% to their \
                                Voter Weight, and don’t budge from their spot at 31st in the rankings)."
                            ]),
                        ]),
                    ]),
                ]),
                dbc.Col(md=3),
            ]),
            html.Br(),html.Br(),
            dbc.Row([
                dbc.Col(md=3, children=[
                    html.H4("Drag slider to see change →", className="text-white", style={'text-align': 'center'}),
                ]),
                dbc.Col(md=6, children=[
                    dcc.Slider(
                        id="year-input-census-2020-color-by-vw",
                        min=2020.1,
                        max=2020.4,
                        step=None,
                        marks={
                            2020.1: {'label': '2020 election, before census', 'style': {'color': 'white'}},
                            2020.2: {'label': 'Pre-census highlights', 'style': {'text-align': 'left', 'color': 'white'}},
                            2020.3: {'label': 'Post-census highlights', 'style': {'color': 'white'}},
                            2020.4: {'label': '2020 election, retrofitted to census', 'style': {'white-space': 'nowrap', 'color': 'white'}},
                        },
                        value=2020.1,
                    ),
                ]),
                dbc.Col(md=3)
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=6, children=[
                    dcc.Graph(id="fig-bar-census-2020-color-by-vw"),
                ]),
                dbc.Col(md=6, children=[
                    dcc.Graph(id="fig-map-census-2020-color-by-vw"),
                    html.Br(),
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.Div(style={"text-align": "center"}, children=[
                                html.P(className="card-text", children=[
                                    "Map and bar chart of states color shaded by Voter Weight. States in bar chart are also ordered by Voter Weight."
                                ]),
                            ]),
                            html.Small(children=[
                                "↑ Open an ", dcc.Link("intractive slideshow animation", target="_blank",
                                href="https://htmlpreview.github.io/?https://github.com/dannynoonan/electoralytics/blob/master/html_figures/anim_map_state_vw_acw4_1000.html"),
                                " illustrating every year for the map above",
                            ]),
                            html.Br(),
                            html.Small(className="card-text", style={"float": "right"}, children=[
                                "Open an ", dcc.Link("intractive slideshow animation", target="_blank",
                                href="https://htmlpreview.github.io/?https://github.com/dannynoonan/electoralytics/blob/master/html_figures/anim_bar_state_vw_color_by_vw_acw4_900.html"),
                                " illustrating every year for the chart to the right →",
                            ]),
                        ]),
                    ])
                ])
            ]),
        ])
    ])
])