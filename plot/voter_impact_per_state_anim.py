import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from electoralytics.metadata import PIVOT_ON_YEAR_CSV, TOTALS_BY_YEAR_CSV, GROUP_AGGS_BY_YEAR_CSV


# metadata
GROUPS = ['Small', 'Confederate', 'Border', 'Northeast', 'Midwest', 'West']
GROUPS_SER = pd.Series(np.array(GROUPS + ['Total']))

COL_ABBREV = 'Abbrev'
COL_STATE = 'State'
COL_GROUP = 'Group'
COL_YEAR = 'Year'
COL_EC_VOTES = 'EC votes'
COL_VOTES_COUNTED = 'Votes counted'
COL_VOTES_COUNTED_PCT = 'Votes counted %'
COL_EC_VOTES_NORM = 'EC votes normalized'
COL_VOTE_WEIGHT = 'Vote weight'
COL_AVG_WEIGHT = 'Average weight'
COL_PARTY = 'Party'
COL_POP_PER_EC = 'Population per EC vote'
COL_STATE_COUNT = 'State count'
COL_MOST_EC_VOTES = 'Most EC votes'
COL_STATES_IN_GROUP = 'States in group'
COL_MEAN_POP_AT_MOST_EC = 'Mean pop at most EC votes'

FRAME_RATE = 1000
base_fig_title = 'Voter impact by state'
init_fig_title = f'{base_fig_title}: 1828 - 2016'

category_orders = {COL_GROUP: GROUPS}
color_discrete_sequence = ['Gold', 'Red', 'DarkSalmon', 'MediumBlue', 'Cyan', 'SpringGreen']


# load source data 
PIVOT_ON_YEAR_CSV = '/Users/andyshirey/Documents/dev/mappingProjects/electoralResults/csv/pivotOnYear.csv'
TOTALS_BY_YEAR_CSV = '/Users/andyshirey/Documents/dev/mappingProjects/electoralResults/csv/totalsByYear.csv'
GROUP_AGGS_BY_YEAR_CSV = '/Users/andyshirey/Documents/dev/mappingProjects/electoralResults/csv/groupAggsByYear.csv'

pivot_on_year = pd.read_csv(PIVOT_ON_YEAR_CSV)
pivot_on_year.drop('Unnamed: 0', axis=1, inplace=True)

totals_by_year = pd.read_csv(TOTALS_BY_YEAR_CSV)
totals_by_year.drop('Unnamed: 0', axis=1, inplace=True)

group_aggs_by_year = pd.read_csv(GROUP_AGGS_BY_YEAR_CSV)
group_aggs_by_year.drop('Unnamed: 0', axis=1, inplace=True)


# metadata for all scatters
period_info = "1828-1860: Antebellum<br>1864-1876: Reconstruction<br>1880-1964: Jim Crow<br>1968-2016: Civil Rights"


############################ SCATTER 1 ############################

# calculate axis range boundaries 
ec_max = round(pivot_on_year[COL_EC_VOTES].max() * 1.05)
norm_max = round(pivot_on_year[COL_EC_VOTES_NORM].max() * 1.05)

# override hover_data
hover_data = {COL_VOTES_COUNTED: True, COL_VOTE_WEIGHT: True}

# init figure with core properties
fig = px.scatter(pivot_on_year, x=COL_EC_VOTES_NORM, y=COL_EC_VOTES, animation_frame=COL_YEAR, 
                 animation_group=COL_STATE, color=COL_GROUP, title=init_fig_title, 
                 hover_name=COL_STATE, hover_data=hover_data,
#                  category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
#                  log_x=True, log_y=True, range_x=[.4,norm_max], range_y=[2,ec_max],
                 width=1000, height=800, opacity=0.7, range_x=[0,norm_max], range_y=[0,ec_max])
  
# scatterplot dot formatting
fig.update_traces(marker=dict(size=24, line=dict(width=1, color='DarkSlateGrey')), 
                  selector=dict(mode='markers'))

# reference mean / quazi-linear regression line
fig.add_trace(go.Scatter(x=[0,ec_max], y=[0,ec_max], mode='lines', 
                         name='Nationwide mean', line=dict(color='black', width=1)))

# axis labels
fig.update_xaxes(title_text='State EC votes if adjusted for popular vote turnout')
fig.update_yaxes(title_text='Electoral college votes per state')

