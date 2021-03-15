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
                        html.A(className="page-link", href="/voter-weight-conclusions", children=[
                            "Part 4: Conclusions and Discussion →"
                        ])
                    ]),
                ])
            ]),
            html.Hr(className="border-light"),
            html.Br(),
            dbc.Row(className="text-white", justify="center", align="center", children=[
                html.H3("Part 3: Reconstruction, Redemption, and suppression-state bias"),
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
                            html.H4("Reconstruction and Black voting rights"),
                            html.P(className="card-text", children=[
                                "The enfranchisement of former slaves has a feeling of logical inevitability in hindsight, but during the late 1860s Black \
                                suffrage was anything but a certainty. Native Americans, recently arrived Chinese and Europeans, and most notably the entire \
                                population of American women did not yet have the vote, so in the mind of the white Northerner (to say nothing of the white \
                                Southerner) the freedmen’s nascent elevation out of slavery was not part and parcel with evolution into active political \
                                participant. But a combination of factors, ranging from the noble and moral to the practical and political, would ultimately \
                                galvanize popular support behind the movement for Black enfranchisement. Beginning with speeches and publications from Northern \
                                Blacks and former slaves, bolstered by the tireless evangelism and implacability of Congressional abolitionists, the message of \
                                empowering and stabilizing Black equality via suffrage steadily moved the nation from a position of wide skepticism to one of \
                                broad support in the years immediately following the Civil War."
                            ]),
                            html.P(className="card-text", children=[
                                "The oratory of Wendell Phillips at the annual meeting of the Massachusetts Anti-Slavery Society in 1865 captures the spirit \
                                being promulgated from the “radical” Republican wing at the time:"
                            ]),
                            html.Div(className="card-text", style={"margin-left": "50px", "margin-right": "50px"}, children=[
                                html.P(style={"font-style": "italic"}, children=[
                                    "Our philosophy of government since the 4th of July, 1776, is that no class is safe, no freedom is real, no emancipation is \
                                    effectual which does not place in the hands of the man himself the power to protect his own rights.",
                                    dcc.Link(href="/sources-notes", children=[html.Sup("6")]),
                                ]),
                            ]),
                            html.P(className="card-text", children=[
                                "Out front on pro-suffrage messaging was Frederick Douglass, emphasizing the the essential humanity and security conferred by \
                                enfranchising free Blacks:"
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
                                enfranchisement would be “the best permanent protection against oppressive class-legislation, as wellas against individual \
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
                            html.P(className="card-text", children=[
                                "But the moral justice and egalitarian ethics were only one part of the total argument, at least from the vantage point of Republican \
                                legislators. Beyond the soaring rhetoric and appeals to rational humanity, the basic math of Congressional and Electoral College \
                                representation ultimately played a central role in accelerating expanded suffrage as well. This tied directly to the prewar status \
                                quo: with freedmen now counted as full citizens rather than three-fifths chattel slaves, Southern states lay poised to receive even \
                                greater political influence vis-a-vis Congressional and Electoral College representation than they’d had prior to the Civil War. \
                                Absent any buffer or hedge against this, allowing Southern representatives back into Congress risked the reversal of all political \
                                and legislative gains made since the war."
                            ]),
                        ])
                    ])
                ]),
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.P(className="card-text", children=[
                                "For a time, two paths were pursued through Constitutional Amendment:",
                                html.Ol(children=[
                                    html.Li("Give all male citizens over 21 the right to vote, and count every citizen in each state’s basis for representation"),
                                    html.Li("Permit each state to determine its own voting eligibility, but incentivize them toward franchise inclusivity by reducing \
                                        the state’s representation in proportion to the number of eligible males prevented from voting")
                                ])
                            ]),
                            html.P(className="card-text", children=[
                                "W.E.B. Du Bois lays it out plainly, emphasizing the coalition between Northern industry and what he called the “abolitionist-democracy” \
                                movement, the two core Unionist Republican factions whose aligned agendas brought Black enfranchisement to the fore:"
                            ]),
                            html.Div(className="card-text", style={"margin-left": "50px", "margin-right": "50px"}, children=[
                                html.P(style={"font-style": "italic"}, children=[
                                    "When the South went beyond reason and truculently demanded not simply its old political power but increased political power based \
                                    on disfranchised Negroes, which it openly threatened to use for the revision of the tariff, for the repudiation of the national \
                                    debt, for the disestablishing of the national banks, and for putting the new corporate form of industry under strict state \
                                    regulation and rule, Northern industry was frightened and began to move towards… endowed Negro education, legal civil rights, and \
                                    eventually even votes for Negroes to offset the Southern threat of economic attack.",
                                    dcc.Link(href="/sources-notes", children=[html.Sup("10")]),
                                ]),
                            ]),
                            html.P(className="card-text", children=[
                                "This statement from the ", dcc.Link("Congressional Joint Committee on Reconstruction", target="_blank",
                                href="https://en.wikipedia.org/wiki/United_States_Congressional_Joint_Committee_on_Reconstruction"), " in 1866 lays out the basic dilemma, \
                                as well as their inclination to consider reduced representation to non-compliant states as an alternative to the enfranchisement of \
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
                                ":"
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
                                "Prior to the Civil War, full deference to states to prescribe their own voting restrictions was a “settled” Constitutional matter, \
                                so this nascent attempt to link a state’s embrace of expanded franchise with its Electoral College influence and Congressional \
                                representation was fairly radical. Indeed Section 2 appears to have been one of the most contested parts of the sprawling Fourteenth \
                                Amendment, but the advent of universal Black male suffrage in the Fifteenth Amendment ultimately overshadowed any of the nuances of \
                                enfranchisement and apportionment by plainly asserting that every man would be counted, and every man would be allowed to vote - \
                                period, end of story."
                            ]),
                            html.P(className="card-text", children=[
                                "Thus, after several twists and convulsions, Northern consensus arrived at a hybrid moral-political solution: retain political \
                                influence in the South by extending suffrage to four million Union-loyal freedmen. Ultimately, unflinching Congressional stalwarts \
                                like Charles Sumner, here voicing his disagreement with concessions on race built into the Fourteenth Amendment, would win the day \
                                with passage of the Fifteenth Amendment:"
                            ]),
                            html.Div(className="card-text", style={"margin-left": "50px", "margin-right": "50px"}, children=[
                                html.P(style={"font-style": "italic"}, children=[
                                    "I have fought a long battle with slavery; and I confess my solicitude when I see any thing that looks like concession to it... \
                                    From the beginning of our history the country has been afflicted with compromise. It is by compromise that human rights have \
                                    been abandoned… The country needs repose after all its trials, and repose... cannot be found by inserting in your constitution \
                                    the disfranchisement of a race.",
                                    dcc.Link(href="/sources-notes", children=[html.Sup("13")]),
                                ]),
                            ]),
                        ])
                    ])
                ])
            ]),
            html.Br(),
            html.Hr(className="border-light"),
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
                            html.H4("Voter suppression as a “five-fifths” scheme"),
                            html.P(className="card-text", children=[
                                "The voting and legal protections of the Fourteenth and Fifteenth Amendments led to a true flourishing of multi-racial democracy \
                                during Reconstruction. Even prior to their passage and ratification, the Congressional Reconstruction Acts of 1867 set every former \
                                Confederate state on a path toward a greatly expanded electorate. Compared with a total of 721,191 (white) voters \in 1860, the \
                                combined turnout at the constitutional conventions of 1867 nearly doubled this figure at 1,363,640, of which more than half the \
                                participants were Black."
                            ]),
                            html.P(className="card-text", children=[
                                "But the era was short-lived, as even the most radical abolitionists feared it might be. William Lloyd Garrison’s early qualms \
                                regarding federally-imposed enfranchisement, expressed here as published in ", html.I("The Liberator"), " in 1864, were eerily prescient:"
                            ]),
                            html.Div(className="card-text", style={"margin-left": "50px", "margin-right": "50px"}, children=[
                                html.P(style={"font-style": "italic"}, children=[
                                    "Nor, if the freed blacks were admitted to the polls by… fiat, do I see any permanent advantage likely to be secured by it; \
                                    for, submitted to as a necessity from the outset, as soon as the state was organized and left to manage its own affairs, the \
                                    white population, with their superior… wealth and power, would unquestionably alter the franchise in accordance with their \
                                    prejudices, and exclude those thus summarily brought to the polls. Coercion would gain nothing. In other words… universal \
                                    suffrage will be hard to win and to hold without general preparation of feeling and sentiment.",
                                    dcc.Link(href="/sources-notes", children=[html.Sup("15")]),
                                ]),
                            ]),
                            html.P(className="card-text", children=[
                                "Garrison wasn’t the only politically-engaged Northern abolitionist to discern the potential for voting rights to be rolled back \
                                in the aftermath of Reconstruction. His trepidation reflected the concerns of legislators who foresaw the challenge of holding the \
                                fragile multi-racial democratic experiment together. In theory, the Fifteenth Amendment would guarantee Black suffrage, and the \
                                Fourteenth Amendment would operate as a fail-safe to prevent Southern whites from both disenfranchising their Black citizens and \
                                siphoning the influence afforded by counting those Black citizens as fully five-fifths rather than three-fifths in the census."
                            ]),
                            html.P(className="card-text", children=[
                                "In practice, however, it would be nearly a century before either amendment was utilized to this effect."
                            ]),
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
                                "By the late 1870s, Southern white “Redeemer” governments were siphoning influence from disenfranchised Black electorates in nearly \
                                every Southern state, flouting the Reconstruction Amendments through the legally spurious application of poll taxes, literacy tests, \
                                grandfather clauses, as well as more direct intimidation and violence. Every former Confederate state would follow a similar template \
                                of racial voter suppression, with whites silencing the voices of their Black citizens while enjoying a degree of hyper-enfranchisement \
                                for the next 90-odd years that would ultimately far exceed that which they had enjoyed during slavery."
                            ]),
                            html.P(className="card-text", children=[
                                "Hearing the overview laid out in the ", html.I("Throughline"), " episode was the first time I’d considered that suppressing the Black \
                                vote had been part-and-parcel with Southern whites not just retaining, but actually ", html.I("increasing"), " their disproportionate \
                                pre-war influence on national elections, as compared to voters in other states. Did the warped racist logic driving Southern Redeemers \
                                to shamelessly, systematically, and violently prevent their Black populations from voting between the end of Reconstruction in 1877 \
                                and the signing of the Voting Rights Act in 1965 reflect a sense of lingering electoral entitlement, an expectation that the same \
                                preferential treatment for enshrined in the three-fifths clause of the Constitution?",
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
                            html.Div(className="card-text", style={"margin-left": "50px", "margin-right": "50px", "font-size": "12pt"}, children=[
                                html.P(style={"font-style": "italic"}, children=[
                                    "By 1900… gains under the Thirteenth, Fourteenth, and Fifteenth Amendments and various Reconstruction Acts had largely disappeard \
                                    in the former Confederacy. Not only had the US Supreme Court in 1896 validated “separate but equal” in Plessy v. Ferguson, but \
                                    the right to vote had become a distant memory for a huge percentage of Southern black people. Because black voters could have an \
                                    enormous impact on election outcomes—some 90 percent of all African Americans live in the South in 1900—just as they \
                                    demonstrated during Reconstruction, it was of the utmost importance to rob them of the possibility of voting in Southern \
                                    elections. And robbed they were.", dcc.Link(href="/sources-notes", children=[html.Sup("16")]),
                                ]),
                                html.P(children=["—Henry Louis Gates, Jr., ", html.I("“Stony the Road: Reconstruction, White Supremacy, and the Rise of Jim Crow”")])
                            ]),
                            html.Br(),
                            html.H4("Suppression-state bias groupings"),
                            html.P(className="card-text", children=[
                                "Considering our 21st century grumbling about how small-state bias amplifies the voice of an Alaska voter at the expense of a \
                                California voter, and the stomach-churning 18th-19th century slave-state bias which amplified the voice of a Virginia slave-owner \
                                relative to a New York merchant, I was very curious how this third category of hyper-enfranchisement bias in the Jim Crow South \
                                would stack up against those other two."
                            ]),
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
                                "It doesn’t take a degree in advanced statistics to discern from these charts that the hyper-enfranchisement effect evident in former \
                                Confederate states during the Jim Crow Era dwarfs the other biases we’ve explored so far. Highlighting just one example: If Voter \
                                Weight in 1940 was 7.5 in South Carolina compared with 0.96 in Connecticut, that means pound-for-pound it would take 7-8 votes cast \
                                in Connecticut to equal the influence of a single vote cast in South Carolina. This represents a staggering disparity in the influence \
                                of individual voters—that is, those permitted to vote—in these states."
                            ]),
                            html.P(className="card-text", children=[
                                "Absent the factors of state size (both state’s populations earned them 8 Electoral College votes) or slavery (abolished a full 75 \
                                years prior) the bias revealed in this bar graph has no explanation in Electoral apportionment “originalist” logic. Nothing accounts \
                                for this disparity other than staggering differences in voter participation, almost certainly tied to massive institutional voter \
                                suppression."
                            ]),
                            html.Br(),
                            html.Div(className="card-text", style={"margin-left": "50px", "margin-right": "50px", "font-size": "12pt"}, children=[
                                html.P(style={"font-style": "italic"}, children=[
                                    "During the first decades of the twentieth century, white southerners were wielding more influence in national politics than \
                                    they had before the Civil War. After the abolition of slavery and the “three-fifths” clause, African-Americans counted fully \
                                    toward representation, and southern states consequently gained additional seats in the House of Representatives and votes in \
                                    the Electoral College. Yet once blacks were again denied the right to vote, white Democrats effectively became the \
                                    beneficiaries of an unwritten “five-fifths” clause: they wielded national power on their own behalf and in the name of the \
                                    region’s entire African-American population.", dcc.Link(href="/sources-notes", children=[html.Sup("17")]),
                                ]),
                                html.P(children=["—Alexander Keyssar, ", html.I("“Why Do We Still Have the Electoral College?”")])
                            ]),
                        ])
                    ]),
                    html.Br(),
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
                        html.A(className="page-link", href="/voter-weight-conclusions", children=[
                            "Part 4: Conclusions and Discussion →"
                        ])
                    ]),
                ])
            ]),
        ])
    ])
])