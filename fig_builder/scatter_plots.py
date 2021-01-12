import plotly.express as px
import plotly.graph_objects as go

from data_processor.functions import apply_animation_settings, get_era_for_year, map_to_subdir
from metadata import Columns, FigDimensions, GROUPS_FOR_DIR, GROUP_COLORS, YEAR_0, YEAR_N


cols = Columns()
fig_dims = FigDimensions()


def build_ivw_by_state_scatter_dots(data_obj, groups_dir, max_small, display_elements=None, fig_width=None, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    pivot_on_year_df = data_obj.state_vote_weights_pivot_dfs[subdir]
    groups = GROUPS_FOR_DIR[groups_dir]

    if not display_elements:
        display_elements = 'dots'

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] == frame].sort_values(cols.GROUP, ascending=True)

    # while I would prefer the NaNs to declare themselves as such, they don't render nicely as customdata params in hovertemplates
    pivot_on_year_df.fillna(-1, inplace=True)

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.crt(fig_width)
    
    # calculate axis range boundaries 
    ec_max = round(pivot_on_year_df[cols.EC_VOTES].max() * 1.05)
    # display metadata
    custom_data = [cols.STATE, cols.VOTES_COUNTED, cols.VOTE_WEIGHT, cols.POP_PER_EC, cols.VOTES_COUNTED_NORM]
    base_fig_title = 'Vote Weight Per Person Per State'
    y_axis_title = 'Electoral College Votes Per State'

    # set fields and values that differ for static years (frame) vs animations (!frame)
    if frame:
        # for static years, x axis is simply popular vote counted
        x_max = round(pivot_on_year_df[cols.VOTES_COUNTED].max() * 1.05)
        # for static years, calculate avg pop vote for ec max
        totals_by_year_df = data_obj.totals_by_year_df
        pop_per_ec = totals_by_year_df[totals_by_year_df[cols.YEAR] == frame][cols.POP_PER_EC].item()
        x_mean_line_max = ec_max * pop_per_ec
        # x axis details
        x_axis_col = cols.VOTES_COUNTED
        x_axis_title = 'Votes counted per state'
        # for static years, set specific era title
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
        
    else:
        # for animations, keep amplitude of 'reference mean' trace constant by pegging x axis max against EC Votes normalized
        x_max = round(pivot_on_year_df[cols.EC_VOTES_NORM].max() * 1.05)
        if display_elements == 'dots':
            # for dots (linear) animations, x_mean_line_max is same max EC Votes normalized
            x_mean_line_max = x_max
        else:
            # for abbrevs (log) animations, x_mean_line_max is same max EC Votes
            x_mean_line_max = ec_max
        # x axis details
        x_axis_col = cols.EC_VOTES_NORM
        x_axis_title = 'State EC votes if adjusted for popular vote turnout' 
        # for animations, set base title (it will change during animation)
        fig_title = f'{base_fig_title}: {YEAR_0} - {YEAR_N}'
              
    # slight rendering variations for dots vs abbrevs 
    if display_elements == 'dots':
        # init figure with core properties
        fig = px.scatter(pivot_on_year_df, x=x_axis_col, y=cols.EC_VOTES, color=cols.GROUP, title=fig_title, 
                        custom_data=custom_data, animation_frame=cols.YEAR, # ignored if df is for single year
                        color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                        width=fig_width, height=fig_height, 
                        opacity=0.7, range_x=[0,x_max], range_y=[0,ec_max])
        # scatterplot dot formatting
        fig.update_traces(marker=dict(size=24, line=dict(width=1, color='white')), 
                        selector=dict(mode='markers'))
        # axis labels
        fig.update_xaxes(title_text=x_axis_title)
        fig.update_yaxes(title_text=y_axis_title)

    elif display_elements == 'abbrevs':
        # 
        if frame:
            range_x = None 
        else:
            range_x = range_x=[.4,x_max]
        # init figure with core properties
        fig = px.scatter(pivot_on_year_df, x=x_axis_col, y=cols.EC_VOTES, color=cols.GROUP, title=fig_title, 
                        custom_data=custom_data, text=cols.ABBREV, animation_frame=cols.YEAR, # ignored if df is for single year
                        color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                        width=fig_width, height=fig_height, opacity=0.7, 
                        log_x=True, log_y=True, range_x=range_x, range_y=[2.5,ec_max])
        # scatterplot dot formatting
        fig.update_traces(marker=dict(size=24, line=dict(width=1, color='DarkSlateGrey')), 
                        selector=dict(mode='markers'))
        # axis labels
        x_axis_title = f"{x_axis_title} (log)"
        y_axis_title = f"{y_axis_title} (log)"
        fig.update_xaxes(title_text=x_axis_title)
        fig.update_yaxes(title_text=y_axis_title)
        # axis tick overrides
        layout = dict(
            yaxis=dict(tickmode='array', tickvals=[3,4,5,6,7,8,9,10,12,15,20,25,30,40,50]),
            # xaxis=dict(tickmode='array', tickvals=[.5,.75,1,1.5,2,3,4,5,6,7,8,10,12,15,20,25,30,40,50,60])
        )
        fig.update_layout(layout)
        if not frame:
            layout = dict(
                xaxis=dict(tickmode='array', tickvals=[.5,.75,1,1.5,2,3,4,5,6,7,8,10,12,15,20,25,30,40,50,60])
            )
            fig.update_layout(layout)
    
    # reference mean / quazi-linear regression line
    fig.add_trace(go.Scatter(x=[0,x_mean_line_max], y=[0,ec_max], mode='lines', 
                            name='Nationwide mean', line=dict(color='black', width=1)))

    fig.update_layout(title_x=0.45)

    if not frame:
        apply_animation_settings(fig, base_fig_title)

    # TODO where are x, y, and customdata actually defined, in fig? I'd like to avoid these redundant key-value mappings and use an f-string for this but not sure how
    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>%{customdata[0]}</b><br>",
            "Electoral College votes: <b>%{y}</b>",
            "Popular vote: <b>%{customdata[1]:,}</b>",
            # "Vote weight: <b>%{customdata[2]:.2f}</b>",
            "Vote weight: <b>%{customdata[2]}</b>",
            "Population per EC vote: <b>%{customdata[3]:,}</b>",
            "<br><b>Normalized to nat'l average:</b>",
            "%{customdata[1]:,} pop votes => %{x} EC votes",
            "%{y} EC votes => %{customdata[4]:,} pop votes",
        ])
    )

    return fig


