import math
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from data_processor.functions import apply_animation_settings, fill_out_state_year_matrix, flatten_state_color_map, get_era_for_year, map_to_subdir
from metadata import Columns, DataDirs, FigDimensions, GROUPS_FOR_DIR, GROUP_COLORS, PARTIES, PARTY_COLORS, YEAR_0, YEAR_N


cols = Columns()
ddirs = DataDirs()
fig_dims = FigDimensions()


def build_vw_by_state_bar(data_obj, groups_dir, max_small, fig_width=None, fig_height=None, frame=None, color_col=None, 
                            alt_groups=[], base_fig_title=None, show_era=True, show_year=True, groups_label=None, alt_data=None):
    """
    swiss army knife function for generating a px.bar plot, color-shading states by a category or along a data spectrum,
    in descending order by voter weight. supports static single-year plots or animations. 
    """
    subdir = map_to_subdir(groups_dir, max_small)
    groups = GROUPS_FOR_DIR[groups_dir].copy()

    # hackish hijack of custom census comparison logic 
    census_diff_hilites = False
    if alt_data and alt_data in 'census_diff_2020':
        data_obj.load_census_diff_2020()
        pivot_on_year_df = data_obj.census_diff_2020_df.copy()
        if frame in [2020.2, 2020.3]:
            census_diff_hilites = True
        if frame in [2020.1, 2020.2]:
            frame = '2020'
        if frame in [2020.3, 2020.4]:
            frame = '2020 retrofit'
    else:
        data_obj.load_dfs_for_subdir(subdir)
        pivot_on_year_df = data_obj.state_vote_weights_pivot_dfs[subdir].copy()

    if not color_col:
        color_col = cols.GROUP

    if not groups_label:
        groups_label = color_col
        if groups_label == 'Group':
            groups_label = 'State Grouping'

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] == frame]

    if alt_groups:
        if 'slave_free' in alt_groups:
            pivot_on_year_df.loc[pivot_on_year_df[cols.GROUP] == 'Union', cols.GROUP] = 'Free'
            pivot_on_year_df.loc[pivot_on_year_df[cols.GROUP] == 'Confederate', cols.GROUP] = 'Slave'
            pivot_on_year_df.loc[pivot_on_year_df[cols.GROUP] == 'Border', cols.GROUP] = 'Slave'
            groups = ['Free', 'Slave', 'Small']
        if 'split_small' in alt_groups:
            pivot_on_year_df.loc[pivot_on_year_df[cols.EC_VOTES] <= 5, cols.GROUP] = '4-5 ECV'
            pivot_on_year_df.loc[pivot_on_year_df[cols.EC_VOTES] == 3, cols.GROUP] = '3 ECV'
            groups.extend(['3 ECV', '4-5 ECV'])
        if 'ecv_only' in alt_groups:
            pivot_on_year_df.loc[pivot_on_year_df[cols.EC_VOTES] == 3, cols.GROUP] = '3 ECV'
            pivot_on_year_df.loc[pivot_on_year_df[cols.EC_VOTES] >= 4, cols.GROUP] = '4-5 ECV'
            pivot_on_year_df.loc[pivot_on_year_df[cols.EC_VOTES] >= 6, cols.GROUP] = '6-8 ECV'
            pivot_on_year_df.loc[pivot_on_year_df[cols.EC_VOTES] >= 9, cols.GROUP] = '9-13 ECV'
            pivot_on_year_df.loc[pivot_on_year_df[cols.EC_VOTES] >= 14, cols.GROUP] = '14-19 ECV'
            pivot_on_year_df.loc[pivot_on_year_df[cols.EC_VOTES] >= 20, cols.GROUP] = '20+ ECV'
            groups = ['3 ECV', '4-5 ECV', '6-8 ECV', '9-13 ECV', '14-19 ECV', '20+ ECV']
            groups_label = 'EC Votes (Size)'

    if not fig_width:
        fig_width = fig_dims.MD6
    if not fig_height:
        fig_height = fig_dims.wide_door(fig_width)

    if not base_fig_title:
        base_fig_title = 'Voter Weight Per State'

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
    if frame:
        fig_title = base_fig_title
        if show_year:
            fig_title = f'{fig_title} ({frame})'
        if show_era:
            era = get_era_for_year(frame)
            fig_title = f'{fig_title}<br>{era}'
    else:
        fig_title = f'{base_fig_title} ({YEAR_0} - {YEAR_N})'
    x_axis_title = 'Voter Weight (log scale)'
    # custom_data enables dynamic variable substitution in hovertemplates for static frames    
    custom_data = [cols.VOTES_COUNTED, cols.EC_VOTES, cols.POP_PER_EC, cols.VOTES_COUNTED_NORM, cols.EC_VOTES_NORM, cols.GROUP]
    # hover_data is the fallback plan for animations where custom_data doesn't work
    hover_data = {cols.ABBREV: False, cols.VOTE_WEIGHT: False, cols.LOG_VOTE_WEIGHT: False, cols.LOG_EC_VOTES: False, 
                    cols.GROUP: True, cols.STATE: True, cols.YEAR: True, cols.VOTES_COUNTED: True, cols.EC_VOTES: True, 
                    cols.POP_PER_EC: True, cols.EC_VOTES_NORM: True, cols.VOTES_COUNTED_NORM: True}

    # init figure with core properties, set color scale or color category map based on color_col
    if color_col in [cols.LOG_VOTE_WEIGHT, cols.LOG_EC_VOTES]:
        if color_col == cols.LOG_VOTE_WEIGHT:
            color_continuous_scale = px.colors.diverging.BrBG[::-1]
            color_continuous_midpoint = 0
        elif color_col == cols.LOG_EC_VOTES:
            color_continuous_scale = 'sunset_r'
            color_continuous_midpoint = None
            # not sure to put this, so far only using LOG_EC_VOTES variant for a one-off
            fig_title = f'Small-State Bias: Fewer Electoral College Votes -> High Voter Weight ({frame})'

        # init figure with core properties
        fig = px.bar(pivot_on_year_df, x=cols.VOTE_WEIGHT, y=cols.STATE, color=color_col, title=fig_title, 
                    custom_data=custom_data, hover_name=cols.VOTE_WEIGHT, hover_data=hover_data,
                    text=cols.EC_VOTES, animation_frame=cols.YEAR, # ignored if df is for single year
                    color_continuous_scale=color_continuous_scale, color_continuous_midpoint=color_continuous_midpoint,
                    labels={cols.GROUP: groups_label}, 
                    range_x=[vw_min,vw_max], log_x=True, height=fig_height)

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
                    text=cols.EC_VOTES, animation_frame=cols.YEAR, # ignored if df is for single year
                    color_discrete_map=color_discrete_map, category_orders=category_orders,
                    labels={cols.GROUP: groups_label},
                    range_x=[vw_min,vw_max], log_x=True, height=fig_height)

    elif color_col == cols.PARTY:
        category_orders = {cols.PARTY: PARTIES}
        color_discrete_map = PARTY_COLORS
        x_axis_title = 'Electoral College votes'

        # init figure with core properties
        fig = px.bar(pivot_on_year_df, x=cols.EC_VOTES, y=cols.STATE, color=color_col, title=fig_title, 
                    custom_data=custom_data, hover_name=cols.VOTE_WEIGHT, hover_data=hover_data,
                    text=cols.EC_VOTES, animation_frame=cols.YEAR, # ignored if df is for single year
                    color_discrete_map=color_discrete_map, category_orders=category_orders,
                    labels={cols.PARTY: groups_label}, height=fig_height)

    # overlay info on top of bars
    if frame:
        if color_col == cols.LOG_EC_VOTES:
            # superimpose EC votes on top of bar
            fig.update_traces(texttemplate='EC: %{text}', textposition='inside')
        else:
            # display vote weight alongside bar
            fig.update_traces(texttemplate='%{x:,}', textposition='outside')
    else:
        # superimpose state + vote weight on top of bar
        fig.update_traces(texttemplate='%{y} (%{x:,})', textposition='inside')

    # super hackish custom census data for border widths and colors 
    if alt_data and alt_data == 'census_diff_2020' and census_diff_hilites:
        if color_col == cols.LOG_VOTE_WEIGHT:
            fig.data[0].marker.line.width = [0, 0, 0, 0, 3, 3, 0, 0, 0, 3, 
                                            0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 
                                            0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 
                                            0, 0, 3, 3, 0, 3, 0, 3, 3, 0, 
                                            0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0]
            fig.data[0].marker.line.color = ['blue', 'blue', 'blue', 'blue', 'black', 'lime', 'blue', 'blue', 'blue', 'lime', 
                                            'blue', 'blue', 'blue', 'black', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 
                                            'blue', 'blue', 'black', 'blue', 'blue', 'blue', 'lime', 'blue', 'blue', 'blue', 
                                            'blue', 'blue', 'black', 'lime', 'blue', 'black', 'blue', 'lime', 'black', 'blue',  
                                            'blue', 'blue', 'blue', 'lime', 'blue', 'blue', 'blue', 'blue', 'black', 'blue', 'blue']
        elif color_col == cols.PARTY:
            fig.data[0].marker.line.width = [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 
                                            0, 0, 3, 0, 3, 0, 3, 0, 0, 0, 
                                            0, 3, 0, 3, 0]
            fig.data[1].marker.line.width = [0, 3, 3, 0, 0, 0, 0, 0, 3, 0,
                                            0, 0, 3, 0, 0, 0, 0, 0, 3, 3, 
                                            3, 0, 0, 0, 0, 0, 0]
            fig.data[0].marker.line.color = ['blue', 'blue', 'blue', 'lime', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue',  
                                            'blue', 'blue', 'lime', 'blue', 'lime', 'blue', 'black', 'blue', 'blue', 'blue', 
                                            'blue', 'lime', 'blue', 'black', 'blue']
            fig.data[1].marker.line.color = ['blue', 'black', 'lime', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'blue', 
                                            'blue', 'blue', 'black', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'lime', 
                                            'black', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']


    # axis metadata
    fig.update_xaxes(title_text=x_axis_title)
    fig.update_yaxes(title_text='')
    fig.update_layout(
        yaxis={'tickangle': 35, 'showticklabels': True, 'type': 'category', 'tickfont_size': 8},
        yaxis_categoryorder='total ascending')
    # calculate log values to plot on the color bar
    # TODO pretty sure this works around a plotly bug, also present in choropleth, open ticket or post to stackoverflow
    if color_col == cols.LOG_VOTE_WEIGHT:
        tick_text = ['0.5', '0.7', '1.0', '1.5', '2.5', '4', '6', '9']
        lin_ticks = [float(x) for x in tick_text]
        log_ticks = [math.log(t, 2) for t in lin_ticks]
        fig.update_layout(
            coloraxis_colorbar=dict(tickvals=log_ticks, ticktext=tick_text, title='Voter<br>Weight'))
    elif color_col == cols.LOG_EC_VOTES:
        tick_text = ['3', '5', '10', '20', '50']
        lin_ticks = [float(x) for x in tick_text]
        log_ticks = [math.log(t, 10) for t in lin_ticks]
        fig.update_layout(
            coloraxis_colorbar=dict(tickvals=log_ticks, ticktext=tick_text, title='EC votes (log)'))

    # display formatting
    fig.update_layout(title_x=0.5, uniformtext_minsize=10)
    fig.update_layout(margin=go.layout.Margin(l=0))

    # apply animation settings
    if not frame:
        apply_animation_settings(fig, base_fig_title, frame_rate=1500)
        # hide unhelpful legend of alphabetized states from state group animations
        if color_col == cols.STATE:
            fig.update_layout(showlegend=False)

    # hovertemplate formatting and variable substitution using customdata
    fig.update_traces(
        hovertemplate="<br>".join([
            "Voter Weight: <b>%{x}</b> (%{y})</b><br>",
            "Popular Vote (Turnout): <b>%{customdata[0]:,}</b>",
            "Electoral College Votes: <b>%{customdata[1]}</b>",
            "Popular Vote Per Elector: <b>%{customdata[2]:,}</b>",
            # "Group: %{customdata[5]}",
            "<br><b>Normalized to Nat'l Average:</b>",
            "%{customdata[0]:,} Pop Votes → %{customdata[4]:.2f} EC Votes",
            "%{customdata[1]} EC Votes → %{customdata[3]:,} Pop Votes",
        ]),
    )

    return fig


# ref: https://towardsdatascience.com/how-to-create-a-grouped-bar-chart-with-plotly-express-in-python-e2b64ed4abd7
def build_actual_vs_adjusted_ec_votes_bar(data_obj, groups_dir, max_small, fig_width=None, frame=None, show_era=True):
    """
    generate a px.bar plot displaying actual ec votes data vs ec votes data adjusted for pop vote, side by side for each state 
    """
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
        fig_title = f'{base_fig_title} ({frame})'
        if show_era:
            era = get_era_for_year(frame)
            fig_title = f'{fig_title}<br>{era}'
    else:
        fig_title = f'{base_fig_title} ({YEAR_0} - {YEAR_N})'
    x_axis_title = 'Actual EC Votes / EC Votes if Adjusted for Voter Turnout'
    # custom_data enables dynamic variable substitution in hovertemplates for static frames
    custom_data = [cols.YEAR, cols.EC_VOTES, cols.VOTES_COUNTED, cols.VOTE_WEIGHT, cols.POP_PER_EC, cols.VOTES_COUNTED_NORM, cols.EC_VOTES_NORM]
    # set color sequence
    color_discrete_sequence = ['DarkGreen', 'LimeGreen']

    # init figure with core properties
    fig = px.bar(melted_ec_votes_pivot_df, x='EC Votes*', y=cols.STATE, color='Actual vs Adjusted EC Votes*', title=fig_title, 
                custom_data=custom_data, barmode='group', animation_frame=cols.YEAR, # ignored if df is for single year
                color_discrete_sequence=color_discrete_sequence, height=fig_height)

    # axis metadata
    fig.update_xaxes(title_text=x_axis_title)
    fig.update_yaxes(title_text='')
    fig.update_layout(
        yaxis={'tickangle': 35, 'showticklabels': True, 'type': 'category', 'tickfont_size': 8},
        yaxis_categoryorder='total descending')

    # display formatting
    fig.update_layout(title_x=0.5)
    fig.update_layout(margin=go.layout.Margin(l=0))

    # hovertemplate formatting and variable substitution using customdata
    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>%{x}</b>*<br>",
            "<b>%{y}</b> (%{customdata[0]}):",
            "Popular Vote (Turnout): <b>%{customdata[2]:,}</b>",
            "Popular Vote Per Elector: <b>%{customdata[4]:,}</b>",
            "Voter Weight: <b>%{customdata[3]:.2f}</b>",
            "<br><b>Normalized to Nat'l Average:</b>",
            "%{customdata[2]:,} Pop Votes → %{customdata[6]:.2f} EC Votes",
            "%{customdata[1]} EC Votes → %{customdata[5]:,} Pop Votes",
        ])
    )

    return fig


