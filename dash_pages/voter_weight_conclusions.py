import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash_pages.components import navbar


content = html.Div([
    navbar,
    dbc.Card(className="bg-success", children=[
        dbc.CardBody([
            html.Div(children=[
                html.Ul(className="pagination pagination-lg justify-content-center", children=[
                    html.Li(className="page-item flex", style={"width": "50%"}, children=[
                        html.A(className="page-link", href="/voter-weight-electoral-college-bias-page3", children=[
                            "← Part 3: Reconstruction, Redemption, and suppression-state bias"
                        ])
                    ]),
                    html.Li(className="page-item flex", style={"width": "20%"}),
                    html.Li(className="page-item flex", style={"width": "50%", "text-align": "right"}, children=[
                        html.A(className="page-link", href="/voter-weight-calculation", children=[
                            "Appendix 1: Calculating Voter Weight →"
                        ])
                    ]),
                ])
            ]),
            html.Hr(className="border-light"),
            html.Br(),
            dbc.Row(className="text-white", justify="center", align="center", children=[
                html.H3("Part 4: Conclusions and Discussion"),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.Div(className="card-text", style={"margin-left": "50px", "margin-right": "50px", "font-size": "13pt"}, children=[
                                html.P(style={"font-style": "italic"}, children=[
                                    "By 1890 the disenfranchisement of African-Americans was well underway, and by the early years of the twentieth century it was \
                                    complete.", dcc.Link(href="/sources-notes", children=[html.Sup("18")]),
                                ]),
                                html.P(children=["—Alexander Keyssar, ", html.I("“Why Do We Still Have the Electoral College?”")])
                            ]),
                            html.Br(),
                            html.Div(className="card-text", style={"margin-left": "50px", "margin-right": "50px", "font-size": "13pt"}, children=[
                                html.P(style={"font-style": "italic"}, children=[
                                    "By the 1940s… registration among voting-age Black citizens hovered around 3 percent… In the 11 Presidential elections held \
                                    between 1908 and 1948, 44 percent of all minority votes in the country were not represented by a single electoral vote.",
                                    dcc.Link(href="/sources-notes", children=[html.Sup("19")]),
                                ]),
                                html.P(children=["—Jesse Wegman, ", html.I("“Let the People Pick the President”")])
                            ]),
                            html.Br(),
                            html.H4("Old story, new angle"),
                            html.Img(src="/static/stockImages/voter-intimidation-1876.jpg", style={"float": "right", "padding-left": "10px"}, width="50%"),
                            html.P(className="card-text", children=[
                                "Depending on your familiarity with racial voter suppression in the century following the Civil War, you may or may not be surprised \
                                that the small-state and slave-state biases mathematically-prescribed in the Constitution—that is, the apportionment imbalances that \
                                have made it onto every AP American History exam since the arrival of the Number 2 pencil—might in fact pale in comparison to other \
                                permutations of sustained, systemic electoral inequity."
                            ]),
                            html.P(className="card-text", children=[
                                "The bigger story here, of course, isn’t that Southern states’ (white) voters counted for more than Northern and Western states’ \
                                (predominantly white) voters. The bigger story is that hundreds of thousands of Southern Blacks were prevented from voting \
                                altogether, through the uneven application of poll taxes, literacy tests, grandfather clauses, as well as more direct intimidation \
                                and violence for 90-odd years during the Jim Crow era."
                            ]),
                            html.P(className="card-text", children=[
                                "However, these graphs illustrate that the villainous cackling of turn-of-the-century Southern racist political scheming didn’t \
                                simply end with racial disenfranchisement. Under an Electoral College system that grants influence based on population rather than \
                                participation, voter suppression has a corollary effect — and another perverse incentive — at the national level: it amplifies \
                                precisely those voices responsible for suppressing their local voter turnout, relative to the voices of voters in states not \
                                engaged in systemic voter suppression."
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
                            html.P(className="card-text", children=[
                                "Regardless of underlying intent, the disconnect between census population and voter participation is seared into the historical \
                                record, offering a way to compare and quantify democratic and anti-democratic behavior over time - and to potentially infer \
                                correlation or causation between specific external factors and Voter Weight trends."
                            ]),
                            html.Br(),
                            html.H4("Passing the eye test", className="card-title"),
                            html.P(className="card-text", children=[
                                "Being neither a historian nor a statistician, there probably isn’t much I should presume to “conclude” from this \
                                assortment of data visualizations. As a software engineer (with a budding interest in racial justice history) my idea \
                                here was to use some new tech to breathe life into an old data set, try to validate a surprising claim I’d heard on a \
                                podcast, and ultimately see if visualizing the data would point to any other conclusions, effectively letting it tell \
                                its own story."
                            ]),
                            html.P(className="card-text", children=[
                                "And sure enough: the slave-state bias is plain to see in the slave states leading up to the Civil War, the small-state \
                                bias is plain to see all the way from the founding to the present, and what I’m calling a suppression-state bias is \
                                plain to see during the period between the end of Reconstruction in 1877 and the passage of the Voting Rights Act in 1965."
                            ]),
                            html.P(className="card-text", children=[
                                "In the two decades following Reconstruction, the voter suppression effect in former Confederate states appears to have \
                                ticked up to levels matching the antebellum hyper-enfranchisement status quo, followed by a period of ", 
                                html.I("significant"), " amplification during the first five decades of the 20th century."
                            ]),
                            html.P(className="card-text", children=[
                                "These aren’t rigorously-defensible scholarly claims, they’re layperson interpretations of a data set that’s much easier \
                                to examine in two-dimensional interactive color than in rows and columns. Nonetheless, I’d wager many of the inflection \
                                points in the figures links back to some specific set of historic events, the sort of thing that a historian might look at \
                                and immediately say “oh right — yeah that sudden change in X could easily be a side-effect of Y.”"
                            ]),
                            html.Br(),
                            html.H4("A few things that stood out", className="card-title"),
                            html.P(className="card-text", children=[
                                "It’s been interesting pausing to research events and periods along the way, attempting to interpret underlying causes of \
                                twists and turns in the data. Here’s a short list of the many data ripples that I initially mistook for errors, anomalies, \
                                or unexplained distortions:",
                                html.Ul([
                                    html.Li("The impact of the “Mississippi Plan,” a scheme to introduce discriminatory voting language into every Southern \
                                    state’s constitution, beginning in the 1890s"),
                                    html.Li("The staggered state-by-state expansion of women’s suffrage (and therefore voter turnout overall) in the early \
                                    20th century, prior to the 19th Amendment’s ratification enfranchising women in every state in 1920"),
                                    html.Li("The “high watermark” of suppression-state bias in the election of 1924 and its proximity to events like the \
                                    Tulsa Race Massacre in 1921, peak KKK membership in 1924, and the segregationist presidency of Woodrow Wilson"),
                                    html.Li("The erratic differences in popular voter participation from state to state and year to year in the pre-Jacksonian \
                                    era, as states experimented with everything from state-wide popular vote to district-level selection to electors being \
                                    appointed by legislatures"),
                                    html.Li("The cyclical effect of the decennial census and of Electoral College reapportionment catching up to population \
                                    swells"),
                                    html.Li("A curious 120-year uninterrupted streak where Midwestern states appear to have been more democratic than their \
                                    Northeastern neighbors (toggle to the “Regional Census” groupings to see, it still has me baffled)"),
                                ]),
                            ]),
                            html.Br(),
                            html.H4("Other interpretations of Voter Weight trends and Electoral College bias", className="card-title"),
                            html.P(className="card-text", children=[
                                "To avoid wrapping every comment in a caveat, I’ve been fairly loose in my pronouncements that hyper-enfranchisement correlates \
                                to higher levels of voter suppression, so I wanted to rattle off a few things that most certainly also have an effect on a \
                                state’s Voter Weight metric:",
                                html.Ul([
                                    html.Li("Voter apathy, and hence lower voter participation. Since the “solid south” of the early 20th century was effectively \
                                        a non-competitive one-party regional bloc (in part due to the wild success of their voter suppression tactics), the fact \
                                        that down-ballot winners were a foregone conclusion may have further depressed turnout"),
                                    html.Li("Other eligibility factors such as age, gender, incarceration status, felony record, etc vary from state to state"),
                                    html.Li("Census apportionment is decennial, so Electoral College influence always lags a few years behind a population \
                                        explosion, lowering the Voter Weight in fast-growing states near the end of the decade"),
                                    html.Li("Census apportionment in states with a higher percentage of undocumented residents who can’t legally vote increases \
                                        Voter Weight in that state. This is generally regarded as to the benefit, not the detriment, of those who are tabulated \
                                        but not enfranchised, but this creates a “five-fifths” type effect nonetheless."),
                                ]),
                            ]),
                            html.Br(),
                        ]),
                    ]),
                ]),
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.H4("Border states", className="card-title"),
                            html.P(className="card-text", children=[
                                "Earlier I described my reasoning for creating a Border state group, consisting of slave states that had stayed in the \
                                Union rather than seceding to join the Confederacy. The idea was that this might serve as a control group, for determining \
                                which factor was more predictive of a state’s subsequent embrace of voter suppression tactics: (a) its relationship to \
                                slavery prior to the war, or (b) the side it had fought with in the war."
                            ]),
                            html.P(className="card-text", children=[
                                "At the moment, my knowledge of Reconstruction, Redemption, Reconciliation, and Jim Crow is almost entirely limited to a \
                                North vs South narrative, excluding the details of Border and Western states. Caveats aside: knowing little to nothing of \
                                the ", html.I("details"), " of post-Reconstruction enfranchisement practices in Border states, it sure looks to me as \
                                though those practices led to much higher voter participation (and, by inverse relationship, little to no \
                                hyper-enfranchisement of individual voters) than that of Confederate slave states."
                            ]),
                            html.P(className="card-text", children=[
                                "In fact, from the 40,000’ view enabled by these data visualizations, post-war voter turnout in Union-loyal former-slave \
                                states appears almost indistinguishable from voter participation in Union-loyal free states. I’d be reaching way out of my \
                                lane to interpret this here, but suffice to say I think this has fascinating implications."
                            ]),
                            html.P(className="card-text", children=[
                                "One last thought, with respect to demographics. It’s true that, when the Civil War began, Union-loyal Border states like \
                                Kentucky, Maryland, and Missouri had somewhat fewer slaves per capita than their Confederate counterparts to the south. But \
                                these were not anecdotally slave “ish” states: more than 425K Blacks were enslaved in these three states per the ",
                                dcc.Link("1860 census", href="https://www.census.gov/history/pdf/ApportionmentInformation-1860Census.pdf", target="_blank"), 
                                "."
                            ]),
                            html.P(className="card-text", children=[
                                "In absolute terms, Kentucky had more people enslaved than Texas, Missouri had more slaves than Arkansas, and Maryland had \
                                more slaves than Florida. Yet the differences in the voter enfranchisement practices in these states a full 100 years after \
                                the abolition of slavery couldn’t be more stark."
                            ]),
                            html.P(className="card-text", children=[
                                html.B("Bottom line:"), html.I(" Post-Reconstruction voter disenfranchisement seems to have had less to do with a state’s historic connection to \
                                slavery than to the side it fought with in the Civil War."),
                            ]),
                            html.Br(),
                            html.H4("The Voting Rights Act of 1965", className="card-title"),
                            html.P(className="card-text", children=[
                                "I wanted to acknowledge an aspect of the historical data that I’ve danced around so far, but that’s hard to miss the longer \
                                you spend interacting with it. Since passage of the Voting Right Acts in 1965, it would appear that voter participation in \
                                presidential elections in the slow-to-be-Reconstructed South has improved to the point where it’s effectively indistinguishable \
                                from voter participation nationwide."
                            ]),
                            html.P(className="card-text", children=[
                                "Needless to say, this was not part of what I was digging for. And while I certainly don’t mean to imply that voter \
                                disenfranchisement is “solved,” it is sort of incredible to see the impact that the activism, legislation, and court rulings of \
                                the Civil Rights era ultimately had in carving out such a clear, positive voter participation trend against a 220 year \
                                historical backdrop steeped in layers of inequity."
                            ]),
                            html.P(className="card-text", children=[
                                "THAT SAID... anybody who’s intently focused on present-day voting rights issues will be quick to point out that (a) omg there’s \
                                hella disenfranchisement out there today, worse than ever with regards to felons, voter ID laws, overzealous signature matching, \
                                precinct-targeted voter roll purges, etc etc, and (b) the Supreme Court’s recent 2013 meddling in the Voting Rights Act of 1965 \
                                vis-à-vis their ", html.I("Shelby County v. Holder"), " ruling actually presents a very real threat to the durability of positive \
                                historical trends."
                            ]),
                            html.P(className="card-text", children=[
                                "Although my quasi-scientific 40,000’ view of historical Voter Weight doesn’t show any obvious reversal of aggregate positive \
                                trends in 2016 or 2020 (again: not an actual statistician, I just play one on the internet), it’s worth noting that it took a few \
                                election cycles after Reconstruction for the Redeemer South’s suppression strategies to translate into pre-war \
                                hyper-enfranchisement levels — only to wildly exceed that antebellum status quo over the course of several generations to follow."
                            ]),
                            html.P(className="card-text", children=[
                                "Moreover, if there’s a lesson I’ve gleaned from reading about the Electoral College and racial justice history, it’s that \
                                familiar old discriminatory policies tend to continually reinvent themselves, often using familiar old tricks wrapped in thinly \
                                veiled language. And as long as the inherent asymmetry between population and participation leave the Electoral College \
                                vulnerable to manipulation, people are going to exploit it to increase their influence at the expense of others, promulgating \
                                stories about why the imbalance is justified — even patriotic, “as the framers intended,” etc."
                            ]),
                            html.P(className="card-text", children=[
                                "And as long as the lights remain on in the twisted halls of white supremacy — and oh boy do they seem to be on right now — \
                                there will be attempts to disenfranchise based on race, ranging from the subtle to the obvious, the innovative to the familiar. \
                                As antiquated an institution as the Electoral College is, as many tricks as have already been tried, past methods of manipulation \
                                should always be viewed as prologue to future attempts."
                            ]),
                            html.Br(),
                            html.H4("Hyper-enfranchisement: Implications and interpretation", className="card-title"),
                            html.P(className="card-text", children=[
                                "The three-fifths compromise, that infamously dehumanizing fraction baked into the Constitution, would have been worse for the \
                                plight of slaves if it had been five-fifths. This was actually what Southern slave-owners wanted: fully-counted slaves whose census \
                                tabulation would result in greater congressional and Electoral College influence for Southern states, i.e. Southern white voters and \
                                the institution of slavery."
                            ]),
                            html.P(className="card-text", children=[
                                "After slavery was abolished and a dozen hopeful years of Reconstruction had fizzled out, the Southern white dream of fully-counted \
                                yet disenfranchised Blacks was finally realized, via Jim Crow voter suppression. The paradoxical interaction between citizenship \
                                status, representational apportionment, and voter participation converged to enable a level of Electoral College manipulation almost \
                                unfathomable in its scale. The result was that even more political influence was siphoned from the toil of freed Black citizens into \
                                the ballots of Southern whites than had previously been siphoned from Black slaves. This latter period of five-fifths \
                                hyper-enfranchisement under Jim Crow lasted roughly 90 years, compared to not quite 80 years of three-fifths slavery under the \
                                Constitution."
                            ]),
                            html.P(className="card-text", children=[
                                "From Jesse Wegman’s 2019 book ", html.I("Let the People Pick the President"), ": “[The Fourteenth Amendment] was the official \
                                eradication of the three-fifths clause: if you prevent eligible voters from voting, you don’t get to count them toward your \
                                representation in Congress… That, at any rate, was the hope. As of 2020, Section 2 of the Fourteenth Amendment has never been \
                                enforced.”", dcc.Link(href="/sources-notes", children=[html.Sup("20")]), " Neither the clear suffrage mandate of the Fifteenth Amendment, nor the language tying voter disenfranchisement to reduced \
                                representation in the Fourteenth Amendment, prevented institutionalized Jim Crow voter suppression. The impediments to legal voting \
                                concocted by Southern Redeemers in the wake of Reconstuction went unchallenged for a full century after the Civil War. During the \
                                Jim Crow interim, again quoting Wegman: “One of the great ironies of American history is that the end of slavery actually made \
                                the white power structures in the former slave states stronger.”", dcc.Link(href="/sources-notes", children=[html.Sup("14")]),
                            ]),
                            html.P(className="card-text", children=[
                                "The means by which the staggering electoral imbalances of the pre-war slavery era and the post-war Jim Crow era were perpetuated \
                                have potentially far-reaching implications. How many government programs, pieces of legislation, legal judgments and the like \
                                were cultivated with intent to perpetuate a status quo grounded in Southern whites silencing and extracting political influence from \
                                their Black populations? How many ideologies and narratives, designed to maintain entrenched Southern white interests or linked \
                                to ill-gotten political gains, were amplified and exported to the rest of the country?"
                            ]),
                            html.P(className="card-text", children=[
                                "The ubiquitous embrace of Lost Cause mythology in the early 20th century, the prevalence of Sambo caricatures, the national \
                                expansion of the Georgia-born KKK, the flying of the Confederate flag at events in Northern and Western states in the late 20th \
                                century - these are just the most obvious examples, but it stands to reason that the larger megaphones and greater voting influence \
                                enjoyed by Southern whites at the expense of their Black populations have propagated countless artifacts into the national \
                                character during 200 years of outsized Southern white influence."
                            ]),
                        ])
                    ])
                ])
            ]),
            html.Br(),
            html.Hr(className="border-light"),
            html.Div(children=[
                html.Ul(className="pagination pagination-lg justify-content-center", children=[
                    html.Li(className="page-item flex", style={"width": "50%"}, children=[
                        html.A(className="page-link", href="/voter-weight-electoral-college-bias-page3", children=[
                            "← Part 3: Reconstruction, Redemption, and suppression-state bias"
                        ])
                    ]),
                    html.Li(className="page-item flex", style={"width": "20%"}),
                    html.Li(className="page-item flex", style={"width": "50%", "text-align": "right"}, children=[
                        html.A(className="page-link", href="/voter-weight-calculation", children=[
                            "Appendix 1: Calculating Voter Weight →"
                        ])
                    ]),
                ])
            ]),
        ])
    ])
])