import dash
from dash.dependencies import Input, Output, State
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
                html.H3("Using “Voter Weight” to explore Electoral College bias"),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.H4("Different states, different weights"),
                            html.P(className="card-text", children=[
                                "There’s some funny math built into the way we elect the US president."
                            ]),
                            html.P(className="card-text", children=[
                                "Unlike more run-of-the-mill democratic contests where every vote is tallied and the candidate with the most votes is declared \
                                the winner (", html.I("BOHHH"), "-ring), here the weight of each individual vote depends on the state from which it is cast. \
                                Specifically:", 
                                html.Ul(children=[
                                    html.Li("the Electoral College apportionment granted to that state"),
                                    html.Li("how many people turn out to vote in that state"),
                                ]),
                                "On the surface, this is pretty straight-forward. But the way these factors have been implemented and manipulated over the \
                                centuries reveals an eye-opening history of inequity, entitlement, and imbalance - all of which is enshrined in historical \
                                election data."
                            ]),
                            html.Br(),
                            html.H4("Small-state bias"),
                            html.P(className="card-text", children=[
                                "One of the more familiar Electoral College imbalances is between voters in larger states and voters in smaller states."
                            ]),
                            html.P(className="card-text", children=[
                                "Quick review: each state’s Electoral College votes equal the sum of its Representatives + Senators in Congress, the same \
                                bicameral balance that was part of the Constitutional Convention’s ", dcc.Link("Great Compromise", 
                                href="https://en.wikipedia.org/wiki/Connecticut_Compromise", target="_blank"), ". And just as every state sends the same number \
                                of Senators to DC, even the smallest states receive the same +2 Senator “bicameral boost” in their Electoral College vote count, \
                                hence the “3-vote-minimum” for even the least populous states. The effect of the +2 boost tapers off as states increase in \
                                population and Electoral College apportionment, but if a state’s population garners it only 1 or 2 Congressional Representatives \
                                then that +2 Senator boost easily doubles or triples the relative impact of that state’s voters."
                            ]),
                            html.P(className="card-text", children=[
                                "This “small-state bias” are often calculated by comparing the ratio of each state’s population to its Electoral College \
                                votes, but the same effect is evident—and arguably more precise—if we base the calculation on voter ", html.I("participation"), 
                                " (turnout) instead of population. This is the basis of “Voter Weight,” which is reused throughout my analysis and which I explore in \
                                detail in an upcoming section."
                            ]),
                            html.P(className="card-text", children=[
                                "In ", html.B("Figure 1"), ", each state is listed in descending order by Voter Weight, and color shading indicates its number of votes in the \
                                Electoral College. If, in this most recent election, Voter Weight was 3.19 in Wyoming compared with 0.81 in neighboring Colorado, \
                                that means a vote cast in Cheyenne counted for 4X a vote cast 45 minutes south in Fort Collins. Want to make your voice heard \
                                in Washington? Move to Wyoming!"
                            ]),
                            html.P(className="card-text", children=[
                                html.I("(Astute critics of this crude voter influence metric will be quick to point out that it completely ignores the reality of \
                                “battleground states,” which Wyoming isn't but Colorado arguably is. The Electoral College's “winner take all” implementation, \
                                and the safe-state vs swing-state electioneering it engenders, tends to overshadow nibbling irritatants like small-state bias, \
                                but stick with me — the applications of this crude Voter Weight metric might surprise you.)")
                            ]),
                            html.Br(),
                            html.H4("As the framers intended"),
                            html.P(className="card-text", children=[
                                "In the present-day political balance, rural states (like Wyoming) benefitting from small-state bias tend to lean conservative, adding \
                                an air of political urgency to recent grievances against this electoral wrinkle. But the influence boost for states with smaller \
                                populations has been part of the Electoral College since its inception, and suffice to say this was not its most controversial piece. \
                                From its genesis during the Constitutional Convention, each state’s apportionment in the Electoral College was based on two things:",
                                html.Ol(children=[
                                    html.Li("the same hybrid of flat (Senate) + proportional (House) representation that was the basis of the bicameral Great \
                                        Compromise - aka “small-state bias”"),
                                    html.Li("the infamous “Three-fifths Compromise” that rewarded white property-owning male voters in slave states with increased \
                                        congressional representation (and electoral vote allocation) in direct proportion to the size of their enslaved populations \
                                        - aka “slave-state bias”")
                                ])
                            ]),
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
                    ])                  
                ]),
                dbc.Col(md=6, children=[
                    html.Br(),
                    dcc.Slider(
                        id="small-state-bias-year-input",
                        className="text-white",
                        min=2000,
                        max=2020,
                        step=None,
                        marks={
                            int(y): {'label': str(y), 'style': {'transform': 'rotate(45deg)', 'color': 'white'}}
                            for y in data_obj.all_years if y >= 2000
                        },
                        value=2020,
                    ),
                    html.Br(),
                    dcc.Graph(id="fig-bar-small-state-bias"),
                    html.P(className="card-text", style={"padding": "5px"}, children=[
                        html.Small("Figure 1: Small-state bias, shown by color-shading states according to Electoral College votes, then listing them in \
                            descending order by Voter Weight."),
                    ]),
                    html.Br(),
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.P(className="card-text", style={"font-style": "italic"}, children=[
                                "The figure above, the figures below, and every other figure in this publication use presidential election data accessible via this ",
                                dcc.Link("Wikipedia portal", href="https://en.wikipedia.org/wiki/List_of_United_States_presidential_election_results_by_state", 
                                target="_blank"), ". A consolidated version of that data (what I’m using to power this website) is available in csv format in the ",
                                dcc.Link("data/ directory", href="https://github.com/dannynoonan/electoralytics/tree/master/data", target="_blank"), " of the ",
                                dcc.Link("electoralytics repo", href="https://github.com/dannynoonan/electoralytics", target="_blank"), " on github."
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
                            html.H4("Slave state bias"),
                            html.P(className="card-text", children=[
                                "Sticking with the same “Voter Weight” calculation above, but turning the clock back 160 years, we encounter the infamous slave-state \
                                bias in ", html.B("Figure 2"), ". I’ve added new color shading to states in this second bar plot, using each state’s relationship to \
                                slavery as a grouping heuristic. For small states I’ve also carried forward color shading based on state size."
                            ]),
                            html.P(className="card-text", children=[
                                "Highlighting an example: If Voter Weight in 1852 was 2.24 in Alabama (9 Electoral College votes) compared with 0.78 in Illinois \
                                (11 Electoral College votes), that means pound-for-pound it would take ~3 votes cast in Illinois to equal the influence of a \
                                single vote cast in Alabama. States benefitting from the small-state boost, whether free states or slave states, still rise to \
                                the top of the Voter Weight rankings, but since the larger slave states send more electors to the Electoral College the magnitude \
                                of slave-state bias has measurably greater impact overall."
                            ]),
                            html.P(className="card-text", children=[
                                html.B("Figure 3"), " rearranges the data from Figure 2 into a scatter plot, crossing each state's Popular Vote (x axis) with its Electoral \
                                College votes (y axis). The intersection between the axes where Voter Weight = 1.0 is plotted as a diagonal line signifying the \
                                nationwide mean. If every vote in every state counted equally, every state’s dot would be directly on top of that nationwide mean \
                                line. To the extent that some state’s voters have greater impact than others (through favorable Electoral College apportionment, \
                                depressed turnout, etc), states whose dots appear above and to the left of the median line have greater impact, while states whose \
                                dots appear below and to the right of the median line have less."
                            ]),
                            html.P(className="card-text", children=[
                                html.B("Figure 4"), " displays each state's group affiliation on a map. All three figures are controlled using the same Year selection \
                                slider below."
                            ])
                        ])
                    ]),
                    html.Br(),html.Br(),
                    dcc.Slider(
                        id="slave-state-bias-year-input",
                        min=1840,
                        max=1860,
                        step=None,
                        marks={
                            int(y): {'label': str(y), 'style': {'transform': 'rotate(45deg)', 'color': 'white'}}
                            for y in data_obj.all_years if y >= 1840 and y <= 1860
                        },
                        value=1852,
                    ),
                    html.Br(),
                    dcc.Graph(id="fig-bar-slave-state-bias"),
                    html.P(className="card-text", style={"padding": "5px"}, children=[
                        html.Small("Figure 2: Slave-state bias, shown by color-shading states into Free, Slave, and Small groupings, then listing them in \
                            descending order by Voter Weight. Voter Weights are higher in slave states than free states, with small states still having some \
                            of the highest weights."),
                    ]),
                ]),
                dbc.Col(md=6, children=[
                    dcc.Graph(id="fig-scatter-dots-slave-state-bias"),
                    html.P(className="card-text", style={"padding": "5px"}, children=[
                        html.Small("Figure 3: Slave-state bias, shown by color-shading states into Free, Slave, and Small groupings, and plotting Popular Vote \
                            (turnout) on the x axis against Electoral College Votes on the y axis. The average Popular Vote tally per Electoral College vote — \
                            that is, the intersection between the axes where the Voter Weight ratio is 1.0 — is plotted as a diagonal line signifying the \
                            nationwide mean. States whose dots appear above and to the left of the nationwide mean line have Voter Weights greater than 1, those \
                            whose dots are below and to the right have Voter Weights less than 1."),
                    ]),
                    html.Br(),
                    dcc.Graph(id="fig-map-slave-state-bias"),
                    html.P(className="card-text", style={"padding": "5px"}, children=[
                        html.Small("Figure 4: Reference map illustrating which states fit into which group. Areas lacking color shading or hover data \
                            are states that haven’t been admitted to the Union yet."),
                    ]),
                    html.Br(),
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([                           
                            html.H4("Voter Weight"),
                            html.Img(style={"float": "right", "padding-right": "10px"}, src="/static/voteWeightEquations.png", width="400"),
                            html.P(className="card-text", children=[
                                "Despite small-state bias and slave-state bias deriving from different legal statutes and census formulas, I’ve applied the same \
                                “Voter Weight” calculation to illustrate each in the figures above. Check out the ", dcc.Link("Calculating Voter Weight",
                                href="/voter-weight-calculation"), " section for a detailed breakdown of the math behind this metric, but a couple top line \
                                observations for now:",
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
                            html.H4("Voter suppression as a “five-fifths” scheme"),
                            html.P(className="card-text", children=[
                                "Here’s where things get interesting. Shortly before last November’s election, an episode of ", html.I("NPR’s Throughline"), 
                                " made a case I’d never considered before, connecting the lingering effects of the three-fifths compromise to attitudes toward \
                                enfranchisement in the post-war South. The hosts, joined by Yale Professor and noted constitutional scholar Akhil Reed Amar, \
                                argued that although the three-fifths compromise did ", html.I("technically"), " end with the abolition of slavery, it was \
                                effectively replaced by an even ", html.I("less"), " equitable permutation of that infamous inaugural Electoral College bias. \
                                Part of their “(mis)Representative Democracy” series, the full episode is 58 minutes, but this ", 
                                dcc.Link("5-minute video snippet", href="https://www.npr.org/2020/09/30/918717270/the-electoral-college", target="_blank"), 
                                " gets to the heart of what caught my attention:"
                            ]),
                            html.Iframe(id="jw_embed", width="750", height="423", 
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
                                grandfather clauses, as well as more direct intimidation and violence for 90-odd years during the Jim Crow era is (a) fucking insane, \
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
                                "Considering all our 21st century grumbling about how small-state bias amplifies the voice of an Alaska voter at the expense of a \
                                California voter, and the stomach-churning 18th-19th century slave-state bias which amplified the voice of a Virginia slave-owner \
                                relative to a New York merchant, I was pretty darn curious how this third category of electoral bias during Jim Crow — let’s call it \
                                “suppression-state bias” — would stack up against those other two."
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
                                slave state, or their political alliance (and military defeat) as part of the Confederacy. In a sense, the Border states function as \
                                a control group for examining that question."
                            ]),
                            html.P(className="card-text", children=[
                                "With that in mind, I grouped states into Union (free), Confederate (slave), and Border (slave-Union) state groups, using the familiar \
                                blue and butternut uniform colors to identify the first two. I also retained the “Small” group used above, and added a “Postbellum” \
                                group for states admitted to the Union after the Civil War."
                            ]),
                            html.P(className="card-text", children=[
                                "Maps and more details about these “Civil War” groupings as well as alternative “Regional Census” groupings are in the ", 
                                dcc.Link("Explanation of Groupings", href="/explanation-of-groupings"), " section."
                            ]),
                        ])
                    ]),
                    html.Br(),html.Br(),
                    dcc.Graph(id="fig-scatter-bubbles-suppress-state-bias"),
                    html.P(className="card-text", style={"padding": "5px"}, children=[
                        html.Small("Figure 7: Suppression-state bias, shown by color-shading states by Civil War groupings, and plotting Electoral College votes on \
                            the x axis against derived Voter Weight on the y axis, with Popular Vote now represented by the size of each state’s “bubble.” The \
                            national mean is plotted at all points on the x axis where Voter Weight is 1.0 on the y axis, and any bubble above the mean line indicates \
                            a state whose voters — that is, those who were able to vote — wielded disproportionately high Voter Weight in that election. For small \
                            bubbles with low EC vote counts, high Voter Weight can be explained by small-state bias. For larger bubbles, we are looking at \
                            suppression-state bias."),
                    ]),
                    html.Br(),
                    dcc.Graph(id="fig-map-suppress-state-bias"),
                    html.P(className="card-text", style={"padding": "5px"}, children=[
                        html.Small("Figure 9: Reference map illustrating which states fit into which group. Areas lacking color shading or hover data are states \
                            that haven’t been admitted to the Union yet."),
                    ]),
                    html.Br(),
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.H4("Five-fifths and then some"),
                            html.P(className="card-text", children=[
                                "If the range of Voter Weights seems more extreme in this era than it did in the other two time periods, that’s because it is. \
                                Highlighting just one example: If Voter Weight in 1940 was 7.5 in South Carolina compared with 0.96 in Connecticut, that means \
                                pound-for-pound it would take 7-8 votes cast in Connecticut to equal the influence of a single vote cast in South Carolina. This \
                                represents a staggering disparity in the influence of individual voters—that is, those permitted to vote—in these states."
                            ]),
                            html.P(className="card-text", children=[
                                "Absent the factors of state size (both state’s populations earned them 8 Electoral College votes) or slavery (abolished a full 75 \
                                years prior) the bias revealed in this bar graph has no explanation in Electoral apportionment “originalist” logic. Nothing accounts \
                                for this disparity other than staggering differences in voter participation, almost certainly tied to massive institutional voter \
                                suppression."
                            ]),
                        ])
                    ])
                ]),
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.H4("Suppression-state visualizations"),
                            html.P(className="card-text", children=[
                                html.B("Figures 6, 8, and 9"), " use the same background axes and maps from above to generate and render Voter Weight data during \
                                the Jim Crow era, using Civil War groupings."
                            ]),
                            html.P(className="card-text", children=[
                                html.B("Figure 7"), " plots each state’s Electoral College votes on the x axis and its derived Voter Weight on the y axis, with \
                                Popular Vote now represented by the size of each state’s “bubble.” The horizontal line at 1.0 on the y axis corresponds to the \
                                national mean. The higher a bubble is above the mean, the greater the weight of individual votes cast in that state. For those \
                                states whose Electoral Vote counts (x values) and Popular Votes (bubble sizes) are very low, a high Voter Weight can be explained \
                                by small-state bias. For the rest, another bias is at play."
                            ]),
                        ])
                    ]),
                    html.Br(),
                    dcc.Graph(id="fig-scatter-dots-suppress-state-bias"),
                    html.P(className="card-text", style={"padding": "5px"}, children=[
                        html.Small("Figure 6: Suppression-state bias, shown by color-shading states by Civil War groupings, and plotting Popular Vote (turnout) on \
                            the x axis against Electoral College Votes on the y axis. The average Popular Vote tally per Electoral College vote (where the Voter \
                            Weight ratio is 1.0) is plotted as a diagonal line signifying the nationwide mean. States whose dots appear above and to the left of the \
                            nationwide mean line have Voter Weights greater than 1, those whose dots are below and to the right have Voter Weights less than 1."),
                    ]),
                    html.Br(),
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
                        html.Small("Figure 8: Suppression-state bias, shown by color-shading states by Civil War groupings, then listing them in descending order \
                            by Voter Weight. Voter Weights are generally higher in former Confederate states than in Union, Border, or Postbellum states, with \
                            small states still having some of the highest weights."),
                    ]),
                ])
            ]),
            html.Br(),
            html.Hr(className="border-light"),
            html.Br(),
            dbc.Row([
                dbc.Col(md=5, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.H4("Old story, new angle"),
                            html.P(className="card-text", children=[
                                "Depending on your familiarity with racial voter suppression in the century following the Civil War, you may or may not be surprised \
                                that the small-state and slave-state biases mathematically-prescribed in the Constitution—that is, the apportionment imbalances that \
                                have made it onto every AP American History exam since the arrival of the Number 2 pencil—might in fact pale in comparison to other \
                                permutations of sustained, systemic electoral inequity."
                            ]),
                            html.P(className="card-text", children=[
                                "The bigger story here, of course, isn’t that Southern states’ (white) voters counted for more than Northern and Western states’ \
                                (predominantly white) voters, it’s that hundreds of thousands of Southern Blacks (and poor whites) were prevented from voting \
                                altogether, through the uneven application of poll taxes, literacy tests, grandfather clauses, as well as more direct intimidation \
                                and violence for 90-odd years during the Jim Crow era."
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
                            html.Br(),
                            html.H4("Zooming out to zoom in"),
                            html.P(className="card-text", children=[
                                "Regardless of underlying plans or purpose, this disconnect between census population and voter participation is seared into the \
                                historical record, offering a way to compare and quantify democratic and anti-democratic behavior over time - and to potentially \
                                infer correlation or causation between specific external factors and Voter Weight trends."
                            ]),
                            html.P(className="card-text", children=[
                                "This ", dcc.Link("annotated line-chart timeline", href="/voter-weight-timeline-viz"), " of state- and group-level Voter \
                                Weights stretching from 1800 to 2020 attempts to mix a (very thin) layer of historical context in with the full gamut of Voter \
                                Weight data. It’s a lot to absorb, but it’s configurable, so strip it down to the studs and build it back up however you’d like, \
                                comparing any combination of states or groups over any time period you’d like to zoom in on."
                            ]),
                            html.P(className="card-text", children=[
                                "Other electoralytics resources to drill into:",
                                html.Li(children=[dcc.Link("How Voter Weight is calculated", href="/voter-weight-calculation")]), 
                                html.Li(children=[dcc.Link("How the state groupings break down", href="/explanation-of-groupings")]), 
                                html.Li(children=[dcc.Link("The full vault of year-by-year data visualizations", href="/voter-weight-figure-vault")]),
                                html.Li(children=[dcc.Link("Discussion and Conclusion", href="/voter-weight-conclusions")]),
                            ])
                        ])
                    ])
                ]),
                dbc.Col(md=7, children=[
                    dcc.Slider(
                        id="map-color-by-vw-year-input",
                        min=1800,
                        max=2020,
                        step=None,
                        marks={
                            int(y): {'label': str(y), 'style': {'transform': 'rotate(45deg)', 'color': 'white'}}
                            for y in data_obj.all_years 
                        },
                        value=1960,
                    ),
                    html.Br(),
                    dcc.Graph(id="fig-map-color-by-vw"),
                    html.P(className="card-text", style={"padding": "5px"}, children=[
                        html.Small(children=["Figure 10: States color-shaded by Voter Weight, over the course of 56 presidential elections between 1800 and 2020. Control \
                            the year using the slider above, or open an ", dcc.Link("intractive slideshow animation", className="text-white",
                            href="https://htmlpreview.github.io/?https://github.com/dannynoonan/electoralytics/blob/master/html_figures/anim_map_state_vw_acw4_1000.html",
                            target="_blank"), " illustrating the full history."]),
                    ]),
                ]),
            ])
        ])
    ])
])