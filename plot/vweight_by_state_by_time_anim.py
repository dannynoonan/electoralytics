import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from electoralytics.metadata import PIVOT_ON_YEAR_CSV, TOTALS_BY_YEAR_CSV


# metadata
COL_ABBREV = 'Abbrev'
COL_STATE = 'State'
COL_GROUP = 'Group'
COL_YEAR = 'Year'
COL_EC_VOTES = 'EC votes'
COL_VOTES_COUNTED = 'Votes counted'
COL_VOTE_WEIGHT = 'Vote weight'
COL_AVG_WEIGHT = 'Average weight'
COL_PARTY = 'Party'
COL_POP_PER_EC = 'Population per EC vote'
COL_STATE_COUNT = 'State count'
COL_MOST_EC_VOTES = 'Most EC votes'
COL_MEAN_POP_AT_MOST_EC = 'Mean pop at most EC votes'

groups = pd.Series(np.array(['Small', 'Confederate', 'Border', 'Northeast', 'Midwest', 'West', 'Total']))
category_orders = {COL_GROUP: ['Small', 'Confederate', 'Border', 'Northeast', 'Midwest', 'West']}
color_discrete_sequence = ['Gold', 'Red', 'DarkSalmon', 'MediumBlue', 'Cyan', 'SpringGreen']

# load source data 
pivot_on_year = pd.read_csv(PIVOT_ON_YEAR_CSV)
pivot_on_year.drop('Unnamed: 0', axis=1, inplace=True)

totals_by_year = pd.read_csv(TOTALS_BY_YEAR_CSV)
totals_by_year.drop('Unnamed: 0', axis=1, inplace=True)

# break source data up into 3 eras
pivot_on_year_1 = pivot_on_year.loc[pivot_on_year[COL_YEAR] <= 1876]
pivot_on_year_2 = pivot_on_year.loc[pivot_on_year[COL_YEAR] >= 1868].loc[pivot_on_year[COL_YEAR] <= 1976]
pivot_on_year_3 = pivot_on_year.loc[pivot_on_year[COL_YEAR] >= 1956]

# calculate COL_MEAN_POP_AT_MOST_EC
totals_by_year[COL_MEAN_POP_AT_MOST_EC] = totals_by_year[COL_MOST_EC_VOTES] * totals_by_year[COL_POP_PER_EC]
totals_by_year_1 = totals_by_year.loc[totals_by_year[COL_YEAR] <= 1876]
totals_by_year_2 = totals_by_year.loc[totals_by_year[COL_YEAR] >= 1868].loc[pivot_on_year[COL_YEAR] <= 1976]
totals_by_year_3 = totals_by_year.loc[totals_by_year[COL_YEAR] >= 1956]

# scatter 1
fig_title = 'Voter impact by state in presidential elections'

df = pivot_on_year_1
totals = totals_by_year_1

ec_max = round(df[COL_EC_VOTES].max() * 1.1)
pop_max = round(df[COL_VOTES_COUNTED].max() * 1.1)

fig = px.scatter(df, x=COL_VOTES_COUNTED, y=COL_EC_VOTES, animation_frame=COL_YEAR, 
                 animation_group=COL_STATE, color=COL_GROUP, hover_name=COL_STATE, title=fig_title,
#                  category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
                 width=1000, height=800, opacity=0.7, range_y=[0,ec_max], range_x=[0,pop_max])
    
fig.update_traces(marker=dict(size=12, line=dict(width=1, color='DarkSlateGrey')), selector=dict(mode='markers'))

# nationwide mean line (DERP)
# fig.add_trace(go.Scatter(x=totals[COL_MEAN_POP_AT_MOST_EC], y=totals[COL_MOST_EC_VOTES], 
#                          mode='lines', name='Nationwide mean', line=dict(color='black', width=1)))

# fig.add_trace(go.Scatter(x=totals_by_year[COL_VOTES_COUNTED], y=totals_by_year[COL_EC_VOTES], 
#                          animation_frame=COL_YEAR, animation_group=COL_STATE,
#                          mode='lines', name='Mean voter impact', line=dict(color='black', width=1)))

fig.update_xaxes(title_text='Popular votes counted per state')
fig.update_yaxes(title_text='Electoral college votes per state')
fig.update_layout(title_x=0.45)
fig.show()

# scatter 2
df = pivot_on_year_1
ec_max = round(df[COL_EC_VOTES].max() * 1.1)
weight_min = df[df[COL_VOTE_WEIGHT] > 0][COL_VOTE_WEIGHT].min() * 0.9
weight_max = df[COL_VOTE_WEIGHT].max() * 1.1

fig = px.scatter(df, x=COL_EC_VOTES, y=COL_VOTE_WEIGHT, animation_frame=COL_YEAR, 
                 animation_group=COL_STATE, size=COL_VOTES_COUNTED, color=COL_GROUP, hover_name=COL_STATE, 
#                  category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
                 title=fig_title, width=1000, height=800, opacity=0.5,
                 log_y=True, size_max=80, range_x=[0,ec_max], range_y=[weight_min,weight_max])

fig.add_trace(go.Scatter(x=[0,ec_max], y=[1,1], mode='lines', name='Nationwide mean', line=dict(color='black', width=1)))

fig.update_traces(marker=dict(line=dict(width=1, color='white')),
                  selector=dict(mode='markers'))

fig.update_xaxes(title_text='Electoral college votes per state')
fig.update_yaxes(title_text='Impact per individual voter per state')
fig.update_layout(title_x=0.46)
fig.show()