def build_actual_vs_adjusted_pop_vote_bar(data_obj, groups_dir, max_small, fig_width=None, frame=None, show_era=True):
    """
    generate a px.bar plot displaying actual pop vote data vs pop vote data adjusted for voter weight, side by side for each state 
    """
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
    base_fig_title = "Voter Turnout: 'Actual' vs 'Adjusted for Voter Weight'"
    if frame:
        fig_title = f'{base_fig_title} ({frame})'
        if show_era:
            era = get_era_for_year(frame)
            fig_title = f'{fig_title}<br>{era}'
    else:
        fig_title = f'{base_fig_title} ({YEAR_0} - {YEAR_N})'
    x_axis_title = 'Actual Pop Vote / Pop Vote if Adjusted for Voter Weight'
    # custom_data enables dynamic variable substitution in hovertemplates for static frames
    custom_data = [cols.YEAR, cols.EC_VOTES, cols.VOTES_COUNTED, cols.VOTE_WEIGHT, cols.POP_PER_EC, cols.VOTES_COUNTED_NORM, cols.EC_VOTES_NORM]
    color_discrete_sequence = ['DarkBlue', 'DodgerBlue']
    
    # init figure with core properties
    fig = px.bar(melted_vote_count_pivot_df, x='Popular Vote*', y=cols.STATE, color='Actual vs Adjusted Popular Vote*', title=fig_title, 
                custom_data=custom_data, barmode='group', animation_frame=cols.YEAR, # ignored if df is for single year
                color_discrete_sequence=color_discrete_sequence, height=fig_height)

    # axis metadata
    fig.update_xaxes(title_text=x_axis_title)
    fig.update_yaxes(title_text='')
    fig.update_layout(
        yaxis={'tickangle': 35, 'showticklabels': True, 'type': 'category', 'tickfont_size': 8},
        yaxis_categoryorder='total descending')

    # display formatting
    fig.update_layout(title_x=0.5)
    fig.update_layout(margin=go.layout.Margin(l=0))

    # hovertemplate formatting and variable substitution using customdata
    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>%{x:,}</b>*<br>",
            "<b>%{y}</b> (%{customdata[0]}):",
            "Popular Vote (Turnout): <b>%{customdata[2]:,}</b>",
            "Popular Vote Per Elector: <b>%{customdata[4]:,}</b>",
            "Voter Weight: <b>%{customdata[3]:.2f}</b>",
            "<br><b>Normalized to Nat'l Average:</b>",
            "%{customdata[2]:,} Pop Votes → %{customdata[6]:.2f} EC Votes",
            "%{customdata[1]} EC Votes → %{customdata[5]:,} Pop Votes",
        ])
    )

    return fig


def build_swallowed_vote_bar(data_obj, view, fig_width=None):
    """
    generate a px.bar tuned specifically to swallowed vote sampler data, for comparing vote counts side by side
    raw view shows colors each candidate's vote bars, muted view grays out the losing candidate's vote bars
    """
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
    """
    generate a px.bar tuned specifically to swallowed vote sampler data, for stacking both candidate's vote counts in relative barmode 
    """
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
    """
    generate a px.bar tuned specifically to swallowed vote sampler data, for showing winning candidate's ec votes 
    """
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
    