import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import flask

import pandas as pd
import plotly.express as px

from data_processor.data_objects import DataObject
from data_processor import fig_builder 
from data_processor.functions import validate_input


# base config
app = dash.Dash(external_stylesheets=[dbc.themes.SOLAR])
# server is needed for heroku deployment
server = app.server


# load source data for default subdir
data_obj = DataObject()
data_obj.load_pivot_on_year()
data_obj.melt_pivot_on_year()
data_obj.load_swallowed_vote_sampler()
data_obj.load_group_aggs_by_year()


### BOOTSTRAP COMPONENTS ###
# url / page  
url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# navbar
navbar = html.Div([
    html.H1('Electoralytics', id="nav-pills"),
    dbc.Nav(className="nav nav-pills", children=[
        dbc.DropdownMenu(label="Pages / Graphs", nav=True, children=[
            dbc.DropdownMenuItem([html.I(className="fa"), "Voter impact per state"], href='/page-1', target="_blank"), 
            dbc.DropdownMenuItem([html.I(className="fa"), "Swallowed vote sampler"], href='/page-2', target="_blank"),
            dbc.DropdownMenuItem([html.I(className="fa"), "Voter impact per state group"], href='/page-3', target="_blank"),
            dbc.DropdownMenuItem([html.I(className="fa"), "Maps"], href='/page-4', target="_blank"),
            dbc.DropdownMenuItem([html.I(className="fa"), "State scatter plots"], href='/page-5', target="_blank"),
            dbc.DropdownMenuItem([html.I(className="fa"), "State group scatter plots"], href='/page-6', target="_blank"),
            dbc.DropdownMenuItem([html.I(className="fa"), "State group line chart"], href='/page-7', target="_blank"),
        ]),
        dbc.DropdownMenu(label="References / Resources", nav=True, children=[
            dbc.DropdownMenuItem([html.I(className="fa"), "Source code"], href='https://github.com/dannynoonan/electoralytics', target="_blank"), 
            dbc.DropdownMenuItem([html.I(className="fa"), "Articles"], href='/resources/articles'),
            dbc.DropdownMenuItem([html.I(className="fa"), "Podcasts"], href='/resources/podcasts'),
            dbc.DropdownMenuItem([html.I(className="fa"), "Books"], href='/resources/books'),
        ])
    ])
])

# inputs
year_dropdown = dbc.FormGroup([
    html.H4("Election Year"),
    dcc.Dropdown(id="year-input", options=[{"label": y, "value": y} for y in data_obj.all_years], value="2020")
])

swallowed_vote_view_dropdown = dbc.FormGroup([
    html.H4("Swallowed vote view"),
    dcc.Dropdown(id="display-type", options=[{"label": "2020", "value": "2020"}], value="2020")
])


# page 1
layout_page_1 = html.Div([
    ## Top
    navbar,
    html.Br(),html.Br(),

    dbc.Row([
        ### input + panel
        dbc.Col(md=3, children=[
            year_dropdown, 
            html.Br(),html.Br(),html.Br(),
            html.Div(id="year-summary")
        ]),
        ### figures
        dbc.Col(md=9, children=[
            dbc.Col(html.H4("States where votes count the most"), width={"size": 6, "offset": 3}), 
            dbc.Tabs(className="nav nav-pills", children=[
                dbc.Tab(dcc.Graph(id="voter-impact-per-state"), label="Voter impact per state"),
                dbc.Tab(dcc.Graph(id="adjusted-ec-votes-per-state"), label="Actual vs Adjusted EC votes"),
            ])
        ])
    ])
])


