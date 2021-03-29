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
                        html.A(className="page-link", href="/voter-weight-electoral-college-bias-page2", children=[
                            "← Part 2: Small-state bias and slave-state bias: As the framers intended"
                        ])
                    ]),
                    html.Li(className="page-item flex", style={"width": "20%"}),
                    html.Li(className="page-item flex", style={"width": "50%", "text-align": "right"}, children=[
                        html.A(className="page-link", href="/voter-weight-electoral-college-bias-page4", children=[
                            "Part 4: Suppression-state bias →"
                        ])
                    ]),
                ])
            ]),
            html.Hr(className="border-light"),
            html.Br(),
            dbc.Row(className="text-white", justify="center", align="center", children=[
                html.H3("Part 3: Reconstruction and Black voting rights"),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.Div(className="card-text lead", style={"margin-left": "50px", "margin-right": "50px"}, children=[
                                html.P(style={"font-style": "italic"}, children=[
                                    "From the nature of man we may be sure, that those who have power in their hands will not give it up while they can retain \
                                    it. On the contrary we know they will always when they can rather increase it.",
                                    dcc.Link(href="/sources-notes", children=[html.Sup("5")]),
                                ]),
                                html.P("—George Mason, at the Constitutional Convention in 1787")
                            ]),
                            html.Br(),
                            html.H4("Black suffrage: Equality, security, morality"),
                            html.P(className="card-text", children=[
                                "The enfranchisement of former slaves has a feeling of logical inevitability in hindsight, but during the late 1860s Black \
                                suffrage was anything but a certainty. Native Americans, recently arrived Chinese and Europeans, and most notably the entire \
                                population of American women did not yet have the vote, so in the mind of the white Northerner (to say nothing of the white \
                                Southerner) the freedmen’s nascent elevation out of slavery was not part-and-parcel with his evolution into active political \
                                participant. But a combination of factors, ranging from the noble and moral to the practical and political, would ultimately \
                                galvanize popular support behind the movement for Black enfranchisement."
                            ]),
                            html.P(className="card-text", children=[
                                "Beginning with speeches and publications from Northern Blacks and former slaves, bolstered by the tireless evangelism and \
                                implacability of white abolitionist publishers and politicians, the message of empowering and stabilizing Black equality via \
                                suffrage steadily moved the Union-loyal states from a position of wide skepticism to one of broad support. Out front on \
                                pro-suffrage messaging was Frederick Douglass, emphasizing the the essential humanity and security conferred by enfranchising \
                                free Blacks to the Massachusetts Anti-Slavery Society in 1865:"
                            ]),
                            html.Div(className="card-text", style={"margin-left": "50px", "margin-right": "50px"}, children=[
                                html.P(style={"font-style": "italic"}, children=[
                                    "I am for the immediate, unconditional, and universal enfranchisement of the Black man, in every state in the Union. Without \
                                    this his liberty is a mockery; without this, you might as well almost retain the old name of slavery for his condition; for, in \
                                    fact, if he is not the slave of the industrial master, he is the slave of society, and holds his liberty as a privilege, not as \
                                    a right. He is at the mercy of the mob, and has no means of protecting himself.",
                                    dcc.Link(href="/sources-notes", children=[html.Sup("7")]),
                                ]),
                            ]),
                            html.P(className="card-text", children=[
                                "This argument for the practical necessity of suffrage for freedmen was echoed in German-born Carl Schurz’s ", 
                                dcc.Link("field report on post-war conditions in the South", target="_blank", 
                                href="https://wwnorton.com/college/history/america9/brief/docs/CSchurz-South_Report-1865.pdf"), ". In his view, Black \
                                enfranchisement would be “the best permanent protection against oppressive class-legislation, as well as against individual \
                                persecution.”", dcc.Link(href="/sources-notes", children=[html.Sup("8")]), " The argument for Black suffrage as a shield against \
                                regional racial tyranny was further amplified by Black Southerners such as John F. Cook, descendent of an affluent free Black family \
                                in New Orleans:"
                            ]),
                            html.Div(className="card-text", style={"margin-left": "50px", "margin-right": "50px"}, children=[
                                html.P(style={"font-style": "italic"}, children=[
                                    "Without the right of suffrage, we are without protection, and liable to combinations of outrage. Petty officers of the law, \
                                    respecting the source of power, will naturally defer to the one having a vote, and the partiality thus shown will work much to \
                                    the disadvantage of the colored citizens.",
                                    dcc.Link(href="/sources-notes", children=[html.Sup("9")]),
                                ]),
                            ]),
                        ])
                    ])
                ]),
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.H4("Black suffrage: The political argument"),
                            html.P(className="card-text", children=[
                                "From the vantage point of Northern legislators, moral justice and egalitarian ethics were only part of the total argument for Black \
                                suffrage. Beyond the soaring rhetoric and appeals to rational humanity, the basic math of Congressional and Electoral College \
                                representation ultimately played a central role in accelerating expanded suffrage as well. This tied directly to the prewar status \
                                quo: with freedmen now counted as full citizens rather than three-fifths chattel slaves, Southern states lay poised to receive even \
                                greater political influence vis-à-vis Congressional and Electoral College representation than they’d had prior to the Civil War. \
                                Absent any buffer or hedge against this, allowing Southern representatives back into Congress risked the reversal of all political \
                                and legislative gains made since the war."
                            ]),
                            html.P(className="card-text", children=[
                                "For a time, two paths were pursued through Constitutional Amendment:",
                                html.Ol(children=[
                                    html.Li("Give all male citizens over 21 the right to vote, and count every citizen in each state’s basis for representation"),
                                    html.Li("Permit each state to determine its own voting eligibility, but incentivize them toward franchise inclusivity by reducing \
                                        the state’s representation in proportion to the number of eligible males prevented from voting")
                                ])
                            ]),
                            html.P(className="card-text", children=[
                                "This statement from the ", dcc.Link("Congressional Joint Committee on Reconstruction", target="_blank",
                                href="https://en.wikipedia.org/wiki/United_States_Congressional_Joint_Committee_on_Reconstruction"), " in 1866 lays out the basic dilemma, \
                                hinting at their willingness to consider reduced representation to non-compliant states as an alternative to full enfranchisement of \
                                former slaves:"
                            ]),
                            html.Div(className="card-text", style={"margin-left": "50px", "margin-right": "50px"}, children=[
                                html.P(style={"font-style": "italic"}, children=[
                                    "It did not seem just or proper that all the political advantages derived from [Southern Blacks] becoming free should be confined \
                                    to their former masters, who had fought against the Union, and withheld from themselves, who had always been loyal… [our] committee \
                                    came to the conclusion that political power should be possessed in all the states exactly in proportion as the right of suffrage \
                                    should be granted, without distinction of color or race…",
                                    dcc.Link(href="/sources-notes", children=[html.Sup("11")]),
                                ]),
                            ]),
                            html.P(className="card-text", children=[
                                "And indeed, language along these lines ends up making it into ", dcc.Link("Section 2 of the Fourteenth Amendment", target="_blank",
                                href="https://en.wikipedia.org/wiki/Fourteenth_Amendment_to_the_United_States_Constitution#Section_2:_Apportionment_of_Representatives"),
                                ", also known as the “reduction clause:”"
                            ]),
                            html.Div(className="card-text", style={"margin-left": "50px", "margin-right": "50px"}, children=[
                                html.P(style={"font-style": "italic"}, children=[
                                    "When the right to vote at any election for the choice of electors for President..., Representatives in Congress, or [other \
                                    elected officials] is denied to any of the male inhabitants of such State, being twenty-one years of age, and citizens of the \
                                    United States, ...the basis of representation therein shall be reduced in the proportion which the number of such male citizens \
                                    shall bear to the whole number of male citizens twenty-one years of age in such State.",
                                    dcc.Link(href="/sources-notes", children=[html.Sup("12")]),
                                ]),
                            ]),
                            html.P(className="card-text", children=[
                                "Prior to the Civil War, deference to “state sovereignty” was presumed as it related to voting restrictions, so this nascent attempt \
                                to link a state’s embrace of expanded franchise with its Electoral College influence and Congressional representation was a radical \
                                shift. Indeed Section 2 appears to have been one of the most contested parts of the sprawling Fourteenth Amendment,",
                                dcc.Link(href="/sources-notes", children=[html.Sup("TODO")]), " but the advent of universal Black male suffrage in the Fifteenth \
                                Amendment ultimately overshadowed any of the nuances of enfranchisement and apportionment laid out in the Fourteenth by plainly \
                                asserting that all freedmen would be counted, and all freedmen would be allowed to vote - period."
                            ]),
                            html.P(className="card-text", children=[
                                "Thus, after several twists and convulsions, Northern consensus arrived at a hybrid moral-political solution: retain political \
                                influence in the South by extending suffrage to Union-loyal Southern Blacks."
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
                            html.Div(className="card-text lead", style={"margin-left": "50px", "margin-right": "50px"}, children=[
                                html.P(style={"font-style": "italic"}, children=[
                                    "One of the great ironies of American history is that the end of slavery actually made the white power structures in the \
                                    former slave states stronger.", dcc.Link(href="/sources-notes", children=[html.Sup("14")]),
                                ]),
                                html.P(children=["—Jesse Wegman, ", html.I("“Let the People Pick the President”")])
                            ]),
                            html.Br(),
                            html.H4("Reconstruction Amendments in practice"),
                            html.P(className="card-text", children=[
                                "The voting and legal protections of the Fourteenth and Fifteenth Amendments led to a true flourishing of multi-racial democracy \
                                during Reconstruction. Even prior to their passage and ratification, the Congressional Reconstruction Acts of 1867 set every former \
                                Confederate state on a path toward a greatly expanded electorate. Compared with a total of 721,191 (white) voters in 1860, the \
                                combined turnout at the constitutional conventions of 1867 nearly doubled this figure at 1,363,640, of which more than half the \
                                participants were Black.", dcc.Link(href="/sources-notes", children=[html.Sup("TODO")]),
                            ]),
                            html.P(className="card-text", children=[
                                "But the era was short-lived, as even the most radical abolitionists feared it might be. Concerns regarding federally-imposed \
                                enfranchisement, such as these published by William Lloyd Garrison in ", html.I("The Liberator"), " in 1864, were eerily prescient:"
                            ]),
                            html.Div(className="card-text", style={"margin-left": "50px", "margin-right": "50px"}, children=[
                                html.P(style={"font-style": "italic"}, children=[
                                    "If the freed blacks were admitted to the polls by… fiat, [I do not] see any permanent advantage likely to be secured by it; \
                                    for, submitted to as a necessity from the outset, as soon as the state was organized and left to manage its own affairs, the \
                                    white population, with their superior… wealth and power, would unquestionably alter the franchise in accordance with their \
                                    prejudices, and exclude those thus summarily brought to the polls. Coercion would gain nothing. In other words… universal \
                                    suffrage will be hard to win and to hold without general preparation of feeling and sentiment.",
                                    dcc.Link(href="/sources-notes", children=[html.Sup("15")]),
                                ]),
                            ]),
                            html.P(className="card-text", children=[
                                "Garrison's trepidation that voting rights may not be secure in the aftermath of Reconstruction was widely felt. Legislators were \
                                not naive to these concerns, and the Reconstruction amendments anticipated them with a political fail-safe mechanism: The Fifteenth \
                                amendment was unambiguous in its language prohibiting race-based voting restriction, but if Southern whites succeeded in evading \
                                the Fifteenth and disenfranchising their Black citizens then the Fourteenth amendment's reduction clause would kick in, preventing \
                                those states from reaping the representational benefits of fully-counted Black citizens. Given the choice to embrace multi-racial \
                                voter access or accept reduced national influence, the expectation was that former Confederate states would choose not to give up \
                                their influence."
                            ]),
                            html.P(className="card-text", children=[
                                "In practice, however, it would be nearly a century before the voting provisions of either amendment were meaningfully enforced."
                            ]),
                            html.Br(),
                            html.H4("Voter suppression as a “five-fifths” scheme"),
                            html.P(className="card-text", children=[
                                "A recent episode of ", html.I("NPR’s Throughline"), " (the original inspiration for this project!) explores the end of \
                                Reconstruction, the rise of Black voter suppression, and its effects in terms of Electoral College influence. The show's hosts, \
                                joined by Yale Professor and noted constitutional scholar Akhil Reed Amar, lay out how the three-fifths compromise was effectively \
                                replaced by an even ", html.I("less"), " equitable permutation of that infamous inaugural Electoral College bias. Part of their \
                                “(mis)Representative Democracy” series, the full episode is 58 minutes, but this ",  dcc.Link("5-minute video snippet", 
                                href="https://www.npr.org/2020/09/30/918717270/the-electoral-college", target="_blank"), " gets to the heart of what caught my \
                                attention:"
                            ]),
                        ])
                    ])
                ]),
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.Iframe(id="jw_embed", width="100%", height="423", 
                                src="https://www.npr.org/embedded-video?storyId=918717270&mediaId=930549092&jwMediaType=null"),
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
                                    "By suppressing Black voters, the southern states actually got a better deal when the three-fifths compromise ended.",
                                    dcc.Link(href="/sources-notes", children=[html.Sup("2")]),
                                ])
                            ]),
                            html.Br(),
                            html.P(className="card-text", children=[
                                "By the 1880s and 1890s, Southern white “Redeemer” governments were siphoning influence from disenfranchised Black electorates in \
                                every Southern state, flouting the Reconstruction Amendments through the legally spurious application of poll taxes, literacy tests, \
                                grandfather clauses, as well as more direct intimidation and violence. Every former Confederate state would follow a similar template \
                                of racial voter suppression, with whites silencing the voices of their Black citizens while enjoying a degree of hyper-enfranchisement \
                                for the next 90-odd years that would ultimately far exceed that which they had enjoyed during slavery."
                            ]),
                            html.P(className="card-text", children=[
                                "Listening to this ", html.I("Throughline"), " episode was the first time I’d considered that suppressing the Black vote had been \
                                part-and-parcel with Southern whites not just retaining, but actually ", html.I("increasing"), " their disproportionate pre-war \
                                influence on national elections. To what extent did the warped racist logic driving Southern Redeemers to shamelessly, systematically, \
                                and violently prevent their Black populations from voting between the end of Reconstruction in 1877 and the signing of the Voting \
                                Rights Act in 1965 reflect a sense of lingering electoral entitlement, an expectation that the same preferential treatment enshrined \
                                in the three-fifths clause of the Constitution should elevate the influence of Southern whites going into the 20th century?",
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
                        html.A(className="page-link", href="/voter-weight-electoral-college-bias-page2", children=[
                            "← Part 2: Small-state bias and slave-state bias: As the framers intended"
                        ])
                    ]),
                    html.Li(className="page-item flex", style={"width": "20%"}),
                    html.Li(className="page-item flex", style={"width": "50%", "text-align": "right"}, children=[
                        html.A(className="page-link", href="/voter-weight-electoral-college-bias-page4", children=[
                            "Part 4: Suppression-state bias →"
                        ])
                    ]),
                ])
            ]),
        ])
    ])
])