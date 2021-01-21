import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import flask

import pandas as pd
import plotly.express as px

from data_processor.data_objects import DataObject
from fig_builder import bar_plots, box_plots, choropleths, line_charts, scatter_plots
from data_processor.functions import validate_input, map_to_subdir
from metadata import Columns, DataDirs, FigDimensions, YEAR_0, YEAR_N


# base config
app = dash.Dash(external_stylesheets=[dbc.themes.SOLAR])
# server is needed for heroku deployment
server = app.server


# load source data for default subdir
data_obj = DataObject()
data_obj.load_dfs_for_subdir()
data_obj.load_all_states_meta()
data_obj.load_abbrevs_to_states()
data_obj.load_totals_by_year()
data_obj.load_swallowed_vote_sampler()

cols = Columns()
ddirs = DataDirs()
fig_dims = FigDimensions()

vicennial_gap = 20
vicennial_years = [x for x in range(YEAR_0, YEAR_N+vicennial_gap, vicennial_gap)]


### LAYOUT COMPONENTS ###
url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


navbar = html.Div([
    html.Br(),
    html.H1("Electoralytics - Visualizing Historical Presidential Election Data", id="nav-pills", style={"text-align": "center"}),
    dbc.Nav(className="nav nav-pills", children=[
        dbc.DropdownMenu(label="Introduction and Methodology", nav=True, children=[
            dbc.DropdownMenuItem([html.I(className="fa"), "What Is It About the Electoral College"], href='/electoral-college-intro', target="_blank"), 
            dbc.DropdownMenuItem([html.I(className="fa"), "Calculating Voter Weight"], href='/calculating-voter-weight', target="_blank"), 
            dbc.DropdownMenuItem([html.I(className="fa"), "Explanation of State Aggregate Groupings"], href='/explanation-of-groupings', target="_blank"), 
        ]),
        dbc.DropdownMenu(label="Maps, Charts, and Graphs", nav=True, children=[
            dbc.DropdownMenuItem([html.I(className="fa"), "Comparing Voter Weight Per State - Overview"], href='/voter-weight-comparison-overview', target="_blank"), 
            dbc.DropdownMenuItem([html.I(className="fa"), "Comparing Voter Weight Per State - Details"], href='/voter-weight-comparison-details', target="_blank"), 
        ]),
        dbc.DropdownMenu(label="References / Resources", nav=True, children=[
            dbc.DropdownMenuItem([html.I(className="fa"), "Source code"], href='https://github.com/dannynoonan/electoralytics', target="_blank"), 
            dbc.DropdownMenuItem([html.I(className="fa"), "Articles"], href='/resources/articles'),
            dbc.DropdownMenuItem([html.I(className="fa"), "Podcasts"], href='/resources/podcasts'),
            dbc.DropdownMenuItem([html.I(className="fa"), "Books"], href='/resources/books'),
        ])
    ])
])


# groups_pulldown = dbc.Col(md=2, children=[
#     dcc.Dropdown(
#         id="groupings-input", 
#         options=[
#             {'label': 'Civil War', 'value': ddirs.ACW},
#             {'label': 'Regional Census', 'value': ddirs.CENSUS}
#         ], 
#         value=ddirs.ACW
#     )
# ]),

# small_pulldown = dbc.Col(md=2, children=[
#     dcc.Dropdown(
#         id="max-small-input", 
#         options=[
#             {'label': 'No Small Group', 'value': '0'},
#             {'label': '3 EC Votes', 'value': '3'},
#             {'label': '3 or 4 EC Votes', 'value': '4'},
#             {'label': '3 - 5 EC Votes', 'value': '5'},
#         ], 
#         value="4"
#     )
# ])


# year_slider = dbc.Col(md=8, children=[
#     dcc.Slider(
#         id="year-input",
#         min=YEAR_0,
#         max=YEAR_N,
#         marks={
#             int(y): {'label': str(y), 'style': {'transform': 'rotate(45deg)'}}
#             for y in data_obj.all_years
#         },
#         value=1960,
#     )
# ])


