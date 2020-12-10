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