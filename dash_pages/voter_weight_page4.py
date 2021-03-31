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
                        html.A(className="page-link", href="/voter-weight-electoral-college-bias-page3", children=[
                            "← Part 3: Reconstruction and Black voting rights"
                        ])
                    ]),
                    html.Li(className="page-item flex", style={"width": "20%"}),
                    html.Li(className="page-item flex", style={"width": "50%", "text-align": "right"}, children=[
                        html.A(className="page-link", href="/voter-weight-results", children=[
                            "Part 5: Results and Observations →"
                        ])
                    ]),
                ])
            ]),
            html.Hr(className="border-light"),
            html.Br(),
            dbc.Row(className="text-white", justify="center", align="center", children=[
                html.H3("Part 4: Suppression-state bias"),
            ]),
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
                                straight-forward as grouping by “Slave states” vs “Free states.” Most slave states seceded to join the Confederacy during the Civil \
                                War, but a small handful of “Border states,” where slavery continued to be legal when Lincoln assumed the presidency, remained loyal \
                                to the Union."
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
                            html.Br(),
                        ])
                    ]),
                    html.Br(),
                ]),
                dbc.Col(md=6, children=[
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
                    dcc.Graph(id="fig-scatter-dots-suppress-state-bias"),
                    html.P(className="card-text", style={"padding": "5px"}, children=[
                        html.Small("Figure 6: Suppression-state bias, shown by color shading states by Civil War groupings, and plotting voter turnout on the x \
                            axis against Electoral College Votes on the y axis. The average voter turnout tally per Electoral College vote (where the Voter Weight \
                            ratio is 1.0) is plotted as a diagonal line signifying the nationwide mean. States whose dots appear above and to the left of the \
                            nationwide mean line have Voter Weights greater than 1, those whose dots are below and to the right have Voter Weights less than 1."),
                    ]),
                    html.Br(),
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
                        html.A(className="page-link", href="/voter-weight-electoral-college-bias-page3", children=[
                            "← Part 3: Reconstruction and Black voting rights"
                        ])
                    ]),
                    html.Li(className="page-item flex", style={"width": "20%"}),
                    html.Li(className="page-item flex", style={"width": "50%", "text-align": "right"}, children=[
                        html.A(className="page-link", href="/voter-weight-results", children=[
                            "Part 5: Results and Observations →"
                        ])
                    ]),
                ])
            ]),
        ])
    ])
])