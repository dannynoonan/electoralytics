import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash_pages.components import navbar
from metadata import YEAR_0, YEAR_N


vicennial_gap = 20
vicennial_years = [x for x in range(YEAR_0, YEAR_N+vicennial_gap, vicennial_gap)]


content = html.Div([
    navbar,
    html.Br(),
    dbc.Row([
        html.H3("Explanation of State Aggregate Groupings"),
    ], justify="center", align="center"),
    html.Br(),
    dbc.Row([
        dbc.Col(md=6, children=[
            dcc.Slider(
                id="year-input",
                min=YEAR_0,
                max=YEAR_N,
                step=None,
                marks={
                    int(y): {'label': str(y), 'style': {'transform': 'rotate(45deg)'}}
                    for y in vicennial_years
                },
                value=2020,
            )
        ]), 
        dbc.Col(md=2, style={'textAlign': 'right'}, children=[
            html.H5("Extract Small Group?")
        ]), 
        dbc.Col(md=2, children=[
            dcc.Dropdown(
                id="max-small-input", 
                options=[
                    {'label': 'No Small Group', 'value': '0'},
                    {'label': '3 EC Votes', 'value': '3'},
                    {'label': '3 - 4 EC Votes', 'value': '4'},
                    {'label': '3 - 5 EC Votes', 'value': '5'},
                ], 
                value="0"
            )
        ]),
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col(md=6, children=[
            dcc.Graph(id="fig-map-acw"),
            html.Br(),
        ]),
        dbc.Col(md=6, children=[
            dcc.Graph(id="fig-map-census"),
            html.Br(),
        ])
    ]),
    dbc.Row([
        dbc.Col(md=6, children=[
            dbc.Card([
                dbc.CardBody([
                    html.P(className="card-text", children=[
                        "50 states + DC over the course of 58 elections spanning 232 years is a lot of data to sift through and absorb. I’ve \
                        attempted to make the output easier to visualize and interpret by classifying states into groups based on regional, \
                        economic, political, and military alliances.",
                    ]),
                    html.Br(),
                    html.H4("Civil War Groupings", className="card-title"),
                    html.P(className="card-text", children=[
                        "In the context of slavery, the three-fifths compromise, the 15th Amendment, and Jim Crow voter suppression, one obvious \
                        grouping heuristic is to divide between “slave states” and “free states” on the eve of the Civil War in 1860. This \
                        oversimplifies things somewhat, since only 11 of the 15 slave states seceded to join the Confederacy, while four “Border” \
                        slave states remained in the Union. This small cluster of slave states that didn’t join the Confederacy felt like an \
                        interesting control group for examining what aspect was more predictive of racialized voter suppression in the decades \
                        after the Civil War: slavery before the war, or military defeat during/after it. Even though Border states comprise a much \
                        smaller group (increasing to five when Union-loyal West Virginia was cleaved off of Virginia), I opted to break them out \
                        into their own group, leaving me with ", html.I("Union"), ", ", html.I("Confederate"), ", and ", html.I("Border"), 
                        " state groups. The remaining 15 states that joined the Union after the war began (not during it — sorry Nevada!) I’ve \
                        lumped together in a fourth ", html.I("Postbellum"), " group.",
                    ]),
                    dbc.CardImg(src="/assets/borderStatesVenn.png", top=False),
                ]),
            ])
        ]),
        dbc.Col(md=6, children=[
            dbc.Card([
                dbc.CardBody([
                    html.H4("Regional Census Groupings", className="card-title"),
                    html.P(
                        "To hedge my bets, I also mapped states into alternate groupings based entirely on US Census classifications: South, \
                        Northeast, Midwest, and West. I figured slicing the groupings up in a couple of ways would help highlight distortion only \
                        present in one, reveal effects present in both, validate overall findings, etc.",
                        className="card-text"
                    ),
                    html.H4("Small State Groupings", className="card-title"),
                    html.P(
                        "Not surprisingly, I quickly found that the presence of smaller states warps and distorts Voter Weight trends that are \
                        otherwise evident within and between state groupings. However, controlling for small-state bias is not as clear-cut as \
                        creating an additional “Small” state group and adopting states into it, at least not permanently. Whereas membership in \
                        Civil War and Regional Census groupings are constant over time, a state’s population (and Electoral College representation, \
                        and inherent biases therein) changes over time, with nearly every newborn state beginning with 3 or 4 Electoral votes. It’s \
                        also not entirely clear where to set the threshold for Small-hood, since states of all sizes carry the bias of their +2 \
                        senator apportionment, to a certain degree.",
                        className="card-text",
                    ),
                    html.P(
                        "What I settled on is that every state fits into a primary grouping (well, two primary groupings: one Civil War grouping and \
                        one Regional Census grouping), but any state with few enough Electoral College votes in a given election can “phase shift” \
                        into or out of the “Small” group. As for where to set the threshold for Small-hood, 4 EC votes seems to produce the \
                        cleanest trend lines, but I ended up making this a configurable setting, so you can designate the Small group threshold to \
                        be anywhere from from 0 EC votes (i.e. no Small group at all) up to 5 EC votes.",
                        className="card-text",
                    ),
                ]),
            ])
        ])
    ])
])