#!/usr/bin/env python
# import argparse
# import os

import datapane as dp 
import plotly.io as pio

from metadata import Columns, DataDirs, FigDimensions
from data_processor.data_objects import DataObject
from fig_builder import bar_plots, choropleths, line_charts, scatter_plots

cols = Columns()
ddirs = DataDirs()
fig_dims = FigDimensions()
data_obj = DataObject()
data_obj.load_dfs_for_subdir()
data_obj.load_totals_by_year()
data_obj.load_all_states_meta()
html_dir = 'html_figures'

# publishing params 
max_small = 4
groupings = ddirs.ACW
fig_width = 1000
frame = 1960

# publishing templates
# (1) html
# pio.write_html(fig, file=f'{html_dir}/{filename}.html', auto_open=True)
# (2) datapane
# report = dp.Report(dp.Plot(fig)) 
# report.publish(name=filename, open=True, visibility='PUBLIC') 
# (3) plotly
# py.plot(fig, filename=filename, auto_open=True)


# animations
fig = scatter_plots.build_ivw_by_state_scatter_dots(data_obj, groupings, max_small, fig_width=fig_width)
filename = f'anim_scatter_state_vw_dots_{groupings}{max_small}_{fig_width}'

fig = scatter_plots.build_ivw_by_state_scatter_dots(data_obj, groupings, max_small, fig_width=fig_width, display_elements='abbrevs')
filename = f'anim_scatter_state_vw_abbrevs_{groupings}{max_small}_{fig_width}'

fig = scatter_plots.build_ivw_by_state_group_scatter_dots(data_obj, groupings, max_small, fig_width=fig_width)
filename = f'anim_scatter_stategroup_vw_dots_{groupings}{max_small}_{fig_width}'

fig = scatter_plots.build_ivw_by_state_scatter_bubbles(data_obj, groupings, max_small, fig_width=fig_width)
filename = f'anim_scatter_state_vw_bubbles_{groupings}{max_small}_{fig_width}'

fig = scatter_plots.build_ivw_by_state_group_scatter_bubbles(data_obj, groupings, max_small, fig_width=fig_width)
filename = f'anim_scatter_stategroup_vw_bubbles_{groupings}{max_small}_{fig_width}'

fig = choropleths.build_ivw_by_state_map(data_obj, groupings, max_small, cols.LOG_VOTE_WEIGHT, fig_width=fig_width)
filename = f'anim_map_state_vw_{groupings}{max_small}_{fig_width}'

fig = choropleths.build_ivw_by_state_map(data_obj, groupings, max_small, cols.GROUP, fig_width=fig_width)
filename = f'anim_map_state_groups_{groupings}{max_small}_{fig_width}'

fig = bar_plots.build_ivw_by_state_bar(data_obj, groupings, 0, fig_width=fig_width, color_col=cols.GROUP)
filename = f'anim_bar_state_vw_color_by_group_{groupings}0_{fig_width}'

# fig = bar_plots.build_ivw_by_state_bar(data_obj, groupings, max_small, fig_width=fig_width, color_col=cols.LOG_VOTE_WEIGHT)
# filename = f'anim_bar_state_vw_color_by_vw_{groupings}{max_small}_{fig_width}'



# single year statics
fig = bar_plots.build_ivw_by_state_bar(data_obj, groupings, max_small, fig_width=fig_width, frame=2020, color_col=cols.LOG_EC_VOTES)
filename = f'fig_bar_state_vw_color_by_ecv_{fig_width}'

fig = bar_plots.build_ivw_by_state_bar(data_obj, groupings, max_small, fig_width=fig_width, frame=1960, color_col=cols.LOG_VOTE_WEIGHT)
filename = f'fig_bar_state_vw_color_by_vw_{fig_width}'

fig = choropleths.build_ivw_by_state_map(data_obj, groupings, max_small, cols.LOG_VOTE_WEIGHT, fig_width=fig_width, frame=1960)
filename = f'fig_map_state_vw_acw4_{fig_width}'

fig = choropleths.build_ivw_by_state_map(data_obj, groupings, max_small, cols.GROUP, fig_width=fig_width, frame=1960)
filename = f'fig_map_color_by_group_acw4_{fig_width}'

fig = bar_plots.build_ivw_by_state_bar(data_obj, groupings, max_small, fig_width=fig_width, frame=1960, color_col=cols.GROUP)
filename = f'fig_bar_state_vw_color_by_group_{fig_width}'

frame = 1860
fig = bar_plots.build_ivw_by_state_bar(data_obj, groupings, max_small, fig_width=fig_width, frame=frame, color_col=cols.GROUP, alt_groups=['split_small'])
filename = f'fig_bar_state_vw_color_by_group_{frame}_{groupings}{max_small}_{fig_width}'
pio.write_html(fig, file=f'{html_dir}/{filename}.html', auto_open=True)

line_plot_width = fig_dims.MD12
fig = line_charts.build_ivw_by_state_group_line_chart(data_obj, groupings, max_small, fig_width=line_plot_width)
filename = f'fig_line_group_vw_acw4_{line_plot_width}'

fig = scatter_plots.build_ivw_by_state_scatter_dots(data_obj, groupings, max_small, fig_width=fig_width, frame=1960)
filename = f'fig_scatter_state_vw_dots_acw4_{fig_width}'

fig = scatter_plots.build_ivw_by_state_scatter_bubbles(data_obj, groupings, max_small, fig_width=fig_width, frame=1960)
filename = f'fig_scatter_state_vw_bubbles_{frame}_{groupings}{max_small}_{fig_width}'