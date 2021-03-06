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
                html.H3("Part 6: Conclusions and interpretation"),
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
                                    dcc.Link(href="/sources-notes", children=[html.Sup("26")]),
                                ]),
                                html.P(children=["—Akhil Reed Amar, summarizing Justice Hugo Black, ", html.I("“The Law of the Land: A Grand Tour of our \
                                    Constitutional Republic”")])
                            ]),
                            html.Br(),
                            html.H4("Hyper-enfranchisement: Implications and interpretation", className="card-title"),
                            html.P(className="card-text", children=[
                                "The three-fifths compromise, that infamously dehumanizing fraction baked into the Constitution, would have been worse for the plight \
                                of enslaved persons if it had been five-fifths. This was actually what Southern slaveholders wanted: fully-counted slaves whose census \
                                tabulation would result in greater congressional and Electoral College influence for Southern states, i.e. Southern white voters and \
                                the institution of slavery.", dcc.Link(href="/sources-notes", children=[html.Sup("27")])
                            ]),
                            html.Img(src="/static/stockImages/fourteenth-amendment-fail.jpg", style={"float": "left", "padding-right": "10px", "padding-top": "5px"}, 
                                width="50%"),
                            html.P(className="card-text", children=[
                                "After slavery was abolished and a dozen hopeful years of Reconstruction had fizzled out, the Southern white dream of fully-counted \
                                yet disenfranchised Blacks was finally realized, via Jim Crow voter suppression. The paradoxical interaction between citizenship \
                                status, representational apportionment, and voter participation converged to enable a level of Electoral College manipulation almost \
                                unfathomable in its scale. The result was that even more political influence was siphoned from the toil of freed Black citizens into \
                                the ballots of Southern whites than had previously been siphoned from enslaved Blacks. This latter period of five-fifths \
                                hyper-enfranchisement under Jim Crow lasted roughly 90 years, compared to not quite 80 years of three-fifths slavery under the \
                                Constitution (the institution of slavery having, of course, been pervasive in the colonies since 1619, but formally protected as a \
                                United States institution beginning in 1788)."
                            ]),
                            html.P(className="card-text", children=[
                                "The reduction clause of the Fourteenth Amendment formally ended the three-fifths clause, not by enfranchising Blacks, but by \
                                reducing the congressional representation (and Electoral College votes) of states that disenfranchised their eligible voters. But \
                                the reduction clause of the Fourteenth Amendment has never been enforced,", dcc.Link(href="/sources-notes", children=[html.Sup("28")]), 
                                " so neither the crystal clear suffrage mandate of the Fifteenth Amendment nor the Fourteenth Amendment’s threat of reduced \
                                representation prevented Southern states from pursuing a total assault on Black voting rights for nearly a century."
                            ]),
                            html.Br(),
                            html.H4("How the ‘Slave Power’ perpetuated slavery", className="card-title"),
                            html.Img(src="/static/stockImages/dred-scott-newspaper.jpg", style={"float": "right", "padding-left": "10px", "padding-top": "5px"}, 
                                width="40%"),
                            html.P(className="card-text", children=[
                                "Now that we’ve explored the electoral mechanics behind suppression-state bias in the Jim Crow South, what can we infer about its \
                                impact? What consequences might nine decades of Southern white votes counting for 3x, 4x, even as much as a 7x-8x their Northern \
                                and Western counterparts’ votes, in combination with near-total suppression of the Southern Black vote, have had on present day \
                                laws, policies, and institutions, or on American culture and belief systems generally?"
                            ]),
                            html.P(className="card-text", children=[
                                "As a proxy, let’s briefly review the well-documented effects of the white South’s three-fifths electoral advantage during the \
                                ‘peculiar’ institution of slavery, both within the South and across America as a whole. Despite being home to less than a third of \
                                the country’s free population, significant majorities of high-level representatives and appointments went to Southern slaveholders. \
                                Here’s a quick round-up:",
                                html.Ul(style={"margin-left": "10px", "padding-left": "10px"}, children=[
                                    html.Li("10 of the first 17 Presidents, serving ~13 of the first 20 terms, were Southern slaveholders"), 
                                    html.Li(children=["21 of the first 33 Speakers of the House were Southern slaveholders", dcc.Link(href="/sources-notes", 
                                        children=[html.Sup("29")])
                                    ]),
                                    html.Li(children=["18 of the first 31 Supreme Court justices were Southern slaveholders (including a majority of those who \
                                        ruled on the infamous 1857 Dred Scott decision)", dcc.Link(href="/sources-notes", children=[html.Sup("30")])
                                    ]),
                                    html.Li(children=["14 of the first 19 Attorneys General were Southern slaveholders", dcc.Link(href="/sources-notes", 
                                        children=[html.Sup("29")])
                                    ]),
                                    html.Li(children=["84 of the first 134 Foreign Ministers were Southern slaveholders", dcc.Link(href="/sources-notes", 
                                        children=[html.Sup("29")])
                                    ]),
                                    html.Li(children=["Slave states sent one-third more representatives to Congress than they would have if representation were \
                                        based only on the number of free citizens", dcc.Link(href="/sources-notes", children=[html.Sup("30")])
                                    ]),
                                ])
                            ]),
                            html.Img(src="/static/stockImages/fugitive-slave-newspaper.jpg", style={"float": "right", "padding-left": "10px"}, width="50%"),
                            html.P(className="card-text", children=[
                                "With its inflated national representation and influence, the Slave Power pursued an agenda favorable to the protection and expansion \
                                of slavery, repeatedly passing major pro-slavery legislation on behalf of an ever-shrinking minority of voters:", 
                                dcc.Link(href="/sources-notes", children=[html.Sup("30")]),
                                html.Ul(style={"margin-left": "10px", "padding-left": "10px"}, children=[
                                    html.Li("1820: The Missouri Compromise, admitting Missouri to the Union as a slave state in exchange for an agreement to halt the \
                                        expansion of slavery in the Northwestern territories"), 
                                    html.Li("1830: The Indian Removal Act, which forced the removal of 100,000 Native Americans from Southern states via the Trail of \
                                        Tears"),
                                    html.Li("1840: The House “Gag rule” protecting slavery in Washington D.C."),
                                    html.Li(children=["1840s: Inception of the filibuster, developed by South Carolina’s John C. Calhoun for the express purpose of \
                                        protecting slavery ", dcc.Link(href="/sources-notes", children=[html.Sup("31")])
                                    ]),
                                    html.Li("1847: Defeat of the Wilmot Proviso, which would’ve banned slavery in territory claimed during the Mexican-American War"),
                                    html.Li("1850: Passage of the Fugitive Slave Act, requiring those living in free states to cooperate in the capture and return of \
                                        escaped slaves to Southern slaveholders"),
                                    html.Li("1854: The Kansas-Nebraska Act, giving Western territories the right of “popular sovereignty” with respect to slavery, \
                                        thus repealing the compromise that had been the basis for Missouri’s admission as a slave state"),
                                ])
                            ]),
                            html.Img(src="/static/stockImages/kansas-nebraska-freesoil-cartoon.jpg", style={"float": "left", "padding-right": "10px", 
                                "padding-top": "5px"}, width="50%"),
                            html.P(className="card-text", children=[
                                "Northern acceptance of or apathy toward slavery was certainly a factor during the earliest years of the Republic, but this doesn’t \
                                account for the overwhelming representation of Southern slaveholders in every branch of the federal government, nor the inordinate \
                                amount of slave-expansionist legislation passed and court decisions rendered. The legislative items above represented minority \
                                positions, elevated by an electoral system mathematically biased toward slaveholder interests, pushed through the legislature by a \
                                puffed-up minority faction whose inflated national power derived directly from their enslaved population."
                            ]),
                            html.Img(src="/static/stockImages/wilmot-proviso-reaction.jpg", style={"float": "right", "padding-left": "10px"}, width="40%"),
                            html.P(className="card-text", children=[
                                "In his memoirs, Frederick Douglass describes the influence he believed Southern whites and the Slave Power were having on \
                                communities in the North by the mid nineteenth century. Recalling the hostile and at times violent reactions of Northern crowds to \
                                the anti-slavery conventions he participated in in free states like Vermont, Rhode Island, and Indiana in the 1840s, he himself could \
                                hardly reconcile the change these communities would undergo in their full-throated denouncement and disavowal of slavery mere decades \
                                later.", dcc.Link(href="/sources-notes", children=[html.Sup("32")]), " To Douglass, the pernicious influence of the Slave Power \
                                was so great it had effectively cast a spell on the Northernern mind, twisting it into accepting a status quo it would reject and \
                                recoil from when it came to its senses in the 1860s and 1870s."
                            ]),
                            html.P(className="card-text", children=[
                                "Northern complicity aside, the electoral boost that Southern whites extracted from their enslaved population was highly effective at \
                                perpetuating the Slave Power, preserving and even expanding its disproportionate influence, in a self-sustaining feedback loop. It \
                                also set the table for the Civil War, which is what it took for the South to realize that their artificially inflated political power \
                                was not the same as actual man-for-man physical, industrial, or military power. And even after that cataclysmic collision, the \
                                disproportionate impact of prewar slaveholding policies and politicians remained deeply woven into American culture and the fabric of \
                                institutional memory and identity, in ways we’ve still not fully reconciled a century and a half later."
                            ]),
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
                                    dcc.Link(href="/sources-notes", children=[html.Sup("33")]),
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
                            html.Img(src="/static/stockImages/russell-senate-office-building.jpg", style={"float": "left", "padding-right": "10px", 
                                "padding-top": "5px"}, width="45%"),
                            html.P(className="card-text", children=[
                                "The most well-known achievement of Southern white legislators during the Jim Crow era is in what was prevented from being achieved: \
                                nationwide Civil Rights legislation. Georgia Senator Richard Russell’s notorious use of the filibuster to block legislation from the \
                                1930s through the 1960s (echoing Calhoun’s usage of the filibuster to protect slavery a century prior) exemplifies the potency of \
                                the “Solid South,” what we might call the “Jim Crow Power” to emphasize the greater degree of national influence enjoyed by Southern \
                                (white) voters. Russell isn’t even the best-known white supremacist Southern Senator to use the filibuster in this way, but his \
                                longevity in the Senate gave him a hand in obstructing everything from the 1938 Wagner-Van Nuys Anti-Lynching Bill up through the \
                                1964 Civil Rights Act, when his one-time protégé Lyndon Johnson—inspired by the incredible sacrifices made by those in the Civil \
                                Rights movement—finally broke the decades-long white supremacist stranglehold on the Senate.", dcc.Link(href="/sources-notes", 
                                children=[html.Sup("34")]),
                            ]),
                            html.Img(src="/static/stockImages/redlining-brooklyn.jpg", style={"float": "right", "padding-left": "10px", "padding-top": "5px"}, 
                                width="40%"),
                            html.P(className="card-text", children=[
                                "Today, the Russell Senate Office Building is workplace to over a thousand senate staffers, and continues to symbolically enshrine \
                                the Senator’s legacy of white supremacy and legislative obstructionism.", dcc.Link(href="/sources-notes", children=[html.Sup("35")]), 
                                " But most examples of Jim Crow’s self-perpetuating and still-lingering effects are both less symbolic and more insidiously relevant. \
                                Handy tallies of politicians, legislation, and judicial rulings promoted by hyper-enfranchised 20th-century Southern whites \
                                may not be as neatly compiled in history books as those linked to the three-fifths-amplified Slave Power, but as a thought \
                                experiment it’s worth looking for the fingerprints of the Jim Crow South’s mathematical advantage in present-day policies and \
                                institutions. Just to explore the very tip of the iceberg:",
                                html.Ul(style={"margin-left": "10px", "padding-left": "10px"}, children=[
                                    html.Li(style={"padding-top": "5px"}, children=["Segregated neighborhoods carving up nearly every American city today trace back \
                                        overwhelmingly to the ", dcc.Link("FHA", href="https://en.wikipedia.org/wiki/Federal_Housing_Administration", target="_blank"), 
                                        "’s and ", dcc.Link("HOLC", href="https://en.wikipedia.org/wiki/Home_Owners%27_Loan_Corporation", target="_blank"), "’s racist \
                                        redlining and lending practices beginning in the 1930s,", dcc.Link(href="/sources-notes", children=[html.Sup("36")]), " while \
                                        “spot” rezoning to permit toxic sites adjacent to Black neighborhoods and the targeted demolition of Black communities to \
                                        build highways further restricted housing options and depressed housing value.", dcc.Link(href="/sources-notes", 
                                        children=[html.Sup("37")]), " These government-imposed impediments to building personal and community wealth through real \
                                        estate in the 20th century continue to be a major source of financial inequity between Blacks and whites today."
                                    ]),
                                    html.Li(style={"padding-top": "5px"}, children=["Continuing on the filibuster theme: in 1890, six years before ", html.I("Plessy"),
                                        ", when the “Mississippi Plan” was still a Southern white pipe dream, and when the nation’s descent into the Jim Crow \
                                        segregationist abyss was by no means assured, Henry Cabot Lodge introduced a Federal Elections Bill into Congress, designed to \
                                        close loopholes in the Fifteenth Amendment used by white Southern state governments to suppress the Black vote. Known \
                                        derisively as the “Force Bill” to Southern (white) politicians, the legislation enjoyed majority support in both chambers of \
                                        Congress and was backed by President Harrison, but was stalled via filibuster in the Senate until support eroded, eventually \
                                        disintegrating in a web of compromise favoring other unrelated measures. Mississippi and other Southern legislatures took the \
                                        bill’s failure as a “green light to eliminate Black suffrage entirely.”", dcc.Link(href="/sources-notes", 
                                        children=[html.Sup("38")]), " It would be 67 years before Congress would try again to enforce the Fifteenth Amendment."
                                    ]),
                                    html.Img(src="/static/stockImages/pullman-dining-car2.png", style={"float": "right", "padding-left": "10px", "padding-top": "10px"}, 
                                        width="42%"),
                                    html.Li(style={"padding-top": "5px"}, children=["The present day exclusion of agricultural, food service, and domestic workers \
                                        from minimum wage, unemployment, and other New Deal-era benefits and protections,", dcc.Link(href="/sources-notes", 
                                        children=[html.Sup("39")]), " and even modern-day tipping in lieu of proper workplace compensation,", 
                                        dcc.Link(href="/sources-notes", children=[html.Sup("40")]), " derive from Southern politicians and racially-exploitative \
                                        entrepreneurs seeking to minimize wages for Black labor in the Jim Crow South.", dcc.Link(href="/sources-notes", 
                                        children=[html.Sup("41")])
                                    ]),  
                                    html.Li(style={"padding-top": "5px"}, children=["As previously mentioned, exploitation of the Fifteenth Amendment’s loophole \
                                        regarding ", html.I("non"), "-racial discrimination (vis-à-vis the application of poll taxes, literacy tests, and grandfather \
                                        clauses) became standard practice for removing Black citizens from voter rolls during Jim Crow. And while these practices were \
                                        generally limited to Southern states, the practice of denying voting rights ", html.I("due to prior felony conviction"), " \
                                        also began in the South, and this would eventually become an institutional mainstay of Black voter disenfranchisement \
                                        nationwide.", dcc.Link(href="/sources-notes", children=[html.Sup("42")])
                                    ]), 
                                    # html.Li(children=["With racially-motivated incarceration we encounter \
                                    #     another perverse incentive structure, wherein criminalizing a political opponent permanently strips them of their political \
                                    #     rights, while in this case also contributing to the perception of Blacks as criminals and the normalization of policing with \
                                    #     political intent (to say nothing of the direct legal and financial effects borne upon the wrongfully convicted)."
                                    # ])               
                                    html.Li(style={"padding-top": "5px"}, children=["On the topic of policing: Extreme racial inequality in nationwide 21st-century \
                                        policing, from racial profiling in overly-aggressive traffic stops to violent stop-and-frisk encounters, backed by the \
                                        normalization of militarized police presence in Black communities nationwide, echoes patterns consistent with antebellum \
                                        Southern Slave Patrols, Black Codes of the late 1860s, and the brazen police brutality of the Jim Crow South.", 
                                        dcc.Link(href="/sources-notes", children=[html.Sup("43")]), " It’s worth noting, however, that Northern cities had already \
                                        established their own brand of violent, racially-charged professional police forces as early as the 1830s, initially oriented \
                                        toward controlling recent immigrants from Ireland, Germany, and Eastern Europe, so the routine violence and brutality inflicted \
                                        by Northern police toward Black refugees fleeing Southern persecution had plenty of precedent with previous influxes of ethnic \
                                        minorities.", dcc.Link(href="/sources-notes", children=[html.Sup("44")]), 
                                    ]),
                                    html.Img(src="/static/stockImages/school-segregation.jpg", style={"float": "right", "padding-left": "10px", "padding-top": "10px"}, 
                                        width="45%"),
                                    html.Li(style={"padding-top": "5px"}, children=["Racially segregated schools, though illegal in many states by the 1950s and \
                                        concentrated in the Jim Crow South, were widespread enough that the Supreme Court had its pick of venues to challenge the \
                                        practice in, selecting Kansas as its lead case in ", html.I("Brown v. Board of Education"), ". In doing so, the court was able \
                                        to go after school segregation without singling out the South, effectively using the ubiquity of this Southern export to go \
                                        after the institution without directly attacking its Southern proponents.", dcc.Link(href="/sources-notes", 
                                        children=[html.Sup("45")]), " Recent analysis shows racial integration in American schools to have peaked in the 1980s, \
                                        declining since to segregation levels worse than the 1970s.", dcc.Link(href="/sources-notes", children=[html.Sup("46")]), 
                                    ])
                                ])
                            ]),
                            html.Img(src="/static/stockImages/gone_with_the_wind.jpg", style={"float": "left", "padding-right": "10px", "padding-top": "5px"}, 
                                width="25%"),
                            html.P(className="card-text", children=[
                                "At a cultural level, this country continues to deal with its once ubiquitous embrace of ‘Lost Cause’ mythology, with 20th century \
                                media saturation of criminal Black ‘brute’ caricatures and Tarzan-esque tropes, with the legacy of nationwide support for the KKK and \
                                tepid reaction to public lynching, with the scientific community’s once fervent embrace of the Eugenics movement and its present-day \
                                relics like the SAT,", dcc.Link(href="/sources-notes", children=[html.Sup("47")])," and with Confederate flags flying at events in \
                                Northern and Western states (to say nothing of Southern states that were once part of the actual Confederacy). But behind these \
                                lingering expressions of white supremacy are decades of legislated, bureaucratic, institutional racism, all normalized after \
                                generations of unchallenged precedent and repetition, and all born out of a political system that granted its most avowed white \
                                supremacist element 3x-8x the influence of the rest of its voters, while silencing its African-American voices almost entirely."
                            ]),
                            html.Img(src="/static/stockImages/kkk-children.jpg", style={"float": "right", "padding-left": "10px", "padding-top": "5px"}, width="40%"),
                            html.P(className="card-text", children=[
                                "I’m not suggesting that Northern citizens aren’t culpable for their complicity in the adoption and expansion of a Jim Crow \
                                segregationist mindset nationally during those 90 years. Many of these campaigns were enacted with broad national support, some like \
                                the Eugenics movement actually emanated from North to South, all during an age of “Reconciliation” between Northern and Southern \
                                whites. I’m simply pointing out that the element of the country most notorious in its white supremacist ethos and agenda was also the \
                                most politically influential, and that this influence undoubtedly left an indelible institutional mark commensurate with that \
                                influence. Southern whites had a vested interest in slowing nationwide progress, in preserving another ‘peculiar’ socioeconomic \
                                status quo, and our electoral system provided them with a disproportionately loud megaphone to press their case."
                            ]),
                            html.Img(src="/static/stockImages/confederate-flag-capitol-riot.jpg", style={"float": "left", "padding-right": "10px", "padding-top": "5px"}, 
                                width="40%"),
                            html.P(className="card-text", children=[
                                "How many federal appointments, government programs, legal precedents, or pieces \
                                of national legislation passed during this era were cultivated with intent to perpetuate a status quo grounded in Southern whites \
                                silencing and extracting political influence from their Black populations? How many ideologies and narratives, designed to maintain \
                                entrenched Southern white interests but promoted as ‘heritage’ or as bedrock American virtues, were amplified and exported to the \
                                rest of the country during those nine decades? How many coalitions were built, compromises brokered, and principles abandoned in \
                                service of a hyper-enfranchised faction whose hold on power depended on the perpetuation and expansion of white supremacist ideology? \
                                And how many of the laws, institutions, and ideologies crafted in this reactionary white supremacist crucible continue to endure and \
                                thrive, at the national level, to this day?"
                            ]),
                        ])
                    ]),
                ])
            ]),
            html.Br(),html.Br(),
            dbc.Row([
                dbc.Col(md=6, children=[
                    html.H4(className="text-white", style={"text-align": "center"}, children=["Voter Weight per election: Antebellum period"]),
                    html.Div(style={"float": "right", "width": "30%", "padding-top": "10px"}, children=[
                        dcc.Dropdown(
                            id="slave-state-bias-figure-type",
                            options=[
                                {'label': 'Bar chart', 'value': 'bar_chart'},
                                {'label': 'Box plot', 'value': 'box_plot'},
                                {'label': 'Scatter plot: dots', 'value': 'scatter_dots'},
                                {'label': 'Scatter plot: bubbles', 'value': 'scatter_bubbles'},
                                {'label': 'Scatter plot: abbrevs', 'value': 'scatter_abbrevs'},
                                {'label': 'Map', 'value': 'map'},
                            ], 
                            value='bar_chart',
                        )
                    ]),
                    html.Br(),
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
                    html.Br(),
                    dcc.Graph(id="fig-bar-slave-state-bias2")
                ]),
                dbc.Col(md=6, children=[
                    html.H4(className="text-white", style={"text-align": "center"}, children=["Voter Weight per election: Reconstruction thru Jim Crow"]),
                    html.Div(style={"float": "right", "width": "30%", "padding-top": "10px"}, children=[
                        dcc.Dropdown(
                            id="suppress-state-bias-figure-type",
                            options=[
                                {'label': 'Bar chart', 'value': 'bar_chart'},
                                {'label': 'Box plot', 'value': 'box_plot'},
                                {'label': 'Scatter plot: dots', 'value': 'scatter_dots'},
                                {'label': 'Scatter plot: bubbles', 'value': 'scatter_bubbles'},
                                {'label': 'Scatter plot: abbrevs', 'value': 'scatter_abbrevs'},
                                {'label': 'Map', 'value': 'map'},
                            ], 
                            value='bar_chart',
                        )
                    ]),
                    html.Br(),
                    html.H4("Select year:", className="text-white"),
                    dcc.Slider(
                        id="suppress-state-bias-year-input",
                        min=1868,
                        max=1964,
                        step=None,
                        marks={
                            int(y): {'label': str(y), 'style': {'transform': 'rotate(45deg)', 'color': 'white'}}
                            for y in data_obj.all_years if y >= 1868 and y <= 1964
                        },
                        value=1932,
                    ),
                    html.Br(),
                    dcc.Graph(id="fig-bar-suppress-state-bias2")
                ])
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