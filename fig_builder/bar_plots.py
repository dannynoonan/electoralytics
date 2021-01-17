import math
import pandas as pd
import plotly.express as px

from data_processor.functions import apply_animation_settings, fill_out_state_year_matrix, flatten_state_color_map, get_era_for_year, map_to_subdir
from metadata import Columns, DataDirs, FigDimensions, GROUPS_FOR_DIR, GROUP_COLORS, PARTIES, PARTY_COLORS, YEAR_0, YEAR_N


cols = Columns()
ddirs = DataDirs()
fig_dims = FigDimensions()


def build_ivw_by_state_bar(data_obj, groups_dir, max_small, fig_width=None, frame=None, color_col=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    pivot_on_year_df = data_obj.state_vote_weights_pivot_dfs[subdir].copy()
    groups = GROUPS_FOR_DIR[groups_dir]

    if not color_col:
        color_col = cols.GROUP

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] == frame]

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.wide_door(fig_width)

    # remove placeholder group rows, clean up empty state row data  
    pivot_on_year_df = pivot_on_year_df[pd.notnull(pivot_on_year_df[cols.STATE])]
    # part of my battle to keep states with no popular vote on the chart, while excluding states that hadn't been admitted yet
    pivot_on_year_df.loc[pd.isnull(pivot_on_year_df[cols.VOTE_WEIGHT]), cols.VOTE_WEIGHT] = 0.000000000001  # causes problems if set to 0
    # animations need every state in every year to have a placeholder row
    if not frame:
        pivot_on_year_df = fill_out_state_year_matrix(pivot_on_year_df, data_obj.all_states_meta_df, groups_dir)

    # calculate axis range boundaries
    vw_min = pivot_on_year_df[cols.VOTE_WEIGHT].min()
    vw_max = pivot_on_year_df[cols.VOTE_WEIGHT].max()
    if vw_min < 0.2:
        # states with no popular vote have extremely low placeholder vote weights, this gets around those weights skewing the log x axis 
        temp_df = pivot_on_year_df[pivot_on_year_df[cols.VOTE_WEIGHT] > 0.2]
        vw_min = temp_df[cols.VOTE_WEIGHT].min()
    if frame:
        vw_min = vw_min * 0.85
        vw_max = vw_max * 1.15

    # display metadata
    base_fig_title = 'Voter Weight Per State'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        fig_title = f'{base_fig_title}: {YEAR_0} - {YEAR_N}'
    x_axis_title = 'Voter Weight (log)'
    # custom_data enables dynamic variable substitution in hovertemplates for static frames    
    custom_data = [cols.VOTES_COUNTED, cols.EC_VOTES, cols.POP_PER_EC, cols.VOTES_COUNTED_NORM, cols.EC_VOTES_NORM, cols.GROUP]
    # hover_data is the fallback plan for animations where custom_data doesn't work
    hover_data = {cols.ABBREV: False, cols.VOTE_WEIGHT: False, cols.LOG_VOTE_WEIGHT: False, cols.GROUP: True, cols.STATE: True, 
                    cols.YEAR: True, cols.VOTES_COUNTED: True, cols.EC_VOTES: True, cols.POP_PER_EC: True, cols.EC_VOTES_NORM: True, 
                    cols.VOTES_COUNTED_NORM: True}

    # init figure with core properties, set color scale or color category map based on color_col
    if color_col == cols.LOG_VOTE_WEIGHT:
        color_continuous_scale = px.colors.diverging.BrBG[::-1]
        color_continuous_midpoint = 0

        # init figure with core properties
        fig = px.bar(pivot_on_year_df, x=cols.VOTE_WEIGHT, y=cols.STATE, color=color_col, title=fig_title, 
                    custom_data=custom_data, hover_name=cols.VOTE_WEIGHT, hover_data=hover_data,
                    text=cols.VOTE_WEIGHT, animation_frame=cols.YEAR, # ignored if df is for single year
                    color_continuous_scale=color_continuous_scale, color_continuous_midpoint=color_continuous_midpoint,
                    # labels={cols.VOTE_WEIGHT: 'Relative Voter Weight'}, 
                    range_x=[vw_min,vw_max], log_x=True, width=fig_width, height=fig_height)

    elif color_col in [cols.GROUP, cols.PARTY]:
        if color_col == cols.PARTY:
            category_orders = {cols.PARTY: PARTIES}
            color_discrete_map = PARTY_COLORS
        elif color_col == cols.GROUP:
            if frame:
                category_orders = {cols.GROUP: groups}
                color_discrete_map = GROUP_COLORS
            else:
                # animations don't work against categorical groupings... unless every state is its own category
                all_states = data_obj.all_states_meta_df[cols.STATE].tolist()
                category_orders = {cols.STATE: all_states}
                color_discrete_map = flatten_state_color_map(data_obj.all_states_meta_df, groups_dir)
                color_col = cols.STATE

        # init figure with core properties
        fig = px.bar(pivot_on_year_df, x=cols.VOTE_WEIGHT, y=cols.STATE, color=color_col, title=fig_title, 
                    custom_data=custom_data, hover_name=cols.VOTE_WEIGHT, hover_data=hover_data,
                    text=cols.VOTE_WEIGHT, animation_frame=cols.YEAR, # ignored if df is for single year
                    color_discrete_map=color_discrete_map, category_orders=category_orders,
                    range_x=[vw_min,vw_max], log_x=True, width=fig_width, height=fig_height)

    # overlay info on top of bars
    if frame:
        # display x value alongside bar
        fig.update_traces(texttemplate='%{text:,}', textposition='outside')
    else:
        # display x value alongside bar
        fig.update_traces(texttemplate='%{y} (%{text:,})', textposition='inside')

    # axis metadata
    fig.update_xaxes(title_text=x_axis_title)
    fig.update_yaxes(title_text='')
    fig.update_layout(
        yaxis={'tickangle': 35, 'showticklabels': True, 'type': 'category', 'tickfont_size': 8},
        yaxis_categoryorder='total ascending')
    if color_col == cols.LOG_VOTE_WEIGHT:
        # calculate log values for weights so I can plot the familiar linear numbers on the color bar
        # TODO pretty sure this works around a plotly bug, also present in choropleth, open ticket or post to stackoverflow
        tick_text = ['0.5', '0.7', '1.0', '1.5', '2.5', '4', '6', '9']
        lin_ticks = [float(x) for x in tick_text]
        log_ticks = [math.log(t, 2) for t in lin_ticks]
        fig.update_layout(
            coloraxis_colorbar=dict(tickvals=log_ticks, ticktext=tick_text, title='IPV (log)'))

    # center title
    fig.update_layout(title_x=0.5, uniformtext_minsize=10)

    # apply animation settings
    if not frame:
        apply_animation_settings(fig, base_fig_title, frame_rate=1500)
        # hide unhelpful legend of alphabetized states from state group animations
        if color_col == cols.STATE:
            fig.update_layout(showlegend=False)

    # hovertemplate formatting and variable substitution using customdata
    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>%{x}</b> (%{y})<br>",
            "Popular Vote: <b>%{customdata[0]:,}</b>",
            "Electoral College Votes: <b>%{customdata[1]}</b>",
            "Popular Vote Per Elector: <b>%{customdata[2]:,}</b>",
            # "Group: %{customdata[5]}",
            "<br><b>Normalized to Nat'l Average:</b>",
            "%{customdata[0]:,} Pop Votes => %{customdata[4]:.2f} EC Votes",
            "%{customdata[1]} EC Votes => %{customdata[3]:,} Pop Votes",
        ])
    )

    return fig


