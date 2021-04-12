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
                        html.A(className="page-link", href="/voter-weight-conclusions", children=[
                            "← Part 6: Conclusions and interpretation"
                        ])
                    ]),
                    html.Li(className="page-item flex", style={"width": "20%"}),
                    html.Li(className="page-item flex", style={"width": "50%", "text-align": "right"}, children=[
                        html.A(className="page-link", href="/voter-weight-timeline-visualization", children=[
                            "Appendix 2: Annotated Timeline Charting Voter Weight Trends →"
                        ])
                    ]),
                ])
            ]),
            html.Hr(className="border-light"),
            html.Br(),
            dbc.Row(className="text-white", justify="center", align="center", children=[
                html.H3("Appendix 1: Calculating “Voter Weight” Per State"),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.Div(className="card-text lead", style={"margin-left": "50px", "margin-right": "50px"}, children=[
                                html.P(style={"font-style": "italic"}, children=[
                                    "Because each state gets its prescribed number of electors based on total population, not on how many of its residents \
                                    cast a ballot, there is no incentive to expand the electorate.",
                                    dcc.Link(href="/sources-notes", children=[html.Sup("44")]),
                                ]),
                                html.P(children=["—Jesse Wegman, ", html.I("“Let the People Pick the President”")])
                            ]),
                            html.Br(),
                            html.H4("Ratios and averages", className="card-title"),
                            html.P(className="card-text", children=[
                                "“Small-state bias,” “slave-state bias,” and this idea of “suppression-state bias” all derive from different legal statutes, \
                                census formulas, and state-level behaviors. Although different factors skew the relationship between apportionment and \
                                participation for each variant of bias, the Voter Weight calculation works the same way for each, agnostic of which type of \
                                bias it is measuring. It is a generic method of measuring imbalances that arise in the Electoral College system."
                            ]),
                            html.P(className="card-text", children=[
                                "Disproportionate voter influence in the Electoral College boils down to the ratio between two factors:",
                                html.Ul(children=[
                                    html.Li(children=[html.B("Popular Vote"), " (turnout / number of ballots cast)"]),
                                    html.Li(children=[html.B("Electoral College Votes"), " (based on population census, the three-fifths clause during slavery, \
                                        and the +2 senator “bicameral boost”)"])
                                ])
                            ]),
                            html.Img(src="/static/vwMath/derivingPvpeVw.png", style={"float": "left", "padding-right": "10px"}, width="55%"),
                            html.P(className="card-text", children=[
                                "The higher the Popular Vote is relative to the Electoral College vote apportionment, the lower the impact of any individual \
                                voter in that state, since slicing the state’s pie into more pieces doesn’t change the overall size of the pie, it just reduces \
                                the size of each piece."
                            ]),
                            html.P(className="card-text", children=[
                                "The ratio generated by dividing Popular Vote (turnout) by Electoral College Votes gets us a “Popular Vote per Elector” (or \
                                PVPE) value, equaling the number of people whose voices are represented by a single Electoral College vote."
                            ]),
                            html.P(className="card-text", children=[
                                "On its own, this absolute PVPE metric loses any meaning when compared between different years, so my Voter Weight calculation \
                                takes the additional step of normalizing each state’s PVPE against the nationwide PVPE average in a given year."
                            ]),
                            html.Img(src="/static/vwMath/vwEcSummQuotEquation.png", style={"float": "right", "padding-left": "10px"}, width="50%"),
                            html.P(className="card-text", children=[
                                "Higher Voter Weights in certain states are offset by lower Voter Weights in other states. The sum total of every state’s Vote \
                                Weight multiplied by its Electoral College Votes, divided by the total number of Electoral College votes nationally, evens out at 1."
                            ]),
                            html.P(className="card-text", children=[
                                html.I("Disclaimer:"), " I’m neither a historian nor a mathematician, so I don’t know if this is ", html.I("the"), " way to \
                                measure these types of voter influence disparities, but it certainly is ", html.I("a"), " way is to measure them.",                            
                            ]),
                            html.Br(),
                            html.H4("Implications / literal meaning of Voter Weight", className="card-title"),
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
                            ]),
                        ])
                    ]),
                    html.Br(),
                    html.H4("Select year:", className="text-white"),
                    dcc.Slider(
                        id="map-color-by-vw-year-input",
                        min=1800,
                        max=2020,
                        step=None,
                        marks={
                            int(y): {'label': str(y), 'style': {'transform': 'rotate(45deg)', 'color': 'white', 'font-size': '10px'}}
                            for y in data_obj.all_years 
                        },
                        value=1960,
                    ),
                    html.Br(),
                    dcc.Graph(id="fig-map-color-by-vw"),
                    html.P(className="card-text", style={"padding": "5px"}, children=[
                        html.Small(children=["States color shaded by Voter Weight, over the course of 56 presidential elections between 1800 and 2020. Control \
                            the year using the slider above, or open an ", dcc.Link("intractive slideshow animation", className="text-white",
                            href="https://htmlpreview.github.io/?https://github.com/dannynoonan/electoralytics/blob/master/html_figures/anim_map_state_vw_acw4_1000.html",
                            target="_blank"), " illustrating the full history."]),
                    ]),
                ]),
                dbc.Col(md=6, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([ 
                            html.H4("Example: Georgia vs Wisconsin in early 20th Century", className="card-title"),  
                            html.Img(style={"float": "right", "padding-left": "10px"}, src="/static/vwMath/vwMathSampler/popToEcWIGA1900.png", width="60%"),
                            html.P(className="card-text", children=[
                                "Both Georgia’s and Wisconsin’s populations in the 1900 census (2.22 million and 2.07 million respectively) garnered 11 \
                                representatives and 13 Electoral College votes. In the 1904 congressional and presidential election that followed, 131K \
                                Georgians turned out to vote, while 443K turned out to vote in Wisconsin — more than triple that of Georgia. But, because \
                                federal influence-allocation is determined by population census, both states sent the same number of reps to congress and \
                                the same number of electors to the EC, despite the disparity in voter participation."
                            ]),
                            html.P(className="card-text", children=[
                                "The net effect is that, pound for pound, any individual Wisconsinite’s voice counted for less than a third of a Georgian’s \
                                voice in that election:",                              
                            ]),
                            html.Br(),
                            dbc.CardImg(src="/static/vwMath/vwMathSampler/vwCalcWIGA1904.png", top=False),
                            html.Br(), html.Br(),
                            html.P(className="card-text", children=[
                                "A few decades later, despite the intervening rise of Progressivism and passage of the 19th Amendment guaranteeing women \
                                the right to vote, the disparity between these two states had widened. Each state’s population in the 1930 census garnered \
                                it 10 representatives and 12 EC votes, but in the 1932 election 1.11M people voted in Wisconsin compared to 256K in Georgia, \
                                giving each ballot cast in Georgia more than 4X the national-level influence of a Wisconsinite’s:",
                            ]),
                            dbc.CardImg(src="/static/vwMath/vwMathSampler/vwCalcWIGA1932.png", top=False),
                            html.Br(), html.Br(),
                            html.P(className="card-text", children=[
                                "It’s worth noting that this 3–4X disparity suggests a voter suppression dragnet in Georgia that reaches well beyond its African \
                                American population (which was ", dcc.Link("46.7% of Georgia’s total population in 1900", target="_blank",
                                href="https://en.wikipedia.org/wiki/Disenfranchisement_after_the_Reconstruction_era#Southern_black_populations_in_1900"), "). This \
                                likely refects the way poll taxes were aimed not only to disenfranchise Blacks, but also to purge poor whites with Populist party \
                                sympathies from the voter rolls. Blacks and poor whites had momentarily joined forces to take over a handful of Southern state \
                                legislatures in the 1890s, prompting swift retaliation by Southern white elites who rewrote state constitutions en masse (the \
                                “Mississippi Plan”) to implement poll taxes and other disenfranchising devices.", 
                                dcc.Link(href="/sources-notes", children=[html.Sup("45")]),
                            ]),
                            html.P(className="card-text", children=[
                                "While African Americans were undoubtedly the principal target of Southern disenfranchisement practices, the idea that \
                                certain forms of voter suppression also impacted poor whites should be factored into any interpretation of the data. \
                                But demographics aside, the Voter Weight / voter suppression calculation is the same — it may just turn out that \
                                suppression-state bias goes beyond “five-fifths.”",
                            ]),
                            html.Img(src="/static/screenshots/lineChartWIvsGA.png", style={"float": "left", "padding-right": "10px"}, width="100%"),
                        ])
                    ]),
                ]),
            ]),
            html.Br(),
            html.Hr(className="border-light"),
            html.Div(children=[
                html.Ul(className="pagination pagination-lg justify-content-center", children=[
                    html.Li(className="page-item flex", style={"width": "50%"}, children=[
                        html.A(className="page-link", href="/voter-weight-conclusions", children=[
                            "← Part 6: Conclusions and interpretation"
                        ])
                    ]),
                    html.Li(className="page-item flex", style={"width": "20%"}),
                    html.Li(className="page-item flex", style={"width": "50%", "text-align": "right"}, children=[
                        html.A(className="page-link", href="/voter-weight-timeline-visualization", children=[
                            "Appendix 2: Annotated Timeline Charting Voter Weight Trends →"
                        ])
                    ]),
                ])
            ]),
        ])
    ])
])