import dash
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
                html.H3("The Vault: 220 Years of Electoral College Bias Revealed in Figures and Maps"),
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
                        dbc.Tab(label="Scatter and Box Plots", tab_style={"font-size": "20px", "color": "white"}, children=[
                            dbc.Row([
                                dbc.Col(md=6, children=[
                                    dcc.Graph(id="fig-scatter-dots-vw-state"),
                                    dbc.Card(className="border-success", children=[
                                        dbc.CardBody([
                                            html.Small(className="card-text", children=[
                                                html.Li("Electoral College bias, shown by plotting Popular Vote (turnout) on the x axis against Electoral \
                                                    College Votes on the y axis."),
                                                html.Li("The average Popular Vote tally per Electoral College vote — where the Voter Weight ratio is 1.0 — \
                                                    is plotted as a diagonal line (labeled 'Nationwide mean')."),
                                                html.Li("States whose dots appear above and to the left of the nationwide mean line have Voter Weights greater \
                                                    than 1, those whose dots are below and to the right have Voter Weights less than 1."),
                                                html.Li(["Open an ", dcc.Link("intractive slideshow animation", 
                                                    href="https://htmlpreview.github.io/?https://github.com/dannynoonan/electoralytics/blob/master/html_figures/anim_scatter_state_vw_dots_acw4_1000.html",
                                                    target="_blank"), " illustrating the full history for the scatter plot above."]),
                                            ]),
                                        ]),
                                    ]), 
                                    html.Br(),                     
                                    dcc.Graph(id="fig-scatter-abbrevs-vw-state"),
                                    dbc.Card(className="border-success", children=[
                                        dbc.CardBody([
                                            html.Small(className="card-text", children=[
                                                html.Li("Same as plot above, except dots are replaced with abbreviations, and both the x and y axes are \
                                                    logarithmic to space out the entries at lower vote counts."),
                                                html.Li(["Open an ", dcc.Link("intractive slideshow animation", 
                                                    href="https://htmlpreview.github.io/?https://github.com/dannynoonan/electoralytics/blob/master/html_figures/anim_scatter_state_vw_abbrevs_acw4_1000.html",
                                                    target="_blank"), " illustrating the full history for the scatter plot above."]),
                                            ]),
                                        ]),
                                    ]), 
                                    html.Br(),
                                    dcc.Graph(id="fig-scatter-dots-vw-group"),
                                    dbc.Card(className="border-success", children=[
                                        dbc.CardBody([
                                            html.Small(className="card-text", children=[
                                                html.Li("Similar to scatter plots above, except rather than showing each individual state, this figure \
                                                    aggregates the Popular Vote and Electoral College votes for every state from a group into a single dot."),
                                                html.Li(["Open an ", dcc.Link("intractive slideshow animation", 
                                                    href="https://htmlpreview.github.io/?https://github.com/dannynoonan/electoralytics/blob/master/html_figures/anim_scatter_stategroup_vw_dots_acw4_1000.html",
                                                    target="_blank"), " illustrating the full history for the scatter plot above."]),
                                            ]),
                                        ]),
                                    ]),
                                ]),
                                dbc.Col(md=6, children=[
                                    dcc.Graph(id="fig-scatter-bubbles-vw-state"),
                                    dbc.Card(className="border-success", children=[
                                        dbc.CardBody([
                                            html.Small(className="card-text", children=[
                                                html.Li("Electoral College bias, shown by plotting Electoral College votes on the x axis against derived Voter \
                                                    Weight on the y axis, with Popular Vote represented by the size of each state’s “bubble.”"),
                                                html.Li("The national mean is anyplace where Voter Weight = 1.0. Voter Weights in states whose bubbles appear \
                                                    above the mean line were higher than average, suggesting some form of Electoral College bias."),
                                                html.Li("For small bubbles with low EC vote counts, high Voter Weight can be explained by small-state bias. \
                                                    For larger bubbles, high Voter Weight suggests depressed turnout or some other disparity between census \
                                                    apportionment and voter participation."),
                                                html.Li(["Open an ", dcc.Link("intractive slideshow animation", 
                                                    href="https://htmlpreview.github.io/?https://github.com/dannynoonan/electoralytics/blob/master/html_figures/anim_scatter_state_vw_bubbles_acw4_1000.html",
                                                    target="_blank"), " illustrating the full history for the scatter plot above."]),
                                            ]),
                                        ]),
                                    ]),
                                    html.Br(),
                                    dcc.Graph(id="fig-box-vw-group"),
                                    dbc.Card(className="border-success", children=[
                                        dbc.CardBody([
                                            html.Small(className="card-text", children=[
                                                "Box plot showing range of Voter Weights within each state grouping. Voter Weight is on a logarithmic scale.",
                                            ]),
                                        ]), 
                                    ]),
                                    html.Br(),
                                    dcc.Graph(id="fig-scatter-bubbles-vw-group"),
                                    dbc.Card(className="border-success", children=[
                                        dbc.CardBody([
                                            html.Small(className="card-text", children=[
                                                html.Li("Similar to bubble plot at top of the page, except rather than showing each individual state, this figure \
                                                    aggregates the Popular Vote and Electoral College votes for every state from a group into a single bubble."),
                                                html.Li(["Open an ", dcc.Link("intractive slideshow animation", 
                                                    href="https://htmlpreview.github.io/?https://github.com/dannynoonan/electoralytics/blob/master/html_figures/anim_scatter_stategroup_vw_bubbles_acw4_1000.html",
                                                    target="_blank"), " illustrating the full history for the scatter plot above."]),
                                            ]),
                                        ]),
                                    ]),
                                ]),
                            ])
                        ]),
                    ]),
                ]),
            ])
        ])
    ])
])