# groups_selection = dbc.FormGroup([
#     dbc.Row([
#         # groups_pulldown,
#         dbc.Col(md=2, children=[
#             dcc.Dropdown(
#                 id="groupings-input", 
#                 options=[
#                     {'label': 'Civil War', 'value': ddirs.ACW},
#                     {'label': 'Regional Census', 'value': ddirs.CENSUS}
#                 ], 
#                 value=ddirs.ACW
#             )
#         ]),
#         # small_pulldown,
#         dbc.Col(md=2, children=[
#             dcc.Dropdown(
#                 id="max-small-input", 
#                 options=[
#                     {'label': 'No Small Group', 'value': '0'},
#                     {'label': '3 EC Votes', 'value': '3'},
#                     {'label': '3 or 4 EC Votes', 'value': '4'},
#                     {'label': '3 - 5 EC Votes', 'value': '5'},
#                 ], 
#                 value="4"
#             )
#         ])
#     ])
# ])


year_slider_and_groups_selection = dbc.FormGroup([
    html.Br(),
    dbc.Row([
        dbc.Col(md=8, children=[
            html.H4("Election Year:")
        ]),
        dbc.Col(md=2, children=[
            html.H4("State Grouping Heuristic:")
        ]),
        dbc.Col(md=2, children=[
            html.H4("Extract Small Group?")
        ])
    ]),
    dbc.Row([
        # year_slider,
        dbc.Col(md=8, children=[
            dcc.Slider(
                id="year-input",
                min=YEAR_0,
                max=YEAR_N,
                step=None,
                marks={
                    int(y): {'label': str(y), 'style': {'transform': 'rotate(45deg)'}}
                    for y in data_obj.all_years
                },
                value=1960,
            )
        ]),
        # groups_pulldown,
        dbc.Col(md=2, children=[
            dcc.Dropdown(
                id="groupings-input", 
                options=[
                    {'label': 'Civil War', 'value': ddirs.ACW},
                    {'label': 'Regional Census', 'value': ddirs.CENSUS}
                ], 
                value=ddirs.ACW
            )
        ]),
        # small_pulldown,
        dbc.Col(md=2, children=[
            dcc.Dropdown(
                id="max-small-input", 
                options=[
                    {'label': 'No Small Group', 'value': '0'},
                    {'label': '3 EC Votes', 'value': '3'},
                    {'label': '3 - 4 EC Votes', 'value': '4'},
                    {'label': '3 - 5 EC Votes', 'value': '5'},
                ], 
                value="4"
            )
        ])
    ])
])


form_input_vw_over_time_line_chart = dbc.FormGroup([
    html.Br(),
    dbc.Row([
        dbc.Col(md=2),
        dbc.Col(md=2, children=[
            html.H5("Display individual states:")
        ]),
        dbc.Col(md=2, children=[
            html.H5("Show / Hide:")
        ]),
        dbc.Col(md=2, children=[
            html.H5("State Grouping Heuristic:")
        ]),
        dbc.Col(md=2, children=[
            html.H5("Extract Small Group?")
        ]),
        dbc.Col(md=2, children=[
            html.H5("Y axis scale:")
        ]),
    ]),
    dbc.Row([
        dbc.Col(md=2, style={'textAlign': 'center'}, children=[
            dbc.Button("Clear canvas", id="clear-all-input", className="mr-2")
        ]),
        dbc.Col(md=2, style={'textAlign': 'left'}, children=[
            dcc.Dropdown(
                id="multi-state-input",
                options=[{'label': state, 'value': abbrev} for abbrev, state in data_obj.abbrevs_to_states.items()],
                multi=True,
                value=''
            )
        ]),
        dbc.Col(md=2, style={'textAlign': 'center'}, children=[
            dcc.Checklist(
                id="show-hide-input",
                options=[
                    {'label': 'State Groups', 'value': 'show_groups'},
                    {'label': 'Events', 'value': 'show_events'},
                    {'label': 'Eras', 'value': 'show_eras'}
                ],
                value=['show_groups','show_events','show_eras'],
                inputStyle={"margin-left": "4px", "margin-right": "4px"}
            )
        ]),
        dbc.Col(md=2, children=[
            dcc.Dropdown(
                id="groupings-input", 
                options=[
                    {'label': 'Civil War', 'value': ddirs.ACW},
                    {'label': 'Regional Census', 'value': ddirs.CENSUS}
                ], 
                value=ddirs.ACW
            )
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
                value="4"
            )
        ]),
        dbc.Col(md=2, style={'textAlign': 'left'}, children=[
            dcc.RadioItems(
                id="y-axis-input",
                options=[
                    {'label': 'Linear', 'value': 'linear'},
                    {'label': 'Log', 'value': 'log'}
                ],
                value='linear',
                inputStyle={"margin-left": "4px", "margin-right": "4px"}
            )
        ]),
    ])
])


