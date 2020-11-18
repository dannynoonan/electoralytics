import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
%matplotlib notebook

# load electoral college data
the_one_ring = pd.read_csv('/Users/andyshirey/Documents/dev/mappingProjects/electoralResults/csv/theOneRing.csv')

# initialize new data frames
groups = pd.Series(np.array(['Small','Confederate','Border','Northeast','Midwest','West','Total']))
groups_by_year = pd.DataFrame({'Group': groups})
avg_weight_by_year = pd.DataFrame({'Group': groups})

# set Group as key/index for each row
groups_by_year = groups_by_year.set_index('Group')
avg_weight_by_year = avg_weight_by_year.set_index('Group')

### PROCESS CSV DATA ###
year = 1828
while year <= 2016:
    
    # column names for current year
    ec_votes_col = f'{year} EC votes'
    votes_counted_col = f'{year} Votes counted'
    vote_weight_col = f'{year} Vote weight'
    avg_weight_col = f'{year} Average weight'

    # extract electoral college data for year
    year_data = the_one_ring[['Abbrev', 'State', 'Group', ec_votes_col, votes_counted_col, vote_weight_col]]

    # set state abbrev as key/index for each row
    year_data = year_data.set_index('Abbrev')

    # DATA CLEANSING
    # remove states lacking vote weight for this year 
    year_data = year_data[pd.notnull(year_data[vote_weight_col])]

    # explicitly set type of votes counted and vote margin data to int (not sure why this isn't automatic)
    year_data[[votes_counted_col]] = year_data[[votes_counted_col]].astype(int)

    # extract US totals data before removing US column
    ec_total = year_data.loc['US'][ec_votes_col]
    pop_total = year_data.loc['US'][votes_counted_col]
    # calculate average popular vote per EC vote
    pop_per_ec = round(pop_total / ec_total)
    # remove US column
    year_data = year_data.drop('US')

    # map states having 4 or fewer electoral college votes to 'Small' Group
    year_data.loc[year_data[ec_votes_col] <= 4, 'Group'] = 'Small'

    # DATA AGGREGATION
    # aggregate EC votes and popular votes for each Group, assign summed values to new year_agg dataframe
    year_agg = year_data.groupby('Group').agg({ec_votes_col: 'sum', votes_counted_col: 'sum'})
    # add Average weight column by dividing EC votes by popular votes and multiplying by national pop-per-EC factor
    year_agg[avg_weight_col] = pop_per_ec * year_agg[ec_votes_col] / year_agg[votes_counted_col]
    # add Total row to end of of year_agg
    total_row = pd.DataFrame([['Total', ec_total, pop_total, 1.0]], 
                             columns=['Group', ec_votes_col, votes_counted_col, avg_weight_col])
    total_row = total_row.set_index('Group')
    # append total_row by merging dataframes
    year_agg = year_agg.append(total_row)
    
    # combine year_agg into groups_by_year
    #pd.concat([groups_by_year, year_agg], axis=1)
    #pd.merge(groups_by_year, year_agg, left_index=True, right_index=True, how='outer')
    groups_by_year = groups_by_year.join(year_agg, how='outer')
    
    # extract avg_weight column into its own dataframe, rename column to be simply the year
    avg_weight_df = year_agg.drop([ec_votes_col, votes_counted_col], axis=1)
    avg_weight_df = avg_weight_df.rename(columns={avg_weight_col: year})
    avg_weight_by_year = avg_weight_by_year.join(avg_weight_df, how='outer')
    
    # increment to next election
    year = year + 4

# write groups_by_year to file
# groups_by_year.to_csv('/Users/andyshirey/Documents/dev/mappingProjects/electoralResults/csv/groupsByYear.csv')

# remove Total row/index from avg_weight_by_year
# avg_weight_by_year = avg_weight_by_year.drop(['Total'])
# rename Total row/index to 
avg_weight_by_year = avg_weight_by_year.rename(index={'Total': 'Nat\'l Average'})


### STATIC PLOT ###
# static line plot
layout = go.Layout(
    title="Individual voter impact per state grouping over time",
    plot_bgcolor="#FFFFFF",
    legend=dict(
        # Adjust click behavior
        itemclick="toggleothers",
        itemdoubleclick="toggle",
    ),
    xaxis=dict(
        title="Year",
        linecolor="#BCCCDC",
    ),
    yaxis=dict(
        title="State Grouping",
        linecolor="#BCCCDC"
    ),
    height=500,
    width=1000
)

scatters = []
for group in avg_weight_by_year.index:
    x_years = avg_weight_by_year.keys()
    y_vote_weights = []
    for year in x_years:
        group_in_year = avg_weight_by_year.loc[group, year]
        #print(f"state: {state}, year {year}, vote_weight: {state_in_year}")
        y_vote_weights.append(group_in_year)
    
    line_chart = go.Scatter(
        x=x_years,
        y=y_vote_weights,
        name=group
    )
    scatters.append(line_chart)

fig = go.Figure(data=scatters, layout=layout)
#fig.update_yaxes(type="log", range=[-.4,0.8])
fig.show(config={"displayModeBar": False, "showTips": False}) # Remove floating menu


### ANIMATION ###
# init animation writer
Writer = animation.writers['ffmpeg']
writer = Writer(fps=20, metadata=dict(artist='Me'), bitrate=1800)

# init pyplot figure
fig = plt.figure(figsize=(10,6))
plt.xlim(1828,2016)
plt.ylim(0,4)
plt.xlabel('Year', fontsize=20)
plt.ylabel('Avg voter impact', fontsize=20)
#plt.yscale('log')
plt.title('Voter impact per election', fontsize=20)

col_count = len(avg_weight_by_year.columns)

# define animation loop
def animate(i):
    year = 1828 + (i * 4)
    groups = ['Small','Confederate','Border','Northeast','Midwest','West']
    colors = ['yellow','red','orange','blue','cyan','green']
    for j in range(len(groups)):
        group_data = avg_weight_by_year.loc[groups[j], :str(year)] 
        p = sns.lineplot(x=group_data.index, y=group_data.values, data=group_data, palette=[colors[j]], linewidth=0.5)
        p.tick_params(labelsize=col_count)
        plt.setp(p.lines, linewidth=7)

# generate animation 
ani = matplotlib.animation.FuncAnimation(fig, animate, frames=col_count, repeat=True)
# plot animation
plt.show()
# save animation
ani.save('/Users/andyshirey/Documents/dev/mappingProjects/electoralResults/csv/aniTime2.mp4', writer=writer)