# embedded period_info
fig.add_annotation(
        x=14, y=52, xref="x", yref="y", align="left", ax=0, ay=0, text=period_info,
        font={'family': "Courier New, monospace", 'size': 16, 'color': "#ffffff"}, 
        bordercolor="#c7c7c7", borderwidth=2, borderpad=4, bgcolor="#ff7f0e", opacity=0.8)


### SHARED FOR ALL SCATTER ANIMATIONS
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = FRAME_RATE
    
for button in fig.layout.updatemenus[0].buttons:
    button["args"][1]["frame"]["redraw"] = True
    
for step in fig.layout.sliders[0].steps:
    step["args"][1]["frame"]["redraw"] = True

for k in range(len(fig.frames)):
    year = 1828 + (k*4)
    if year <= 1860:
        period = 'Antebellum period'
    elif year <= 1876:
        period = 'Reconstruction'
    elif year <= 1964:
        period = 'Jim Crow era'
    else:
        period = 'Civil Rights era'
    fig.frames[k]['layout'].update(title_text=f'{base_fig_title}: {year} ({period})')

fig.update_layout(title_x=0.45)
fig.show()


############################ SCATTER 1a ############################

# calculate axis range boundaries 
ec_max = round(pivot_on_year[COL_EC_VOTES].max() * 1.05)
norm_max = round(pivot_on_year[COL_EC_VOTES_NORM].max() * 1.05)

# override hover_data
hover_data = {COL_VOTES_COUNTED: True, COL_VOTE_WEIGHT: True}

# init figure with core properties
fig = px.scatter(pivot_on_year, x=COL_EC_VOTES_NORM, y=COL_EC_VOTES, animation_frame=COL_YEAR, 
                 animation_group=COL_STATE, color=COL_GROUP, title=init_fig_title, 
                 hover_name=COL_STATE, hover_data=hover_data, text=COL_ABBREV,
#                  category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
                 log_x=True, log_y=True, range_x=[.4,norm_max], range_y=[2.5,ec_max],
                 width=1000, height=800, opacity=0.7)
    
# scatterplot dot formatting
fig.update_traces(marker=dict(size=24, line=dict(width=1, color='DarkSlateGrey')), 
                  selector=dict(mode='markers'))

# reference mean / quazi-linear regression line
fig.add_trace(go.Scatter(x=[0,ec_max], y=[0,ec_max], mode='lines', 
                         name='Nationwide mean', line=dict(color='black', width=1)))

# axis labels
fig.update_xaxes(title_text='State EC votes if adjusted for popular vote turnout')
fig.update_yaxes(title_text='Electoral college votes per state')

# axis tick overrides
layout = dict(
    yaxis=dict(tickmode='array', tickvals=[3,4,5,6,7,8,9,10,12,15,20,25,30,40,50]),
    xaxis=dict(tickmode='array', tickvals=[.5,.75,1,1.5,2,3,4,5,6,7,8,10,12,15,20,25,30,40,50,60])
)
fig.update_layout(layout)

# embedded period_info - TODO why isn't this working?
fig.add_annotation(
        x=20, y=20, xref="x", yref="y", align="left", ax=0, ay=0, text=period_info,
        font={'family': "Courier New, monospace", 'size': 16, 'color': "#ffffff"}, 
        bordercolor="#c7c7c7", borderwidth=2, borderpad=4, bgcolor="#ff7f0e", opacity=0.8)


### SHARED FOR ALL SCATTER ANIMATIONS
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = FRAME_RATE
    
for button in fig.layout.updatemenus[0].buttons:
    button["args"][1]["frame"]["redraw"] = True
    
for step in fig.layout.sliders[0].steps:
    step["args"][1]["frame"]["redraw"] = True

for k in range(len(fig.frames)):
    year = 1828 + (k*4)
    if year <= 1860:
        period = 'Antebellum period'
    elif year <= 1876:
        period = 'Reconstruction'
    elif year <= 1964:
        period = 'Jim Crow era'
    else:
        period = 'Civil Rights era'
    fig.frames[k]['layout'].update(title_text=f'{base_fig_title}: {year} ({period})')

fig.update_layout(title_x=0.45)
fig.show()


############################ SCATTER 2 ############################