form_input_y_axis = dbc.FormGroup([
    dbc.Row([
        dbc.Col(md=2, style={'textAlign': 'left'}, children=[
            html.H4("Y axis:"),
            dcc.RadioItems(
                id="y-axis-input-2",
                options=[
                    {'label': 'Linear', 'value': 'linear'},
                    {'label': 'Log', 'value': 'log'}
                ],
                value='linear',
                inputStyle={"margin-left": "4px", "margin-right": "4px"}
            )
        ])
    ])
])


swallowed_vote_view_dropdown = dbc.FormGroup([
    html.H4("Swallowed vote view"),
    dcc.Dropdown(id="display-type", options=[{"label": "2020", "value": "2020"}], value="2020")
])


groupings_explanation_dropdown = dbc.FormGroup([
    html.H4("Groupings explanation"),
    dcc.Dropdown(id="year-input", options=[{"label": "2020", "value": "2020"}], value="2020")
])



### LAYOUTS ###
voter_weight_comparison_overview = html.Div([
    navbar,
    html.Br(),
    dbc.Row([
        html.H2("Voter Weight Per State/Group Over Time"),
    ], justify="center", align="center"),
    dbc.Row([
        dbc.Col(md=12, children=[
            form_input_vw_over_time_line_chart,
            # groups_selection,
            dbc.Row([
                dbc.Col(md=12, children=[
                    dcc.Graph(id="fig-line-vote-weight-by-state-group"),
                ])
            ])
        ])
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col(md=5, children=[
            dbc.Card([
                dbc.CardBody([
                    html.H4("Using the Voter Weight timeline chart", className="card-title"),
                    html.P(className="card-text", children=[
                        "The line chart above shows Voter Weight trends as a function of time, spanning every US presidential election between 1800 and \
                        2020. When you first load the page, it displays aggregate/average data at the state group level, but using the dropdown menu above \
                        you can select individual states to compare, and using the legend to the right or the checkbox above you can hide the group-level \
                        trend lines one at a time or en masse."
                    ]),
                    html.P(className="card-text", children=[
                        "Background colors, markers, and text annotations denoting significant events and eras are there to add context, relating to \
                        African American rights and to voting rights generally. These can also be hidden using the checkboxes above the chart.",                            
                    ]),
                    html.P(className="card-text", children=[
                        "If things get too cluttered and you decide to assemble a comparison from scratch, hit the “Clear canvas” button to start fresh. \
                        Toggling from “linear” to “log” scale for Vote Weight (Y axis) can help de-clutter trend lines in the lower registers as well.",                              
                    ]),
                    html.P(className="card-text", children=[
                        "As with most other charts and maps on the site, you can toggle between grouping states by their Civil War affiliations or their \
                        Regional Census designation, and you can specify the Electoral College vote threshold at which states are extracted into the “Small” \
                        group to reduce the effects of small-state bias in the trend lines.",                              
                    ]),
                ])
            ])
        ]),
        dbc.Col(md=7, children=[
            dbc.Card([
                dbc.CardBody([
                    html.H4("Election year range; quirks in the early years", className="card-title"),
                    html.P(className="card-text", children=[
                        "Where’s 1788-1796? And what’s with the zig-zaggy lines in the early 1800s?"
                    ]),
                    html.P(className="card-text", children=[
                        "So, I’d actually forgotten this detail about US history, but for the first 40-odd years after its founding there wasn’t a whole lot \
                        of actual ", html.I("voting"), " for president in this country. I don’t mean among women and racial minorities specifically, I mean \
                        among ", html.I("people"), ". Before phrases like “populism,” “democratic,” and the “politics of the common man” gained cachet in the \
                        1820s, a majority of presidential electors were chosen by state legislatures, or in states holding a so-called “popular” vote this \
                        voting was the exclusive purview of a tiny sliver of property-owning white males.",                              
                    ]),
                    html.P(className="card-text", children=[
                        "As a result, fewer than 2% of people voted in each of these first 10 US presidential elections, hitting a 30-year low in 1820 \
                        at 1.11% of the total population. Popular vote data before 1800 is too scant to really work with, then from 1800 to 1824 the amount \
                        of data increases but it’s erratic, as several states switch back and forth between elector selection by legislature, by very limited \
                        popular vote, and by significantly wider popular vote. My regional tallies exclude states that don’t even hold popular presidential \
                        elections in a given year, meaning states like North Carolina and Kentucky that have very ", html.I("restrictive"), " voting end up \
                        being “penalized” more than states like New York, South Carolina, occasionally Massachusetts, and other states in years when ",
                        html.I("nobody"), " ends up voting.",                              
                    ]),
                    html.P(className="card-text", children=[
                        "Between 1820 and 1828 the popular vote increased 10-fold, marking the dawn of “populism” and “Jacksonian democracy,” and from 1828 \
                        onward some form of popular vote has been the norm in every state (except South Carolina, which didn’t switch to popular vote until \
                        Reconstruction). I considered excluding the years prior to 1828 altogether, since those years tell a much different story than what \
                        emerges from the late 1820s onward, but in the end I held onto them - less for the trend analysis than for the novelty and intrigue.",                              
                    ]),
                    html.P(className="card-text", children=[
                        "The “Votes cast as a percentage of population” chart below shows the increase (and decrease) in national popular vote over time.",                              
                    ]),
                ])
            ])
        ])
    ]),
    html.Br(),
    # dbc.Row([
    #     html.H2("Voter Participation Nationally Over Time"),
    # ], justify="center", align="center"),
    dbc.Row([
        dbc.Col(md=12, children=[
            form_input_y_axis,
            dcc.Graph(id="fig-line-total-vote-over-time")
        ])
    ]),
    html.Br(),html.Br(),
])


