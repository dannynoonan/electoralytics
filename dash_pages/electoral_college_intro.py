import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash_pages.components import navbar, data_obj
from metadata import YEAR_N


content = html.Div([
    navbar,
    html.Br(),
    dbc.Row([
        dbc.Col(md=6, children=[
            dbc.Card(className="border-success", children=[
                dbc.CardBody([
                    html.H3("What Are Our Hangups with the Electoral College?", style={"text-align": "center"}),
                    html.Br(),
                    html.P(className="card-text", children=[
                        "Chances are you have an opinion on the Electoral College. This steam-punk-era Wonka-esque Rube-Goldberg influence-allocating \
                        and vote-tabulating system has managed to translate popular election victories into crushing defeats twice in my brief political \
                        lifetime, earning the bewildered scorn of Democrats while being coopted as something like another Second Amendment by Republicans. \
                        But interest in and attitudes toward this curious institution have oscillated between thundering support, fiery antagonism, and \
                        fizzling apathy for centuries, following the currents of demographic shift and perceived party advantage. So, putting our present \
                        partisan motivations aside, what do we genuinely hate about the EC?"
                    ]),
                    html.H4("(1) Small-state bias"),
                    html.P(className="card-text", children=[
                        "Here’s one: you live in a big state, and you’re peeved that individual voters in less populous states have a disproportionate impact \
                        on the national election:",                            
                    ]),
                    html.Img(src="/assets/arrows/arrow_right_1v_thick_transparent.png", width="75", style={"float": "right"})
                ])
            ]),
            html.Br(),
            dbc.Card(className="border-success", children=[
                dbc.CardBody([
                    html.H4("(2) Winner-take-all 'muting' and 'flipping' votes"),
                    html.P(className="card-text", children=[
                        "Or... maybe you consider the edge that smaller states get from the +2 senators / 3-vote-minimum “bicameral boost” to be one of the few \
                        bulwarks against big-state tyranny, where our winner-take-all system swallows up gazillions of opposition votes, effectively flipping \
                        and re-casting them for the majority candidate:",                            
                    ])
                ]),
                html.Div(style={"text-align": "center"}, children=[
                    html.Img(src="/assets/arrows/arrow_down_1v_thick_transparent.png", width="75")
                ]),
                html.Br(),
            ]),
            html.Br(),
            dbc.Tabs(className="nav nav-pills", children=[
                dbc.Tab(dcc.Graph(id="fig-bar-swallowed-vote-sampler-1"), label="Raw Popular Vote"),
                dbc.Tab(dcc.Graph(id="fig-bar-swallowed-vote-sampler-2"), label="Muted Popular Vote"),
                dbc.Tab(dcc.Graph(id="fig-bar-swallowed-vote-sampler-3"), label="Stacked Popular Vote"),
                dbc.Tab(dcc.Graph(id="fig-bar-swallowed-vote-sampler-4"), label="Converted to EC Vote"),
            ]),
            html.Br(),
            dbc.Card(className="border-success", children=[
                dbc.CardBody([           
                    html.P(className="card-text", children=[
                        "And that’s just a quick sampler. If I haven’t mentioned your specific grievance, I’m willing to wager it boils down to this: ",
                        html.I("that some people’s votes count more than others."), " And, beyond its direct effect on you personally, that the implications \
                        are systemic: the variation in voter value warps and distorts everything from party platforms to campaign priorities to candidate \
                        selection. Regardless of your contribution to the economy or the merits of your views, if your vote is only half as impactful as \
                        someone in another state, it’s a safe bet that your interests are only considered half as relevant as those of the constituents in \
                        that other state."
                    ]),
                    html.H4("(4) As the framers intended"),
                    html.P(className="card-text", children=[
                        "And of course, there’s the inescapable fact that some of these imbalances are by design. From its genesis during the Constitutional \
                        Convention, each state’s apportionment in the Electoral College was based on two things:",
                        html.Ul(children=[
                            html.Li(
                                "the same hybrid of flat (Senate) + proportional (House) representation that was the basis of the bicameral “Great \
                                Compromise” — aka “small-state bias”"
                            ),
                            html.Li(
                                "the infamous “Three-fifths Compromise” that rewarded white property-owning male voters in slave states with increased \
                                congressional representation (and electoral vote allocation) in direct proportion to the size of their enslaved populations \
                                — aka “slave-state bias”"
                            )
                        ])
                    ]),
                    html.P(className="card-text", children=[
                        "Ok fine, you say, but small-state bias does have a functional — if controversial — role to play in presidential elections (and, \
                        frankly, one not nearly so controversial as the role it plays in the legislative branch, where ",
                        dcc.Link("16% of the nation’s population elected 50% of the Senate in 2010", 
                        href="https://ballotpedia.org/Population_represented_by_state_legislators", target="_blank"), "). And the three-fifths compromise \
                        was rendered moot by the Reconstruction amendments following the Civil War 150 years ago, so... why even bring that up?"
                    ])
                ])
            ])
        ]),
        dbc.Col(md=6, children=[
            dcc.Slider(
                id="year-input",
                min=1972,
                max=YEAR_N,
                step=None,
                marks={
                    int(y): {'label': str(y), 'style': {'transform': 'rotate(45deg)'}}
                    for y in data_obj.all_years if y >= 1972
                },
                value=2020,
            ),
            html.Br(),
            dcc.Graph(id="fig-bar-state-vw-color-by-ecv"),
            html.Br(),
            dbc.Card(className="border-success", children=[
                dbc.CardBody([
                    html.H4("(3) Winner-take-all and 'swing states'"),
                    html.P(className="card-text", children=[
                        "Or maybe the safe-state vs swing-state implications of winner-take-all electioneering is what gets your goat, twisting entire \
                        elections to suit the interests of “battleground states” at the expense of the broader population. This bar plot from a 2017 \
                        article in ", html.I("The Nation"), " called ", dcc.Link("The Electoral College Is Even More Biased Than You Think", target="_blank",
                        href="https://www.thenation.com/article/archive/the-electoral-college-is-even-more-biased-than-you-think-heres-how-democrats-can-beat-it/"),
                        " measures the “Voter Influence On Presidential Election By State” in 2016 by combining how tight each state’s race was with how \
                        many Electoral College votes each state cast.",                              
                    ])
                ]),
                html.Div(style={"text-align": "center"}, children=[
                    html.Img(src="/assets/arrows/arrow_down_1v_thick_transparent.png", width="75")
                ]),
                html.Br(),
            ]),
            html.Br(),
            html.Img(src="/assets/Voter-Influence-on-Presidential-Election-by-State-Type.png", width="800")
        ]),
    ]),
    html.Br(),
])