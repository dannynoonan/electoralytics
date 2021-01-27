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
                html.H3("Calculating “Voter Weight” Per State"),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.H4("The math", className="card-title"),
                            html.P(className="card-text", children=[
                                "“Small-state bias,” “slave-state bias,” and this idea of “suppression-state bias” all derive from different legal statutes, \
                                census formulas, and state-level behaviors. Although different factors skew the relationship between apportionment and \
                                participation for each, throughout the electoralytics site I’ve applied the same “Voter Weight” calculation to determine any \
                                evidence of bias, in a uniform (you might say unbiased) fashion."
                            ]),
                            html.P(className="card-text", children=[
                                "Disproportionate voter influence in the Electoral College boils down to the ratio between two factors:",
                                html.Ul(children=[
                                    html.Li(children=[html.B("Popular Vote"), " (turnout / number of ballots cast)"]),
                                    html.Li(children=[html.B("Electoral College Votes"), " (based on population census, the three-fifths clause during slavery, \
                                        and the +2 senator “bicameral boost”)"])
                                ])
                            ]),
                            html.Img(style={"float": "left", "padding-right": "10px"}, src="/static/voteWeightEquations.png", width="400"),
                            html.P(className="card-text", children=[
                                "The higher the Popular Vote is relative to the Electoral College vote apportionment, the lower the impact of any individual \
                                voter in that state, since slicing the state’s pie into more pieces doesn’t change the overall size of the pie, it just reduces \
                                the size of each piece."
                            ]),
                            html.P(className="card-text", children=[
                                "The ratio generated by dividing Popular Vote (PV) by Electoral College Votes (ECV) gets us a “Popular Vote per Elector” (or \
                                PVPE) value, or the number of people whose voices are represented by a single Electoral College vote. On its own, this metric \
                                loses any meaning when compared between different years, so my Voter Weight calculation takes the additional step of normalizing \
                                PVPE against the nationwide PVPE average in a given year."
                            ]),
                            html.P(className="card-text", children=[
                                html.I("Disclaimer:"), " I’m neither a historian nor a mathematician, so I don’t know if this is ", html.I("the"), " way to \
                                measure these types of voter influence disparities, but it certainly is ", html.I("a"), " way is to measure them.",                            
                            ]),
                            html.P(className="card-text", children=[
                                "A couple general observations about Voter Weight:",
                                html.Ul(children=[
                                    html.Li("Voter Weight is a zero sum game: in aggregate all weights average out to 1.0, so an increase in one state must be \
                                        offset by a decrease in another"),
                                    html.Li("While a higher Voter Weight benefits those to whom it directly applies by amplifying their individual voice, it is \
                                        ultimately a marker of anti-democratic outcomes that favor one population over another"),
                                    html.Li("Regardless of which factors of apportionment or participation are responsible for shifts or distortions in Voter \
                                        Weight, the resulting comparison is apples-to-apples - that is, the same calculation can be applied regardless of \
                                        underlying bias / combination of biases")
                                ]),
                                "The higher the Popular Vote is relative to the Electoral College vote apportionment, the lower the impact of any individual \
                                voter in that state, since slicing the state’s pie into more pieces doesn’t change the overall size of the pie, it just reduces \
                                the size of each piece."
                            ]),
                        ])
                    ]),
                ]),
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([ 
                            html.H4("Example: Georgia vs Wisconsin in early 20th Century", className="card-title"),  
                            html.Img(style={"float": "right", "padding-left": "10px"}, src="/static/vwCalcSampler/popToEcWIGA1900.png", width="450"),
                            html.P(className="card-text", children=[
                                "Both Georgia’s and Wisconsin’s populations in the 1900 census (2.22 million and 2.07 million respectively) garnered 11 \
                                representatives and 13 Electoral College votes. In the 1904 congressional and presidential election that followed, 131K \
                                Georgians turned out to vote, while 443K turned out to vote in Wisconsin — more than triple that of Georgia. But, because \
                                federal influence-allocation is determined by population census, both states sent the same number of reps to congress and \
                                the same number of electors to the EC, despite the disparity in voter participation. The net effect is that, pound for pound, \
                                any individual Wisconsinite’s voice counted for less than a third of a Georgian’s voice in that election:",                              
                            ]),
                            html.Br(),
                            dbc.CardImg(src="/static/vwCalcSampler/vwCalcWIGA1904.png", top=False),
                            html.Br(), html.Br(),
                            html.P(className="card-text", children=[
                                "A few decades later, despite the intervening rise of Progressivism and passage of the 19th Amendment guaranteeing women \
                                the right to vote, the disparity between these two states had widened: each state’s population in the 1930 census garnered \
                                it 10 representatives and 12 EC votes, but in the 1932 election 1.11M people voted in Wisconsin compared to 256K in Georgia, \
                                giving each ballot cast in Georgia more than 4X the national-level influence of a Wisconsinite’s:",
                            ]),
                            dbc.CardImg(src="/static/vwCalcSampler/vwCalcWIGA1932.png", top=False),
                            html.Br(), html.Br(),
                            html.P(className="card-text", children=[
                                "It’s worth noting that this 3–4X disparity suggests a voter suppression dragnet in Georgia that reaches well beyond its \
                                African American population (which was 46.7% of Georgia’s total population in 1900). My intent isn’t to get too deep into the \
                                historical weeds here, but this might be the effect of poll taxes aimed not only to disenfranchise Blacks, but also to purge \
                                poor whites with Populist party sympathies from the voter rolls (since — per this Wikipedia page on Southern disenfranchisement \
                                after Reconstruction — these two factions had momentarily joined forces to take over a handful of Southern state legislatures \
                                in the 1890s, prompting swift retaliation by Southern white elites who rewrote state constitutions en masse to implement poll \
                                taxes and other disenfranchising devices). While African Americans were undoubtedly the principal target of Southern \
                                disenfranchisement practices, the idea that certain forms of voter suppression also impacted poor whites should be factored \
                                into any interpretation of the data. But demographics aside, the Voter Weight / voter suppression calculation is the same — it \
                                may just turn out that suppression-state bias goes beyond “five-fifths.”",
                            ]),
                        ])
                    ])
                ]),
            ])
        ])
    ])
])