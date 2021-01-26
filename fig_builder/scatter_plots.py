import plotly.express as px
import plotly.graph_objects as go

from data_processor.functions import apply_animation_settings, get_era_for_year, map_to_subdir
from metadata import Columns, FigDimensions, GROUPS_FOR_DIR, GROUP_COLORS, YEAR_0, YEAR_N


cols = Columns()
fig_dims = FigDimensions()


def build_ivw_by_state_scatter_dots(data_obj, groups_dir, max_small, display_elements=None, fig_width=None, frame=None,
                                    alt_groups=[], base_fig_title=None, show_era=True):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    pivot_on_year_df = data_obj.state_vote_weights_pivot_dfs[subdir].copy()
    groups = GROUPS_FOR_DIR[groups_dir].copy()

    if not display_elements:
        display_elements = 'dots'

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

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.crt(fig_width)

    if not base_fig_title:
        base_fig_title = 'Voter Weight Per State'

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] == frame].sort_values(cols.GROUP, ascending=True)

    # while I would prefer the NaNs to declare themselves as such, they don't render nicely as customdata params in hovertemplates
    pivot_on_year_df.fillna(-1, inplace=True)

    # display metadata common to (or that doesn't interfere with) all display types
    y_axis_title = 'Electoral College Votes Per State'
    # custom_data enables dynamic variable substitution in hovertemplates for static frames
    custom_data = [cols.STATE, cols.VOTES_COUNTED, cols.VOTE_WEIGHT, cols.POP_PER_EC, cols.VOTES_COUNTED_NORM, cols.EC_VOTES_NORM]
    # hover_data is the fallback plan for animations where custom_data doesn't work
    # hack to work around lack of control in animation hover_data: copy EC_VOTES_NORM to new field, hide EC_VOTES_NORM, and add copy in desired sequence
    col_ec_votes_norm_copy = 'EC votes, normalized'
    pivot_on_year_df[col_ec_votes_norm_copy] = pivot_on_year_df[cols.EC_VOTES_NORM]
    hover_data = {cols.EC_VOTES_NORM: False, cols.ABBREV: False, cols.VOTES_COUNTED: True, cols.VOTE_WEIGHT: True, 
                cols.POP_PER_EC: True, col_ec_votes_norm_copy: True, cols.VOTES_COUNTED_NORM: True}

    # calculate axis range boundaries 
    ec_max = round(pivot_on_year_df[cols.EC_VOTES].max() * 1.05)

    # set fields and values that differ for static years (frame) vs animations (!frame)
    if frame:
        # for static years, x axis is popular vote counted
        x_axis_col = cols.VOTES_COUNTED
        x_axis_title = 'Popular Vote Per State'
        x_max = round(pivot_on_year_df[cols.VOTES_COUNTED].max() * 1.05)
        # for static years, x_mean_line_max is max EC * population per EC vote 
        totals_by_year_df = data_obj.totals_by_year_df.copy()
        pop_per_ec = totals_by_year_df[totals_by_year_df[cols.YEAR] == frame][cols.POP_PER_EC].item()
        x_mean_line_max = ec_max * pop_per_ec
        # for static years, title is based on frame and show_era
        fig_title = f'{base_fig_title}: {frame}'
        if show_era:
            era = get_era_for_year(frame)
            fig_title = f'{fig_title} ({era})'
        
    else:
        # for animations, x axis is EC votes normalized - this keeps amplitude of 'reference mean' trace constant
        x_axis_col = cols.EC_VOTES_NORM
        x_axis_title = 'State EC Votes if Adjusted for Popular Vote' 
        x_max = round(pivot_on_year_df[cols.EC_VOTES_NORM].max())
        # for animations, x_mean_line_max is same max EC Votes
        x_mean_line_max = ec_max
        # for animations, set base title (it will change during animation)
        fig_title = f'{base_fig_title}: {YEAR_0} - {YEAR_N}'
              
    # slight rendering variations for dots vs abbrevs 
    if display_elements == 'dots':
        # init figure with core properties
        fig = px.scatter(pivot_on_year_df, x=x_axis_col, y=cols.EC_VOTES, color=cols.GROUP, 
                        title=fig_title, custom_data=custom_data, 
                        hover_name=cols.STATE, hover_data=hover_data, animation_frame=cols.YEAR, # ignored if df is for single year
                        color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                        width=fig_width, height=fig_height, opacity=0.7, 
                        range_x=[0,x_max], range_y=[0,ec_max])
        # axis metadata
        fig.update_xaxes(title_text=x_axis_title)
        fig.update_yaxes(title_text=y_axis_title)

    elif display_elements == 'abbrevs':
        # for animations where x axis keys off of EC votes, x axis range is constant, otherwise allow it to be set automagically 
        range_x = None
        if not frame:
            range_x = [.4,x_max]
        # init figure with core properties
        fig = px.scatter(pivot_on_year_df, x=x_axis_col, y=cols.EC_VOTES, color=cols.GROUP,  
                        title=fig_title, custom_data=custom_data, text=cols.ABBREV, 
                        hover_name=cols.STATE, hover_data=hover_data, animation_frame=cols.YEAR, # ignored if df is for single year
                        color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                        width=fig_width, height=fig_height, opacity=0.7, 
                        log_x=True, log_y=True, range_x=range_x, range_y=[2.5,ec_max])
        # axis metadata
        fig.update_xaxes(title_text=f"{x_axis_title} (log)")
        fig.update_yaxes(title_text=f"{y_axis_title} (log)")
        # tick overrides for y and x axes (animation only for x axis) representing EC votes, whose ranges are constant over time
        fig.update_layout(
            dict(yaxis=dict(tickmode='array', tickvals=[3,4,5,6,7,8,9,10,12,15,20,25,30,40,50])))
        if not frame:
            fig.update_layout(
                dict(xaxis=dict(tickmode='array', tickvals=[.5,.75,1,1.5,2,3,4,5,6,7,8,10,12,15,20,25,30,40,50,60])))
    
    # reference mean / quazi-linear regression line
    fig.add_trace(go.Scatter(x=[0,x_mean_line_max], y=[0,ec_max], mode='lines', name='Nationwide mean', 
                            line=dict(color='black', width=1)))

    # scatterplot dot formatting
    fig.update_traces(marker=dict(size=24, line=dict(width=1, color='white')), selector=dict(mode='markers'))

    # center title
    fig.update_layout(title_x=0.5)

    if not frame:
        apply_animation_settings(fig, base_fig_title)

    # hovertemplate formatting and variable substitution using customdata
    # since x axis is different for dots vs abbrevs, don't use x and instead explicitly rely on columns (redundantly) set in customdata
    # note hovertemplates only work on first frame of animations, but may as well include them in animations for that one frame
    fig.update_traces(
        hovertemplate = "<br>".join([
            "<b>%{customdata[0]}</b><br>",
            "Electoral College Votes: <b>%{y}</b>",
            "Popular Vote: <b>%{customdata[1]:,}</b>",
            "Voter Weight: <b>%{customdata[2]}</b>",
            "Popular Vote Per Elector: <b>%{customdata[3]:,}</b>",
            "<br><b>Normalized to Nat'l Average:</b>",
            "%{customdata[1]:,} Pop Votes => %{customdata[5]:.2f} EC Votes",
            "%{y} EC Votes => %{customdata[4]:,} Pop Votes",
        ])
    )

    return fig


