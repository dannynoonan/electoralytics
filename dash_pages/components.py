import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from data_processor.data_objects import DataObject
from metadata import Columns, DataDirs, FigDimensions, YEAR_0, YEAR_N


# load source data for default subdir
data_obj = DataObject()
data_obj.load_dfs_for_subdir()
data_obj.load_all_states_meta()
data_obj.load_abbrevs_to_states()
data_obj.load_totals_by_year()

ddirs = DataDirs()


url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


navbar = dbc.Card(className="text-white bg-primary", children=[
    dbc.CardBody([
        html.Br(),
        html.H2("Electoralytics", id="nav-pills"),
        html.H5("Exploring imbalance, inequity, and bias in US political representation"),
        html.Hr(className="border-light"),
        dbc.Nav(className="nav nav-pills", children=[
            dbc.NavItem(dbc.NavLink("Home", href="/")),
            dbc.DropdownMenu(label="Visualizing Jim Crow voter suppression", nav=True, children=[
                dbc.DropdownMenuItem([html.I(className="fa"), "Intro: American voter enfranchisement"], href='/voter-weight-electoral-college-bias-intro', target="_blank"), 
                dbc.DropdownMenuItem([html.I(className="fa"), "Part 1: Electoral College bias"], href='/voter-weight-electoral-college-bias-page1', target="_blank"), 
                dbc.DropdownMenuItem([html.I(className="fa"), "Part 2: Small-state bias and slave-state bias"], href='/voter-weight-electoral-college-bias-page2', target="_blank"), 
                dbc.DropdownMenuItem([html.I(className="fa"), "Part 3: Reconstruction and Black voting rights"], href='/voter-weight-electoral-college-bias-page3', target="_blank"), 
                dbc.DropdownMenuItem([html.I(className="fa"), "Part 4: Suppression-state bias"], href='/voter-weight-electoral-college-bias-page4', target="_blank"), 
                dbc.DropdownMenuItem([html.I(className="fa"), "Part 5: Results and observations"], href='/voter-weight-results', target="_blank"), 
                dbc.DropdownMenuItem([html.I(className="fa"), "Part 6: Conclusions and interpretation"], href='/voter-weight-conclusions', target="_blank"), 
                dbc.DropdownMenuItem([html.I(className="fa"), "Appendix 1: Calculating Voter Weight"], href='/voter-weight-calculation', target="_blank"), 
                dbc.DropdownMenuItem([html.I(className="fa"), "Appendix 2: Annotated timeline"], href='/voter-weight-timeline-visualization', target="_blank"), 
                dbc.DropdownMenuItem([html.I(className="fa"), "Appendix 3: Explanation of state groupings"], href='/explanation-of-groupings', target="_blank"), 
                dbc.DropdownMenuItem([html.I(className="fa"), "The vault: 220 years of maps, charts, & figures"], href='/voter-weight-figure-vault', target="_blank"), 
            ]),
            dbc.DropdownMenu(label="References / Resources", nav=True, children=[
                dbc.DropdownMenuItem([html.I(className="fa"), "Sources / Notes"], href='/sources-notes', target="_blank"), 
                dbc.DropdownMenuItem([html.I(className="fa"), "Wikipedia election data portal"], href='https://en.wikipedia.org/wiki/List_of_United_States_presidential_election_results_by_state', target="_blank"),
                dbc.DropdownMenuItem([html.I(className="fa"), "Project source code"], href='https://github.com/dannynoonan/electoralytics', target="_blank"), 
            ])
        ])
    ])
])


year_slider_and_groups_selection = dbc.FormGroup([
    html.Br(),
    dbc.Row([
        dbc.Col(md=8, className="text-white", children=[
            html.H5("Election Year:")
        ]),
        dbc.Col(md=2, className="text-white", children=[
            html.H5("State Grouping Heuristic:")
        ]),
        dbc.Col(md=2, className="text-white", children=[
            html.H5("Extract Small States?")
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
                    int(y): {'label': str(y), 'style': {'transform': 'rotate(45deg)', 'color': 'white'}}
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
        dbc.Col(md=2, className="text-white", children=[
            html.H5("Display individual states:")
        ]),
        dbc.Col(md=2, className="text-white", children=[
            html.H5("Show / Hide:")
        ]),
        dbc.Col(md=2, className="text-white", children=[
            html.H5("State Grouping Heuristic:")
        ]),
        dbc.Col(md=2, className="text-white", children=[
            html.H5("Extract Small Group?")
        ]),
        dbc.Col(md=2, className="text-white", children=[
            html.H5("Y axis scale:")
        ]),
    ]),
    dbc.Row([
        dbc.Col(md=2, style={'textAlign': 'center'}, children=[
            dbc.Button("Clear canvas", id="clear-all-input", className="mr-2 bg-primary")
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
                className="text-white", 
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
                className="text-white", 
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


form_input_line_vw_timeline_short = dbc.FormGroup([
    html.Br(),
    dbc.Row([
        dbc.Col(md=2),
        dbc.Col(md=2, className="text-white", children=[
            html.H5("Display individual states:")
        ]),
        dbc.Col(md=2, className="text-white", children=[
            html.H5("Show / Hide:")
        ]),
        dbc.Col(md=2, className="text-white", children=[
            html.H5("State Grouping Heuristic:")
        ]),
        dbc.Col(md=2, className="text-white", children=[
            html.H5("Extract Small Group?")
        ]),
        dbc.Col(md=2, className="text-white", children=[
            html.H5("Y axis scale:")
        ]),
    ]),
    dbc.Row([
        dbc.Col(md=2, style={'textAlign': 'center'}, children=[
            dbc.Button("Clear canvas", id="clear-all-input", className="mr-2 bg-primary")
        ]),
        dbc.Col(md=2, style={'textAlign': 'left'}, children=[
            dcc.Dropdown(
                id="multi-state-input-short",
                options=[{'label': state, 'value': abbrev} for abbrev, state in data_obj.abbrevs_to_states.items()],
                multi=True,
                value=''
            )
        ]),
        dbc.Col(md=2, style={'textAlign': 'center'}, children=[
            dcc.Checklist(
                id="show-hide-input-short",
                className="text-white", 
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
                className="text-white", 
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


# def make_accordion_item(i, label, images, height):
#     """
#     generate reusable accordion elements
#     https://dash-bootstrap-components.opensource.faculty.ai/docs/components/collapse/
#     """
#     html_imgs = []
#     for img in images:
#         html_imgs.append(html.Img(src=f"{img}", height=f"{height}", style={"padding": "5px", "padding-top": "10px"}))
#     return dbc.Card(className="bg-success text-white", children=[
#         dbc.CardHeader(
#             html.H2(
#                 dbc.Button(f"{label}", className="text-white btn-lg", color="link", id=f"group-{i}-toggle")
#             )
#         ),
#         dbc.Collapse(
#             dbc.CardBody(
#                 html_imgs
#             ),
#             id=f"collapse-{i}",
#         ),
#     ])
