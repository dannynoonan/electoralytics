import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# constant metadata
category_orders = {'Group': ['Confederate','Border','Northeast','Midwest','West','Small']}
color_discrete_sequence = ['Red','DarkSalmon','MediumBlue','Cyan','SpringGreen','Gold']

# load electoral college data
the_one_ring = pd.read_csv('/Users/andyshirey/Documents/dev/mappingProjects/electoralResults/csv/theOneRing.csv')

# input year and set properties derived from year
year = 1900
ec_votes_col = f'{year} EC votes'
votes_counted_col = f'{year} Votes counted'
vote_weight_col = f'{year} Vote weight'
vote_margin_col = f'{year} Vote margin'
swing_weight_col = f'{year} Swing weight'
party_col = f'{year} Party'
hover_data={vote_weight_col: True, 'State': True, votes_counted_col: True, ec_votes_col: True, 'Group': True}
scatter_labels = {vote_weight_col: 'Impact per voter'}

# extract electoral college data for year
scatter_data = the_one_ring[
    ['Abbrev', 'State', 'Group', 
     ec_votes_col, votes_counted_col, vote_weight_col, 
     vote_margin_col, swing_weight_col, party_col]
]
# set state abbrev as key (index) for each row
scatter_data = scatter_data.set_index('Abbrev')

# remove states lacking electoral college votes for this year
# scatter_data = scatter_data[pd.notnull(scatter_data[ec_votes_col])]
# remove states lacking vote weight for this year 
scatter_data = scatter_data[pd.notnull(scatter_data[vote_weight_col])]

# explicitly set type of votes counted and vote margin data to int (not sure why this isn't automatic)
scatter_data[[votes_counted_col, vote_margin_col]] = scatter_data[[votes_counted_col, vote_margin_col]].astype(int)

# extract US totals data before removing US column
ec_total = scatter_data.loc['US'][ec_votes_col]
pop_total = scatter_data.loc['US'][votes_counted_col]
pop_margin = scatter_data.loc['US'][vote_margin_col]
# remove US column
scatter_data = scatter_data.drop('US')

# map states having 4 or fewer electoral college votes to 'Small' Group
scatter_data.loc[scatter_data[ec_votes_col] <= 4, 'Group'] = 'Small'

# mean popular-to-ec vote data
ec_max = round(scatter_data[ec_votes_col].max() * 1.1) + 1
pop_per_ec = round(pop_total / ec_total)
linear_pop_per_ec = [i*pop_per_ec for i in range(ec_max)]
all_ec = [i for i in range(ec_max)]
mean_data = pd.DataFrame({'Mean votes counted': linear_pop_per_ec, 'Mean EC votes': all_ec})
flat_data = pd.DataFrame({'EC votes': [0, ec_max], 'Mean vote weight': [1, 1]})

# titles and labels
scatter_title = f'{year} presidential election: voter impact per state'
box_title = f'{year} presidential election: voter impact per state grouping'
trace_name_natl_avg = f'Nat\'l avg (1 EC : {pop_per_ec} pop)'

# scatter plot 1
fig = px.scatter(scatter_data, x=votes_counted_col, y=ec_votes_col, color='Group', labels=scatter_labels,
                 category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
                 width=1000, height=800, opacity=0.7, hover_data=hover_data, title=scatter_title)

fig.update_traces(marker=dict(size=12, line=dict(width=1, color='DarkSlateGrey')),
                  selector=dict(mode='markers'))

fig.add_trace(go.Scatter(x=mean_data['Mean votes counted'], y=mean_data['Mean EC votes'], 
                         mode='lines', name='Mean voter impact', line=dict(color='black', width=1)))

fig.update_xaxes(title_text='Popular votes counted per state')
fig.update_yaxes(title_text='Electoral college votes per state')
fig.update_layout(title_x=0.45)
fig.show()

# scatter plot 2
fig = px.scatter(scatter_data, x=ec_votes_col, y=vote_weight_col, color='Group', size=votes_counted_col, size_max=60,
                 category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
                 width=1000, height=800, opacity=0.5, hover_data=hover_data, title=scatter_title, log_y=True,
                 labels=scatter_labels)

fig.add_trace(go.Scatter(x=flat_data['EC votes'], y=flat_data['Mean vote weight'], 
                         mode='lines', name=trace_name_natl_avg, line=dict(color='black', width=1)))

fig.update_traces(marker=dict(line=dict(width=1, color='white')),
                  selector=dict(mode='markers'))

fig.update_xaxes(title_text='Electoral college votes per state')
fig.update_yaxes(title_text='Impact per individual voter per state')
fig.update_layout(title_x=0.46)
fig.show()

# box plot
box_data = scatter_data[['Group', vote_weight_col]]
pivot = box_data.pivot(columns='Group', values=vote_weight_col)

fig = px.box(pivot, color='Group', category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
             width=1000, height=600, log_y=True, title=box_title)

fig.add_trace(go.Scatter(x=flat_data['EC votes'], y=flat_data['Mean vote weight'], 
                         mode='lines', name=trace_name_natl_avg, line=dict(color='black', width=1)))

fig.update_xaxes(title_text='')
fig.update_yaxes(title_text='Range of individual voter impact within state grouping')
fig.update_layout(title_x=0.46)
fig.show()