voter_weight_comparison_details = html.Div([
    navbar,
    html.Br(),
    dbc.Row([
        html.H3("Comparing Voter Weight Per State/Per Grouping"),
    ], justify="center", align="center"),
    dbc.Row([
        dbc.Col(md=12, children=[
            year_slider_and_groups_selection,
            # group_select,
        ])
    ]),
    dbc.Row([
        dbc.Col(md=12, children=[
            dbc.Tabs(className="nav nav-pills", children=[
                dbc.Tab(label="Maps and Bar Charts", tab_style={"font-size": "20px"}, children=[
                    dbc.Row([
                        dbc.Col(md=7, children=[
                            dcc.Graph(id="fig-map-color-by-state-vw"),
                            html.Br(),
                        ]),
                        dbc.Col(md=5, children=[
                            dcc.Graph(id="fig-bar-state-vw-color-by-vw"),
                            html.Br(),
                        ])
                    ]),
                    dbc.Row([
                        dbc.Col(md=7, children=[
                            dcc.Graph(id="fig-map-color-by-group"),
                            html.Br(),
                        ]),
                        dbc.Col(md=5, children=[
                            dcc.Graph(id="fig-bar-state-vw-color-by-group"),
                            html.Br(),
                        ])
                    ]),
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-bar-actual-vs-adj-ec"),
                            html.Br(),
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-bar-actual-vs-adj-vw"),
                            html.Br(),
                        ])
                    ])
                ]),

                dbc.Tab(label="Scatter Plots", tab_style={"font-size": "20px"}, children=[
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-scatter-dots-vw-state"),
                            html.Br(),                          
                            dcc.Graph(id="fig-scatter-bubbles-vw-state"),
                            html.Br(), 
                            dcc.Graph(id="fig-scatter-abbrevs-vw-state"),
                            html.Br(),
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-scatter-dots-vw-group"),
                            html.Br(),
                            dcc.Graph(id="fig-scatter-bubbles-vw-group"),
                            html.Br(),
                            dcc.Graph(id="fig-box-vw-group"),
                            html.Br(),
                        ]),
                    ])
                ]),

                # dbc.Tab(label="State-Level Animations - TODO move", tab_style={"font-size": "20px"}, children=[
                #     dbc.Row([
                #         dbc.Col(md=6, children=[
                #             dcc.Graph(id="vote-weight-comparison-by-state-map-1-anim"),
                #             html.Br(),
                #             dcc.Graph(id="vote-weight-comparison-by-state-scatter-dots-anim"),
                #             html.Br(),
                #             # dcc.Graph(id="vote-weight-comparison-by-state-bar-1-anim"),
                #             # html.Br(),
                #         ]),
                #         dbc.Col(md=6, children=[
                #             dcc.Graph(id="vote-weight-comparison-by-state-scatter-bubbles-anim"),
                #             html.Br(), 
                #             dcc.Graph(id="vote-weight-comparison-by-state-scatter-abbrevs-anim"),
                #             html.Br(),
                #             # dcc.Graph(id="vote-weight-comparison-by-state-bar-2-anim"),
                #             # html.Br(),
                #         ])
                #     ])
                # ]),

                # dbc.Tab(label="Aggregate Group Animations - TODO move", tab_style={"font-size": "20px"}, children=[
                #     dbc.Row([
                #         dbc.Col(md=6, children=[
                #             dcc.Graph(id="vote-weight-comparison-by-state-group-scatter-bubbles-anim"),
                #             html.Br(),
                #             dcc.Graph(id="vote-weight-comparison-by-state-group-map-1-anim"),
                #             html.Br(),
                #         ]),
                #         dbc.Col(md=6, children=[
                #             dcc.Graph(id="vote-weight-comparison-by-state-group-scatter-dots-anim"),
                #             html.Br(),
                #         ]),
                #     ])
                # ]),

            ])
        ])
    ])
])


