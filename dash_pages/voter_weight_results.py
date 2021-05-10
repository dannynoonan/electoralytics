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
                        html.A(className="page-link", href="/voter-weight-electoral-college-bias-page4", children=[
                            "← Part 4: Suppression-state bias"
                        ])
                    ]),
                    html.Li(className="page-item flex", style={"width": "20%"}),
                    html.Li(className="page-item flex", style={"width": "50%", "text-align": "right"}, children=[
                        html.A(className="page-link", href="/voter-weight-conclusions", children=[
                            "Part 6: Conclusions and interpretation →"
                        ])
                    ]),
                ])
            ]),
            html.Hr(className="border-light"),
            html.Br(),
            dbc.Row(className="text-white", justify="center", align="center", children=[
                html.H3("Part 5: Results and observations"),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.Div(className="card-text", style={"margin-left": "50px", "margin-right": "50px", "font-size": "13pt"}, children=[
                                html.P(style={"font-style": "italic"}, children=[
                                    "By 1890 the disenfranchisement of African-Americans was well underway, and by the early years of the twentieth century it was \
                                    complete.", dcc.Link(href="/sources-notes", children=[html.Sup("22")]),
                                ]),
                                html.P(children=["—Alexander Keyssar, ", html.I("“Why Do We Still Have the Electoral College?”")])
                            ]),
                            html.Br(),
                            html.H4("Old story, new angle"),
                            html.Img(src="/static/stockImages/voter-intimidation-1876.jpg", style={"float": "right", "padding-left": "10px", "padding-top": "5px"}, 
                                width="50%"),
                            html.P(className="card-text", children=[
                                "Depending on your familiarity with racial voter suppression in the decades following the Civil War, you may or may not be surprised \
                                that the small-state and slave-state biases mathematically-prescribed in the Constitution — that is, the apportionment imbalances \
                                that have appeared on AP American History exams since the arrival of the Number 2 pencil — might in fact pale in comparison to other \
                                permutations of sustained, systemic electoral inequity."
                            ]),
                            html.P(className="card-text", children=[
                                "The bigger backstory here, of course, is of the practice and impact of voting discrimination on Black Americans: The uneven \
                                application of poll taxes, the flagrant racial bias in literacy tests and grandfather clauses, and the use of direct violent \
                                intimidation and terror to perpetuate a system of political, social, and economic apartheid in America. The fact that Southern \
                                whites derived greater voting influence at the national level through their sustained discriminatory action at the local level is \
                                merely an anecdotal extension of the broader backstory of Jim Crow."
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
                                plausible nefarious objectives motivated white supremacist voter suppression in the postbellum South is well beyond my purview — \
                                leave that to the historians and social scientists."
                            ]),
                            html.Img(src="/static/stockImages/jimcrow-poll-tax.jpg", style={"float": "left", "padding-right": "10px", "padding-top": "5px"}, 
                                width="45%"),
                            html.P(className="card-text", children=[
                                "Whether a side-effect of racist voter suppression or an intentional strategy unto itself, Southern white elites appear to have not \
                                just maintained, but significantly increased, their disproportionate influence over national-level politics during the Jim Crow \
                                Era. This despite the abolition of slavery, the nullification of the three-fifths compromise, and their total military and \
                                political defeat in the Civil War. And they couldn’t have done it without the Electoral College, since a pure national popular vote \
                                would have simply diluted their states’ lower turnouts among the much higher participation levels in states holding fair, \
                                egalitarian, and democratic elections during the same time period."
                            ]),
                            html.P(className="card-text", children=[
                                "Regardless of underlying intent, the disconnect between census population and voter participation is seared into the historical \
                                record, offering a way to compare and quantify democratic and anti-democratic behavior over time — and to potentially infer \
                                correlation or causation between specific external factors and Voter Weight trends."
                            ]),
                            html.Br(),
                            html.H4("A few things that stood out", className="card-title"),
                            html.P(className="card-text", children=[
                                "I'm neither a historian nor a statistician (in case this wasn’t obvious), so it’s been interesting pausing to research events and \
                                periods along the way, attempting to interpret underlying causes of twists and turns in the data. Here’s a short list of the many \
                                data ripples that I initially mistook for errors, anomalies, or unexplained distortions:",
                                html.Ul(style={"margin-left": "10px", "padding-left": "10px"}, children=[
                                    html.Li(children=["The impact of the “Mississippi Plan,” a scheme to introduce discriminatory voting language into every \
                                        Southern state’s constitution, beginning in the 1890s", dcc.Link(href="/sources-notes", children=[html.Sup("23")]),
                                    ]),
                                    html.Li("The staggered state-by-state expansion of women’s suffrage (and therefore voter turnout overall) in the early \
                                        20th century, prior to the 19th Amendment’s ratification enfranchising women in every state in 1920"),
                                    html.Li("The “high watermark” of suppression-state bias in the election of 1924 and its proximity to events like the \
                                        Tulsa Race Massacre in 1921, peak KKK membership in 1924, and the segregationist presidency of Woodrow Wilson"),
                                    html.Li("The erratic differences in popular voter participation from state to state and year to year in the pre-Jacksonian \
                                        era, as states experimented with everything from state-wide popular vote to district-level selection to electors being \
                                        appointed by legislatures (off-topic, but interesting)"),
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
                                html.Ul(style={"margin-left": "10px", "padding-left": "10px"}, children=[
                                    html.Li(children=["Voter apathy, and hence lower voter participation. Since the “Solid South” of the early 20th century was \
                                        effectively a non-competitive one-party regional bloc (in part due to the wild success of their voter suppression \
                                        tactics), the fact that down-ballot winners were a foregone conclusion may have further depressed turnout", 
                                        dcc.Link(href="/sources-notes", children=[html.Sup("24")]),
                                    ]),
                                    html.Li("Other voting eligibility factors such as age, gender, incarceration status, felony record, ID laws, etc have varied \
                                        from state to state over the years"),
                                    html.Li("Census apportionment is decennial, so Electoral College influence always lags a few years behind a population \
                                        explosion, lowering the Voter Weight in fast-growing states near the end of the decade"),
                                    html.Li("Census apportionment in states with a higher percentage of undocumented residents who can’t legally vote increases \
                                        Voter Weight in that state. This is generally regarded as to the benefit, not the detriment, of those who are tabulated \
                                        but not enfranchised, but this results in a “five-fifths” type effect nonetheless."),
                                ]),
                            ]),
                        ]),
                    ]),
                ]),
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.Img(src="/static/borderStatesVenn.png", style={"float": "right", "padding-left": "10px"}, width="55%"),
                            html.H4("Border states", className="card-title"),
                            html.P(className="card-text", children=[
                                "On the ", dcc.Link("previous page", href="/voter-weight-electoral-college-bias-page4"), " I described my reasoning for creating \
                                a “Border state” group, consisting of slave states that had stayed in the Union rather than seceding to join the Confederacy. The \
                                idea was that this might serve as a control group, for determining which factor was more predictive of a state’s subsequent embrace \
                                of voter suppression tactics: (a) its relationship to slavery prior to the war, or (b) the side it had fought with in the war."
                            ]),
                            html.P(className="card-text", children=[
                                "My knowledge of Reconstruction, Redemption, Reconciliation, and Jim Crow is generally limited to a North vs South narrative, and \
                                what little I do know of the politics of Border and Western states tends to be through the lens of Northern vs Southern politicians \
                                (e.g. Lincoln's political dexterity in balancing the interests of Northern abolitionists against Border state slaveholders, and his \
                                success in preventing Border states from seceding). Caveats aside: knowing little to nothing of the ", html.I("details"), " of \
                                post-Reconstruction enfranchisement practices in Border states, it sure looks to me as though those practices led to much higher \
                                voter participation (and, by inverse relationship, little to no hyper-enfranchisement of individual voters) than that of Confederate \
                                slave states."
                            ]),
                            html.Img(src="/static/stockImages/census-1860.png", style={"float": "left", "padding-right": "10px", "padding-top": "5px"}, width="50%"),
                            html.P(className="card-text", children=[
                                "In fact, from the 40,000’ view enabled by these data visualizations, post-war voter turnout in Union-loyal former-slave states \
                                appears almost indistinguishable from voter participation in Union-loyal free states. I’d be reaching way out of my lane to \
                                interpret this any further here, but suffice to say I think this has fascinating implications."
                            ]),
                            html.P(className="card-text", children=[
                                "One last thought, with respect to demographics: It’s true that, when the Civil War began, Union-loyal Border states like Kentucky, \
                                Maryland, and Missouri had somewhat fewer enslaved persons per capita than their Confederate counterparts to the south. But these \
                                were not anecdotally slave “ish” states: more than 425K Blacks were enslaved in these three states per the ", dcc.Link("1860 census", 
                                href="https://www.census.gov/history/pdf/ApportionmentInformation-1860Census.pdf", target="_blank"), "."
                            ]),
                            html.P(className="card-text", children=[
                                "In absolute terms, in 1860 Union-loyal Kentucky had more enslaved people than Confederate Texas, Union-loyal Missouri had more \
                                enslaved people than Confederate Arkansas, and Union-loyal Maryland had more people enslaved than Confederate Florida. Yet the \
                                differences in the voter enfranchisement practices in these states a full 100 years after the abolition of slavery couldn’t be more \
                                stark."
                            ]),
                            html.P(className="card-text", children=[
                                html.B("Bottom line:"), html.I(" Post-Reconstruction voter disenfranchisement seems to have had less to do with a state’s historic \
                                connection to slavery than to the side it fought with in the Civil War."),
                            ]),
                            html.Br(),
                            html.H4("The Voting Rights Act of 1965", className="card-title"),
                            html.Img(src="/static/stockImages/voting-rights-act-1965-signed.jpg", style={"float": "right", "padding-left": "10px", "padding-top": "5px"}, 
                                width="50%"),
                            html.P(className="card-text", children=[
                                "I feel compelled to acknowledge an aspect of the historical data that I’ve danced around so far, but that’s hard to miss the \
                                longer you spend interacting with it. Since passage of the Voting Right Acts in 1965, it would appear that voter participation in \
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
                                "THAT SAID... anybody who’s tuned in to present-day voting rights issues will be quick to point out that (a) there’s massive \
                                amounts of disenfranchisement out there today, worse than ever with regards to felons, voter ID laws, overzealous signature \
                                matching, precinct-targeted voter roll purges, etc, and (b) the Supreme Court’s recent 2013 meddling in the Voting Rights Act of \
                                1965 vis-à-vis their ", html.I("Shelby County v. Holder"), " ruling actually presents a very real threat to the durability of \
                                positive historical trends."
                            ]),
                            html.Img(src="/static/stockImages/shelby-vs-holder-ruling.png", style={"float": "left", "padding-right": "10px", "padding-top": "5px"}, 
                                width="50%"),
                            html.P(className="card-text", children=[
                                "Although my quasi-scientific zoomed-out view of historical Voter Weight doesn’t show any obvious reversal of aggregate positive \
                                trends in 2016 or 2020 (again: not an actual statistician, I just play one on the internet), it’s worth noting that it took a few \
                                election cycles after Reconstruction for the Redeemer South’s suppression strategies to restore pre-war hyper-enfranchisement \
                                levels — only to wildly exceed that antebellum status quo over the course of several generations to follow. It’s also worth \
                                pointing out that, even in the few short months I’ve been working on this project, over 360 bills with restrictive voting \
                                provisions have been introduced in the legislatures of 47 states.", dcc.Link(href="/sources-notes", children=[html.Sup("25")])
                            ]),
                            html.P(className="card-text", children=[
                                "Moreover, if there’s a lesson I’ve gleaned from reading about American elections and racial justice history, it’s that familiar \
                                old discriminatory policies tend to continually reinvent themselves, often using familiar old tricks wrapped in thinly veiled \
                                language. And as long as the lights remain on in the twisted halls of white supremacy — and oh boy do they seem to be on right \
                                now — there will be attempts to disenfranchise based on racial demographics, ranging from the subtle to the obvious, the \
                                innovative to the familiar. As antiquated as the American electoral system is, as many tricks as have already been tried, past \
                                methods of manipulation should always be viewed as prologue to future attempts."
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
                        html.A(className="page-link", href="/voter-weight-electoral-college-bias-page4", children=[
                            "← Part 4: Suppression-state bias"
                        ])
                    ]),
                    html.Li(className="page-item flex", style={"width": "20%"}),
                    html.Li(className="page-item flex", style={"width": "50%", "text-align": "right"}, children=[
                        html.A(className="page-link", href="/voter-weight-conclusions", children=[
                            "Part 6: Conclusions and interpretation →"
                        ])
                    ]),
                ])
            ]),
        ])
    ])
])