def build_ivw_by_state_group_scatter_dots(data_obj, groups_dir, max_small, fig_width=None, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    group_aggs_by_year_df = data_obj.group_agg_weights_pivot_dfs[subdir].copy()
    groups = GROUPS_FOR_DIR[groups_dir].copy()

    # if frame is set, extract single-year data
    if frame:
        group_aggs_by_year_df = group_aggs_by_year_df[group_aggs_by_year_df[cols.YEAR] == frame]

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.crt(fig_width)

    # remove the Nat'l Average data
    group_aggs_by_year_df = group_aggs_by_year_df.loc[~(group_aggs_by_year_df[cols.GROUP] == "Nat'l Average")]

    # calculate axis range boundaries
    ec_max = round(group_aggs_by_year_df[cols.EC_VOTES].max() * 1.05)
    # pop_max = round(group_aggs_by_year_df[cols.VOTES_COUNTED].max() * 1.05)
    norm_max = round(group_aggs_by_year_df[cols.EC_VOTES_NORM].max() * 1.05)

    # display metadata common to (or that doesn't interfere with) all display types
    base_fig_title = 'Average Voter Weight Per State Group'
    y_axis_title = 'Electoral College Votes Per State Group'
    # custom_data enables dynamic variable substitution in hovertemplates for static frames
    custom_data = [cols.GROUP, cols.VOTES_COUNTED, cols.AVG_WEIGHT, cols.POP_PER_EC, cols.STATE_COUNT, cols.STATES_IN_GROUP, cols.VOTES_COUNTED_NORM, cols.EC_VOTES_NORM]
    # hover_data is the fallback plan for animations where custom_data doesn't work
    # hack to work around lack of control in animation hover_data: copy EC_VOTES_NORM to new field, hide EC_VOTES_NORM, and add copy in desired sequence
    col_ec_votes_norm_copy = 'EC votes, normalized'
    group_aggs_by_year_df[col_ec_votes_norm_copy] = group_aggs_by_year_df[cols.EC_VOTES_NORM]
    hover_data = {cols.EC_VOTES_NORM: False, cols.GROUP: False, cols.VOTES_COUNTED: True, cols.AVG_WEIGHT: True, cols.POP_PER_EC: True, 
                col_ec_votes_norm_copy: True, cols.VOTES_COUNTED_NORM: True, cols.STATES_IN_GROUP: True}

    # set fields and values that differ for static years (frame) vs animations (!frame)
    if frame:
        # for static years, x axis is popular vote counted
        x_axis_col = cols.VOTES_COUNTED
        x_axis_title = 'Aggregate Popular Vote Per State Group'
        x_max = round(group_aggs_by_year_df[cols.VOTES_COUNTED].max() * 1.05)
        # for static years, x_mean_line_max is max EC * population per EC vote 
        totals_by_year_df = data_obj.totals_by_year_df.copy()
        pop_per_ec = totals_by_year_df[totals_by_year_df[cols.YEAR] == frame][cols.POP_PER_EC].item()
        x_mean_line_max = ec_max * pop_per_ec
        # for static years, set specific era title
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
        
    else:
        # for animations, x axis is EC votes normalized - this keeps amplitude of 'reference mean' trace constant
        x_axis_col = cols.EC_VOTES_NORM
        x_axis_title = 'EC Votes if Adjusted for Popular Vote' 
        x_max = round(group_aggs_by_year_df[cols.EC_VOTES_NORM].max())
        # for animations, x_mean_line_max is max EC Votes
        x_mean_line_max = ec_max
        # for animations, set base title (it will change during animation)
        fig_title = f'{base_fig_title}: {YEAR_0} - {YEAR_N}'

    # init figure with core properties
    fig = px.scatter(group_aggs_by_year_df, x=x_axis_col, y=cols.EC_VOTES, color=cols.GROUP, 
                    title=fig_title, custom_data=custom_data, 
                    hover_name=cols.GROUP, hover_data=hover_data, animation_frame=cols.YEAR, animation_group=cols.GROUP, # ignored if df is for single year
                    color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                    width=fig_width, height=fig_height, opacity=0.7, 
                    range_x=[0,x_max], range_y=[0,ec_max])
        
    # scatterplot dot formatting
    fig.update_traces(marker=dict(size=24, line=dict(width=1, color='white')), selector=dict(mode='markers'))

    # reference mean / quazi-linear regression line
    fig.add_trace(go.Scatter(x=[0,x_mean_line_max], y=[0,ec_max], mode='lines', name='Nationwide mean', 
                            line=dict(color='black', width=1)))

    # axis metadata
    fig.update_xaxes(title_text=x_axis_title)
    fig.update_yaxes(title_text=y_axis_title)

    # center title
    fig.update_layout(title_x=0.5)

    # for animations, manually lay out a constant x axis and apply animation settings
    if not frame:
        num_xticks = round(norm_max / 50) + 1
        fig.update_layout(dict(xaxis=dict(tickmode='array', tickvals=[t*50 for t in range(num_xticks)])))
        apply_animation_settings(fig, base_fig_title)

    # hovertemplate formatting and variable substitution using customdata
    # since x axis is different for dots vs abbrevs, don't use x and instead explicitly rely on columns (redundantly) set in customdata
    # note hovertemplates only work on first frame of animations, but may as well include them in animations for that one frame
    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>%{customdata[0]}</b>",
            "%{customdata[4]} States: %{customdata[5]}<br>",
            "Aggregate EC Votes: <b>%{y}</b>",
            "Aggregate Popular Vote: <b>%{customdata[1]:,}</b>",
            "Average Voter Weight: <b>%{customdata[2]:.2f}</b>",
            "Average Pop Vote Per Elector: <b>%{customdata[3]:,}</b>",
            "<br><b>Normalized to Nat'l Average:</b>",
            "%{customdata[1]:,} Pop Votes => %{customdata[7]} EC Votes",
            "%{y} EC Votes => %{customdata[6]:,} Pop Votes",
        ])
    )

    return fig


