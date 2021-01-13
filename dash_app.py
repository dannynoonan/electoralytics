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


### LAYOUT COMPONENTS ###
url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


navbar = html.Div([
    html.Br(),
    html.H1('Electoralytics - Visualizing Historical Presidential Election Data', id="nav-pills"),
    dbc.Nav(className="nav nav-pills", children=[
        dbc.DropdownMenu(label="Pages / Graphs", nav=True, children=[
            dbc.DropdownMenuItem([html.I(className="fa"), "Comparing Voter Impact Per State - Overview"], href='/voter-impact-comparison-overview', target="_blank"), 
            dbc.DropdownMenuItem([html.I(className="fa"), "Comparing Voter Impact Per State - Details"], href='/voter-impact-comparison-details', target="_blank"), 
            dbc.DropdownMenuItem([html.I(className="fa"), "Voter Participation Over Time"], href='/voter-participation', target="_blank"), 
            dbc.DropdownMenuItem([html.I(className="fa"), "Explanation of State Aggregate Groupings"], href='/explanation-of-groupings', target="_blank"), 
            dbc.DropdownMenuItem([html.I(className="fa"), "Sampler of Swallowed Votes"], href='/swallowed-vote-sampler', target="_blank"),
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
                id="y-axis-input",
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
voter_impact_comparison_overview = html.Div([
    navbar,
    html.Br(),
    dbc.Row([
        html.H2("Impact Per Voter Per State/Group Over Time"),
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
    html.Br(),html.Br(),
])


voter_impact_comparison_details = html.Div([
    navbar,
    html.Br(),
    dbc.Row([
        # html.H3("Comparing Individual Voter Impact Per State"),
        # html.H3("Comparing Vote Weight Per Ballot Cast Per State"),
        html.H3("Comparing Vote Weight Per Ballot Cast (Per State/Per Grouping)"),
    ], justify="center", align="center"),
    dbc.Row([
        dbc.Col(md=12, children=[
            year_slider_and_groups_selection,
            # group_select,
        ])
    ]),
    dbc.Row([
        dbc.Col(md=12, children=[
            # dbc.Col(html.H4("Inter-State Voter Impact Comparison"), width={"size": 6, "offset": 3}), 
            # html.Br(),
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
                            # dcc.Graph(id="fig-map-color-by-group"),
                            # html.Br(),
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


voter_participation = html.Div([
    navbar,
    html.Br(),
    dbc.Row([
        html.H2("Voter Participation Nationally Over Time"),
    ], justify="center", align="center"),
    dbc.Row([
        dbc.Col(md=12, children=[
            form_input_y_axis,
            dcc.Graph(id="fig-line-total-vote-over-time")
        ])
    ]),
    html.Br(),html.Br(),
])


explanation_of_groupings = html.Div([
    navbar,
    html.Br(),
    dbc.Row([
        html.H3("Explanation of State Aggregate Groupings"),
    ], justify="center", align="center"),
    html.Br(),
    dbc.Row([
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
        dbc.Col(md=12, children=[
            dbc.Tabs(className="nav nav-pills", children=[
                dbc.Tab(label="Civil War vs Regional Census - 2020", tab_style={"font-size": "20px"}, children=[
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-acw-2020"),
                            html.Br(),
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-census-2020"),
                            html.Br(),
                        ])
                    ])
                ]),
                dbc.Tab(label="2000", tab_style={"font-size": "20px"}, children=[
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-acw-2000"),
                            html.Br(),
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-census-2000"),
                            html.Br(),
                        ])
                    ])
                ]),
                dbc.Tab(label="1980", tab_style={"font-size": "20px"}, children=[
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-acw-1980"),
                            html.Br(),
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-census-1980"),
                            html.Br(),
                        ])
                    ])
                ]),
                dbc.Tab(label="1960", tab_style={"font-size": "20px"}, children=[
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-acw-1960"),
                            html.Br(),
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-census-1960"),
                            html.Br(),
                        ])
                    ])
                ]),
                dbc.Tab(label="1940", tab_style={"font-size": "20px"}, children=[
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-acw-1940"),
                            html.Br(),
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-census-1940"),
                            html.Br(),
                        ])
                    ])
                ]),
                dbc.Tab(label="1920", tab_style={"font-size": "20px"}, children=[
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-acw-1920"),
                            html.Br(),
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-census-1920"),
                            html.Br(),
                        ])
                    ])
                ]),
                dbc.Tab(label="1900", tab_style={"font-size": "20px"}, children=[
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-acw-1900"),
                            html.Br(),
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-census-1900"),
                            html.Br(),
                        ])
                    ])
                ]),
                dbc.Tab(label="1880", tab_style={"font-size": "20px"}, children=[
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-acw-1880"),
                            html.Br(),
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-census-1880"),
                            html.Br(),
                        ])
                    ])
                ]),
                dbc.Tab(label="1860", tab_style={"font-size": "20px"}, children=[
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-acw-1860"),
                            html.Br(),
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-census-1860"),
                            html.Br(),
                        ])
                    ])
                ]),
                dbc.Tab(label="1840", tab_style={"font-size": "20px"}, children=[
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-acw-1840"),
                            html.Br(),
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-census-1840"),
                            html.Br(),
                        ])
                    ])
                ]),
                dbc.Tab(label="1820", tab_style={"font-size": "20px"}, children=[
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-acw-1820"),
                            html.Br(),
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-census-1820"),
                            html.Br(),
                        ])
                    ])
                ]),
                dbc.Tab(label="1800", tab_style={"font-size": "20px"}, children=[
                    dbc.Row([
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-acw-1800"),
                            html.Br(),
                        ]),
                        dbc.Col(md=6, children=[
                            dcc.Graph(id="fig-map-census-1800"),
                            html.Br(),
                        ])
                    ])
                ])
            ])
        ])
    ])
])


