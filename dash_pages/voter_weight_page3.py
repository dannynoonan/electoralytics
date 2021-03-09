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
                html.H3("Visualizing Jim Crow Voter Suppression: Apportionment, Participation, and Electoral College Bias"),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.H4("Voter suppression as a “five-fifths” scheme"),
                            html.P(className="card-text", children=[
                                "Here’s where things veer off of the standard storyline about the Electoral College. Shortly before last November’s election, \
                                an episode of ", html.I("NPR’s Throughline"), " made a case I’d never considered before, connecting the lingering effects of the \
                                three-fifths compromise to attitudes toward enfranchisement in the post-war South. The hosts, joined by Yale Professor and noted \
                                constitutional scholar Akhil Reed Amar, argued that although the three-fifths compromise did ", html.I("technically"), " end with \
                                the abolition of slavery, it was effectively replaced by an even ", html.I("less"), " equitable permutation of that infamous \
                                inaugural Electoral College bias."
                            ]),
                            html.P(className="card-text", children=[
                                "Part of their “(mis)Representative Democracy” series, the full episode is 58 minutes, but this ", 
                                dcc.Link("5-minute video snippet", href="https://www.npr.org/2020/09/30/918717270/the-electoral-college", target="_blank"), 
                                " gets to the heart of what caught my attention:"
                            ]),
                            html.Iframe(id="jw_embed", width="100%", height="423", 
                                src="https://www.npr.org/embedded-video?storyId=918717270&mediaId=930549092&jwMediaType=null"),
                        ])
                    ])
                ]),
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.P(className="card-text", children=[
                                "If you aren't able to watch or listen to the clip, this section gets to the essence:"
                            ]),
                            html.Div(style={"margin-left": "50px", "margin-right": "50px", "font-style": "italic"}, children=[
                                html.P(className="card-text", children=[
                                    "After the Civil War and the passage of the 13th amendment abolishing slavery, [southern states’] resistance to direct election \
                                    [as an alternative to the Electoral College] only grew stronger."
                                ]),
                                html.P(className="card-text", children=[
                                    "It's the “oh, crap” moment, because now we've gotten rid of slavery. So what happens to three-fifths? It becomes ", 
                                    html.B("FIVE"), "-fifths, because now technically everyone is free."
                                ]),
                                html.P(className="card-text", children=[
                                    "Suddenly, former slaves were fully counted in their populations. And now, the former Confederacy wielded even more power. \
                                    Because the Electoral College system rewards population over participation, southern states started to systematically keep \
                                    Black citizens from voting."
                                ]),
                                html.P(className="card-text", children=[
                                    "So actually, the South is going to have more seats in the Electoral College than ever before, more seats in the House of \
                                    Representatives, and they're not letting their people vote."
                                ]),
                                html.P(className="card-text", children=[
                                    "By suppressing Black voters, the southern states actually got a better deal when the three-fifths compromise ended."
                                ])
                            ]),
                            html.Br(),
                            html.P(className="card-text", children=[
                                "That Southern white “Redeemers” disenfranchised the Black electorate through the uneven application of poll taxes, literacy tests, \
                                grandfather clauses, as well as more direct intimidation and violence for 90-odd years during the Jim Crow era is (a) f***ing insane, \
                                horrific, and infuriating, but also (b) not breaking news."
                            ]),
                            html.P(className="card-text", children=[
                                "What did feel “news-breaking” in the podcast was the idea that suppressing the Black vote had been part-and-parcel with Southern \
                                whites retaining — nay, ", html.I("increasing"), " — their disproportionate pre-war influence on national elections, as compared to \
                                voters in other states. The idea that, buried in the warped racist logic that drove Southern Redeemers to shamelessly, systematically, \
                                and violently prevent their Black populations from voting between the end of Reconstruction in 1877 and the signing of the Voting \
                                Rights Act in 1965, was a sense of lingering electoral entitlement, an expectation that the same preferential treatment for Southern \
                                whites enshrined in the “three-fifths” clause of the Constitution ought to be protected and perpetuated.",
                            ]),
                        ])
                    ])
                ])
            ]),
            html.Br(),
            html.Hr(className="border-light"),
            html.Br(),
            dbc.Row([
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.H4("Suppression-state bias"),
                            html.P(className="card-text", children=[
                                "Considering our 21st century grumbling about how small-state bias amplifies the voice of an Alaska voter at the expense of a \
                                California voter, and the stomach-churning 18th-19th century slave-state bias which amplified the voice of a Virginia slave-owner \
                                relative to a New York merchant, I was very curious how this third category of hyper-enfranchisement bias in the Jim Crow South \
                                would stack up against those other two."
                            ]),
                            html.Br(),
                            html.H4("Grouping heuristic"),
                            html.P(className="card-text", children=[
                                "Choosing a state grouping heuristic that would correlate with voter suppression practices during Jim Crow wasn’t quite as \
                                straight-forward as grouping by slave states vs free states. Most slave states seceded to join the Confederacy during the Civil War, \
                                but a small handful of “Border” states, where slavery was legal, remained loyal to the Union."
                            ]),
                            html.P(className="card-text", children=[
                                "I was curious what would be more predictive of a state’s tendency toward post-war voter suppression: the fact that they’d been a \
                                slave state, or their political alliance (and military defeat) with the Confederacy. In a sense, the Border states function as a \
                                control group for examining that question."
                            ]),
                            html.P(className="card-text", children=[
                                "With that in mind, I grouped states into Union (free), Confederate (slave), and Border (slave-Union) state groups, using the familiar \
                                blue and butternut uniform colors to identify the first two. I also retained the “Small” group used above, and added a “Postbellum” \
                                group for states admitted to the Union after the Civil War."
                            ]),
                            html.P(className="card-text", children=[
                                "Maps and more details about these Civil War groupings as well as alternative Regional Census groupings are in the ", 
                                dcc.Link("Explanation of Groupings", href="/explanation-of-groupings"), " section."
                            ]),
                            html.Br(),
                            html.H4("Suppression-state bias visualizations"),
                            html.P(className="card-text", children=[
                                html.B("Figures 6, 8, and 9"), " recycle the same axes and mapping parameters from above to generate and render Voter Weight data during \
                                the Jim Crow era, this time grouping states by their Civil War affiliations."
                            ]),
                            html.P(className="card-text", children=[
                                html.B("Figure 7"), " plots each state’s Electoral College votes on the x axis, plots the derived Voter Weight on the y axis, and \
                                now represents voter turnout as the size of each state’s “bubble.” The horizontal line at 1.0 on the y axis corresponds to the \
                                national mean. The higher a bubble is above the mean, the greater the weight of individual votes cast in that state."
                            ]),
                            html.P(className="card-text", children=[
                                "Similar to the ratio-based scatter plots in Figure 5 and Figure 6: if every vote in every state counted equally, every state’s bubble \
                                in Figure 7 would be directly on top of that nationwide mean line (horizontal in this case)."
                            ]),
                            html.P(className="card-text", children=[
                                "For those states in Figure 7 whose Electoral College vote counts (x values) and voter turnout (bubble sizes) are very low, a high Voter \
                                Weight can be explained by small-state bias. For the rest, another bias is at play."
                            ]),
                        ])
                    ]),
                    html.Br(),html.Br(),
                    dcc.Graph(id="fig-scatter-bubbles-suppress-state-bias"),
                    html.P(className="card-text", style={"padding": "5px"}, children=[
                        html.Small("Figure 7: Suppression-state bias, shown by color shading states by Civil War groupings, and plotting Electoral College votes on \
                            the x axis against derived Voter Weight on the y axis, with voter turnout now represented by the size of each state’s “bubble.” The \
                            national mean is plotted at all points on the x axis where Voter Weight is 1.0 on the y axis, and any bubble above the mean line indicates \
                            a state whose voters — that is, those who were able to vote — wielded disproportionately high Voter Weight in that election. For small \
                            bubbles with low EC vote counts, high Voter Weight can be explained by small-state bias. For larger bubbles, we are looking at \
                            suppression-state bias."),
                    ]),
                    html.Br(),
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.H4("Five-fifths and then some"),
                            html.P(className="card-text", children=[
                                "If the hyper-enfranchisement effect seems more extreme in this era than it did in the other two time periods, well... that’s because \
                                it is. Highlighting just one example: If Voter Weight in 1940 was 7.5 in South Carolina compared with 0.96 in Connecticut, that means \
                                pound-for-pound it would take 7-8 votes cast in Connecticut to equal the influence of a single vote cast in South Carolina. This \
                                represents a staggering disparity in the influence of individual voters—that is, those permitted to vote—in these states."
                            ]),
                            html.P(className="card-text", children=[
                                "Absent the factors of state size (both state’s populations earned them 8 Electoral College votes) or slavery (abolished a full 75 \
                                years prior) the bias revealed in this bar graph has no explanation in Electoral apportionment “originalist” logic. Nothing accounts \
                                for this disparity other than staggering differences in voter participation, almost certainly tied to massive institutional voter \
                                suppression."
                            ]),
                            html.Br(),
                            html.H4("Old story, new angle"),
                            html.P(className="card-text", children=[
                                "Depending on your familiarity with racial voter suppression in the century following the Civil War, you may or may not be surprised \
                                that the small-state and slave-state biases mathematically-prescribed in the Constitution—that is, the apportionment imbalances that \
                                have made it onto every AP American History exam since the arrival of the Number 2 pencil—might in fact pale in comparison to other \
                                permutations of sustained, systemic electoral inequity."
                            ]),
                            html.P(className="card-text", children=[
                                "The bigger story here, of course, isn’t that Southern states’ (white) voters counted for more than Northern and Western states’ \
                                (predominantly white) voters. The bigger story is that hundreds of thousands of Southern Blacks (and poor whites) were prevented from \
                                voting altogether, through the uneven application of poll taxes, literacy tests, grandfather clauses, as well as more direct \
                                intimidation and violence for 90-odd years during the Jim Crow era."
                            ]),
                            html.P(className="card-text", children=[
                                "However, if ", html.I("Throughline’s"), " “five-fifths” post-war status-quo idea holds water, the villainous cackling of \
                                turn-of-the-century Southern racist political scheming doesn’t end there. Under an Electoral College system that grants influence \
                                based on population rather than participation, voter suppression has a corollary effect — and another perverse incentive — at the \
                                national level: it amplifies precisely those voices responsible for suppressing their local voter turnout, relative to the voices \
                                of voters in states not engaged in systemic voter suppression."
                            ]),
                            html.P(className="card-text", children=[
                                "I don’t mean to get out over my skis on the notion of intent. The question of which nefarious objectives out of an assortment of \
                                plausible nefarious objectives motivated white supremacist voter suppression in the postbellum South is well beyond my purview - \
                                leave that to the historians and social scientists."
                            ]),
                            html.P(className="card-text", children=[
                                "Whether a side-effect of racist voter suppression or an intentional strategy unto itself, Southern white elites appear to have \
                                maintained, and even increased, their disproportionate influence over national-level politics throughout the Jim Crow Era. This \
                                despite the abolition of slavery, the nullification of the three-fifths compromise, and their total military and political defeat \
                                in the Civil War. And they couldn't have done it without the Electoral College, since a pure national popular vote would have \
                                simply diluted their states' lower turnouts among the much higher participation levels in states holding fair, egalitarian, and \
                                democratic elections during the same time period."
                            ]),
                        ])
                    ]),
                    html.Br(),
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.P(className="card-text", children=[
                                html.B("Next section >> "), dcc.Link("Part 4: Conclusions and Discussion", href="/voter-weight-conclusions")
                            ]),
                            html.P(children=[
                                html.Ul(children=[
                                    html.Li(
                                        dcc.Link("Intro: Hyper-enfranchisement and the Electoral College", href="/voter-weight-electoral-college-bias-intro")
                                    ),
                                    html.Li(
                                        dcc.Link("Part 1: Electoral College bias breakdown", href="/voter-weight-electoral-college-bias-page1")
                                    ),
                                    html.Li(
                                        dcc.Link("Part 2: Small-state bias and slave-state bias: As the framers intended", href="/voter-weight-electoral-college-bias-page2")
                                    ),
                                    html.Li("Part 3: Reconstruction, Redemption, and suppression-state bias"),
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
                    ])
                ]),
                dbc.Col(md=6, children=[
                    dcc.Graph(id="fig-scatter-dots-suppress-state-bias"),
                    html.P(className="card-text", style={"padding": "5px"}, children=[
                        html.Small("Figure 6: Suppression-state bias, shown by color shading states by Civil War groupings, and plotting voter turnout on the x \
                            axis against Electoral College Votes on the y axis. The average voter turnout tally per Electoral College vote (where the Voter Weight \
                            ratio is 1.0) is plotted as a diagonal line signifying the nationwide mean. States whose dots appear above and to the left of the \
                            nationwide mean line have Voter Weights greater than 1, those whose dots are below and to the right have Voter Weights less than 1."),
                    ]),
                    html.H4("Select year:", className="text-white"),
                    dcc.Slider(
                        id="suppress-state-bias-year-input",
                        min=1880,
                        max=1960,
                        step=None,
                        marks={
                            int(y): {'label': str(y), 'style': {'transform': 'rotate(45deg)', 'color': 'white'}}
                            for y in data_obj.all_years if y >= 1880 and y <= 1960
                        },
                        value=1940,
                    ),
                    html.Br(),
                    dcc.Graph(id="fig-bar-suppress-state-bias"),
                    html.P(className="card-text", style={"padding": "5px"}, children=[
                        html.Small("Figure 8: Suppression-state bias, shown by color shading states by Civil War groupings, then listing them in descending order \
                            by Voter Weight. Voter Weights are generally higher in former Confederate states than in Union, Border, or Postbellum states, with \
                            small states still having some of the highest weights."),
                    ]),
                    html.Br(),
                    dcc.Graph(id="fig-map-suppress-state-bias"),
                    html.P(className="card-text", style={"padding": "5px"}, children=[
                        html.Small("Figure 9: Reference map illustrating which states fit into which group. Areas lacking color shading or hover data are states \
                            that haven’t been admitted to the Union yet."),
                    ]),
                ])
            ]),
            html.Br(),
            # html.Hr(className="border-light"),
            # html.Br(),
            # dbc.Row([
            #     dbc.Col(md=6, children=[
            #         dbc.Card(className="border-success", children=[
            #             dbc.CardBody([
            #                 html.H4("Supplemental sections"),
            #                 html.P(className="card-text", children=[
            #                     "Regardless of underlying plans or purpose, this disconnect between census population and voter participation is seared into the \
            #                     historical record, offering a way to compare and quantify democratic and anti-democratic behavior over time - and to potentially \
            #                     infer correlation or causation between specific external factors and Voter Weight trends."
            #                 ]),
            #                 html.P(className="card-text", children=[
            #                     "This ", dcc.Link("annotated line-chart timeline", href="/voter-weight-timeline-visualization"), " of state- and group-level Voter \
            #                     Weights stretching from 1800 to 2020 attempts to mix a (very thin) layer of historical context in with the full gamut of Voter \
            #                     Weight data. It’s a lot to absorb, but it’s configurable, so strip it down to the studs and build it back up however you’d like, \
            #                     comparing any combination of states or groups over any time period you’d like to zoom in on."
            #                 ]),
            #             ])
            #         ])
            #     ]),
            #     dbc.Col(md=6, children=[
            #         dbc.Card(className="border-success", children=[
            #             dbc.CardBody([
            #                 html.P(className="card-text", children=[
            #                     "Following that, there are four other sections to this presentation that are here for you to dig into:",
            #                     html.Li(children=[dcc.Link("How Voter Weight is calculated", href="/voter-weight-calculation")]), 
            #                     html.Li(children=[dcc.Link("How the state groupings break down", href="/explanation-of-groupings")]), 
            #                     html.Li(children=[dcc.Link("The full vault of year-by-year data visualizations", href="/voter-weight-figure-vault")]),
            #                     html.Li(children=[dcc.Link("Discussion and Conclusions", href="/voter-weight-conclusions")]),
            #                 ])
            #             ])
            #         ]),
            #     ]),
            # ])
        ])
    ])
])