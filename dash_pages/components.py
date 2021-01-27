import dash
from dash.dependencies import Input, Output, State
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
data_obj.load_swallowed_vote_sampler()

cols = Columns()
ddirs = DataDirs()
fig_dims = FigDimensions()


url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


navbar = dbc.Card(className="text-white bg-primary", children=[
    dbc.CardBody([
        html.Br(),
        html.H2("Electoralytics - Visualizing Historical Presidential Election Data", id="nav-pills", style={"text-align": "center"}),
        html.Hr(className="border-light"),
        dbc.Nav(className="nav nav-pills", children=[
            dbc.DropdownMenu(label="Visualizing Voter Inequity", nav=True, children=[
                dbc.DropdownMenuItem([html.I(className="fa"), "Intro to Voter Weight And Electoral College Bias"], href='/voter-weight-electoral-college-bias-overview', target="_blank"), 
                dbc.DropdownMenuItem([html.I(className="fa"), "Calculating Voter Weight"], href='/voter-weight-calculation', target="_blank"), 
                dbc.DropdownMenuItem([html.I(className="fa"), "Explanation of State Groupings"], href='/explanation-of-groupings', target="_blank"), 
                dbc.DropdownMenuItem([html.I(className="fa"), "Discussion and Conclusions"], href='/voter-weight-conclusions', target="_blank"), 
            ]),
            dbc.DropdownMenu(label="Maps, Charts, and Graphs", nav=True, children=[
                dbc.DropdownMenuItem([html.I(className="fa"), "Voter Weight Timeline Visualizations"], href='/voter-weight-timeline-visualization', target="_blank"), 
                dbc.DropdownMenuItem([html.I(className="fa"), "Voter Weight Figure Vault"], href='/voter-weight-figure-vault', target="_blank"), 
            ]),
            dbc.DropdownMenu(label="References / Resources", nav=True, children=[
                dbc.DropdownMenuItem([html.I(className="fa"), "Project source code"], href='https://github.com/dannynoonan/electoralytics', target="_blank"), 
                # dbc.DropdownMenuItem([html.I(className="fa"), "Articles, Podcasts, Books"], href='/resources/articles-podcasts-books'),
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
            html.H5("Extract Small Group?")
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


form_input_y_axis = dbc.FormGroup([
    dbc.Row([
        dbc.Col(md=2, className="text-white", style={'textAlign': 'left'}, children=[
            html.H4("Y axis:"),
            dcc.RadioItems(
                id="y-axis-input-2",
                className="text-white", 
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