swallowed_vote_sampler = html.Div([
    ## Top
    navbar,
    html.Br(),html.Br(),

    dbc.Row([
        ### input + panel
        dbc.Col(md=3, children=[
            swallowed_vote_view_dropdown,
            html.Br(),html.Br(),html.Br(),
            html.Div(id="todo")
        ]),
        ### figures
        dbc.Col(md=9, children=[
            dbc.Col(html.H4("2020 sampler of votes 'flipped' by the Electoral College"), width={"size": 6, "offset": 3}), 
            dbc.Tabs(className="nav nav-pills", children=[
                dbc.Tab(dcc.Graph(id="swallowed-vote-sampler-1"), label="Raw popular vote"),
                dbc.Tab(dcc.Graph(id="swallowed-vote-sampler-2"), label="Muted popular vote"),
                dbc.Tab(dcc.Graph(id="swallowed-vote-sampler-3"), label="Stacked popular vote"),
                dbc.Tab(dcc.Graph(id="swallowed-vote-sampler-4"), label="Converted to EC vote"),
            ])
        ])
    ])
])


empty_layout = html.Div([
    navbar,
])


# app layout
app.layout = dbc.Container(fluid=True, children=[
    url_bar_and_content_div,
])

# app layout
app.validation_layout = dbc.Container(fluid=True, children=[
    url_bar_and_content_div,

    ## Body
    voter_impact_comparison_overview,
    voter_impact_comparison_details,
    voter_participation,
    explanation_of_groupings,
    swallowed_vote_sampler,
    empty_layout,
])



# Index callbacks
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/voter-impact-comparison-overview":
        return voter_impact_comparison_overview
    elif pathname == "/voter-impact-comparison-details":
        return voter_impact_comparison_details
    elif pathname == "/voter-participation":
        return voter_participation
    elif pathname == "/explanation-of-groupings":
        return explanation_of_groupings
    elif pathname == "/swallowed-vote-sampler":
        return swallowed_vote_sampler
    else:
        return empty_layout


# voter-impact-comparison-overview callbacks
@app.callback(
    Output('fig-line-vote-weight-by-state-group', 'figure'),
    Input('groupings-input', 'value'),
    Input('max-small-input', 'value'),
    [Input('multi-state-input', 'value')],
    Input('y-axis-input', 'value'),
    [Input('show-hide-input', 'value')],
)
def display_voter_impact_comparison_overview(groupings_input, max_small_input, state_abbrevs, y_axis_input, show_hide_input):
    print(f"#### in display_voter_impact_comparison_overview")
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
    # generate figs
    fig_line_ivw_by_state_group = line_charts.build_ivw_by_state_group_line_chart(
        data_obj, groupings_input, max_small, fig_width=fig_dims.MD12, state_abbrevs=state_abbrevs, log_y=log_y, 
        display_groups=show_groups, display_events=show_events, display_eras=show_eras)
    return fig_line_ivw_by_state_group

