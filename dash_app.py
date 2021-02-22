import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import flask

import pandas as pd
import plotly.express as px

from dash_pages import (
    components, electoral_college_intro, explanation_of_groupings, home_page, voter_weight_landing, voter_weight_calculation, 
    voter_weight_conclusions, voter_weight_main, voter_weight_figure_vault, voter_weight_timeline_viz)
from data_processor.data_objects import DataObject
from data_processor.functions import map_to_subdir
from fig_builder import bar_plots, box_plots, choropleths, line_charts, scatter_plots
from metadata import Columns, DataDirs, FigDimensions, YEAR_0, YEAR_N


# base config
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY], title='Electoralytics - Visualizing Historical Presidential Election Data')
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

# app validation_layout
app.validation_layout = dbc.Container(fluid=True, children=[
    components.url_bar_and_content_div,

    ## Body
    home_page.content,
    voter_weight_landing.content,
    voter_weight_main.content,
    voter_weight_calculation.content,
    explanation_of_groupings.content,
    voter_weight_conclusions.content,
    voter_weight_timeline_viz.content,
    voter_weight_figure_vault.content,
    electoral_college_intro.content,
])


# Index callbacks
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/voter-weight-electoral-college-bias-intro":
        return voter_weight_landing.content
    elif pathname == "/voter-weight-electoral-college-bias-main":
        return voter_weight_main.content
    elif pathname == "/voter-weight-calculation":
        return voter_weight_calculation.content
    elif pathname == "/explanation-of-groupings":
        return explanation_of_groupings.content
    elif pathname == "/voter-weight-conclusions":
        return voter_weight_conclusions.content
    elif pathname == "/voter-weight-timeline-visualization":
        return voter_weight_timeline_viz.content
    elif pathname == "/voter-weight-figure-vault":
        return voter_weight_figure_vault.content
    elif pathname == "/electoral-college-intro":
        return electoral_college_intro.content
    else:
        return home_page.content


############ voter-weight-electoral-college-bias-intro
@app.callback(
    Output('fig-bar-slavery-jimcrow-vw-bias', 'figure'),
    Output('fig-scatter-dots-slavery-jimcrow-vw-bias', 'figure'),
    Input('year-input-slavery-jimcrow-vw-bias-bar', 'value'),
    Input('year-input-slavery-jimcrow-vw-bias-scatter-dots', 'value'))
def display_landing_page(bar_year_input, scatter_year_input):
    # process input
    bar_year = int(bar_year_input)
    scatter_year = int(scatter_year_input)
    # fig titles
    bar_title = "How much did each person’s vote count in each state?"
    scatter_title = "How did each state’s Electoral College apportionment<br>compare to its voter turnout?"
    # generate figs
    fig_bar_slavery_jimcrow_vw_bias = bar_plots.build_vw_by_state_bar(
        data_obj, ddirs.ACW, 4, frame=bar_year, color_col=cols.GROUP, show_era=False, base_fig_title=bar_title, fig_height=850)
    fig_scatter_dots_slavery_jimcrow_vw_bias = scatter_plots.build_vw_by_state_scatter_dots(
        data_obj, ddirs.ACW, 4, frame=scatter_year, show_era=False, base_fig_title=scatter_title)
    return fig_bar_slavery_jimcrow_vw_bias, fig_scatter_dots_slavery_jimcrow_vw_bias


############ voter-weight-electoral-college-bias-main callbacks
@app.callback(
    Output('fig-bar-small-state-bias', 'figure'),
    Output('fig-map-small-state-bias', 'figure'),
    Output('fig-bar-slave-state-bias', 'figure'),
    Output('fig-scatter-dots-slave-state-bias', 'figure'),
    Output('fig-map-slave-state-bias', 'figure'),
    Output('fig-bar-suppress-state-bias', 'figure'),
    Output('fig-scatter-dots-suppress-state-bias', 'figure'),
    Output('fig-scatter-bubbles-suppress-state-bias', 'figure'),
    Output('fig-map-suppress-state-bias', 'figure'),
    # Output('fig-map-color-by-vw', 'figure'),
    Input('small-state-bias-year-input', 'value'),
    Input('slave-state-bias-year-input', 'value'),
    Input('suppress-state-bias-year-input', 'value'))    
    # Input('map-color-by-vw-year-input', 'value'))