# page 2
layout_page_2 = html.Div([
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


# page 3
layout_page_3 = html.Div([
    ## Top
    navbar,
    html.Br(),html.Br(),

    dbc.Row([
        ### input + panel
        dbc.Col(md=3, children=[
            year_dropdown, 
            html.Br(),html.Br(),html.Br(),
            html.Div(id="year-info")
        ]),
        ### figures
        dbc.Col(md=9, children=[
            dbc.Col(html.H4("Individual voter impact by state group"), width={"size": 6, "offset": 3}), 
            dcc.Graph(id="voter-impact-by-state-group-box")
        ])
    ])
])


# page 4
layout_page_4 = html.Div([
    ## Top
    navbar,
    html.Br(),html.Br(),

    dbc.Row([
        ### input + panel
        dbc.Col(md=3, children=[
            year_dropdown, 
            html.Br(),html.Br(),html.Br(),
            html.Div(id="year-details")
        ]),
        ### figures
        dbc.Col(md=9, children=[
            dbc.Col(html.H4("Maps of state groupings and influence"), width={"size": 6, "offset": 3}), 
            dbc.Tabs(className="nav nav-pills", children=[
                dbc.Tab(dcc.Graph(id="voter-impact-by-state-map"), label="Voter impact by state"),
                dbc.Tab(dcc.Graph(id="state-groups-map"), label="State groupings"),
            ])
        ])
    ])
])


# page 5
layout_page_5 = html.Div([
    ## Top
    navbar,
    html.Br(),html.Br(),

    dbc.Row([
        ### input + panel
        dbc.Col(md=3, children=[
            year_dropdown, 
            html.Br(),html.Br(),html.Br(),
            html.Div(id="year-stuff")
        ]),
        ### figures
        dbc.Col(md=9, children=[
            dbc.Col(html.H4("Scatter plots of voter impact by state"), width={"size": 6, "offset": 3}), 
            dbc.Tabs(className="nav nav-pills", children=[
                dbc.Tab(dcc.Graph(id="voter-impact-by-state-scatter-1"), label="State scatter 1"),
                dbc.Tab(dcc.Graph(id="voter-impact-by-state-scatter-2"), label="State scatter 2"),
                dbc.Tab(dcc.Graph(id="voter-impact-by-state-scatter-3"), label="State scatter 3"),
            ])
        ])
    ])
])


# page 6
layout_page_6 = html.Div([
    ## Top
    navbar,
    html.Br(),html.Br(),

    dbc.Row([
        ### input + panel
        dbc.Col(md=3, children=[
            year_dropdown, 
            html.Br(),html.Br(),html.Br(),
            html.Div(id="year-stuff")
        ]),
        ### figures
        dbc.Col(md=9, children=[
            dbc.Col(html.H4("Scatter plots of voter impact by state group"), width={"size": 6, "offset": 3}), 
            dbc.Tabs(className="nav nav-pills", children=[
                dbc.Tab(dcc.Graph(id="voter-impact-by-state-group-scatter-1"), label="State group scatter 1"),
                dbc.Tab(dcc.Graph(id="voter-impact-by-state-group-scatter-2"), label="State group scatter 2"),
            ])
        ])
    ])
])


# page 7
layout_page_7 = html.Div([
    ## Top
    navbar,
    html.Br(),html.Br(),

    dbc.Row([
        ### input + panel
        dbc.Col(md=3, children=[
            year_dropdown, 
            html.Br(),html.Br(),html.Br(),
            html.Div(id="year-fluffle")
        ]),
        ### figures
        dbc.Col(md=9, children=[
            dbc.Col(html.H4("Line chart of voter impact by state group"), width={"size": 6, "offset": 3}), 
            dcc.Graph(id="voter-impact-by-state-group-line")
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
    layout_page_1,
    layout_page_2,
    layout_page_3,
    layout_page_4,
    layout_page_5,
    layout_page_6,
    layout_page_7,
    empty_layout,
])



# Index callbacks
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/page-1":
        return layout_page_1
    elif pathname == "/page-2":
        return layout_page_2
    elif pathname == "/page-3":
        return layout_page_3
    elif pathname == "/page-4":
        return layout_page_4
    elif pathname == "/page-5":
        return layout_page_5
    elif pathname == "/page-6":
        return layout_page_6
    elif pathname == "/page-7":
        return layout_page_7
    else:
        return empty_layout


# Page 1 callbacks
@app.callback(
    Output('voter-impact-per-state', 'figure'),
    Input('year-input', 'value'),
)
def update_figure(year_input):
    year = int(year_input)
    fig = fig_builder.build_fig_for_year(data_obj, year)
    return fig


@app.callback(
    Output('adjusted-ec-votes-per-state', 'figure'),
    Input('year-input', 'value'),
)
def update_overlay_figure(year_input):
    year = int(year_input)
    fig = fig_builder.build_actual_vs_adjusted_ec_fig(data_obj, year)
    return fig


# Page 2 callbacks
@app.callback(
    Output('swallowed-vote-sampler-1', 'figure'),
    Input('display-type', 'value'),
)
def display_swallowed_vote_fig_1(display_type):
    fig = fig_builder.build_swallowed_vote_fig_1(data_obj)
    return fig

@app.callback(
    Output('swallowed-vote-sampler-2', 'figure'),
    Input('display-type', 'value'),
)
def display_swallowed_vote_fig_2(display_type):
    fig = fig_builder.build_swallowed_vote_fig_2(data_obj)
    return fig

@app.callback(
    Output('swallowed-vote-sampler-3', 'figure'),
    Input('display-type', 'value'),
)
def display_swallowed_vote_fig_3(display_type):
    fig = fig_builder.build_swallowed_vote_fig_3(data_obj)
    return fig

@app.callback(
    Output('swallowed-vote-sampler-4', 'figure'),
    Input('display-type', 'value'),
)
def display_swallowed_vote_fig_4(display_type):
    fig = fig_builder.build_swallowed_vote_fig_4(data_obj)
    return fig


# Page 3 callbacks
@app.callback(
    Output('voter-impact-by-state-group-box', 'figure'),
    Input('year-input', 'value'),
)
def display_voter_impact_by_state_group_box(year_input):
    year = int(year_input)
    fig = fig_builder.build_ivw_by_state_group_box_plot(data_obj, year)
    return fig


# Page 4 callbacks
@app.callback(
    Output('voter-impact-by-state-map', 'figure'),
    Input('year-input', 'value'),
)
def display_voter_impact_by_state_map(year_input):
    year = int(year_input)
    fig = fig_builder.build_ivw_by_state_map(data_obj, year)
    return fig

@app.callback(
    Output('state-groups-map', 'figure'),
    Input('year-input', 'value'),
)
def display_state_groups_map(year_input):
    year = int(year_input)
    fig = fig_builder.build_state_groups_map(data_obj, year)
    return fig


# Page 5 callbacks
@app.callback(
    Output('voter-impact-by-state-scatter-1', 'figure'),
    Input('year-input', 'value'),
)
def display_voter_impact_by_state_scatter_1(year_input):
    year = int(year_input)
    fig = fig_builder.build_ivw_by_state_scatter_1(data_obj, year)
    return fig

@app.callback(
    Output('voter-impact-by-state-scatter-2', 'figure'),
    Input('year-input', 'value'),
)
def display_voter_impact_by_state_scatter_2(year_input):
    year = int(year_input)
    fig = fig_builder.build_ivw_by_state_scatter_2(data_obj, year)
    return fig

@app.callback(
    Output('voter-impact-by-state-scatter-3', 'figure'),
    Input('year-input', 'value'),
)
def display_voter_impact_by_state_scatter_3(year_input):
    year = int(year_input)
    fig = fig_builder.build_ivw_by_state_scatter_3(data_obj, year)
    return fig


# Page 6 callbacks
@app.callback(
    Output('voter-impact-by-state-group-scatter-1', 'figure'),
    Input('year-input', 'value'),
)
def display_voter_impact_by_state_group_scatter_1(year_input):
    year = int(year_input)
    fig = fig_builder.build_ivw_by_state_group_scatter_1(data_obj, year)
    return fig

@app.callback(
    Output('voter-impact-by-state-group-scatter-2', 'figure'),
    Input('year-input', 'value'),
)
def display_voter_impact_by_state_group_scatter_2(year_input):
    year = int(year_input)
    fig = fig_builder.build_ivw_by_state_group_scatter_2(data_obj, year)
    return fig


# Page 7 callbacks
@app.callback(
    Output('voter-impact-by-state-group-line', 'figure'),
    Input('year-input', 'value'),
)
def display_voter_impact_by_state_group_line(year_input):
    year = int(year_input)
    fig = fig_builder.build_ivw_by_state_group_line_chart(data_obj, year)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)