# calculate axis range boundaries 
ec_max = round(pivot_on_year[COL_EC_VOTES].max())
weight_min = pivot_on_year[pivot_on_year[COL_VOTE_WEIGHT] > 0][COL_VOTE_WEIGHT].min() * 0.9
weight_max = pivot_on_year[COL_VOTE_WEIGHT].max()

# override hover_data
hover_data = {COL_VOTES_COUNTED: True}

# init figure with core properties
fig = px.scatter(pivot_on_year, x=COL_EC_VOTES, y=COL_VOTE_WEIGHT, animation_frame=COL_YEAR, 
                 animation_group=COL_STATE, size=COL_VOTES_COUNTED_PCT, color=COL_GROUP, hover_name=COL_STATE, 
#                  category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
                 title=init_fig_title, hover_data=hover_data, width=1000, height=800, opacity=0.5,
                 log_y=True, size_max=80, range_x=[0,ec_max], range_y=[weight_min,weight_max])

# scatterplot dot formatting
fig.update_traces(marker=dict(line=dict(width=1, color='white')), 
                  selector=dict(mode='markers'))

# reference mean / quazi-linear regression line
fig.add_trace(go.Scatter(x=[0,ec_max], y=[1,1], mode='lines', 
                         name='Nationwide mean', line=dict(color='black', width=1)))

# axis labels
fig.update_xaxes(title_text='Electoral college votes per state')
fig.update_yaxes(title_text='Individual voter impact per state')

# axis tick overrides
layout = dict(yaxis=dict(tickmode='array', tickvals=[0.4,0.5,.6,.8,1,1.5,2,3,5,8]))
fig.update_layout(layout)

# embedded period_info
fig.add_annotation(
        x=45, y=.85, xref="x", yref="y", align="left", ax=0, ay=0, text=period_info,
        font={'family': "Courier New, monospace", 'size': 16, 'color': "#ffffff"}, 
        bordercolor="#c7c7c7", borderwidth=2, borderpad=4, bgcolor="#ff7f0e", opacity=0.8)


### SHARED FOR ALL SCATTER ANIMATIONS
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = FRAME_RATE
    
for button in fig.layout.updatemenus[0].buttons:
    button["args"][1]["frame"]["redraw"] = True
    
for step in fig.layout.sliders[0].steps:
    step["args"][1]["frame"]["redraw"] = True

for k in range(len(fig.frames)):
    year = 1828 + (k*4)
    if year <= 1860:
        period = 'Antebellum period'
    elif year <= 1876:
        period = 'Reconstruction'
    elif year <= 1964:
        period = 'Jim Crow era'
    else:
        period = 'Civil Rights era'
    fig.frames[k]['layout'].update(title_text=f'{base_fig_title}: {year} ({period})')

fig.update_layout(title_x=0.45)
fig.show()


############################ SCATTER 3 ############################

# calculate axis range boundaries
ec_max = round(group_aggs_by_year[COL_EC_VOTES].max() * 1.05)
#pop_max = round(group_aggs_by_year[COL_VOTES_COUNTED].max() * 1.05)
norm_max = round(group_aggs_by_year[COL_EC_VOTES_NORM].max() * 1.05)

# override hover_data
hover_data = {COL_VOTES_COUNTED: True, COL_AVG_WEIGHT: True, COL_STATE_COUNT: True, COL_STATES_IN_GROUP: True}

# init figure with core properties
fig = px.scatter(group_aggs_by_year, x=COL_EC_VOTES_NORM, y=COL_EC_VOTES, animation_frame=COL_YEAR, 
                 animation_group=COL_GROUP, color=COL_GROUP, title=init_fig_title, 
                 hover_name=COL_GROUP, hover_data=hover_data,
#                  category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
#                  log_x=True, log_y=True, range_x=[.4,norm_max], range_y=[2,ec_max],
                 width=1000, height=800, opacity=0.7, range_x=[0,norm_max], range_y=[0,ec_max])
    
# scatterplot dot formatting
fig.update_traces(marker=dict(size=24, line=dict(width=1, color='DarkSlateGrey')), selector=dict(mode='markers'))

# reference mean / quazi-linear regression line
fig.add_trace(go.Scatter(x=[0,ec_max], y=[0,ec_max], mode='lines', 
                         name='Nationwide mean', line=dict(color='black', width=1)))

