import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash_pages.components import navbar, year_slider_and_groups_selection


content = voter_weight_comparison_details = html.Div([
    navbar,
    dbc.Card(className="bg-success", children=[
        dbc.CardBody([
            html.Br(),
            dbc.Row(className="text-white", justify="center", align="center", children=[
                html.H3("Comparing Voter Weight Per State/Per Grouping"),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=12, children=[
                    year_slider_and_groups_selection
                ])
            ]),
            dbc.Row([
                dbc.Col(md=12, children=[
                    dbc.Tabs(className="nav nav-tabs", children=[
                        dbc.Tab(label="Maps and Bar Charts", tab_style={"font-size": "20px", "color": "white"}, children=[
                            dbc.Row([
                                dbc.Col(md=7, children=[
                                    dcc.Graph(id="fig-map-color-by-state-vw"),
                                    html.Br(),
                                    dbc.Card(className="border-success", children=[
                                        dbc.CardBody([
                                            html.P(className="card-text", children=[
                                                "Open an ", dcc.Link("intractive slideshow animation", 
                                                href="https://htmlpreview.github.io/?https://github.com/dannynoonan/electoralytics/blob/master/html_figures/anim_map_state_vw_acw4_1000.html",
                                                target="_blank"), " illustrating the full history for the map above.",
                                            ]),
                                            html.P(className="card-text", style={"float": "right"}, children=[
                                                "Open an ", dcc.Link("intractive slideshow animation", 
                                                href="https://htmlpreview.github.io/?https://github.com/dannynoonan/electoralytics/blob/master/html_figures/anim_bar_state_vw_color_by_vw_acw4_900.html",
                                                target="_blank"), " illustrating the full history for the chart to the right.",
                                            ]),
                                        ]),
                                    ])
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
                                    dbc.Card(className="border-success", children=[
                                        dbc.CardBody([
                                            html.P(className="card-text", children=[
                                                "Open an ", dcc.Link("intractive slideshow animation", 
                                                href="https://htmlpreview.github.io/?https://github.com/dannynoonan/electoralytics/blob/master/html_figures/anim_map_state_groups_acw4_1000.html",
                                                target="_blank"), " illustrating the full history for the map above.",
                                            ]),
                                            html.P(className="card-text", style={"float": "right"}, children=[
                                                "Open an ", dcc.Link("intractive slideshow animation", 
                                                href="https://htmlpreview.github.io/?https://github.com/dannynoonan/electoralytics/blob/master/html_figures/anim_bar_state_vw_color_by_group_acw0_900.html",
                                                target="_blank"), " illustrating the full history for the chart to the right.",
                                            ]),
                                        ]),
                                    ])
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
                        dbc.Tab(label="Scatter Plots", tab_style={"font-size": "20px", "color": "white"}, children=[
                            dbc.Row([
                                dbc.Col(md=6, children=[
                                    dcc.Graph(id="fig-scatter-dots-vw-state"),
                                    html.Br(),
                                    dbc.Card(className="border-success", children=[
                                        dbc.CardBody([
                                            html.P(className="card-text", children=[
                                                "Open an ", dcc.Link("intractive slideshow animation", 
                                                href="https://htmlpreview.github.io/?https://github.com/dannynoonan/electoralytics/blob/master/html_figures/anim_scatter_state_vw_dots_acw4_1000.html",
                                                target="_blank"), " illustrating the full history for the scatter plot above.",
                                            ]),
                                        ]),
                                    ]), 
                                    html.Br(),                     
                                    dcc.Graph(id="fig-scatter-bubbles-vw-state"),
                                    html.Br(), 
                                    dbc.Card(className="border-success", children=[
                                        dbc.CardBody([
                                            html.P(className="card-text", children=[
                                                "Open an ", dcc.Link("intractive slideshow animation", 
                                                href="https://htmlpreview.github.io/?https://github.com/dannynoonan/electoralytics/blob/master/html_figures/anim_scatter_state_vw_bubbles_acw4_1000.html",
                                                target="_blank"), " illustrating the full history for the scatter plot above.",
                                            ]),
                                        ]),
                                    ]), 
                                    html.Br(),
                                    dcc.Graph(id="fig-scatter-abbrevs-vw-state"),
                                    html.Br(),
                                    dbc.Card(className="border-success", children=[
                                        dbc.CardBody([
                                            html.P(className="card-text", children=[
                                                "Open an ", dcc.Link("intractive slideshow animation", 
                                                href="https://htmlpreview.github.io/?https://github.com/dannynoonan/electoralytics/blob/master/html_figures/anim_scatter_state_vw_abbrevs_acw4_1000.html",
                                                target="_blank"), " illustrating the full history for the scatter plot above.",
                                            ]),
                                        ]),
                                    ]), 
                                    html.Br(),
                                ]),
                                dbc.Col(md=6, children=[
                                    dcc.Graph(id="fig-scatter-dots-vw-group"),
                                    html.Br(),
                                    dbc.Card(className="border-success", children=[
                                        dbc.CardBody([
                                            html.P(className="card-text", children=[
                                                "Open an ", dcc.Link("intractive slideshow animation", 
                                                href="https://htmlpreview.github.io/?https://github.com/dannynoonan/electoralytics/blob/master/html_figures/anim_scatter_stategroup_vw_dots_acw4_1000.html",
                                                target="_blank"), " illustrating the full history for the scatter plot above.",
                                            ]),
                                        ]),
                                    ]), 
                                    html.Br(),
                                    dcc.Graph(id="fig-scatter-bubbles-vw-group"),
                                    html.Br(),
                                    dbc.Card(className="border-success", children=[
                                        dbc.CardBody([
                                            html.P(className="card-text", children=[
                                                "Open an ", dcc.Link("intractive slideshow animation", 
                                                href="https://htmlpreview.github.io/?https://github.com/dannynoonan/electoralytics/blob/master/html_figures/anim_scatter_stategroup_vw_bubbles_acw4_1000.html",
                                                target="_blank"), " illustrating the full history for the scatter plot above.",
                                            ]),
                                        ]),
                                    ]), 
                                    html.Br(),
                                    dcc.Graph(id="fig-box-vw-group"),
                                    html.Br(),
                                ]),
                            ])
                        ]),
                    ]),
                ]),
            ])
        ])
    ])
])