# voter-impact-comparison-overview callbacks, tab 1 cont'd: clear-all-input
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
        print(f"n_clicks: {n_clicks}")
        return []
    else:
        return ['show_groups','show_events','show_eras']


# voter-impact-comparison-details callbacks, tab 1
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
    print(f"#### in display_state_level_figs")
    # process input
    year = int(year_input)
    max_small = int(max_small_input)
    # generate figs
    fig_map_color_by_state_vw = choropleths.build_ivw_by_state_map(data_obj, groupings_input, max_small, cols.LOG_VOTE_WEIGHT, fig_width=fig_dims.MD7, frame=year)
    fig_bar_state_vw_color_by_vw = bar_plots.build_ivw_by_state_bar(data_obj, groupings_input, max_small, fig_width=fig_dims.MD5, frame=year, color_col=cols.LOG_VOTE_WEIGHT)
    fig_map_color_by_group = choropleths.build_ivw_by_state_map(data_obj, groupings_input, max_small, cols.GROUP, fig_width=fig_dims.MD7, frame=year)
    fig_bar_state_vw_color_by_group = bar_plots.build_ivw_by_state_bar(data_obj, groupings_input, max_small, fig_width=fig_dims.MD5, frame=year)
    fig_bar_actual_vs_adj_ec = bar_plots.build_actual_vs_adjusted_ec_bar(data_obj, groupings_input, max_small, frame=year)
    fig_bar_actual_vs_adj_vw = bar_plots.build_actual_vs_adjusted_vw_bar(data_obj, groupings_input, max_small, frame=year)
    return fig_map_color_by_state_vw, fig_bar_state_vw_color_by_vw, fig_map_color_by_group, fig_bar_state_vw_color_by_group, fig_bar_actual_vs_adj_ec, fig_bar_actual_vs_adj_vw


# voter-impact-comparison-details callbacks, tab 2
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
def display_regional_aggregate_figs(year_input, groupings_input, max_small_input):
    print(f"#### in display_regional_aggregate_figs")
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


# voter-impact-comparison-details callbacks, tab 3
# @app.callback(
#     Output('vote-weight-comparison-by-state-map-1-anim', 'figure'),
#     Output('vote-weight-comparison-by-state-scatter-dots-anim', 'figure'),
#     Output('vote-weight-comparison-by-state-scatter-abbrevs-anim', 'figure'),
#     Output('vote-weight-comparison-by-state-scatter-bubbles-anim', 'figure'),
#     Input('groupings-input', 'value'),
#     Input('max-small-input', 'value'),
# )
# def display_state_level_anims(groupings_input, max_small_input):
#     print(f"#### in display_state_level_anims")
#     # process input
#     max_small = int(max_small_input)
#     # generate figs
#     anim_map_1 = choropleths.build_ivw_by_state_map(data_obj, groupings_input, max_small)
#     anim_scatter_dots = scatter_plots.build_ivw_by_state_scatter_dots(data_obj, groupings_input, max_small)
#     anim_scatter_abbrevs = scatter_plots.build_ivw_by_state_scatter_dots(data_obj, groupings_input, max_small, display_elements='abbrevs')
#     anim_scatter_bubbles = scatter_plots.build_ivw_by_state_scatter_bubbles(data_obj, groupings_input, max_small)
#     return anim_map_1, anim_scatter_dots, anim_scatter_abbrevs, anim_scatter_bubbles


# voter-impact-comparison-details callbacks, tab 4
# @app.callback(
#     Output('vote-weight-comparison-by-state-group-map-1-anim', 'figure'),
#     Output('vote-weight-comparison-by-state-group-scatter-dots-anim', 'figure'),
#     Output('vote-weight-comparison-by-state-group-scatter-bubbles-anim', 'figure'),
#     Input('groupings-input', 'value'),
#     Input('max-small-input', 'value'),
# )
# def display_regional_aggregate_anims(groupings_input, max_small_input):
#     print(f"#### in display_regional_aggregate_anims")
#     # process input
#     max_small = int(max_small_input)
#     # generate figs
#     anim_map_1 = choropleths.build_ivw_by_state_map(data_obj, groupings_input, max_small, cols.GROUP)
#     anim_scatter_dots = scatter_plots.build_ivw_by_state_group_scatter_dots(data_obj, groupings_input, max_small)
#     anim_scatter_bubbles = scatter_plots.build_ivw_by_state_group_scatter_bubbles(data_obj, groupings_input, max_small)
#     return anim_map_1, anim_scatter_dots, anim_scatter_bubbles


