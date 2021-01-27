import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash_pages.components import navbar


content = html.Div([
    navbar,
    dbc.Card(className="bg-success", children=[
        dbc.CardBody([
            html.Br(),
            dbc.Row(className="text-white", justify="center", align="center", children=[
                html.H3("Visualizing Jim Crow Voter Suppression: Discussion & Conclusions"),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.H4("Passing the eye test", className="card-title"),
                            html.P(className="card-text", children=[
                                "Being neither a historian nor a statistician, there probably isn’t much I should presume to “conclude” from these data \
                                visualizations. My idea here was to use some new tech to breathe life into a data set, try to validate a surprising claim \
                                I’d heard on a podcast, and ultimately see if visualizing the data would point to any other conclusions, effectively \
                                letting it tell its own story."
                            ]),
                            html.P(className="card-text", children=[
                                "And sure enough: the slave-state bias is plain to see in the would-be Confederate (and Border) states up till the Civil \
                                War, the small-state bias is plain to see all the way from the founding to the present, and what I’m calling a \
                                suppression-state bias is plain to see during the period between the end of Reconstruction in 1877 and the passage of the \
                                Voting Rights Act in 1965."
                            ]),
                            html.P(className="card-text", children=[
                                "In the two decades following Reconstruction, the voter suppression effect in former Confederate states appears to have \
                                ticked up to levels matching the antebellum Voter Weight status quo, followed by a period of significant amplification \
                                during the first five decades of the 20th century."
                            ]),
                            html.P(className="card-text", children=[
                                "These aren’t rigorously-defensible scholarly claims, they’re layperson interpretations of a data set that’s much easier \
                                to examine in two-dimensional interactive color than in rows and columns. That said, I’d wager every inflection point in \
                                any of the figures links back to some specific set of historic events, the sort of thing that a historian might look at \
                                and immediately say “oh right — yeah that sudden change in X is probably a side-effect of Y.”"
                            ]),
                            html.Br(),
                            html.H4("A few things that stood out", className="card-title"),
                            html.P(className="card-text", children=[
                                "It’s been interesting pausing to research events and periods along the way, attempting to interpret underlying causes of \
                                twists and turns in the data. Here’s a short list of the many data ripples that I initially mistook for errors, anomalies, \
                                or unexplained distortions:",
                                html.Li("the impact of the “Mississippi Plan,” a scheme to introduce discriminatory voting language into every Southern \
                                state’s constitution, beginning in 1890"),
                                html.Li("the staggered state-by-state expansion of women’s suffrage in the early 20th century, prior to the 19th \
                                Amendment’s ratification in 1920"),
                                html.Li("the “high watermark” of suppression-state bias in the election of 1924 and its proximity to events like the Tulsa \
                                massacre in 1921 and peak KKK membership in 1924"),
                                html.Li("the erratic differences in popular voter participation from state to state and year to year in the pre-Jacksonian \
                                era, as states experimented with everything from state-wide popular vote to district-level selection to electors being \
                                appointed by legislatures"),
                                html.Li("the cyclical effect of the decennial census and of EC reapportionment catching up to population swells"),
                                html.Li("a 120-year uninterrupted streak where Midwestern states appear to have been more democratic than their \
                                Northeastern neighbors (toggle to the “Regional Census” groupings on the electoralytics site to see)"),
                            ]),
                            html.Br(),
                            html.H4("Border states", className="card-title"),
                            html.P(className="card-text", children=[
                                "Earlier I described my reasoning for creating a Border state group, consisting of slave states that had stayed in the \
                                Union rather than seceding to join the Confederacy. The idea was that this might serve as a control group, for determining \
                                which factor was more predictive of a state’s subsequent embrace of voter suppression tactics: (a) its relationship to \
                                slavery prior to the war, or (b) the side it had fought with in the war."
                            ]),
                            html.P(className="card-text", children=[
                                "At the moment, my knowledge of Reconstruction, Redemption, Reconciliation, and Jim Crow is almost entirely limited to a \
                                North vs South narrative, excluding the details of Border and Western states. ", html.I("That said:"), " knowing little to \
                                nothing of the ", html.I("details"), " of post-Reconstruction enfranchisement practices in Border states, it sure looks to \
                                me as though those practices led to much higher voter participation (and, by inverse relationship, lower influence of \
                                individual voters) than that of other slave states that had fought with the Confederacy."
                            ]),
                            html.P(className="card-text", children=[
                                "From the 40,000’ view enabled by these data visualizations, post-war voter turnout in Union-loyal former-slave states \
                                appears almost indistinguishable from voter participation in Union-loyal free states. I’d be reaching way out of my lane to \
                                interpret this here, but suffice to say I think this has fascinating implications."
                            ]),
                            html.P(className="card-text", children=[
                                "One final comment, with respect to demographics. It’s true that, when the Civil War began, Union-loyal Border states like \
                                Kentucky, Maryland, and Missouri had somewhat fewer slaves per capita than their Confederate counterparts to the south. But \
                                these were not anecdotally slave “ish” states: more than 425K Blacks were enslaved in these three states per the ",
                                dcc.Link("1860 census", href="https://www.census.gov/history/pdf/ApportionmentInformation-1860Census.pdf", target="_blank"), 
                                "."
                            ]),
                            html.P(className="card-text", children=[
                                "In absolute terms, Kentucky had more people enslaved than Texas, Missouri had more slaves than Arkansas, and Maryland had \
                                more slaves than Florida. Yet the differences in the voter enfranchisement practices in these states a full 100 years after \
                                the abolition of slavery couldn’t be more stark. Post-Reconstruction voter disenfranchisement seems to have had less to do \
                                with a state’s connection to slavery than to the side it fought with in the Civil War."
                            ]),
                        ]),
                    ]),
                ]),
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.H4("Other interpretations of Voter Weight trends and Electoral College bias", className="card-title"),
                            html.P(className="card-text", children=[
                                "To avoid wrapping every comment in a caveat, I’ve been fairly loose in my pronouncements that higher Voter Weights correlate \
                                to higher levels of voter suppression, so I wanted to rattle off a few things that most certainly also have an effect on a \
                                state’s Voter Weight metric:",
                                html.Li("Voter apathy, and hence lower voter participation. Since the “solid south” of the early 20th century was effectively \
                                    a non-competitive one-party regional bloc (in part due to voter suppression), the fact that down-ballot winners were a \
                                    foregone conclusion may have further depressed turnout"),
                                html.Li("Other eligibility factors such as age, gender, incarceration status, felony record, etc vary from state to state"),
                                html.Li("Census apportionment is decennial, so EC influence always lags a few years behind a population explosion, lowering \
                                    the Voter Weight in fast-growing states near the end of the decade"),
                                html.Li("Census apportionment in states with a higher percentage of undocumented residents who can’t legally vote increases \
                                    Voter Weight in that state (generally regarded as to the benefit, not the detriment, of those who are tabulated but not \
                                    enfranchised, but a five-fifths type effect nonetheless)"),
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
                                precinct-targeted voter roll purges, etc etc, and (b) the Supreme Court’s recent meddling in the Voting Rights Act of 1965 in \
                                2013’s ", html.I("Shelby County v. Holder"), " ruling actually presents a very real threat to the durability of positive \
                                historical trends."
                            ]),
                            html.P(className="card-text", children=[
                                "Although my quasi-scientific 40,000’ view of historical Voter Weight doesn’t show any obvious reversal of aggregate positive \
                                trends in 2016 or 2020 (again: not an actual statistician, I just play one on the internet), it’s worth noting that it took a few \
                                election cycles after Reconstruction for the Redeemer South’s Voter Weight metric to tick back up to pre-war levels - only to \
                                wildly exceed that antebellum status quo a generation later."
                            ]),
                            html.P(className="card-text", children=[
                                "Moreover, if there’s a lesson I’ve gleaned from reading about the Electoral College and racial justice history, it’s that \
                                familiar old discriminatory policies tend to continually reinvent themselves, often using familiar old tricks wrapped in thinly \
                                veiled language. And as long as the inherent asymmetry between population and participation leave the Electoral College \
                                vulnerable to manipulation, people are going to exploit it to increase their influence at the expense of others, promulgating \
                                stories about why the imbalance is justified (even patriotic, “as the framers intended,” etc)."
                            ]),
                            html.P(className="card-text", children=[
                                "And as long as the lights remain on in the twisted halls of white supremacy — and oh boy do they seem to be on right now — \
                                there will be attempts to disenfranchise based on race, ranging from the subtle to the obvious, the innovative to the familiar. \
                                As antiquated an institution as the Electoral College is, as many tricks as have already been tried, past methods of manipulation \
                                should always be viewed as prologue to future attempts."
                            ]),
                        ])
                    ])
                ])
            ])
        ])
    ])
])