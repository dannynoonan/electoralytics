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
                        html.A(className="page-link", href="/voter-weight-calculation", children=[
                            "Appendix 1: Calculating Voter Weight →"
                        ])
                    ]),
                ])
            ]),
            html.Hr(className="border-light"),
            html.Br(),
            dbc.Row(className="text-white", justify="center", align="center", children=[
                html.H3("Part 5: Conclusions and Discussion"),
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
                                "The Fourteenth Amendment formally ended the three-fifths clause, not by enfranchising Blacks, but by reducing the congressional \
                                representation (and Electoral College votes) of states that disenfranchised their eligible voters. At least, that’s how it was laid \
                                out on paper. In actuality, the reduction clause of the Fourteenth Amendment has never been enforced.", dcc.Link(href="/sources-notes", 
                                children=[html.Sup("TODO")]), " Neither the crystal clear suffrage mandate of the Fifteenth Amendment nor the Fourteenth Amendment’s \
                                threat of reduced representation prevented Southern states from charging full steam ahead with Jim Crow voter suppression, most of \
                                which went unchallenged for nearly a century."
                            ]),
                            html.Br(),
                            html.H4("How the ‘Slave Power’ perpetuated slavery", className="card-title"),
                            html.P(className="card-text", children=[
                                "A common argument tactic is to point out how long ago the Jim Crow Era was, how much has changed since then, even to suggest that \
                                highlighting these abuses perpetuates the problems caused by them. Let’s address that head-on. What effects might nine decades of \
                                Southern white votes countring for 3x, 4x, even as much as a 7x-8x their Northern and Western counterparts’ votes have had on \
                                present day laws, policies, and institutions, or on American culture and belief systems generally?"
                            ]),
                            html.P(className="card-text", children=[
                                "As a proxy, let’s examine the well-documented effects of the white South’s three-fifths electoral advantage during slavery, both \
                                within the South and across America as a whole. Despite being home to less than a third of the country’s free population, \
                                significant majorities of high-level representatives and appointments went to Southern slaveholders:",
                                html.Ul([
                                    html.Li("10 of the first 17 Presidents, serving ~13 of the first 20 terms"),
                                    html.Li("21 of the first 33 Speakers of the House"),
                                    html.Li("18 of the first 31 Supreme Court justices (including a majority of those who ruled on the infamous 1857 Dred Scott \
                                        decision)"),
                                    html.Li("14 of the first 19 Attorneys General"),
                                    html.Li("84 of the first 134 Foreign Ministers"),
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
                                later. To Douglass, the pernicious influence of the Slave Power was so great it had effectively cast a spell on the Northernern mind, \
                                twisting it into accepting a status quo it would handily reject and recoil from when it eventually came to its senses."
                            ]),
                            html.P(className="card-text", children=[
                                "Northern complicity aside, the electoral boost that Southern whites extracted from their slaves was highly effective at perpetuating \
                                the Slave Power, preserving and even expanding its disproportionate influence, in a self-sustaining feedback loop. It also set the \
                                table for the Civil War, which is what it took for the South to realize that their artificially inflated political power was not the \
                                same as actual man-for-man physical, industrial, or military power."
                            ]),
                            html.Br(),
                        ]),
                    ]),
                ]),
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.H4("Was there an analogous ‘Jim Crow Power’?", className="card-title"),
                            html.P(className="card-text", children=[
                                "Turning our attention back to the Jim Crow Era, longer by a decade than the post-colonial period of slavery, and even more \
                                mathematically skewed to amplify the voting power of Southern whites: To what degree and in what form was the South’s reactionary \
                                white supremacist agenda manifest and exported nationwide when it was reincarnated post-Reconstruction?"
                            ]),
                            html.P(className="card-text", children=[
                                "The divisions between North and South weren’t as cut and dry after Reconstruction as they had been prior to the war, but once again \
                                Southern whites had a ‘peculiar’ social and economic status quo they were desperate to protect. How many federal appointments, \
                                government programs, legal precedents, or pieces of national legislation passed during this era were cultivated with intent to \
                                perpetuate a status quo grounded in Southern whites silencing and extracting political influence from their Black populations? How \
                                many ideologies and narratives, designed to maintain entrenched Southern white interests but promoted as ‘heritage’ or as bedrock \
                                American virtues, were amplified and exported to the rest of the country during those nine decades? How many coalitions were built, \
                                compromises brokered, and principles abandoned in service of a hyper-enfranchised faction whose hold on power depended on the \
                                perpetuation and expansion of white supremacist ideology? And how many of the laws, institutions, and ideologies crafted in this \
                                reactionary white supremacist crucible continue to endure and thrive, at the national level, to this day?"
                            ]),
                            html.P(className="card-text", children=[
                                "Georgia Senator Richard Russell’s notorious use of the filibuster to block Civil Rights legislation from the 1930s through the 1960s \
                                (echoing Calhoun’s usage of the filibuster to protect slavery a century prior) exemplifies the potency of Jim Crow Power. Workplace \
                                to over a thousand senate staffers today, the Russell Senate Office Building continues to symbolically enshrine Senator Russell’s \
                                white supremacist and legislative obstructionist legacy - but most examples of Jim Crow’s holdover effect are both less symbolic and \
                                more insidiously relevant in everyday life. Among them:",
                                html.Ul([
                                    html.Li("Segregated neighborhoods carving up nearly every American city today trace back overwhelmingly to the FHA’s and HOLC’s \
                                        racist redlining and lending practices beginning in the 1930s, while “spot” rezoning to permit toxic sites adjacent to Black \
                                        neighborhoods and the targeted demolition of Black communities to build highways further restricted housing options and \
                                        depressed housing value"),
                                    html.Li("The present day exclusion of agricultural, food service, and domestic workers from minimum wage, unemployment, and \
                                        other New Deal-era benefits and protections, and even modern-day tipping in lieu of proper workplace compensation, derive \
                                        from Southern politicians plotting ways to minimize Black labor costs in the Jim Crow South"),
                                    html.Li("The exponential disparities in drug war targeting and sentencing, from racial profiling in traffic stops and \
                                        stop-and-frisk encounters to wild disparities in sentencing for crack vs cocaine possession, backed by the normalization of \
                                        militarized police violence toward unarmed Black citizens, bears striking resemblance to Slave patrols, the enforcement of \
                                        Black Codes, the violent suppression of the Southern segregationist status quo, and the paltry legal defense available to \
                                        Black citizens during Jim Crow"),
                                ])
                            ]),
                            html.P(className="card-text", children=[
                                "At a cultural level, the ubiquitous embrace of ‘Lost Cause’ mythology, media saturation of Sambo caricatures and Tarzan-esque tropes, \
                                the national expansion of the KKK and tepid public reaction to lynchings, the fervent embrace of the Eugenics movement and its \
                                present-day relics like the SAT, and Confederate flags flying at events in Northern and Western states are just a few of the most \
                                obvious examples. But concealed behind these brazen expressions of white supremacy are decades of legislated, bureaucratic, \
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
                        ]),
                    ]),
                ]),
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
                        html.A(className="page-link", href="/voter-weight-calculation", children=[
                            "Appendix 1: Calculating Voter Weight →"
                        ])
                    ]),
                ])
            ]),
        ])
    ])
])