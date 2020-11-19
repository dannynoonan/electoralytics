import pandas as pd
import numpy as np
import plotly.graph_objects as go

from electoralytics.metadata import AVG_WEIGHT_BY_YEAR_CSV


# load file
avg_weight_by_year = pd.read_csv(AVG_WEIGHT_BY_YEAR_CSV)
avg_weight_by_year.set_index('Group', inplace=True)

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
        title="Election Year",
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
