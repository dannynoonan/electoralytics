import plotly.express as px


def build_fig_for_year(year, pivot_on_year_df):
    # extract single-year data
    pivot_on_single_year = pivot_on_year_df[pivot_on_year_df['Year'] == year].sort_values('Party', ascending=True)

    # override hover_data
    hover_data = {'Party': False, 'Votes counted': True, 'EC votes': True, 'Pop per EC vote': True, 'EC votes normalized': True}
    
    # declare fig
    fig = px.bar(pivot_on_single_year, x='Vote weight', y='State', color='Party', hover_data=hover_data,
                labels={'Vote weight': 'Relative impact per voter'}, width=1000, height=800)

    fig.update_layout(
        yaxis={'tickangle': 35, 'showticklabels': True, 'type': 'category', 'tickfont_size': 8},
        yaxis_categoryorder='total ascending',
    )

    return fig


def build_actual_vs_adjusted_ec_fig(year, melted_pivot_on_year_df):
    # ref: https://towardsdatascience.com/how-to-create-a-grouped-bar-chart-with-plotly-express-in-python-e2b64ed4abd7
    # extract single-year data
    melted_pivot_on_single_year = melted_pivot_on_year_df[melted_pivot_on_year_df['Year'] == year]

    # override hover_data
    hover_data = {'Party': False, 'Actual vs Adjusted EC votes^': False, 'Votes counted': True, 'Pop per EC vote': True}

    fig = px.bar(melted_pivot_on_single_year, x="EC votes^", y="State", 
                color='Actual vs Adjusted EC votes^', barmode='group', 
                hover_data=hover_data,
                width=1000, height=1200)

    fig.update_layout(
        yaxis={'tickangle': 35, 'showticklabels': True, 'type': 'category', 'tickfont_size': 8},
        yaxis_categoryorder='total descending'
    )

    return fig
    