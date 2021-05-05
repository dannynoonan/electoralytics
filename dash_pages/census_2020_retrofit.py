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
                            "→ Retrofitting the 2020 Presidential election to 2020 Census data"]),
                        html.A(href="/voter-weight-electoral-college-bias-intro", className="list-group-item list-group-item-action", children=[
                            "Visualizing the “Jim Crow Power”"]),
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
                                Congressional seats and Electoral College votes. The changes were less dramatic than some had predicted, with the biggest headlines \
                                being about the slow overall rate of population growth rather than the redistribution of population, representation, and political \
                                influence. The fact that New York lost a Congressional seat and an Electoral College vote by a whisker-thin margin of 89 respondents \
                                has people smacking their foreheads, but by and large the repportionment conversation seems to reduce to the age old question: does a \
                                population influx change the politics of a place, or does a place change the politics of a population influx?"
                            ]),
                            html.P(className="card-text", children=[
                                "It remains to be seen whether migrating Californians turn Texas into California, or whether Texas turns Californians Texan. Not in \
                                dispute: traditionally Red states will be gaining more political headcount than they’re losing, while traditionally Blue states are \
                                losing more than they’re gaining."
                            ]),
                            html.H3("Vicennial Conjunction: Census and Presidential election in the same year"),
                            html.P(className="card-text", children=[
                                "Every 10 years the US conducts a Census, and every 20 years that Census happens to occur in the same year as a Presidential election. \
                                When the two overlap, as they did in 2020, it gives an opportunity to immediately apply the udpated Census apportionment data to the \
                                recent election. In fact, mathematically speaking, the application of 2020 Census data to the 2020 Presidential election is more \
                                accurate—to the extent that Electoral College vote counts “accurately” measure anything—than the crusty old 2010 Census apportionment \
                                data it replaces."
                            ]),
                            html.P(className="card-text", children=[
                                "13 states are having their Congressional headcounts and Electoral College allocation changed due to 2020 Census results, and none of \
                                these changes go into effect until 2022. But, for experimentation’s sake, if we retroactively apply these changes to the 2020 \
                                Presidential election, we see that states Biden picked up lost 3 Electoral College votes overall, compared to states Trump won which \
                                gained 3 Electoral College votes. If 2020’s election results were recalculated through the filter of 2020 Census data, Biden’s \
                                306-232 Electoral College victory would narrow slightly, from a 74-vote margin down to a 68-vote margin."
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
                                and tightens (or reverses) the Electoral College advantage. For example, if Biden had lost Georgia (16 EC votes) and Pennsylvania (20 \
                                EC votes), bringing the November 2020 Electoral College scoreboard to a nail-biting 270-268, then the retrofitted application of 2020 \
                                Census data to the 2020 election would have actually put Biden a couple Electoral College votes behind - not in a legal sense, since \
                                there’s nothing remotely legal about the retroactive application of 2020 Census data to already-certified 2020 election results. But \
                                questions of legality haven’t exactly hindered the GOP’s more fanatical “stop the steal” propagandists up till now."                          
                            ]),
                            html.P(className="card-text", children=[
                                "Historically, Presidential elections that happen to coincide with the Census have largely been Electoral College blowouts, so the \
                                idea of re-assessing a recent election using an updated apportionment filter has never had any reason to gain traction. Even the 1860 \
                                election, where Lincoln only captured 40% of the popular vote, was still a 100-vote Electoral College landslide, as was Kennedy’s \
                                84-vote edge over Nixon in 1960, despite Kennedy’s razor-thin 0.02% lead in the popular vote."
                            ]),                
                            html.P(className="card-text", children=[
                                "Every 10 years the US conducts a Census, and every 20 years that Census happens to occur in the same year as a Presidential election. \
                                When the two overlap, as they did in 2020, it gives an opportunity to immediately apply the udpated Census apportionment data to the \
                                recent election. In fact, mathematically speaking, the application of 2020 Census data to the 2020 Presidential election is more \
                                accurate—to the extent that Electoral College vote counts “accurately” measure anything—than the crusty old 2010 Census apportionment \
                                data it replaces."
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
                            html.H3("Before vs After: Where Does My Vote Count the Most?"),
                            html.P(className="card-text", children=[
                                "“Voter Weight” is a metric that calculates the relative impact of a vote cast in one state vs a vote cast in another, given the total \
                                number of votes cast in each state and the number of Electoral College votes allocated to each state respectively. Throughout much of \
                                American history, disparities in Voter Weight have tended to correlate with systemic voter suppression and other forms of inequality, as \
                                evident in the examples described on the Voter Weight calculation page. Ultimately it’s a crude and simple metric, devoid of nuance with \
                                respect to the contextual importance of a given state in a given election (i.e. whether it’s a “swing state” or a “safe state”), but \
                                it’s one of the emergent quirks of the Electoral College that I think is worth keeping tabs on."
                            ]),                
                            html.P(className="card-text", children=[
                                "The chart below spells out the Voter Weight rankings in greater detail, but I’ve listed them out here as well."
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