def display_voter_weight_main(small_state_bias_year_input, slave_state_bias_year_input, suppress_state_bias_year_input):
    # process input
    small_state_bias_year = int(small_state_bias_year_input)
    slave_state_bias_year = int(slave_state_bias_year_input)
    suppress_state_bias_year = int(suppress_state_bias_year_input)
    # map_color_by_vw_year = int(map_color_by_vw_year_input)
    # fig titles
    title_small_state_bias_bar = 'Whose vote counted more? Small-state bias<br>States ordered by Voter Weight, shaded by size'
    title_small_state_bias_map = 'States shaded by Electoral College votes (i.e. size/population)'
    title_slave_state_bias_bar = 'Whose vote counted more? Slave-State Bias<br>Free vs slave vs small states, ordered by Voter Weight'
    title_slave_state_bias_scatter_dots = 'Slave-state bias<br>Free vs slave vs small states, EC votes x voter turnout'
    title_slave_state_bias_map = 'Free states vs slave states vs small states'
    title_suppress_state_bias_bar = 'Whose vote counted more? Suppression-state bias<br>States shaded by Civil War grouping, ordered by Voter Weight'
    title_suppress_state_bias_scatter_dots = 'Suppression-state bias<br>States shaded by Civil War grouping, EC votes x voter turnout'
    title_suppress_state_bias_scatter_bubbles = 'Suppression-state bias<br>States shaded by Civil War grouping, EC votes x Voter Weight'
    # title_suppress_state_bias_map = 'States Shaded By Civil War Alliance'
    # generate figs
    fig_bar_small_state_bias = bar_plots.build_vw_by_state_bar(
        data_obj, ddirs.CENSUS, 5, color_col=cols.GROUP, frame=small_state_bias_year, show_era=False, alt_groups=['ecv_only'], 
        base_fig_title=title_small_state_bias_bar)
    fig_map_small_state_bias = choropleths.build_vw_by_state_map(
        data_obj, ddirs.CENSUS, 5, color_col=cols.GROUP, frame=small_state_bias_year, show_era=False, alt_groups=['ecv_only'], 
        base_fig_title=title_small_state_bias_map)
    fig_bar_slave_state_bias = bar_plots.build_vw_by_state_bar(
        data_obj, ddirs.ACW, 5, frame=slave_state_bias_year, color_col=cols.GROUP, show_era=False, alt_groups=['slave_free', 'split_small'], 
        base_fig_title=title_slave_state_bias_bar, fig_width=fig_dims.MD6, fig_height=fig_dims.MD6)
    fig_scatter_dots_slave_state_bias = scatter_plots.build_vw_by_state_scatter_dots(
        data_obj, ddirs.ACW, 5, frame=slave_state_bias_year, show_era=False, alt_groups=['slave_free', 'split_small'], 
        base_fig_title=title_slave_state_bias_scatter_dots)
    fig_map_slave_state_bias = choropleths.build_vw_by_state_map(
        data_obj, ddirs.ACW, 5, color_col=cols.GROUP, frame=slave_state_bias_year, show_era=False, alt_groups=['slave_free', 'split_small'], 
        base_fig_title=title_slave_state_bias_map)
    fig_bar_suppress_state_bias = bar_plots.build_vw_by_state_bar(
        data_obj, ddirs.ACW, 5, frame=suppress_state_bias_year, color_col=cols.GROUP, show_era=False, alt_groups=['split_small'], 
        base_fig_title=title_suppress_state_bias_bar)
    fig_scatter_dots_suppress_state_bias = scatter_plots.build_vw_by_state_scatter_dots(
        data_obj, ddirs.ACW, 5, frame=suppress_state_bias_year, show_era=False, alt_groups=['split_small'], 
        base_fig_title=title_suppress_state_bias_scatter_dots)
    fig_scatter_bubbles_suppress_state_bias = scatter_plots.build_vw_by_state_scatter_bubbles(
        data_obj, ddirs.ACW, 5, frame=suppress_state_bias_year, show_era=False, alt_groups=['split_small'], 
        base_fig_title=title_suppress_state_bias_scatter_bubbles)
    fig_map_suppress_state_bias = choropleths.build_vw_by_state_map(
        data_obj, ddirs.ACW, 5, color_col=cols.GROUP, frame=suppress_state_bias_year, show_era=False, alt_groups=['split_small'])
    # fig_map_color_by_vw = choropleths.build_vw_by_state_map(
    #     data_obj, ddirs.ACW, 5, color_col=cols.LOG_VOTE_WEIGHT, fig_width=fig_dims.MD7, frame=map_color_by_vw_year)
    return (fig_bar_small_state_bias, fig_map_small_state_bias, fig_bar_slave_state_bias, fig_scatter_dots_slave_state_bias, fig_map_slave_state_bias, 
        fig_bar_suppress_state_bias, fig_scatter_dots_suppress_state_bias, fig_scatter_bubbles_suppress_state_bias, fig_map_suppress_state_bias)