def build_ivw_by_state_scatter_bubbles(data_obj, groups_dir, max_small, fig_width=None, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    pivot_on_year_df = data_obj.state_vote_weights_pivot_dfs[subdir]
    groups = GROUPS_FOR_DIR[groups_dir]

    # if frame is set, extract single-year data
    if frame:
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] == frame]

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.crt(fig_width)

    # calculate axis range boundaries 
    ec_max = round(pivot_on_year_df[cols.EC_VOTES].max())
    weight_min = pivot_on_year_df[pivot_on_year_df[cols.VOTE_WEIGHT] > 0][cols.VOTE_WEIGHT].min() * 0.9
    weight_max = pivot_on_year_df[cols.VOTE_WEIGHT].max()

    # display metadata
    custom_data = [cols.STATE, cols.VOTES_COUNTED, cols.POP_PER_EC, cols.VOTES_COUNTED_PCT, cols.EC_VOTES_NORM, cols.VOTES_COUNTED_NORM]
    base_fig_title = 'Vote Weight Per Person Per State'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        fig_title = f'{base_fig_title}: {YEAR_0} - {YEAR_N}'

    # init figure with core properties
    fig = px.scatter(pivot_on_year_df, x=cols.EC_VOTES, y=cols.VOTE_WEIGHT, color=cols.GROUP, title=fig_title, 
                    custom_data=custom_data, size=cols.VOTES_COUNTED_PCT, size_max=80, 
                    animation_frame=cols.YEAR, # ignored if df is for single year
                    color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                    width=fig_width, height=fig_height, opacity=0.5, 
                    log_y=True, range_x=[0,ec_max], range_y=[weight_min,weight_max])

    # scatterplot dot formatting
    fig.update_traces(marker=dict(line=dict(width=1, color='white')), 
                    selector=dict(mode='markers'))

    # reference mean / quazi-linear regression line
    fig.add_trace(go.Scatter(x=[0,ec_max], y=[1,1], mode='lines', 
                            name='Nationwide mean', line=dict(color='black', width=1)))

    # axis labels
    fig.update_xaxes(title_text='Electoral college votes per state')
    fig.update_yaxes(title_text='Individual voter impact per state (log)')

    # axis tick overrides
    layout = dict(yaxis=dict(tickmode='array', tickvals=[0.4,0.5,.6,.8,1,1.5,2,3,5,8]))
    fig.update_layout(layout)

    fig.update_layout(title_x=0.45)

    # TODO where are x, y, and customdata actually defined, in fig? I'd like to avoid these redundant key-value mappings and use an f-string for this but not sure how
    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>%{customdata[0]}</b><br>",
            "Electoral College votes: <b>%{x}</b>",
            "Popular vote: <b>%{customdata[1]:,}</b>",
            "Vote weight: <b>%{y:.2f}</b>",
            "Population per EC vote: <b>%{customdata[2]:,}</b>",
            "Pop vote as % of nat'l vote: <b>%{customdata[3]:.2f}%</b>",
            "<br><b>Normalized to nat'l average:</b>",
            "%{customdata[1]:,} pop votes => %{customdata[4]:.2f} EC votes",
            "%{x} EC votes => %{customdata[5]:,} pop votes",
        ])
    )

    return fig