# voter_participation = html.Div([
#     navbar,
#     html.Br(),
#     dbc.Row([
#         html.H2("Voter Participation Nationally Over Time"),
#     ], justify="center", align="center"),
#     dbc.Row([
#         dbc.Col(md=12, children=[
#             form_input_y_axis,
#             dcc.Graph(id="fig-line-total-vote-over-time")
#         ])
#     ]),
#     html.Br(),html.Br(),
# ])


explanation_of_groupings = html.Div([
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
                        "In the context of slavery, the Three-fifths Compromise, the 15th Amendment, and Jim Crow voter suppression, one obvious \
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


electoral_college_intro = html.Div([
    navbar,
    html.Br(),
    dbc.Row([
        dbc.Col(md=6, children=[
            dbc.Card([
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
            dbc.Card([
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
            dbc.Card([
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
                        href="https://ballotpedia.org/Population_represented_by_state_legislators", target="_blank"), "). And the Three-fifths Compromise \
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
            dbc.Card([
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


calculating_voter_weight = html.Div([
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


# swallowed_vote_sampler = html.Div([
#     ## Top
#     navbar,
#     html.Br(),html.Br(),
#     dbc.Row([
#         html.H3("2020 Sampler of Votes 'Swallowed' by the Electoral College"),
#     ], justify="center", align="center"),
#     html.Br(),
#     dbc.Row([
#         ### input + panel
#         dbc.Col(md=2, children=[
#             swallowed_vote_view_dropdown,
#             html.Br(),html.Br(),html.Br(),
#             html.Div(id="todo")
#         ]),
#         ### figures
#         dbc.Col(md=10, children=[ 
#             dbc.Tabs(className="nav nav-pills", children=[
#                 dbc.Tab(dcc.Graph(id="swallowed-vote-sampler-1"), label="Raw Popular Vote"),
#                 dbc.Tab(dcc.Graph(id="swallowed-vote-sampler-2"), label="Muted Popular Vote"),
#                 dbc.Tab(dcc.Graph(id="swallowed-vote-sampler-3"), label="Stacked Popular Vote"),
#                 dbc.Tab(dcc.Graph(id="swallowed-vote-sampler-4"), label="Converted to EC Vote"),
#             ])
#         ])
#     ]),
#     html.Br()
# ])


landing_page = html.Div([
    navbar,
    html.Br(),html.Br(),
    dbc.Row([
        dbc.Col(md=1),
        dbc.Col(md=5, children=[
            dbc.Card([
                dbc.CardBody([
                    html.H4("Landing Page", className="card-title"),
                    html.P(
                        "Landing content",
                        className="card-text",
                    ),
                ]),
            ])
        ]),
        dbc.Col(md=6),
    ]),
    html.Br(),
])


# app layout
app.layout = dbc.Container(fluid=True, children=[
    url_bar_and_content_div,
])

# app layout
app.validation_layout = dbc.Container(fluid=True, children=[
    url_bar_and_content_div,

    ## Body
    landing_page,
    voter_weight_comparison_overview,
    voter_weight_comparison_details,
    # voter_participation,
    electoral_college_intro,
    explanation_of_groupings,
    # swallowed_vote_sampler,
])



# Index callbacks
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/voter-weight-comparison-overview":
        return voter_weight_comparison_overview
    elif pathname == "/voter-weight-comparison-details":
        return voter_weight_comparison_details
    # elif pathname == "/voter-participation":
    #     return voter_participation
    elif pathname == "/electoral-college-intro":
        return electoral_college_intro
    elif pathname == "/explanation-of-groupings":
        return explanation_of_groupings
    elif pathname == "/calculating-voter-weight":
        return calculating_voter_weight
    # elif pathname == "/swallowed-vote-sampler":
    #     return swallowed_vote_sampler
    else:
        return landing_page


# voter-weight-comparison-overview callbacks
@app.callback(
    Output('fig-line-vote-weight-by-state-group', 'figure'),
    Output('fig-line-total-vote-over-time', 'figure'),
    Input('groupings-input', 'value'),
    Input('max-small-input', 'value'),
    [Input('multi-state-input', 'value')],
    Input('y-axis-input', 'value'),
    [Input('show-hide-input', 'value')],
    Input('y-axis-input-2', 'value'),
)
def display_voter_weight_comparison_overview(groupings_input, max_small_input, state_abbrevs, y_axis_input, show_hide_input, y_axis_input_2):
    # process input
    max_small = int(max_small_input)
    if y_axis_input == 'log':
        log_y = True
    else:
        log_y = False
    if not show_hide_input:
        show_groups = False
        show_events = False
        show_eras = False
    else:
        if 'show_groups' in show_hide_input:
            show_groups = True
        else:
            show_groups = False
        if 'show_events' in show_hide_input:
            show_events = True
        else:
            show_events = False
        if 'show_eras' in show_hide_input:
            show_eras = True
        else:
            show_eras = False
    # total voter participation chart
    if y_axis_input_2 == 'log':
        log_y_2 = True
    else:
        log_y_2 = False
    # generate figs
    fig_line_ivw_by_state_group = line_charts.build_ivw_by_state_group_line_chart(
        data_obj, groupings_input, max_small, fig_width=fig_dims.MD12, state_abbrevs=state_abbrevs, log_y=log_y, 
        display_groups=show_groups, display_events=show_events, display_eras=show_eras)
    fig_line_total_vote_over_time = line_charts.build_total_vote_line_chart(data_obj, fig_width=fig_dims.MD12, log_y=log_y_2)
    return fig_line_ivw_by_state_group, fig_line_total_vote_over_time

# voter-weight-comparison-overview callbacks, tab 1 cont'd: clear-all-input
@app.callback(
    Output('multi-state-input', 'value'),
    [Input('clear-all-input', 'n_clicks')],
)
def update(n_clicks):
    return []

@app.callback(
    Output('show-hide-input', 'value'),
    [Input('clear-all-input', 'n_clicks')],
)
def update2(n_clicks):
    if n_clicks and int(n_clicks) > 0:
        return []
    else:
        return ['show_groups','show_events','show_eras']


# voter-weight-comparison-details callbacks, tab 1
@app.callback(
    Output('fig-map-color-by-state-vw', 'figure'),
    Output('fig-bar-state-vw-color-by-vw', 'figure'),
    Output('fig-map-color-by-group', 'figure'),
    Output('fig-bar-state-vw-color-by-group', 'figure'),
    Output('fig-bar-actual-vs-adj-ec', 'figure'),
    Output('fig-bar-actual-vs-adj-vw', 'figure'),
    Input('year-input', 'value'),
    Input('groupings-input', 'value'),
    Input('max-small-input', 'value'),
)
def display_state_level_figs(year_input, groupings_input, max_small_input):
    # process input
    year = int(year_input)
    max_small = int(max_small_input)
    # generate figs
    fig_map_color_by_state_vw = choropleths.build_ivw_by_state_map(data_obj, groupings_input, max_small, color_col=cols.LOG_VOTE_WEIGHT, fig_width=fig_dims.MD7, frame=year)
    fig_bar_state_vw_color_by_vw = bar_plots.build_ivw_by_state_bar(data_obj, groupings_input, max_small, color_col=cols.LOG_VOTE_WEIGHT, fig_width=fig_dims.MD5, frame=year)
    fig_map_color_by_group = choropleths.build_ivw_by_state_map(data_obj, groupings_input, max_small, color_col=cols.GROUP, fig_width=fig_dims.MD7, frame=year)
    fig_bar_state_vw_color_by_group = bar_plots.build_ivw_by_state_bar(data_obj, groupings_input, max_small, fig_width=fig_dims.MD5, frame=year)
    fig_bar_actual_vs_adj_ec = bar_plots.build_actual_vs_adjusted_ec_bar(data_obj, groupings_input, max_small, frame=year)
    fig_bar_actual_vs_adj_vw = bar_plots.build_actual_vs_adjusted_vw_bar(data_obj, groupings_input, max_small, frame=year)
    return fig_map_color_by_state_vw, fig_bar_state_vw_color_by_vw, fig_map_color_by_group, fig_bar_state_vw_color_by_group, fig_bar_actual_vs_adj_ec, fig_bar_actual_vs_adj_vw


# voter-weight-comparison-details callbacks, tab 2
@app.callback(
    Output('fig-scatter-dots-vw-state', 'figure'),
    Output('fig-scatter-dots-vw-group', 'figure'),
    Output('fig-scatter-bubbles-vw-state', 'figure'),
    Output('fig-scatter-bubbles-vw-group', 'figure'),
    Output('fig-scatter-abbrevs-vw-state', 'figure'),
    Output('fig-box-vw-group', 'figure'),    
    # Output('fig-map-color-by-group', 'figure'),
    Input('year-input', 'value'),
    Input('groupings-input', 'value'),
    Input('max-small-input', 'value'),
)
def display_vw_comparison_detail_scatters(year_input, groupings_input, max_small_input):
    # process input
    year = int(year_input)
    max_small = int(max_small_input)
    # generate figs
    fig_scatter_dots_vw_state = scatter_plots.build_ivw_by_state_scatter_dots(data_obj, groupings_input, max_small, frame=year)
    fig_scatter_dots_vw_group = scatter_plots.build_ivw_by_state_group_scatter_dots(data_obj, groupings_input, max_small, frame=year)
    fig_scatter_bubbles_vw_state = scatter_plots.build_ivw_by_state_scatter_bubbles(data_obj, groupings_input, max_small, frame=year)
    fig_scatter_bubbles_vw_group = scatter_plots.build_ivw_by_state_group_scatter_bubbles(data_obj, groupings_input, max_small, frame=year)
    fig_scatter_abbrevs_vw_state = scatter_plots.build_ivw_by_state_scatter_dots(data_obj, groupings_input, max_small, display_elements='abbrevs', frame=year)
    fig_box_vw_group = box_plots.build_ivw_by_state_group_box_plot(data_obj, groupings_input, max_small, frame=year)
    return (fig_scatter_dots_vw_state, fig_scatter_dots_vw_group, fig_scatter_bubbles_vw_state, fig_scatter_bubbles_vw_group, 
        fig_scatter_abbrevs_vw_state, fig_box_vw_group)


# voter-weight-comparison-details callbacks, tab 3
# @app.callback(
#     Output('vote-weight-comparison-by-state-map-1-anim', 'figure'),
#     Output('vote-weight-comparison-by-state-scatter-dots-anim', 'figure'),
#     Output('vote-weight-comparison-by-state-scatter-abbrevs-anim', 'figure'),
#     Output('vote-weight-comparison-by-state-scatter-bubbles-anim', 'figure'),
#     Input('groupings-input', 'value'),
#     Input('max-small-input', 'value'),
# )
# def display_state_level_anims(groupings_input, max_small_input):
#     # process input
#     max_small = int(max_small_input)
#     # generate figs
#     anim_map_1 = choropleths.build_ivw_by_state_map(data_obj, groupings_input, max_small)
#     anim_scatter_dots = scatter_plots.build_ivw_by_state_scatter_dots(data_obj, groupings_input, max_small)
#     anim_scatter_abbrevs = scatter_plots.build_ivw_by_state_scatter_dots(data_obj, groupings_input, max_small, display_elements='abbrevs')
#     anim_scatter_bubbles = scatter_plots.build_ivw_by_state_scatter_bubbles(data_obj, groupings_input, max_small)
#     return anim_map_1, anim_scatter_dots, anim_scatter_abbrevs, anim_scatter_bubbles


# voter-weight-comparison-details callbacks, tab 4
# @app.callback(
#     Output('vote-weight-comparison-by-state-group-map-1-anim', 'figure'),
#     Output('vote-weight-comparison-by-state-group-scatter-dots-anim', 'figure'),
#     Output('vote-weight-comparison-by-state-group-scatter-bubbles-anim', 'figure'),
#     Input('groupings-input', 'value'),
#     Input('max-small-input', 'value'),
# )
# def display_regional_aggregate_anims(groupings_input, max_small_input):
#     # process input
#     max_small = int(max_small_input)
#     # generate figs
#     anim_map_1 = choropleths.build_ivw_by_state_map(data_obj, groupings_input, max_small, cols.GROUP)
#     anim_scatter_dots = scatter_plots.build_ivw_by_state_group_scatter_dots(data_obj, groupings_input, max_small)
#     anim_scatter_bubbles = scatter_plots.build_ivw_by_state_group_scatter_bubbles(data_obj, groupings_input, max_small)
#     return anim_map_1, anim_scatter_dots, anim_scatter_bubbles


# # voter-participation callbacks
# @app.callback(
#     Output('fig-line-total-vote-over-time', 'figure'),
#     Input('y-axis-input', 'value'),
# )
# def display_voter_pct_pop_over_time(y_axis_input):
#     # process input
#     if y_axis_input == 'log':
#         log_y = True
#     else:
#         log_y = False
#     # generate figs
#     fig_line_total_vote_over_time = line_charts.build_total_vote_line_chart(data_obj, fig_width=fig_dims.MD12, log_y=log_y)
#     return fig_line_total_vote_over_time


# electoral-college-intro callbacks, swallowed vote sampler tab 1
@app.callback(
    Output('fig-bar-state-vw-color-by-ecv', 'figure'),
    Output('fig-bar-swallowed-vote-sampler-1', 'figure'),
    Input('year-input', 'value'),
)
def display_electoral_collge_intro(year_input):
    # process input
    year = int(year_input)
    # generate figs
    fig_bar_state_vw_color_by_ecv = bar_plots.build_ivw_by_state_bar(data_obj, ddirs.CENSUS, 0, frame=year, color_col=cols.LOG_EC_VOTES)
    fig_bar_svs_1 = bar_plots.build_swallowed_vote_bar(data_obj, 'raw')
    return fig_bar_state_vw_color_by_ecv, fig_bar_svs_1

# electoral-college-intro callbacks, swallowed vote sampler tab 2
@app.callback(
    Output('fig-bar-swallowed-vote-sampler-2', 'figure'),
    Input('year-input', 'value'),
)
def display_electoral_collge_intro_tab2(year_input):
    suppress_callback_exceptions = True
    fig = bar_plots.build_swallowed_vote_bar(data_obj, 'muted')
    return fig

# electoral-college-intro callbacks, swallowed vote sampler tab 3
@app.callback(
    Output('fig-bar-swallowed-vote-sampler-3', 'figure'),
    Input('year-input', 'value'),
)
def display_electoral_collge_intro_tab3(year_input):
    suppress_callback_exceptions = True
    fig = bar_plots.build_swallowed_vote_relative_bar(data_obj)
    return fig

# electoral-college-intro callbacks, swallowed vote sampler tab 4
@app.callback(
    Output('fig-bar-swallowed-vote-sampler-4', 'figure'),
    Input('year-input', 'value'),
)
def display_electoral_collge_intro_tab4(year_input):
    suppress_callback_exceptions = True
    fig = bar_plots.build_swallowed_vote_ec_bar(data_obj)
    return fig


# explanation-of-groupings callbacks
@app.callback(
    Output('fig-map-acw', 'figure'),
    Output('fig-map-census', 'figure'),
    Input('year-input', 'value'),
    Input('max-small-input', 'value'),
)
def display_state_grouping_explanation(year_input, max_small_input):
    # process input
    year = int(year_input)
    max_small = int(max_small_input)
    # generate figs
    fig_map_acw = choropleths.build_ivw_by_state_map(data_obj, ddirs.ACW, max_small, color_col=cols.GROUP, frame=year)
    fig_map_census = choropleths.build_ivw_by_state_map(data_obj, ddirs.CENSUS, max_small, color_col=cols.GROUP, frame=year)
    return fig_map_acw, fig_map_census


# swallowed-vote-sampler callbacks
# @app.callback(
#     Output('swallowed-vote-sampler-1', 'figure'),
#     Input('display-type', 'value'),
# )
# def display_swallowed_vote_fig_1(display_type):
#     fig = bar_plots.build_swallowed_vote_bar(data_obj, 'raw', fig_width=1000)
#     return fig

# @app.callback(
#     Output('swallowed-vote-sampler-2', 'figure'),
#     Input('display-type', 'value'),
# )
# def display_swallowed_vote_fig_2(display_type):
#     fig = bar_plots.build_swallowed_vote_bar(data_obj, 'muted', fig_width=1000)
#     return fig

# @app.callback(
#     Output('swallowed-vote-sampler-3', 'figure'),
#     Input('display-type', 'value'),
# )
# def display_swallowed_vote_fig_3(display_type):
#     fig = bar_plots.build_swallowed_vote_relative_bar(data_obj, fig_width=1000)
#     return fig

# @app.callback(
#     Output('swallowed-vote-sampler-4', 'figure'),
#     Input('display-type', 'value'),
# )
# def display_swallowed_vote_fig_4(display_type):
#     fig = bar_plots.build_swallowed_vote_ec_bar(data_obj, fig_width=1000)
#     return fig


if __name__ == '__main__':
    app.run_server(debug=True)
    