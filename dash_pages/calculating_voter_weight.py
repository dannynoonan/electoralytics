import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash_pages.components import navbar


content = html.Div([
    navbar,
    html.Br(),
    dbc.Row([
        html.H3("Calculating “Voter Weight” Per State"),
    ], justify="center", align="center"),
    html.Br(),
    dbc.Row([
        dbc.Col(md=3),
        dbc.Col(md=6, children=[
            dbc.Card([
                dbc.CardBody([
                    html.P(className="card-text", children=[
                        "Considering all our 21st century grumbling about how small-state bias amplifies the voice of a Wyoming voter at the \
                        expense of a California voter, and the stomach-churning 18th-19th century slave-state bias which amplified the voice of a \
                        Virginia slave-owner relative to a New York merchant, I was curious how this third category of electoral bias during Jim \
                        Crow — let’s call it “suppression-state bias” — would stack up against those other two."
                    ]),
                    html.Img(style={"float": "left", "padding-right": "10px"}, src="/assets/voteWeightEquations.png", width="400"),
                    html.P(className="card-text", children=[
                        "Though rooted in different causes and calculations, any manifestation of disproportionate voter influence in the \
                        Electoral College system can be measured with the same basic equation: by dividing the number of popular votes cast in \
                        each state by the number of EC votes allocated to that state. The resulting “Popular Vote per Elector” (or PVPE) will vary \
                        from state to state and from year to year, and if normalized against a nationwide PVPE average in any given year, it’s \
                        easy to arrive at a “Voter Weight” (or VW) metric for each state that’s consistent and comparable from one election to another:",                            
                    ]),
                    html.Br(), 
                    html.H4("Example: Georgia vs Wisconsin in early 20th Century", className="card-title"),  
                    html.Img(style={"float": "right", "padding-left": "10px"}, src="/assets/vwCalcSampler/popToEcWIGA1900.png", width="450"),
                    html.P(className="card-text", children=[
                        "Both Georgia’s and Wisconsin’s populations in the 1900 census (2.22 million and 2.07 million respectively) garnered 11 \
                        representatives and 13 Electoral College votes. In the 1904 congressional and presidential election that followed, 131K \
                        Georgians turned out to vote, while 443K turned out to vote in Wisconsin — more than triple that of Georgia. But, because \
                        federal influence-allocation is determined by population census, both states sent the same number of reps to congress and \
                        the same number of electors to the EC, despite the disparity in voter participation. The net effect is that, pound for pound, \
                        any individual Wisconsinite’s voice counted for less than a third of a Georgian’s voice in that election:",                              
                    ]),
                    html.Br(),
                    dbc.CardImg(src="/assets/vwCalcSampler/vwCalcWIGA1904.png", top=False),
                    html.Br(), html.Br(),
                    html.P(className="card-text", children=[
                        "A few decades later, despite the intervening rise of Progressivism and passage of the 19th Amendment guaranteeing women \
                        the right to vote, the disparity between these two states had widened: each state’s population in the 1930 census garnered \
                        it 10 representatives and 12 EC votes, but in the 1932 election 1.11M people voted in Wisconsin compared to 256K in Georgia, \
                        giving each ballot cast in Georgia more than 4X the national-level influence of a Wisconsinite’s:",
                    ]),
                    dbc.CardImg(src="/assets/vwCalcSampler/vwCalcWIGA1932.png", top=False),
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
        dbc.Col(md=3)
    ])
])