############ voter-weight-calculation callbacks
@app.callback(
    Output('fig-map-color-by-vw', 'figure'),
    Input('map-color-by-vw-year-input', 'value'))
def display_voter_weight_calculation(year_input):
    # process input
    year = int(year_input)
    # generate figs
    fig_map_color_by_vw = choropleths.build_vw_by_state_map(
        data_obj, ddirs.ACW, 5, color_col=cols.LOG_VOTE_WEIGHT, fig_width=fig_dims.MD7, frame=year)
    return fig_map_color_by_vw


############ explanation-of-groupings callbacks
@app.callback(
    Output('fig-map-acw', 'figure'),
    Output('fig-map-census', 'figure'),
    Input('year-input', 'value'),
    Input('max-small-input', 'value'))
def display_explanation_of_groupings(year_input, max_small_input):
    # process input
    year = int(year_input)
    max_small = int(max_small_input)
    # generate figs
    fig_map_acw = choropleths.build_vw_by_state_map(data_obj, ddirs.ACW, max_small, color_col=cols.GROUP, frame=year)
    fig_map_census = choropleths.build_vw_by_state_map(data_obj, ddirs.CENSUS, max_small, color_col=cols.GROUP, frame=year)
    return fig_map_acw, fig_map_census


############ voter-weight-timeline-viz callbacks ############ 
@app.callback(
    Output('fig-line-vote-weight-by-state-group', 'figure'),
    Output('fig-line-total-vote-over-time', 'figure'),
    Input('groupings-input', 'value'),
    Input('max-small-input', 'value'),
    [Input('multi-state-input', 'value')],
    Input('y-axis-input', 'value'),
    [Input('show-hide-input', 'value')],
    Input('y-axis-input-2', 'value'))
def display_voter_weight_timeline_viz(groupings_input, max_small_input, state_abbrevs, y_axis_input, show_hide_input, y_axis_input_2):
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
    fig_line_vw_by_state_group = line_charts.build_vw_by_state_group_line_chart(
        data_obj, groupings_input, max_small, fig_width=fig_dims.MD12, state_abbrevs=state_abbrevs, log_y=log_y, 
        display_groups=show_groups, display_events=show_events, display_eras=show_eras)
    fig_line_total_vote_over_time = line_charts.build_total_vote_line_chart(data_obj, fig_width=fig_dims.MD12, log_y=log_y_2)
    return fig_line_vw_by_state_group, fig_line_total_vote_over_time

# voter-weight-timeline-viz callbacks cont'd: clear-all-input
@app.callback(
    Output('multi-state-input', 'value'),
    [Input('clear-all-input', 'n_clicks')])