# ref: https://towardsdatascience.com/how-to-create-a-grouped-bar-chart-with-plotly-express-in-python-e2b64ed4abd7
def build_actual_vs_adjusted_ec_bar(data_obj, groups_dir, max_small, fig_width=None, frame=None):
    # TODO does this need groups_dir and max_small or can it use defaults 100% of time?
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    melted_ec_votes_pivot_df = data_obj.melted_ec_votes_pivot_dfs[subdir].sort_values('EC Votes*', ascending=True)

    # if frame is set, extract single-year data
    if frame:
        melted_ec_votes_pivot_df = melted_ec_votes_pivot_df[melted_ec_votes_pivot_df[cols.YEAR] == frame]

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.square(fig_width)

    # remove placeholder group rows, clean up empty state row data
    melted_ec_votes_pivot_df = melted_ec_votes_pivot_df[pd.notnull(melted_ec_votes_pivot_df[cols.STATE])]
    melted_ec_votes_pivot_df.loc[pd.isnull(melted_ec_votes_pivot_df[cols.VOTE_WEIGHT]), cols.VOTE_WEIGHT] = 0.000000000001  # causes problems if set to 0

    # display metadata
    base_fig_title = "EC Votes: 'Actual' vs 'Adjusted for Turnout'" 
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        fig_title = f'{base_fig_title}: {YEAR_0} - {YEAR_N}'
    x_axis_title = 'Actual EC Votes / EC Votes if Adjusted for Popular Vote'
    # custom_data enables dynamic variable substitution in hovertemplates for static frames
    custom_data = [cols.YEAR, cols.EC_VOTES, cols.VOTES_COUNTED, cols.VOTE_WEIGHT, cols.POP_PER_EC, cols.VOTES_COUNTED_NORM, cols.EC_VOTES_NORM]
    # set color sequence
    color_discrete_sequence = ['DarkGreen', 'LimeGreen']

    # init figure with core properties
    fig = px.bar(melted_ec_votes_pivot_df, x='EC Votes*', y=cols.STATE, color='Actual vs Adjusted EC Votes*', title=fig_title, 
                custom_data=custom_data, barmode='group', animation_frame=cols.YEAR, # ignored if df is for single year
                color_discrete_sequence=color_discrete_sequence, width=fig_width, height=fig_height)

    # axis metadata
    fig.update_xaxes(title_text=x_axis_title)
    fig.update_yaxes(title_text='')
    fig.update_layout(
        yaxis={'tickangle': 35, 'showticklabels': True, 'type': 'category', 'tickfont_size': 8},
        yaxis_categoryorder='total descending')

    # center title
    fig.update_layout(title_x=0.5)

    # hovertemplate formatting and variable substitution using customdata
    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>%{x}</b>*<br>",
            "<b>%{y}</b> (%{customdata[0]}):",
            "Popular Vote: <b>%{customdata[2]:,}</b>",
            "Voter Weight: <b>%{customdata[3]:.2f}</b>",
            "Popular Vote Per Elector: <b>%{customdata[4]:,}</b>",
            "<br><b>Normalized to Nat'l Average:</b>",
            "%{customdata[2]:,} Pop Votes => %{customdata[6]:.2f} EC Votes",
            "%{customdata[1]} EC Votes => %{customdata[5]:,} Pop Votes",
        ])
    )

    return fig


