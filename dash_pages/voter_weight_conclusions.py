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
                        html.A(className="page-link", href="/voter-weight-results", children=[
                            "← Part 5: Results and obervations"
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
                html.H3("Part 6: Conclusions and Discussion"),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.Div(className="card-text", style={"margin-left": "50px", "margin-right": "50px", "font-size": "13pt"}, children=[
                                html.P(style={"font-style": "italic"}, children=[
                                    "In a Republic of equal citizens, votes should generally count equally, lest government be captured by an entrenched, \
                                    self-perpetuating oligarchy within the electorate.",
                                    dcc.Link(href="/sources-notes", children=[html.Sup("TODO")]),
                                ]),
                                html.P(children=["—Akhil Reed Amar, summarizing Justice Hugo Black, ", html.I("“The Law of the Land: A Grand Tour of our Constitutional Republic”")])
                            ]),
                            html.Br(),
                            html.H4("Hyper-enfranchisement: Implications and interpretation", className="card-title"),
                            html.P(className="card-text", children=[
                                "The three-fifths compromise, that infamously dehumanizing fraction baked into the Constitution, would have been worse for the \
                                plight of slaves if it had been five-fifths. This was actually what Southern slave-owners wanted: fully-counted slaves whose census \
                                tabulation would result in greater congressional and Electoral College influence for Southern states, i.e. Southern white voters and \
                                the institution of slavery.", dcc.Link(href="/sources-notes", children=[html.Sup("TODO")])
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
                                "The reduction clause of the Fourteenth Amendment formally ended the three-fifths clause, not by enfranchising Blacks, but by \
                                reducing the congressional representation (and Electoral College votes) of states that disenfranchised their eligible voters. But \
                                the reduction clause of the Fourteenth Amendment has never been enforced,", dcc.Link(href="/sources-notes", children=[html.Sup("TODO")]), 
                                " so neither the crystal clear suffrage mandate of the Fifteenth Amendment nor the Fourteenth Amendment’s threat of reduced \
                                representation prevented Southern states from pursuing a total assault on Black voting rights for nearly a century."
                            ]),
                            html.Br(),
                            html.H4("How the ‘Slave Power’ perpetuated slavery", className="card-title"),
                            html.P(className="card-text", children=[
                                "A common argument tactic is to point out how long ago the Jim Crow Era was, how much has changed since then, even to suggest that \
                                highlighting these abuses perpetuates the problems caused by them. Let’s address that head-on. What effects might nine decades of \
                                Southern white votes counting for 3x, 4x, even as much as a 7x-8x their Northern and Western counterparts’ votes have had on \
                                present day laws, policies, and institutions, or on American culture and belief systems generally?"
                            ]),
                            html.P(className="card-text", children=[
                                "As a proxy, let’s examine the well-documented effects of the white South’s three-fifths electoral advantage during slavery, both \
                                within the South and across America as a whole. Despite being home to less than a third of the country’s free population, \
                                significant majorities of high-level representatives and appointments went to Southern slaveholders:",
                                html.Ul([
                                    html.Li("10 of the first 17 Presidents, serving ~13 of the first 20 terms were Southerner slaveholders"),
                                    html.Li("21 of the first 33 Speakers of the House were Southerner slaveholders"),
                                    html.Li("18 of the first 31 Supreme Court justices were Southerner slaveholders (including a majority of those who ruled on \
                                        the infamous 1857 Dred Scott decision)"),
                                    html.Li("14 of the first 19 Attorneys General were Southerner slaveholders"),
                                    html.Li("84 of the first 134 Foreign Ministers were Southerner slaveholders"),
                                ])
                            ]),
                            html.P(className="card-text", children=[
                                "Here’s a roundup of major legislation favorable to slavery and slave-states during the antebellum period, all passed despite \
                                substantially fewer voters in slave-states:",
                                html.Ul([
                                    html.Li("The Missouri Compromise, admitting Missouri to the Union as a slave state in exchange for an agreement to halt the \
                                        expansion of slavery in the Northwestern territories (1820)"),
                                    html.Li("The Indian Removal Act, which forced the removal of 100,000 Native Americans from Southern states via the Trail of \
                                        Tears (1830)"),
                                    html.Li("The House “Gag rule” protecting slavery in Washington D.C. (1840)"),
                                    html.Li("Inception of the filibuster, developed by South Carolina’s John C. Calhoun for the express purpose of protecting \
                                        slavery (1840s)"),
                                    html.Li("Defeat of the Wilmot Proviso, which would’ve banned slavery in territory claimed during the Mexican-American War \
                                        (1847)"),
                                    html.Li("Passage of the Fugitive Slave Act, requiring those living in free states to cooperate in the capture and return of \
                                        escaped slaves to their Southern masters (1850)"),
                                    html.Li("The Kansas-Nebraska Act, giving Western territories the right of “popular sovereignty” with respect to slavery, \
                                        thus repealing the compromise that had been the basis for Missouri’s admission as a slave state (1854)"),
                                ])
                            ]),
                            html.P(className="card-text", children=[
                                "Northern acceptance of or apathy toward slavery was certainly a factor during the earliest years of the Republic, but this doesn’t \
                                account for the overwhelming representation of Southern slaveholders in every branch of the federal government, nor the inordinate \
                                amount of slave-expansionist legislation passed and court decisions rendered. Each legislative item above represented a minority \
                                position, elevated by an electoral system mathematically biased toward slaveholder interests, pushed through the legislature by a \
                                puffed-up minority faction whose inflated national power derived directly from their enslaved population."
                            ]),
                            html.P(className="card-text", children=[
                                "In his memoirs, Frederick Douglass describes the influence he believed Southern whites and the Slave Power were having on \
                                communities in the North by the mid nineteenth century. Recalling the hostile and at times violent reactions of Northern crowds to \
                                the anti-slavery conventions he participated in in free states like Vermont, Rhode Island, and Indiana in the 1840s, he himself could \
                                hardly reconcile the change these communities would undergo in their full-throated denouncement and disavowal of slavery mere decades \
                                later. ", dcc.Link(href="/sources-notes", children=[html.Sup("TODO")]), " To Douglass, the pernicious influence of the Slave Power \
                                was so great it had effectively cast a spell on the Northernern mind, twisting it into accepting a status quo it would reject and \
                                recoil from when it came to its senses in the 1860s and 1870s."
                            ]),
                            html.P(className="card-text", children=[
                                "Northern complicity aside, the electoral boost that Southern whites extracted from their slaves was highly effective at perpetuating \
                                the Slave Power, preserving and even expanding its disproportionate influence, in a self-sustaining feedback loop. It also set the \
                                table for the Civil War, which is what it took for the South to realize that their artificially inflated political power was not the \
                                same as actual man-for-man physical, industrial, or military power. And even after that cataclysmic collision, which left 620,000 \
                                dead, ignited a multi-year amendment Constitutional amendment process, and kicked off a 12-year military occupation, the \
                                disproportionate impact of prewar slaveholding policies and politicians remains deeply woven into the fabric of American institutional \
                                memory and identity to this day."
                            ]),
                            html.Br(),
                        ]),
                    ]),
                ]),
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.Div(className="card-text", style={"margin-left": "50px", "margin-right": "50px", "font-size": "13pt"}, children=[
                                html.P(style={"font-style": "italic"}, children=[
                                    "By the 1940s… registration among voting-age Black citizens hovered around 3 percent… In the 11 Presidential elections held \
                                    between 1908 and 1948, 44 percent of all minority votes in the country were not represented by a single electoral vote.",
                                    dcc.Link(href="/sources-notes", children=[html.Sup("19")]),
                                ]),
                                html.P(children=["—Jesse Wegman, ", html.I("“Let the People Pick the President”")])
                            ]),
                            html.Br(),
                            html.H4("Was there an analogous ‘Jim Crow Power’ perpetuating Jim Crow?", className="card-title"),
                            html.P(className="card-text", children=[
                                "Turning our attention back to the Jim Crow Era, longer by a decade than the post-colonial period of slavery, and even more \
                                mathematically skewed to amplify the voting power of Southern whites: To what degree and in what form was the South’s reactionary \
                                white supremacist agenda manifest and exported nationwide when it was reincarnated post-Reconstruction?"
                            ]),
                            html.P(className="card-text", children=[
                                "The most well-known achievement of Southern white legislators during the Jim Crow era is what was prevented from being achieved: \
                                nationwide Civil Rights legislation. Georgia Senator Richard Russell’s notorious use of the filibuster to block legislation from the \
                                1930s through the 1960s (echoing Calhoun’s usage of the filibuster to protect slavery a century prior) exemplifies the potency of \
                                the “Solid South,” what we might call the “Jim Crow Power” to emphasize the greater degree of national influence enjoyed by Southern \
                                voters. Russel isn’t even the best-known white supremacist Southern Senator to use the filibuster in this way, but his longevity in \
                                the Senate gave him a hand in obstructing everything from the 1938 Wagner-Van Nuys Anti-Lynching Bill up to the doorstep of the 1964 \
                                Civil Rights Act, when his protégé Lyndon Johnson finally broke the decades-long white supremacist stranglehold on the Senate."
                            ]),
                            html.P(className="card-text", children=[
                                "Today, the Russell Senate Office Building is workplace to over a thousand senate staffers, and continues to symbolically enshrine \
                                the Senator’s legacy of white supremacy and legislative obstructionism. But most examples of Jim Crow’s holdover effect are both \
                                less symbolic and more insidiously relevant in everyday life. Among them:",
                                html.Ul([
                                    html.Li("Segregated neighborhoods carving up nearly every American city today trace back overwhelmingly to the FHA’s and HOLC’s \
                                        racist redlining and lending practices beginning in the 1930s, while “spot” rezoning to permit toxic sites adjacent to Black \
                                        neighborhoods and the targeted demolition of Black communities to build highways further restricted housing options and \
                                        depressed housing value"),
                                    html.Li("The present day exclusion of agricultural, food service, and domestic workers from minimum wage, unemployment, and \
                                        other New Deal-era benefits and protections, and even modern-day tipping in lieu of proper workplace compensation, derive \
                                        from Southern politicians and entrepreneurs seeking to minimize wages for Black labor in the Jim Crow South"),
                                    html.Li("The exponential disparities in drug war targeting and sentencing, from racial profiling in traffic stops and \
                                        stop-and-frisk encounters to wild disparities in sentencing for crack vs cocaine possession, backed by the normalization of \
                                        militarized police violence toward unarmed Black citizens, bears striking resemblance to Slave patrols, the enforcement of \
                                        Black Codes, the violent suppression of the Southern segregationist status quo, and the paltry legal defense available to \
                                        Black citizens during Jim Crow"),
                                    html.Li(children=["Although illegal in much of the country, by the 1950s school segregation was widespread enough that the Supreme \
                                        Court had its pick of venues, selecting Kansas as its lead case in ", html.I("Brown v. Board of Education"), ". In doing so, \
                                        the court was able to go after school segregation without singling out the South, effectively using the ubiquity of this \
                                        Southern export to go after the institution without directly attacking its Southern proponents."
                                    ])
                                ])
                            ]),
                            html.P(className="card-text", children=[
                                "At a cultural level, this country continues to deal with its once ubiquitous embrace of ‘Lost Cause’ mythology, with media saturation \
                                of Sambo caricatures and Tarzan-esque tropes, with the legacy of 25% of eligible (white men) enrolled in the KKK and the country's \
                                tepid reaction to public lynchings, with the scientific community's fervent embrace of the Eugenics movement and its present-day relics \
                                like the SAT, and with Confederate flags flying at events in Northern and Western states (to say nothing of Southern states that were \
                                once part of the actual Confederacy). But behind these brazen expressions of white supremacy are decades of legislated, bureaucratic, \
                                institutional racism, all normalized after generations of unchallenged precedent and repetition, and all born out of a political system \
                                that granted its most avowed white supremacist element 3x-8x the influence of other white voters, while silencing its African-American \
                                voices altogether."
                            ]),
                            html.P(className="card-text", children=[
                                "I’m not suggesting that Northern citizens aren’t culpable for their complicity in the adoption and expansion of a Jim Crow \
                                segregationist mindset nationally during those 90 years. Unlike the Slave Power lists, these campaigns were enacted nationally, during \
                                an age of “Reconciliation” between Northern and Southern whites. I’m simply saying that the element of the country most notorious in \
                                its white supremacist ethos and agenda was also the most politically influential, and that this influence undoubtedly left an \
                                indelible institutional mark commensurate with that influence. That the boost in political influence enjoyed by this white supremacist \
                                element derived directly from white supremacy’s greatest victims feels like tragic irony, but arguably it points to a central flaw in \
                                the design of our political system: that it rewards with greater political influence precisely those citizens most willing to deny \
                                political rights to those around them. It’s a story of staggering political cannibalism, the second such era to afflict the same region \
                                of the country, and the fact that the effects of this second period are less cut-and-dry, not as widely known or documented, not part \
                                of school curriculums, etc possibly just speaks to their continuing pernicious effect on American society."
                            ]),
                            html.P(className="card-text", children=[
                                "The divisions between North and South weren’t as cut-and-dried after Reconstruction as they had been prior to the war, but once \
                                again Southern whites had a ‘peculiar’ social and economic status quo they were desperate to protect. How many federal appointments, \
                                government programs, legal precedents, or pieces of national legislation passed during this era were cultivated with intent to \
                                perpetuate a status quo grounded in Southern whites silencing and extracting political influence from their Black populations? How \
                                many ideologies and narratives, designed to maintain entrenched Southern white interests but promoted as ‘heritage’ or as bedrock \
                                American virtues, were amplified and exported to the rest of the country during those nine decades? How many coalitions were built, \
                                compromises brokered, and principles abandoned in service of a hyper-enfranchised faction whose hold on power depended on the \
                                perpetuation and expansion of white supremacist ideology? And how many of the laws, institutions, and ideologies crafted in this \
                                reactionary white supremacist crucible continue to endure and thrive, at the national level, to this day?"
                            ]),
                            html.P(className="card-text", children=[
                                "The question I’m asking isn’t whether Southern whites had a white supremacist agenda, or whether a Southern white legislators used \
                                their power to perpetuate white supremacy, or even whether the white supremacist messaging emanating from South politicians had an \
                                effect on people and policies in other states. Clearly it did, and no doubt that agenda was received favorably by like-minded white \
                                supremacists in other parts of the country. No, the question I’m asking is: How much was that Southern white supremacist message \
                                amplified by America’s unique system of representation, where political influence derives from census population rather than voter \
                                turnout, giving the most power to the voters who do the best job of preventing their neighbors from voting? And what if the number \
                                of legislators (and electoral college votes) coming from former Confederate states had reflected that suppressed turnout? How \
                                differently might America’s 20th century have unfolded if the South had sent, say, three quarters as many congressmen to the House \
                                between 1900 and 1960? How about two thirds? Half? Without doing all the math, it certainly appears that many if not most Southern \
                                states easily could have had their representation cut in two, if not cut in four or even six or eight, based on how few people \
                                voted - i.e. how many people were prevented from voting."
                            ]),
                            html.Br(),
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
                            html.Br(),      
                        ]),
                    ]),
                ]),
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
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
                        ]),
                    ]),
                ]),
            ]),
            html.Br(),
            html.Hr(className="border-light"),
            html.Div(children=[
                html.Ul(className="pagination pagination-lg justify-content-center", children=[
                    html.Li(className="page-item flex", style={"width": "50%"}, children=[
                        html.A(className="page-link", href="/voter-weight-results", children=[
                            "← Part 5: Results and obervations"
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