def build_ivw_by_state_group_scatter_dots(data_obj, groups_dir, max_small, fig_width=None, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    group_aggs_by_year_df = data_obj.group_agg_weights_pivot_dfs[subdir]
    groups = GROUPS_FOR_DIR[groups_dir]

    # if frame is set, extract single-year data
    if frame:
        group_aggs_by_year_df = group_aggs_by_year_df[group_aggs_by_year_df[cols.YEAR] == frame]

    # remove the Nat'l Average data
    group_aggs_by_year_df = group_aggs_by_year_df.loc[~(group_aggs_by_year_df[cols.GROUP] == "Nat'l Average")]

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.crt(fig_width)

    # calculate axis range boundaries
    ec_max = round(group_aggs_by_year_df[cols.EC_VOTES].max() * 1.05)
    #pop_max = round(group_aggs_by_year[cols.VOTES_COUNTED].max() * 1.05)
    norm_max = round(group_aggs_by_year_df[cols.EC_VOTES_NORM].max() * 1.05)

    # display metadata
    custom_data = [cols.GROUP, cols.VOTES_COUNTED, cols.AVG_WEIGHT, cols.POP_PER_EC, cols.STATE_COUNT, cols.STATES_IN_GROUP, cols.VOTES_COUNTED_NORM]
    base_fig_title = 'Average Vote Weight Per Person Per Region'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        fig_title = f'{base_fig_title}: {YEAR_0} - {YEAR_N}'

    # init figure with core properties
    fig = px.scatter(group_aggs_by_year_df, x=cols.EC_VOTES_NORM, y=cols.EC_VOTES, color=cols.GROUP, title=fig_title, 
                    custom_data=custom_data, color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                    animation_frame=cols.YEAR, animation_group=cols.GROUP, # ignored if df is for single year          
                    width=fig_width, height=fig_height, opacity=0.7, 
    #                  log_x=True, log_y=True, range_x=[.4,norm_max], range_y=[2,ec_max],
                    range_x=[0, norm_max], range_y=[0, ec_max])
        
    # scatterplot dot formatting
    fig.update_traces(marker=dict(size=24, line=dict(width=1, color='DarkSlateGrey')), selector=dict(mode='markers'))

    # reference mean / quazi-linear regression line
    fig.add_trace(go.Scatter(x=[0,ec_max], y=[0,ec_max], mode='lines', 
                            name='Nationwide mean', line=dict(color='black', width=1)))

    # axis labels
    fig.update_xaxes(title_text='State group EC votes if adjusted for popular vote turnout')
    fig.update_yaxes(title_text='Electoral college votes per state group')

    # axis tick overrides
    num_xticks = round(norm_max / 50) + 1
    layout = dict(xaxis=dict(tickmode='array', tickvals=[t*50 for t in range(num_xticks)]))
    fig.update_layout(layout)

    fig.update_layout(title_x=0.45)

    # TODO where are x, y, and customdata actually defined, in fig? I'd like to avoid these redundant key-value mappings and use an f-string for this but not sure how
    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>%{customdata[0]}</b>",
            "%{customdata[4]} states: %{customdata[5]}<br>",
            "Aggregate Electoral College votes: <b>%{y}</b>",
            "Aggregate popular vote: <b>%{customdata[1]:,}</b>",
            "Average vote weight: <b>%{customdata[2]:.2f}</b>",
            "Average population per EC vote: <b>%{customdata[3]:,}</b>",
            "<br><b>Normalized to nat'l average:</b>",
            "%{customdata[1]:,} pop votes => %{x} EC votes",
            "%{y} EC votes => %{customdata[6]:,} pop votes",
        ])
    )

    return fig