def build_actual_vs_adjusted_vw_bar(data_obj, groups_dir, max_small, fig_width=None, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    melted_vote_count_pivot_df = data_obj.melted_vote_count_pivot_dfs[subdir].sort_values('Popular Vote*', ascending=True)

    # if frame is set, extract single-year data
    if frame:
        melted_vote_count_pivot_df = melted_vote_count_pivot_df[melted_vote_count_pivot_df[cols.YEAR] == frame]

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.square(fig_width)

    # remove placeholder group rows, clean up empty state row data
    melted_vote_count_pivot_df = melted_vote_count_pivot_df[pd.notnull(melted_vote_count_pivot_df[cols.STATE])]
    melted_vote_count_pivot_df.loc[pd.isnull(melted_vote_count_pivot_df['Popular Vote*']), 'Popular Vote*'] = 0.000000000001  # causes problems if set to 0

    # display metadata
    base_fig_title = "Popular Vote: 'Actual' vs 'Adjusted for Voter Weight'"
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        fig_title = f'{base_fig_title}: {YEAR_0} - {YEAR_N}'
    x_axis_title = 'Actual Pop Vote / Pop Vote if Adjusted for Voter Weight'
    # custom_data enables dynamic variable substitution in hovertemplates for static frames
    custom_data = [cols.YEAR, cols.EC_VOTES, cols.VOTES_COUNTED, cols.VOTE_WEIGHT, cols.POP_PER_EC, cols.VOTES_COUNTED_NORM, cols.EC_VOTES_NORM]
    color_discrete_sequence = ['DarkBlue', 'DodgerBlue']
    
    # init figure with core properties
    fig = px.bar(melted_vote_count_pivot_df, x='Popular Vote*', y=cols.STATE, color='Actual vs Adjusted Popular Vote*', title=fig_title, 
                custom_data=custom_data, barmode='group', animation_frame=cols.YEAR, # ignored if df is for single year
                color_discrete_sequence=color_discrete_sequence, width=fig_width, height=fig_height)

    # axis metadata
    fig.update_xaxes(title_text=x_axis_title)
    fig.update_yaxes(title_text='')
    fig.update_layout(
        yaxis={'tickangle': 35, 'showticklabels': True, 'type': 'category', 'tickfont_size': 8},
        yaxis_categoryorder='total descending')

    # center title
    fig.update_layout(title_x=0.5)

    # hovertemplate formatting and variable substitution using customdata
    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>%{x:,}</b>*<br>",
            "<b>%{y}</b> (%{customdata[0]}):",
            "Popular Vote: <b>%{customdata[2]:,}</b>",
            "Voter Weight: <b>%{customdata[3]:.2f}</b>",
            "Popular Vote Per Elector: <b>%{customdata[4]:,}</b>",
            "<br><b>Normalized to Nat'l Average:</b>",
            "%{customdata[2]:,} Pop Votes => %{customdata[6]:.2f} EC Votes",
            "%{customdata[1]} EC Votes => %{customdata[5]:,} Pop Votes",
        ])
    )

    return fig