def clear_canvas_1(n_clicks):
    return []

@app.callback(
    Output('show-hide-input', 'value'),
    [Input('clear-all-input', 'n_clicks')])
def clear_canvas_2(n_clicks):
    if n_clicks and int(n_clicks) > 0:
        return []
    else:
        return ['show_groups','show_events','show_eras']


############ voter-weight-figure-vault callbacks, tab 1 ############ 
@app.callback(
    Output('fig-map-color-by-state-vw', 'figure'),
    Output('fig-bar-state-vw-color-by-vw', 'figure'),
    Output('fig-map-color-by-group', 'figure'),
    Output('fig-bar-state-vw-color-by-group', 'figure'),
    Output('fig-bar-actual-vs-adj-ec', 'figure'),
    Output('fig-bar-actual-vs-adj-vw', 'figure'),
    Input('year-input', 'value'),
    Input('groupings-input', 'value'),
    Input('max-small-input', 'value'))
def display_voter_weight_figure_vault_tab1(year_input, groupings_input, max_small_input):
    # process input
    year = int(year_input)
    max_small = int(max_small_input)
    # title overrides
    groupings_label = 'Civil War Alliance'
    if groupings_input == ddirs.CENSUS:
        groupings_label = 'Regional Census'
    title_map_color_by_vw = 'States Shaded by Voter Weight'
    title_bar_color_by_vw = 'States Shaded & Sequenced by Voter Weight'
    title_bar_color_by_group = f'States Grouped by {groupings_label}, Ordered by Voter Weight'
    # generate figs
    fig_map_color_by_state_vw = choropleths.build_vw_by_state_map(
        data_obj, groupings_input, max_small, color_col=cols.LOG_VOTE_WEIGHT, fig_width=fig_dims.MD7, frame=year, 
        base_fig_title=title_map_color_by_vw)
    fig_bar_state_vw_color_by_vw = bar_plots.build_vw_by_state_bar(
        data_obj, groupings_input, max_small, color_col=cols.LOG_VOTE_WEIGHT, fig_width=fig_dims.MD5, frame=year, 
        base_fig_title=title_bar_color_by_vw, show_era=False)
    fig_map_color_by_group = choropleths.build_vw_by_state_map(
        data_obj, groupings_input, max_small, color_col=cols.GROUP, fig_width=fig_dims.MD7, frame=year)
    fig_bar_state_vw_color_by_group = bar_plots.build_vw_by_state_bar(
        data_obj, groupings_input, max_small, fig_width=fig_dims.MD5, frame=year, base_fig_title=title_bar_color_by_group, show_era=False)
    fig_bar_actual_vs_adj_ec = bar_plots.build_actual_vs_adjusted_ec_votes_bar(
        data_obj, groupings_input, max_small, frame=year, show_era=False)
    fig_bar_actual_vs_adj_vw = bar_plots.build_actual_vs_adjusted_pop_vote_bar(
        data_obj, groupings_input, max_small, frame=year, show_era=False)
    return (fig_map_color_by_state_vw, fig_bar_state_vw_color_by_vw, fig_map_color_by_group, fig_bar_state_vw_color_by_group, 
            fig_bar_actual_vs_adj_ec, fig_bar_actual_vs_adj_vw)

# voter-weight-figure-vault callbacks, tab 2
@app.callback(
    Output('fig-scatter-dots-vw-state', 'figure'),
    Output('fig-scatter-bubbles-vw-state', 'figure'),
    Output('fig-scatter-abbrevs-vw-state', 'figure'),
    Output('fig-box-vw-group', 'figure'),  
    Output('fig-scatter-dots-vw-group', 'figure'),  
    Output('fig-scatter-bubbles-vw-group', 'figure'),
    Input('year-input', 'value'),
    Input('groupings-input', 'value'),
    Input('max-small-input', 'value'))