def build_ivw_by_state_scatter_bubbles(data_obj, groups_dir, max_small, fig_width=None, frame=None,
                                    alt_groups=[], base_fig_title=None, show_era=True):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    pivot_on_year_df = data_obj.state_vote_weights_pivot_dfs[subdir].copy()
    groups = GROUPS_FOR_DIR[groups_dir].copy()

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] == frame]
    else:
        # lop off pre-Jacksonian years, early data distorts bubble size of later data
        YEAR_0 = 1828
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] >= YEAR_0]

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.crt(fig_width)

    if not base_fig_title:
        base_fig_title = 'Voter Weight Per State'

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

    # calculate axis range boundaries 
    ec_max = round(pivot_on_year_df[cols.EC_VOTES].max())
    weight_min = pivot_on_year_df[pivot_on_year_df[cols.VOTE_WEIGHT] > 0][cols.VOTE_WEIGHT].min() * 0.9
    weight_max = pivot_on_year_df[cols.VOTE_WEIGHT].max()

    # display metadata common to (or that doesn't interfere with) all display types
    x_axis_title = 'Electoral College Votes per State'
    y_axis_title = 'Voter Weight Per State (log)'
    # custom_data enables dynamic variable substitution in hovertemplates for static frames
    custom_data = [cols.STATE, cols.VOTES_COUNTED, cols.POP_PER_EC, cols.VOTES_COUNTED_PCT, cols.EC_VOTES_NORM, cols.VOTES_COUNTED_NORM]
    # hover_data is the fallback plan for animations where custom_data doesn't work
    # hack to work around lack of control in animation hover_data: copy EC_VOTES_NORM to new field, hide EC_VOTES_NORM, and add copy in desired sequence
    col_votes_counted_pct_copy = "Pop vote as % of nat'l vote"
    pivot_on_year_df[col_votes_counted_pct_copy] = pivot_on_year_df[cols.VOTES_COUNTED_PCT]
    hover_data = {cols.VOTES_COUNTED_PCT: False, cols.VOTES_COUNTED: True, cols.POP_PER_EC: True, 
                col_votes_counted_pct_copy: True, cols.EC_VOTES_NORM: True, cols.VOTES_COUNTED_NORM: True}
    
    # set fields and values that differ for static years (frame) vs animations (!frame)
    if frame:
        fig_title = f'{base_fig_title}: {frame}'
        if show_era:
            era = get_era_for_year(frame)
            fig_title = f'{fig_title} ({era})'
    else:
        fig_title = f'{base_fig_title}: {YEAR_0} - {YEAR_N}'

    # init figure with core properties
    fig = px.scatter(pivot_on_year_df, x=cols.EC_VOTES, y=cols.VOTE_WEIGHT, color=cols.GROUP,  
                    title=fig_title, custom_data=custom_data, size=cols.VOTES_COUNTED_PCT, size_max=80, 
                    hover_name=cols.STATE, hover_data=hover_data, animation_frame=cols.YEAR, # ignored if df is for single year
                    color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                    width=fig_width, height=fig_height, opacity=0.5, 
                    log_y=True, range_x=[0,ec_max], range_y=[weight_min,weight_max])

    # scatterplot dot formatting
    fig.update_traces(marker=dict(line=dict(width=1, color='white')), selector=dict(mode='markers'))

    # reference mean / quazi-linear regression line
    fig.add_trace(go.Scatter(x=[0,ec_max], y=[1,1], mode='lines', name='Nationwide mean', 
                            line=dict(color='black', width=1)))

    # axis metadata
    fig.update_xaxes(title_text=x_axis_title)
    fig.update_yaxes(title_text=y_axis_title)
    # axis tick overrides
    fig.update_layout(dict(yaxis=dict(tickmode='array', tickvals=[0.4,0.5,.6,.8,1,1.5,2,3,5,8])))

    # center title
    fig.update_layout(title_x=0.5)

    # apply animation settings
    if not frame:
        apply_animation_settings(fig, base_fig_title)

    # hovertemplate formatting and variable substitution using customdata
    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>%{customdata[0]}</b><br>",
            "Electoral College Votes: <b>%{x}</b>",
            "Popular Vote: <b>%{customdata[1]:,}</b>",
            "Voter Weight: <b>%{y:.2f}</b>",
            "Popular Vote Per Elector: <b>%{customdata[2]:,}</b>",
            "Pop Vote as % of Nat'l Vote: <b>%{customdata[3]:.2f}%</b>",
            "<br><b>Normalized to Nat'l Average:</b>",
            "%{customdata[1]:,} Pop Votes => %{customdata[4]:.2f} EC Votes",
            "%{x} EC Votes => %{customdata[5]:,} Pop Votes",
        ])
    )

    return fig