def build_ivw_by_state_group_scatter_bubbles(data_obj, groups_dir, max_small, fig_width=None, frame=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    group_aggs_by_year_df = data_obj.group_agg_weights_pivot_dfs[subdir]
    groups = GROUPS_FOR_DIR[groups_dir]

    # if frame is set, extract single-year data
    if frame:
        group_aggs_by_year_df = group_aggs_by_year_df[group_aggs_by_year_df[cols.YEAR] == frame]

    # remove the Nat'l Average data
    group_aggs_by_year_df = group_aggs_by_year_df.loc[~(group_aggs_by_year_df[cols.GROUP] == "Nat'l Average")]

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.crt(fig_width)

    # calculate axis range boundaries
    ec_max = round(group_aggs_by_year_df[cols.EC_VOTES].max() * 1.1)
    weight_min = group_aggs_by_year_df[group_aggs_by_year_df[cols.AVG_WEIGHT] > 0][cols.AVG_WEIGHT].min() * 0.9
    weight_max = group_aggs_by_year_df[cols.AVG_WEIGHT].max() * 1.1

    # display metadata
    custom_data = [cols.GROUP, cols.VOTES_COUNTED, cols.POP_PER_EC, cols.STATE_COUNT, cols.STATES_IN_GROUP, cols.EC_VOTES_NORM, cols.VOTES_COUNTED_NORM]
    base_fig_title = 'Average Vote Weight Per Person Per Region'
    if frame:
        era = get_era_for_year(frame)
        fig_title = f'{base_fig_title}: {frame} ({era})'
    else:
        fig_title = f'{base_fig_title}: {YEAR_0} - {YEAR_N}'

    # init figure with core properties
    fig = px.scatter(group_aggs_by_year_df, x=cols.EC_VOTES, y=cols.AVG_WEIGHT, color=cols.GROUP, title=fig_title, 
                    custom_data=custom_data, size=cols.VOTES_COUNTED_PCT, size_max=80,  
                    animation_frame=cols.YEAR, animation_group=cols.GROUP, # ignored if df is for single year
                    color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                    width=fig_width, height=fig_height, opacity=0.5, 
                    log_y=True, range_x=[0, ec_max], range_y=[weight_min, weight_max])

    # scatterplot dot formatting
    fig.update_traces(marker=dict(line=dict(width=1, color='white')),
                    selector=dict(mode='markers'))

    # reference mean / quazi-linear regression line
    fig.add_trace(go.Scatter(x=[0,ec_max], y=[1,1], mode='lines', name='Nationwide mean', line=dict(color='black', width=1)))

    # axis labels
    fig.update_xaxes(title_text='Electoral college votes per group')
    fig.update_yaxes(title_text='Impact per individual voter per group')

    fig.update_layout(title_x=0.45)

    # TODO where are x, y, and customdata actually defined, in fig? I'd like to avoid these redundant key-value mappings and use an f-string for this but not sure how
    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>%{customdata[0]}</b>",
            "%{customdata[3]} states: %{customdata[4]}<br>",
            "Aggregate Electoral College votes: <b>%{x}</b>",
            "Aggregate popular vote: <b>%{customdata[1]:,}</b>",
            "Average vote weight: <b>%{y:.2f}</b>",
            "Average population per EC vote: <b>%{customdata[2]:,}</b>",
            "<br><b>Normalized to nat'l average:</b>",
            "%{customdata[1]:,} pop votes => %{customdata[5]:.2f} EC votes",
            "%{x} EC votes => %{customdata[6]:,} pop votes",
        ])
    )

    return fig
