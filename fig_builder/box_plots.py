import plotly.express as px

from data_processor.functions import get_era_for_year, map_to_subdir
from metadata import Columns, FigDimensions, GROUPS_FOR_DIR, GROUP_COLORS


cols = Columns()
fig_dims = FigDimensions()


def build_ivw_by_state_group_box_plot(data_obj, groups_dir, max_small, frame, fig_width=None):
    subdir = map_to_subdir(groups_dir, max_small)
    data_obj.load_dfs_for_subdir(subdir)
    pivot_on_year_df = data_obj.state_vote_weights_pivot_dfs[subdir].copy()
    groups = GROUPS_FOR_DIR[groups_dir]

    # extract single-year data
    pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.YEAR] == frame]

    # remove any rows added by other processes  TODO can't reproduce issue, only saw this once. aberration?
    # pivot_on_year_df = pivot_on_year_df[pivot_on_year_df[cols.GROUP].isin(groups)]
    # print(f"pivot_on_year_df after:\n{pivot_on_year_df}")

    if not fig_width:
        fig_width = fig_dims.MD6
    fig_height = fig_dims.crt(fig_width)

    # display metadata
    base_fig_title = 'IPV Ranges Across State Groups'
    era = get_era_for_year(frame)
    fig_title = f'{base_fig_title}: {frame} ({era})'
    y_axis_title = 'Range of impact per voter within state group'

    # box plot
    box_data = pivot_on_year_df[[cols.GROUP, cols.VOTE_WEIGHT]]
    pivot = box_data.pivot(columns=cols.GROUP, values=cols.VOTE_WEIGHT)

    # init figure with core properties
    fig = px.box(pivot, color=cols.GROUP, title=fig_title, 
                color_discrete_map=GROUP_COLORS, category_orders={cols.GROUP: groups},
                width=fig_width, height=fig_height, log_y=True)

    # axis metadata
    fig.update_xaxes(title_text='')
    fig.update_yaxes(title_text=y_axis_title)

    # center title
    fig.update_layout(title_x=0.5)

    return fig