def build_ivw_by_state_group_scatter_bubbles(data_obj, groups_dir, max_small, fig_width=None, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    group_aggs_by_year_df = data_obj.group_agg_weights_pivot_dfs[subdir].copy()
    groups = GROUPS_FOR_DIR[groups_dir].copy()

    # if frame is set, extract single-year data
    if frame:
        group_aggs_by_year_df = group_aggs_by_year_df[group_aggs_by_year_df[cols.YEAR] == frame]
    else:
        # lop off pre-Jacksonian years, early data distorts bubble size of later data
        YEAR_0 = 1828
        group_aggs_by_year_df = group_aggs_by_year_df[group_aggs_by_year_df[cols.YEAR] >= YEAR_0]

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.crt(fig_width)

    # remove the Nat'l Average data
    group_aggs_by_year_df = group_aggs_by_year_df.loc[~(group_aggs_by_year_df[cols.GROUP] == "Nat'l Average")]

    # calculate axis range boundaries
    ec_max = round(group_aggs_by_year_df[cols.EC_VOTES].max() * 1.1)
    weight_min = group_aggs_by_year_df[group_aggs_by_year_df[cols.AVG_WEIGHT] > 0][cols.AVG_WEIGHT].min() * 0.9
    weight_max = group_aggs_by_year_df[cols.AVG_WEIGHT].max() * 1.1

    # display metadata common to (or that doesn't interfere with) all display types
    base_fig_title = 'Average Voter Weight Per State Group'
    x_axis_title = 'Electoral College Votes Per State Group'
    y_axis_title = 'Voter Weight Per State Group (log)'
    # custom_data enables dynamic variable substitution in hovertemplates for static frames
    custom_data = [cols.GROUP, cols.VOTES_COUNTED, cols.POP_PER_EC, cols.VOTES_COUNTED_PCT, cols.STATE_COUNT, cols.STATES_IN_GROUP, 
                cols.EC_VOTES_NORM, cols.VOTES_COUNTED_NORM]
    # hover_data is the fallback plan for animations where custom_data doesn't work
    # hack to work around lack of control in animation hover_data: copy EC_VOTES_NORM to new field, hide EC_VOTES_NORM, and add copy in desired sequence
    col_votes_counted_pct_copy = "Pop vote as % of nat'l vote"
    col_avg_weight_copy = "Average vote weight"
    group_aggs_by_year_df[col_votes_counted_pct_copy] = group_aggs_by_year_df[cols.VOTES_COUNTED_PCT]
    group_aggs_by_year_df[col_avg_weight_copy] = group_aggs_by_year_df[cols.AVG_WEIGHT]
    hover_data = {cols.GROUP: False, cols.AVG_WEIGHT: False, cols.VOTES_COUNTED_PCT: False, cols.VOTES_COUNTED: True, col_avg_weight_copy: True, 
                cols.POP_PER_EC: True, col_votes_counted_pct_copy: True, cols.EC_VOTES_NORM: True, cols.VOTES_COUNTED_NORM: True, cols.STATES_IN_GROUP: True}

    # set fields and values that differ for static years (frame) vs animations (!frame)
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        fig_title = f'{base_fig_title}: {YEAR_0} - {YEAR_N}'

    # init figure with core properties
    fig = px.scatter(group_aggs_by_year_df, x=cols.EC_VOTES, y=cols.AVG_WEIGHT, color=cols.GROUP, 
                    title=fig_title, custom_data=custom_data, size=cols.VOTES_COUNTED_PCT, size_max=80,  
                    hover_name=cols.GROUP, hover_data=hover_data, animation_frame=cols.YEAR, animation_group=cols.GROUP, # ignored if df is for single year
                    color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                    width=fig_width, height=fig_height, opacity=0.5, 
                    log_y=True, range_x=[0, ec_max], range_y=[weight_min, weight_max])

    # scatterplot dot formatting
    fig.update_traces(marker=dict(line=dict(width=1, color='white')), selector=dict(mode='markers'))

    # reference mean / quazi-linear regression line
    fig.add_trace(go.Scatter(x=[0,ec_max], y=[1,1], mode='lines', name='Nationwide mean', 
                    line=dict(color='black', width=1)))

    # axis metadata
    fig.update_xaxes(title_text=x_axis_title)
    fig.update_yaxes(title_text=y_axis_title)

    # center title
    fig.update_layout(title_x=0.5)

    # apply animation settings
    if not frame:
        apply_animation_settings(fig, base_fig_title)

    # hovertemplate formatting and variable substitution using customdata
    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>%{customdata[0]}</b>",
            "%{customdata[4]} States: %{customdata[5]}<br>",
            "Aggregate EC Votes: <b>%{x}</b>",
            "Aggregate Popular Vote: <b>%{customdata[1]:,}</b>",
            "Average Voter Weight: <b>%{y:.2f}</b>",
            "Average Pop Vote Per Elector: <b>%{customdata[2]:,}</b>",
            "Pop Vote as % of Nat'l Vote: <b>%{customdata[3]:.2f}%</b>",
            "<br><b>Normalized to Nat'l Average:</b>",
            "%{customdata[1]:,} Pop Votes => %{customdata[6]:.2f} EC Votes",
            "%{x} EC Votes => %{customdata[7]:,} Pop Votes",
        ])
    )

    return fig
