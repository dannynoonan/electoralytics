import plotly.express as px

from metadata import (
    BASE_DATA_DIR, PIVOT_ON_YEAR_CSV, COL_ABBREV, COL_STATE, COL_GROUP, COL_YEAR, COL_EC_VOTES, COL_EC_VOTES_NORM, 
    COL_VOTES_COUNTED, COL_VOTES_COUNTED_PCT, COL_VOTE_WEIGHT, COL_POP_PER_EC, COL_POP_PER_EC_SHORT, COL_PARTY
)


def build_fig_for_year(year, pivot_on_year_df):
    # extract single-year data
    pivot_on_single_year = pivot_on_year_df[pivot_on_year_df[COL_YEAR] == year].sort_values(COL_PARTY, ascending=True)

    # override hover_data
    hover_data = {COL_PARTY: False, COL_VOTES_COUNTED: True, COL_EC_VOTES: True, COL_POP_PER_EC_SHORT: True, COL_EC_VOTES_NORM: True}
    
    # declare fig
    fig = px.bar(pivot_on_single_year, x=COL_VOTE_WEIGHT, y=COL_STATE, color=COL_PARTY, hover_data=hover_data,
                labels={COL_VOTE_WEIGHT: 'Relative impact per voter'}, width=1000, height=800)

    fig.update_layout(
        yaxis={'tickangle': 35, 'showticklabels': True, 'type': 'category', 'tickfont_size': 8},
        yaxis_categoryorder='total ascending',
    )

    return fig


def build_actual_vs_adjusted_ec_fig(year, melted_pivot_on_year_df):
    # ref: https://towardsdatascience.com/how-to-create-a-grouped-bar-chart-with-plotly-express-in-python-e2b64ed4abd7
    # extract single-year data
    melted_pivot_on_single_year = melted_pivot_on_year_df[melted_pivot_on_year_df[COL_YEAR] == year]

    # override hover_data
    hover_data = {COL_PARTY: False, 'Actual vs Adjusted EC votes^': False, COL_VOTES_COUNTED: True, COL_POP_PER_EC_SHORT: True}

    fig = px.bar(melted_pivot_on_single_year, x='EC votes^', y=COL_STATE, 
                color='Actual vs Adjusted EC votes^', barmode='group', 
                hover_data=hover_data,
                width=1000, height=1200)

    fig.update_layout(
        yaxis={'tickangle': 35, 'showticklabels': True, 'type': 'category', 'tickfont_size': 8},
        yaxis_categoryorder='total descending'
    )

    return fig
    