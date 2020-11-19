import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# constant metadata
COL_ABBREV = 'Abbrev'
COL_STATE = 'State'
COL_GROUP = 'Group'
COL_YEAR = 'Year'
COL_EC_VOTES = 'EC votes'
COL_VOTES_COUNTED = 'Votes counted'
COL_VOTE_WEIGHT = 'Vote weight'
COL_AVG_WEIGHT = 'Average weight'
COL_PARTY = 'Party'

groups = pd.Series(np.array(['Small', 'Confederate', 'Border', 'Northeast', 'Midwest', 'West', 'Total']))
category_orders = {COL_GROUP: ['Small','Confederate','Border','Northeast','Midwest','West']}
color_discrete_sequence = ['Gold','Red','DarkSalmon','MediumBlue','Cyan','SpringGreen']

# load source data 
PIVOT_ON_YEAR_CSV = '/Users/andyshirey/Documents/dev/mappingProjects/electoralResults/csv/pivotOnYear.csv'
pivot_on_year = pd.read_csv(PIVOT_ON_YEAR_CSV)
pivot_on_year.drop('Unnamed: 0', axis=1, inplace=True)

TOTALS_BY_YEAR_CSV = '/Users/andyshirey/Documents/dev/mappingProjects/electoralResults/csv/totalsByYear.csv'
totals_by_year = pd.read_csv(TOTALS_BY_YEAR_CSV)
totals_by_year.drop('Unnamed: 0', axis=1, inplace=True)

# scatter 1
fig_title = 'Voter impact by state in presidential elections'

fig = px.scatter(pivot_on_year, x=COL_VOTES_COUNTED, y=COL_EC_VOTES, animation_frame=COL_YEAR, 
                 animation_group=COL_STATE, color=COL_GROUP, hover_name=COL_STATE, title=fig_title,
#                  category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
#                  log_y=True, 
                 width=1000, height=800, opacity=0.7, 
                 range_y=[0,55], range_x=[0,10000000])
    
fig.update_traces(marker=dict(size=12, line=dict(width=1, color='DarkSlateGrey')), selector=dict(mode='markers'))

# fig.add_trace(go.Scatter(x=totals_by_year[COL_VOTES_COUNTED], y=totals_by_year[COL_EC_VOTES], 
#                          animation_frame=COL_YEAR, animation_group=COL_STATE,
#                          mode='lines', name='Mean voter impact', line=dict(color='black', width=1)))

fig.update_xaxes(title_text='Popular votes counted per state')
fig.update_yaxes(title_text='Electoral college votes per state')
fig.update_layout(title_x=0.45)
fig.show()

# scatter 2
fig = px.scatter(pivot_on_year, x=COL_EC_VOTES, y=COL_VOTE_WEIGHT, animation_frame=COL_YEAR, 
                 animation_group=COL_STATE, size=COL_VOTES_COUNTED, color=COL_GROUP, hover_name=COL_STATE, 
#                  category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
                 title=fig_title, width=1000, height=800, opacity=0.5,
#                  range_y=[0,10],
                 log_y=True, size_max=80, range_x=[0,55])

# fig.add_trace(go.Scatter(x=flat_data['EC votes'], y=flat_data['Mean vote weight'], 
#                          mode='lines', name=trace_name_natl_avg, line=dict(color='black', width=1)))

fig.update_traces(marker=dict(line=dict(width=1, color='white')),
                  selector=dict(mode='markers'))

fig.update_xaxes(title_text='Electoral college votes per state')
fig.update_yaxes(title_text='Impact per individual voter per state')
fig.update_layout(title_x=0.46)
fig.show()
