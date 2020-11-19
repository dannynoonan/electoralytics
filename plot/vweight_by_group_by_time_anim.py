import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#%matplotlib notebook

from electoralytics.metadata import AVG_WEIGHT_BY_YEAR_CSV



# load file
avg_weight_by_year = pd.read_csv(AVG_WEIGHT_BY_YEAR_CSV)
avg_weight_by_year.set_index('Group', inplace=True)

# set column types to int, as they originally were before being saved to csv
avg_weight_by_year.columns = avg_weight_by_year.columns.astype(int)

# init animation writer
Writer = animation.writers['ffmpeg']
writer = Writer(fps=20, metadata=dict(artist='Me'), bitrate=1800)

# init pyplot figure
fig = plt.figure(figsize=(10,6))
plt.xlim(1828,2016)
plt.ylim(0,4)
plt.xlabel('Year', fontsize=20)
plt.ylabel('Avg voter impact', fontsize=20)
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

ani = matplotlib.animation.FuncAnimation(fig, animate, frames=col_count, repeat=True)
plt.show()

#ani.save('/Users/andyshirey/Documents/dev/mappingProjects/electoralResults/csv/aniTime.mp4', writer=writer)
