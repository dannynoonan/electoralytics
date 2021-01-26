import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import flask

import pandas as pd
import plotly.express as px

from dash_pages import (
    calculating_voter_weight, components, electoral_college_intro, explanation_of_groupings, landing_page,
    voter_weight_comparison_details, voter_weight_comparison_overview, voter_weight_reveals_electoral_college_bias)
from data_processor.data_objects import DataObject
from data_processor.functions import validate_input, map_to_subdir
from fig_builder import bar_plots, box_plots, choropleths, line_charts, scatter_plots
from metadata import Columns, DataDirs, FigDimensions, YEAR_0, YEAR_N


# base config
app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])
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


# app layout
app.layout = dbc.Container(fluid=True, children=[
    components.url_bar_and_content_div,
])

# app layout
app.validation_layout = dbc.Container(fluid=True, children=[
    components.url_bar_and_content_div,

    ## Body
    landing_page.content,
    voter_weight_comparison_overview.content,
    voter_weight_comparison_details.content,
    # voter_participation,
    electoral_college_intro.content,
    voter_weight_reveals_electoral_college_bias.content,
    calculating_voter_weight.content,
    explanation_of_groupings.content,
])


# Index callbacks
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/voter-weight-comparison-overview":
        return voter_weight_comparison_overview.content
    elif pathname == "/voter-weight-comparison-details":
        return voter_weight_comparison_details.content
    elif pathname == "/electoral-college-intro":
        return electoral_college_intro.content
    elif pathname == "/voter-weight-reveals-electoral-college-bias":
        return voter_weight_reveals_electoral_college_bias.content
    elif pathname == "/calculating-voter-weight":
        return calculating_voter_weight.content
    elif pathname == "/explanation-of-groupings":
        return explanation_of_groupings.content
    else:
        return landing_page.content


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


# voter-weight-reveals-electoral-college-bias callbacks
@app.callback(
    Output('fig-bar-small-state-bias', 'figure'),
    Output('fig-bar-slave-state-bias', 'figure'),
    Output('fig-scatter-dots-slave-state-bias', 'figure'),
    Output('fig-bar-suppression-state-bias', 'figure'),
    Output('fig-scatter-dots-suppression-state-bias', 'figure'),
    Output('fig-scatter-bubbles-suppression-state-bias', 'figure'),
    Output('fig-map-color-by-vw', 'figure'),
    Input('small-state-bias-year-input', 'value'),
    Input('slave-state-bias-year-input', 'value'),
    Input('suppression-state-bias-year-input', 'value'),    
    Input('map-color-by-vw-year-input', 'value'), 
)
def voter_weight_intro_page(small_state_bias_year_input, slave_state_bias_year_input, suppress_state_bias_year_input, map_color_by_vw_year_input):
    # process input
    small_state_bias_year = int(small_state_bias_year_input)
    slave_state_bias_year = int(slave_state_bias_year_input)
    suppress_state_bias_year = int(suppress_state_bias_year_input)
    map_color_by_vw_year = int(map_color_by_vw_year_input)
    # fig titles
    title_small_state_bias = 'States Grouped By Size, Ordered by Voter Weight (Small-State Bias)'
    title_slave_state_bias = 'Free vs Slave vs Small States, Ordered by Voter Weight (Slave-State Bias)'
    title_slave_state_bias_scatter_dots = 'Free vs Slave vs Small States, Pop Vote X EC Votes (Slave-State Bias)'
    title_suppress_state_bias = 'States Grouped By Civil War Alliance, Ordered by Voter Weight'
    title_suppress_state_bias_scatter_dots = 'States Grouped By Civil War Alliance, Pop Vote X EC Votes'
    title_suppress_state_bias_scatter_bubbles = 'States Grouped By Civil War Alliance, EC Votes X Vote Weight'
    # generate figs
    fig_bar_small_state_bias = bar_plots.build_ivw_by_state_bar(
        data_obj, ddirs.CENSUS, 5, frame=small_state_bias_year, color_col=cols.GROUP, show_era=False, alt_groups=['ecv_only'], 
        base_fig_title=title_small_state_bias)
    fig_bar_slave_state_bias = bar_plots.build_ivw_by_state_bar(
        data_obj, ddirs.ACW, 5, frame=slave_state_bias_year, color_col=cols.GROUP, show_era=False, alt_groups=['slave_free', 'split_small'], 
        base_fig_title=title_slave_state_bias, fig_width=fig_dims.MD6, fig_height=fig_dims.MD6)
    fig_scatter_dots_slave_state_bias = scatter_plots.build_ivw_by_state_scatter_dots(
        data_obj, ddirs.ACW, 5, frame=slave_state_bias_year, show_era=False, alt_groups=['slave_free', 'split_small'], 
        base_fig_title=title_slave_state_bias_scatter_dots)
    fig_bar_suppress_state_bias = bar_plots.build_ivw_by_state_bar(
        data_obj, ddirs.ACW, 5, frame=suppress_state_bias_year, color_col=cols.GROUP, show_era=False, alt_groups=['split_small'], 
        base_fig_title=title_suppress_state_bias)
    fig_scatter_dots_suppress_state_bias = scatter_plots.build_ivw_by_state_scatter_dots(
        data_obj, ddirs.ACW, 5, frame=suppress_state_bias_year, show_era=False, alt_groups=['split_small'], 
        base_fig_title=title_suppress_state_bias_scatter_dots)
    fig_scatter_bubbles_suppress_state_bias = scatter_plots.build_ivw_by_state_scatter_bubbles(
        data_obj, ddirs.ACW, 5, frame=suppress_state_bias_year, show_era=False, alt_groups=['split_small'], 
        base_fig_title=title_suppress_state_bias_scatter_bubbles)
    fig_map_color_by_vw = choropleths.build_ivw_by_state_map(
        data_obj, ddirs.ACW, 5, color_col=cols.LOG_VOTE_WEIGHT, fig_width=fig_dims.MD7, frame=map_color_by_vw_year)
    return (fig_bar_small_state_bias, fig_bar_slave_state_bias, fig_scatter_dots_slave_state_bias, fig_bar_suppress_state_bias, 
        fig_scatter_dots_suppress_state_bias, fig_scatter_bubbles_suppress_state_bias, fig_map_color_by_vw)


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


if __name__ == '__main__':
    app.run_server(debug=True)
    