def build_swallowed_vote_bar(data_obj, view, fig_width=None):
    # bar and legend metadata depend on view input
    if view == 'raw':
        color_col = 'Candidate: Pop Vote'
        category_orders = {'Candidate: Pop Vote': ['Biden', 'Trump']}
        color_discrete_sequence = ['Blue', 'Red']

    elif view == 'muted':
        color_col = 'Candidate: Outcome'
        category_orders = {'Candidate: Outcome': ['Biden: Win', 'Trump: Win', 'Biden: Loss', 'Trump: Loss']}
        color_discrete_sequence = ['Blue', 'Red', 'Gray', 'Gray']

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.crt(fig_width)

    # display metadata
    base_fig_title = 'Winners & Losers Under Winner-Take-All Electoral College System in 2020'
    # custom_data enables dynamic variable substitution in hovertemplates for static frames
    custom_data = ['State', 'Popular Vote', 'EC Votes for Candidate']

    # init figure with core properties
    fig = px.bar(data_obj.swallowed_vote_df, x='Popular Vote', y='State: Candidate', 
                color=color_col, title=base_fig_title, custom_data=custom_data, text='Popular Vote',
                category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
                width=fig_width, height=fig_height)

    # display x value alongside bar
    fig.update_traces(texttemplate='%{text:,}', textposition='auto')

    # axis metadata 
    fig.update_xaxes(range=[0,10000000])
    fig.update_yaxes(title_text='')
    fig.update_layout(yaxis_categoryorder='total ascending')

    # center title
    fig.update_layout(title_x=0.5)

    # hovertemplate formatting and variable substitution using customdata
    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>%{y}</b><br>",
            "Popular vote for candidate: <b>%{customdata[1]:,}</b>",
            "Electoral College votes for candidate: <b>%{customdata[2]}</b>",
        ])
    )

    return fig


def build_swallowed_vote_relative_bar(data_obj, fig_width=None):
    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.crt(fig_width)

    # display metadata
    base_fig_title = 'Winners & Losers Under Winner-Take-All Electoral College System in 2020'
    # custom_data enables dynamic variable substitution in hovertemplates for static frames
    custom_data = ['Candidate: Pop Vote', 'Popular Vote', 'EC Votes for Candidate']
    # bar and legend metadata
    category_orders = {'Candidate: Outcome': ['Biden: Win', 'Trump: Win', 'Biden: Loss', 'Trump: Loss']}
    color_discrete_sequence = ['Blue', 'Red', 'Gray', 'Gray']

    # init figure with core properties
    fig = px.bar(data_obj.swallowed_vote_df, x='Popular Vote', y='State', color='Candidate: Outcome', 
                title=base_fig_title, custom_data=custom_data, text='Popular Vote', barmode='relative', 
                category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
                width=fig_width, height=fig_height)

    # display x value alongside bar
    fig.update_traces(texttemplate='%{text:,}', textposition='auto')

    # axis metadata 
    fig.update_yaxes(title_text='')
    fig.update_xaxes(range=[0,18000000])
    fig.update_layout(yaxis_categoryorder='total ascending')

    # center title
    fig.update_layout(title_x=0.5)

    # hovertemplate formatting and variable substitution using customdata
    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>%{y} for %{customdata[0]}</b><br>",
            "Popular vote for candidate: <b>%{customdata[1]:,}</b>",
            "Electoral College votes for candidate: <b>%{customdata[2]}</b>",
        ])
    )

    return fig


def build_swallowed_vote_ec_bar(data_obj, fig_width=None):
    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.crt(fig_width)

    distilled_svs = data_obj.swallowed_vote_df.sort_values('EC Votes for Candidate', ascending=False)
    distilled_svs = distilled_svs[distilled_svs['EC Votes for Candidate'] != 0]
    
    # display metadata
    base_fig_title = 'Winners & Losers Under Winner-Take-All Electoral College System in 2020'
    x_axis_title = 'Electoral College Votes'
    # custom_data enables dynamic variable substitution in hovertemplates for static frames
    custom_data = ['Candidate: Pop Vote', 'Popular Vote']
    # bar and legend metadata
    category_orders = {'Candidate: Pop Vote': ['Biden', 'Trump']}
    color_discrete_sequence = ['Blue', 'Red']

    # init figure with core properties
    fig = px.bar(distilled_svs, x='EC Votes for Candidate', y='State', color='Candidate: Pop Vote', 
                title=base_fig_title, custom_data=custom_data, text='EC Votes for Candidate',
                category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
                width=fig_width, height=fig_height)

    # display x value alongside bar
    fig.update_traces(texttemplate='EC Votes: %{text:,}', textposition='auto')

    # axis metadata 
    fig.update_xaxes(title_text=x_axis_title)
    fig.update_yaxes(title_text='')
    fig.update_layout(yaxis_categoryorder='total ascending')

    # center title
    fig.update_layout(title_x=0.5)

    # hovertemplate formatting and variable substitution using customdata
    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>%{y} for %{customdata[0]}</b><br>",
            "Popular Vote for Candidate: <b>%{customdata[1]:,}</b>",
            "Electoral College Votes for Candidate: <b>%{x}</b>",
        ])
    )

    return fig
    