# voter-participation callbacks
@app.callback(
    Output('fig-line-total-vote-over-time', 'figure'),
    Input('y-axis-input', 'value'),
)
def display_voter_pct_pop_over_time(y_axis_input):
    print(f"#### in display_voter_pct_pop_over_time")
    # process input
    if y_axis_input == 'log':
        log_y = True
    else:
        log_y = False
    # generate figs
    fig_line_total_vote_over_time = line_charts.build_total_vote_line_chart(data_obj, fig_width=fig_dims.MD12, log_y=log_y)
    return fig_line_total_vote_over_time


# explanation-of-groupings callbacks
@app.callback(
    Output('fig-map-acw-2020', 'figure'),
    Output('fig-map-census-2020', 'figure'),
    Output('fig-map-acw-2000', 'figure'),
    Output('fig-map-census-2000', 'figure'),
    Output('fig-map-acw-1980', 'figure'),
    Output('fig-map-census-1980', 'figure'),
    Output('fig-map-acw-1960', 'figure'),
    Output('fig-map-census-1960', 'figure'),
    Output('fig-map-acw-1940', 'figure'),
    Output('fig-map-census-1940', 'figure'),
    Output('fig-map-acw-1920', 'figure'),
    Output('fig-map-census-1920', 'figure'),
    Output('fig-map-acw-1900', 'figure'),
    Output('fig-map-census-1900', 'figure'),
    Output('fig-map-acw-1880', 'figure'),
    Output('fig-map-census-1880', 'figure'),
    Output('fig-map-acw-1860', 'figure'),
    Output('fig-map-census-1860', 'figure'),
    Output('fig-map-acw-1840', 'figure'),
    Output('fig-map-census-1840', 'figure'),
    Output('fig-map-acw-1820', 'figure'),
    Output('fig-map-census-1820', 'figure'),
    Output('fig-map-acw-1800', 'figure'),
    Output('fig-map-census-1800', 'figure'),
    Input('max-small-input', 'value'),
)
def display_all_state_grouping_map_anims(max_small_input):
    print(f"#### in display_all_state_grouping_map_anims")
    # process input
    max_small = int(max_small_input)
    # generate figs
    fig_map_acw_2020 = choropleths.build_ivw_by_state_map(data_obj, ddirs.ACW, max_small, cols.GROUP, frame=2020)
    fig_map_census_2020 = choropleths.build_ivw_by_state_map(data_obj, ddirs.CENSUS, max_small, cols.GROUP, frame=2020)
    fig_map_acw_2000 = choropleths.build_ivw_by_state_map(data_obj, ddirs.ACW, max_small, cols.GROUP, frame=2000)
    fig_map_census_2000 = choropleths.build_ivw_by_state_map(data_obj, ddirs.CENSUS, max_small, cols.GROUP, frame=2000)
    fig_map_acw_1980 = choropleths.build_ivw_by_state_map(data_obj, ddirs.ACW, max_small, cols.GROUP, frame=1980)
    fig_map_census_1980 = choropleths.build_ivw_by_state_map(data_obj, ddirs.CENSUS, max_small, cols.GROUP, frame=1980)
    fig_map_acw_1960 = choropleths.build_ivw_by_state_map(data_obj, ddirs.ACW, max_small, cols.GROUP, frame=1960)
    fig_map_census_1960 = choropleths.build_ivw_by_state_map(data_obj, ddirs.CENSUS, max_small, cols.GROUP, frame=1960)
    fig_map_acw_1940 = choropleths.build_ivw_by_state_map(data_obj, ddirs.ACW, max_small, cols.GROUP, frame=1940)
    fig_map_census_1940 = choropleths.build_ivw_by_state_map(data_obj, ddirs.CENSUS, max_small, cols.GROUP, frame=1940)
    fig_map_acw_1920 = choropleths.build_ivw_by_state_map(data_obj, ddirs.ACW, max_small, cols.GROUP, frame=1920)
    fig_map_census_1920 = choropleths.build_ivw_by_state_map(data_obj, ddirs.CENSUS, max_small, cols.GROUP, frame=1920)
    fig_map_acw_1900 = choropleths.build_ivw_by_state_map(data_obj, ddirs.ACW, max_small, cols.GROUP, frame=1900)
    fig_map_census_1900 = choropleths.build_ivw_by_state_map(data_obj, ddirs.CENSUS, max_small, cols.GROUP, frame=1900)
    fig_map_acw_1880 = choropleths.build_ivw_by_state_map(data_obj, ddirs.ACW, max_small, cols.GROUP, frame=1880)
    fig_map_census_1880 = choropleths.build_ivw_by_state_map(data_obj, ddirs.CENSUS, max_small, cols.GROUP, frame=1880)
    fig_map_acw_1860 = choropleths.build_ivw_by_state_map(data_obj, ddirs.ACW, max_small, cols.GROUP, frame=1860)
    fig_map_census_1860 = choropleths.build_ivw_by_state_map(data_obj, ddirs.CENSUS, max_small, cols.GROUP, frame=1860)
    fig_map_acw_1840 = choropleths.build_ivw_by_state_map(data_obj, ddirs.ACW, max_small, cols.GROUP, frame=1840)
    fig_map_census_1840 = choropleths.build_ivw_by_state_map(data_obj, ddirs.CENSUS, max_small, cols.GROUP, frame=1840)
    fig_map_acw_1820 = choropleths.build_ivw_by_state_map(data_obj, ddirs.ACW, max_small, cols.GROUP, frame=1820)
    fig_map_census_1820 = choropleths.build_ivw_by_state_map(data_obj, ddirs.CENSUS, max_small, cols.GROUP, frame=1820)
    fig_map_acw_1800 = choropleths.build_ivw_by_state_map(data_obj, ddirs.ACW, max_small, cols.GROUP, frame=1800)
    fig_map_census_1800 = choropleths.build_ivw_by_state_map(data_obj, ddirs.CENSUS, max_small, cols.GROUP, frame=1800)
    return (fig_map_acw_2020, fig_map_census_2020, fig_map_acw_2000, fig_map_census_2000, fig_map_acw_1980, fig_map_census_1980, 
        fig_map_acw_1960, fig_map_census_1960, fig_map_acw_1940, fig_map_census_1940, fig_map_acw_1920, fig_map_census_1920, 
        fig_map_acw_1900, fig_map_census_1900, fig_map_acw_1880, fig_map_census_1880, fig_map_acw_1860, fig_map_census_1860, 
        fig_map_acw_1840, fig_map_census_1840, fig_map_acw_1820, fig_map_census_1820, fig_map_acw_1800, fig_map_census_1800)


