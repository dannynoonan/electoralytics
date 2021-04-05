import plotly.express as px

from data_processor.functions import get_era_for_year, map_to_subdir
from metadata import Columns, FigDimensions, GROUPS_FOR_DIR, GROUP_COLORS


cols = Columns()
fig_dims = FigDimensions()


def build_vw_by_state_group_box_plot(data_obj, groups_dir, max_small, frame, fig_width=None, fig_height=None, 
                                     alt_groups=[], base_fig_title=None, show_era=True, groups_label=None):
    """
    generate a px.box plot grouping voter weight data by state voter and plotting ranges for each group
    """
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    pivot_on_year_df = data_obj.state_vote_weights_pivot_dfs[subdir].copy()
    groups = GROUPS_FOR_DIR[groups_dir].copy()

    # extract single-year data
    pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] == frame]

    if not groups_label:
        groups_label = 'State Grouping'

    if alt_groups:
        if 'slave_free' in alt_groups:
            pivot_on_year_df.loc[pivot_on_year_df[cols.GROUP] == 'Union', cols.GROUP] = 'Free'
            pivot_on_year_df.loc[pivot_on_year_df[cols.GROUP] == 'Confederate', cols.GROUP] = 'Slave'
            pivot_on_year_df.loc[pivot_on_year_df[cols.GROUP] == 'Border', cols.GROUP] = 'Slave'
            groups = ['Free', 'Slave', 'Small (3-5 ECV)']  # this builds on bad design, but now's not the time to fix
        # remove any rows added by other processes
        pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.GROUP].isin(groups)]

    if not fig_width:
        fig_width = fig_dims.MD6
    if not fig_height:
        fig_height = fig_dims.wide_door(fig_width)

    if not base_fig_title:
        base_fig_title = 'Voter Weight Ranges Across State Groups'

    # display metadata
    fig_title = f'{base_fig_title} ({frame})'
    if show_era:
        era = get_era_for_year(frame)
        fig_title = f'{fig_title}<br>{era}'
    y_axis_title = 'Voter Weight (log)'

    # box plot
    box_data = pivot_on_year_df[[cols.GROUP, cols.VOTE_WEIGHT]]
    pivot = box_data.pivot(columns=cols.GROUP, values=cols.VOTE_WEIGHT)

    # init figure with core properties
    fig = px.box(pivot, color=cols.GROUP, title=fig_title, 
                color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                labels={cols.GROUP: groups_label}, height=fig_height, log_y=True)

    # axis metadata
    fig.update_xaxes(title_text='')
    fig.update_yaxes(title_text=y_axis_title)

    # center title
    fig.update_layout(title_x=0.5)

    return fig
