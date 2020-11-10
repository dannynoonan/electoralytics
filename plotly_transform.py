import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from election_year import ElectionYear, year_data

# constant metadata
category_orders = {'Group': ['Confederate','Border','Northern','Midwest','Western','Small']}
color_discrete_sequence = ['Red','DarkSalmon','MediumBlue','Cyan','SpringGreen','Gold']
hover_data={'Vote weight': True, 'State': True, 'Votes counted': True, 'EC votes': True, 'Group': True}
scatter_labels = {'Vote weight': 'Impact per voter'}

# all year metadata
all_years = pd.read_csv('/Users/andyshirey/Documents/dev/mappingProjects/electoralResults/csv/all_year_sums.csv')
all_years = all_years.set_index('year')

# input var
year = 1896

# fetch and generate data based on year
scatter_data = pd.read_csv(f'/Users/andyshirey/Documents/dev/mappingProjects/electoralResults/csv/{year}Plot.csv')

# mean popular-to-ec vote data
ec_max = round(scatter_data['EC votes'].max() * 1.1) + 1
pop_per_ec = round(all_years.loc[year]['pop_total'] / all_years.loc[year]['ec_total'])
linear_pop_per_ec = [i*pop_per_ec for i in range(ec_max)]
all_ec = [i for i in range(ec_max)]
mean_data = pd.DataFrame({'Mean votes counted': linear_pop_per_ec, 'Mean EC votes': all_ec})
flat_data = pd.DataFrame({'EC votes': [0, ec_max], 'Mean vote weight': [1, 1]})

# titles and labels
scatter_title = f'{year} presidential election: voter impact per state'
box_title = f'{year} presidential election: voter impact per state grouping'
trace_name_natl_avg = f'Nat\'l avg (1 EC : {pop_per_ec} pop)'

# scatter plot 1
fig = px.scatter(scatter_data, x="Votes counted", y="EC votes", color="Group", labels=scatter_labels,
                 category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
                 width=1000, height=800, opacity=0.7, hover_data=hover_data, title=scatter_title)

fig.update_traces(marker=dict(size=12, line=dict(width=1, color='DarkSlateGrey')),
                  selector=dict(mode='markers'))

fig.add_trace(go.Scatter(x=mean_data["Mean votes counted"], y=mean_data["Mean EC votes"], 
                         mode='lines', name='Mean voter impact', line=dict(color='black', width=1)))

fig.update_xaxes(title_text='Popular votes counted per state')
fig.update_yaxes(title_text='Electoral college votes per state')
fig.update_layout(title_x=0.45)
fig.show()

# scatter plot 2
fig = px.scatter(scatter_data, x="EC votes", y="Vote weight", color="Group", size="Votes counted", size_max=60,
                 category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
                 width=1000, height=800, opacity=0.5, hover_data=hover_data, title=scatter_title, log_y=True,
                 labels=scatter_labels)

fig.add_trace(go.Scatter(x=flat_data["EC votes"], y=flat_data["Mean vote weight"], 
                         mode='lines', name=trace_name_natl_avg, line=dict(color='black', width=1)))

fig.update_traces(marker=dict(line=dict(width=1, color='white')),
                  selector=dict(mode='markers'))

fig.update_xaxes(title_text='Electoral college votes per state')
fig.update_yaxes(title_text='Impact per individual voter per state')
fig.update_layout(title_x=0.46)
fig.show()

# box plot
box_data = scatter_data[['Group', 'Vote weight']]
pivot = box_data.pivot(columns='Group', values='Vote weight')

fig = px.box(pivot, color='Group', category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
             width=1000, height=600, log_y=True, title=box_title)

fig.add_trace(go.Scatter(x=flat_data["EC votes"], y=flat_data["Mean vote weight"], 
                         mode='lines', name=trace_name_natl_avg, line=dict(color='black', width=1)))

fig.update_xaxes(title_text='')
fig.update_yaxes(title_text='Range of individual voter impact within state grouping')
fig.update_layout(title_x=0.46)
fig.show()