# swallowed-vote-sampler callbacks
@app.callback(
    Output('swallowed-vote-sampler-1', 'figure'),
    Input('display-type', 'value'),
)
def display_swallowed_vote_fig_1(display_type):
    print(f"#### in display_swallowed_vote_fig_1")
    fig = bar_plots.build_swallowed_vote_bar(data_obj, 'raw', fig_width=1000)
    return fig

@app.callback(
    Output('swallowed-vote-sampler-2', 'figure'),
    Input('display-type', 'value'),
)
def display_swallowed_vote_fig_2(display_type):
    print(f"#### in display_swallowed_vote_fig_2")
    fig = bar_plots.build_swallowed_vote_bar(data_obj, 'muted', fig_width=1000)
    return fig

@app.callback(
    Output('swallowed-vote-sampler-3', 'figure'),
    Input('display-type', 'value'),
)
def display_swallowed_vote_fig_3(display_type):
    print(f"#### in display_swallowed_vote_fig_3")
    fig = bar_plots.build_swallowed_vote_relative_bar(data_obj, fig_width=1000)
    return fig

@app.callback(
    Output('swallowed-vote-sampler-4', 'figure'),
    Input('display-type', 'value'),
)
def display_swallowed_vote_fig_4(display_type):
    print(f"#### in display_swallowed_vote_fig_4")
    fig = bar_plots.build_swallowed_vote_ec_bar(data_obj, fig_width=1000)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
    