# axis labels
fig.update_xaxes(title_text='State group EC votes if adjusted for popular vote turnout')
fig.update_yaxes(title_text='Electoral college votes per state group')

# axis tick overrides
layout = dict(xaxis=dict(tickmode='array', tickvals=[20,40,60,80,100,120,140,160,180,200]))
fig.update_layout(layout)

# embedded period_info
fig.add_annotation(
        x=40, y=150, xref="x", yref="y", align="left", ax=0, ay=0, text=period_info,
        font={'family': "Courier New, monospace", 'size': 16, 'color': "#ffffff"}, 
        bordercolor="#c7c7c7", borderwidth=2, borderpad=4, bgcolor="#ff7f0e", opacity=0.8)


### SHARED FOR ALL SCATTER ANIMATIONS
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = FRAME_RATE
    
for button in fig.layout.updatemenus[0].buttons:
    button["args"][1]["frame"]["redraw"] = True
    
for step in fig.layout.sliders[0].steps:
    step["args"][1]["frame"]["redraw"] = True

for k in range(len(fig.frames)):
    year = 1828 + (k*4)
    if year <= 1860:
        period = 'Antebellum period'
    elif year <= 1876:
        period = 'Reconstruction'
    elif year <= 1964:
        period = 'Jim Crow era'
    else:
        period = 'Civil Rights era'
    fig.frames[k]['layout'].update(title_text=f'{base_fig_title}: {year} ({period})')

fig.update_layout(title_x=0.45)
fig.show()


############################ SCATTER 4 ############################

# calculate axis range boundaries
ec_max = round(group_aggs_by_year[COL_EC_VOTES].max() * 1.1)
weight_min = group_aggs_by_year[group_aggs_by_year[COL_AVG_WEIGHT] > 0][COL_AVG_WEIGHT].min() * 0.9
weight_max = group_aggs_by_year[COL_AVG_WEIGHT].max() * 1.1

# override hover_data
hover_data = {COL_VOTES_COUNTED: True, COL_STATE_COUNT: True, COL_STATES_IN_GROUP: True}

# init figure with core properties
fig = px.scatter(group_aggs_by_year, x=COL_EC_VOTES, y=COL_AVG_WEIGHT, animation_frame=COL_YEAR, 
                 animation_group=COL_GROUP, size=COL_VOTES_COUNTED_PCT, color=COL_GROUP, hover_name=COL_GROUP, 
#                  category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
                 title=init_fig_title, hover_data=hover_data, width=1000, height=800, opacity=0.5,
                 log_y=True, size_max=80, range_x=[0,ec_max], range_y=[weight_min,weight_max])

# scatterplot dot formatting
fig.update_traces(marker=dict(line=dict(width=1, color='white')),
                  selector=dict(mode='markers'))

# reference mean / quazi-linear regression line
fig.add_trace(go.Scatter(x=[0,ec_max], y=[1,1], mode='lines', name='Nationwide mean', line=dict(color='black', width=1)))

# axis labels
fig.update_xaxes(title_text='Electoral college votes per group')
fig.update_yaxes(title_text='Impact per individual voter per group')

# embedded period_info
fig.add_annotation(
        x=90, y=0.4, xref="x", yref="y", align="left", ax=0, ay=0, text=period_info,
        font={'family': "Courier New, monospace", 'size': 14, 'color': "#ffffff"}, 
        bordercolor="#c7c7c7", borderwidth=2, borderpad=4, bgcolor="#ff7f0e", opacity=0.8)


### SHARED FOR ALL SCATTER ANIMATIONS
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = FRAME_RATE
    
for button in fig.layout.updatemenus[0].buttons:
    button["args"][1]["frame"]["redraw"] = True
    
for step in fig.layout.sliders[0].steps:
    step["args"][1]["frame"]["redraw"] = True

for k in range(len(fig.frames)):
    year = 1828 + (k*4)
    if year <= 1860:
        period = 'Antebellum period'
    elif year <= 1876:
        period = 'Reconstruction'
    elif year <= 1964:
        period = 'Jim Crow era'
    else:
        period = 'Civil Rights era'
    fig.frames[k]['layout'].update(title_text=f'{base_fig_title}: {year} ({period})')

fig.update_layout(title_x=0.45)
fig.show()