def display_voter_weight_figure_vault_tab2(year_input, groupings_input, max_small_input):
    # process input
    year = int(year_input)
    max_small = int(max_small_input)
    # title overrides
    title_scatter_state_dots = f'State Voter Weight Ratios: Popular Vote x EC Votes'
    title_scatter_state_bubbles = f'State Voter Weight x EC Votes, Scaled to Pop Vote'
    title_scatter_group_dots = f'Aggregate Voter Weight Ratios: Popular Vote x EC Votes'
    title_scatter_group_bubbles = f'Aggregate Voter Weight x EC Votes, Scaled to Pop Vote'
    # generate figs
    fig_scatter_dots_vw_state = scatter_plots.build_vw_by_state_scatter_dots(
        data_obj, groupings_input, max_small, frame=year, base_fig_title=title_scatter_state_dots, show_era=False)
    fig_scatter_bubbles_vw_state = scatter_plots.build_vw_by_state_scatter_bubbles(
        data_obj, groupings_input, max_small, frame=year, base_fig_title=title_scatter_state_bubbles, show_era=False)
    fig_scatter_abbrevs_vw_state = scatter_plots.build_vw_by_state_scatter_dots(
        data_obj, groupings_input, max_small, display_elements='abbrevs', frame=year, base_fig_title=title_scatter_state_dots, show_era=False)
    fig_box_vw_group = box_plots.build_vw_by_state_group_box_plot(data_obj, groupings_input, max_small, frame=year, show_era=False)
    fig_scatter_dots_vw_group = scatter_plots.build_vw_by_state_group_scatter_dots(
        data_obj, groupings_input, max_small, frame=year, base_fig_title=title_scatter_group_dots, show_era=False)
    fig_scatter_bubbles_vw_group = scatter_plots.build_vw_by_state_group_scatter_bubbles(
        data_obj, groupings_input, max_small, frame=year, base_fig_title=title_scatter_group_bubbles, show_era=False)
    return (fig_scatter_dots_vw_state, fig_scatter_bubbles_vw_state, fig_scatter_abbrevs_vw_state, fig_box_vw_group, 
            fig_scatter_dots_vw_group, fig_scatter_bubbles_vw_group)


############ electoral-college-intro callbacks, swallowed vote sampler tab 1
@app.callback(
    Output('fig-bar-state-vw-color-by-ecv', 'figure'),
    Output('fig-bar-swallowed-vote-sampler-1', 'figure'),
    Input('year-input', 'value'))
def display_electoral_collge_intro(year_input):
    # process input
    year = int(year_input)
    # generate figs
    fig_bar_state_vw_color_by_ecv = bar_plots.build_vw_by_state_bar(data_obj, ddirs.CENSUS, 0, frame=year, color_col=cols.LOG_EC_VOTES)
    fig_bar_svs_1 = bar_plots.build_swallowed_vote_bar(data_obj, 'raw')
    return fig_bar_state_vw_color_by_ecv, fig_bar_svs_1

# electoral-college-intro callbacks, swallowed vote sampler tab 2
@app.callback(
    Output('fig-bar-swallowed-vote-sampler-2', 'figure'),
    Input('year-input', 'value'))
def display_electoral_collge_intro_tab2(year_input):
    suppress_callback_exceptions = True
    fig = bar_plots.build_swallowed_vote_bar(data_obj, 'muted')
    return fig

# electoral-college-intro callbacks, swallowed vote sampler tab 3
@app.callback(
    Output('fig-bar-swallowed-vote-sampler-3', 'figure'),
    Input('year-input', 'value'))
def display_electoral_collge_intro_tab3(year_input):
    suppress_callback_exceptions = True
    fig = bar_plots.build_swallowed_vote_relative_bar(data_obj)
    return fig

# electoral-college-intro callbacks, swallowed vote sampler tab 4
@app.callback(
    Output('fig-bar-swallowed-vote-sampler-4', 'figure'),
    Input('year-input', 'value'))
def display_electoral_collge_intro_tab4(year_input):
    suppress_callback_exceptions = True
    fig = bar_plots.build_swallowed_vote_ec_bar(data_obj)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
    