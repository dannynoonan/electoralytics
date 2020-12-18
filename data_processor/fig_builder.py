import plotly.express as px

from metadata import (
    COL_ABBREV, COL_STATE, COL_GROUP, COL_YEAR, COL_EC_VOTES, COL_EC_VOTES_NORM,  COL_VOTES_COUNTED, COL_VOTES_COUNTED_PCT, 
    COL_VOTE_WEIGHT, COL_POP_PER_EC, COL_POP_PER_EC_SHORT, COL_PARTY, GROUPS, GROUP_COLORS, PARTIES, PARTY_COLORS
)


def build_fig_for_year(year, pivot_on_year_df):
    # extract single-year data
    pivot_on_single_year = pivot_on_year_df[pivot_on_year_df[COL_YEAR] == year].sort_values(COL_PARTY, ascending=True)

    # display metadata
    hover_data = {COL_PARTY: False, COL_VOTES_COUNTED: True, COL_EC_VOTES: True, COL_POP_PER_EC_SHORT: True, COL_EC_VOTES_NORM: True}
    category_orders = {COL_PARTY: PARTIES}
    color_discrete_sequence = [PARTY_COLORS[p] for p in PARTIES]
    
    # declare fig
    fig = px.bar(pivot_on_single_year, x=COL_VOTE_WEIGHT, y=COL_STATE, color=COL_PARTY, hover_data=hover_data,
                category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
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

    # display metadata
    hover_data = {COL_PARTY: False, 'Actual vs Adjusted EC votes^': False, COL_VOTES_COUNTED: True, COL_POP_PER_EC_SHORT: True}
    category_orders = {COL_PARTY: PARTIES}
    color_discrete_sequence = [PARTY_COLORS[p] for p in PARTIES]

    fig = px.bar(melted_pivot_on_single_year, x='EC votes^', y=COL_STATE,  
                color='Actual vs Adjusted EC votes^', barmode='group', hover_data=hover_data,
                category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
                width=1000, height=1200)

    fig.update_layout(
        yaxis={'tickangle': 35, 'showticklabels': True, 'type': 'category', 'tickfont_size': 8},
        yaxis_categoryorder='total descending'
    )

    return fig


def build_swallowed_vote_fig_1(swallowed_vote_df):
    print(f"in build_swallowed_vote_fig_1, swallowed_vote_df.head(): {swallowed_vote_df.head()}")

    # override hover_data
    hover_data = {'State': True, 'Candidate': True, 'EC Votes for Candidate': True, 'State: Candidate': False,
                'Candidate: Outcome': False}

    # assign group colors
    category_orders = {'Candidate': ['Biden','Trump']}
    color_discrete_sequence = ['Blue','Red']

    fig = px.bar(swallowed_vote_df, x="Popular Vote", y="State: Candidate", 
                color='Candidate', hover_data=hover_data, width=1000, height=800,
                category_orders=category_orders, color_discrete_sequence=color_discrete_sequence)

    fig.update_layout(yaxis_categoryorder='total ascending')
    fig.update_xaxes(range=[0,10000000])

    return fig
    

def build_swallowed_vote_fig_2(swallowed_vote_df):
    print(f"in build_swallowed_vote_fig_2, swallowed_vote_df.head(): {swallowed_vote_df.head()}")

    # override hover_data
    hover_data = {'State': True, 'Candidate': True, 'EC Votes for Candidate': True, 'State: Candidate': False, 
                'Candidate: Outcome': False}

    # assign group colors
    category_orders = {'Candidate: Outcome': ['Biden: Win','Trump: Win','Biden: Loss','Trump: Loss']}
    color_discrete_sequence = ['Blue','Red','Gray','Gray']

    fig = px.bar(swallowed_vote_df, x="Popular Vote", y="State: Candidate", 
                color='Candidate: Outcome', hover_data=hover_data, width=1000, height=800,
                category_orders=category_orders, color_discrete_sequence=color_discrete_sequence)

    fig.update_layout(yaxis_categoryorder='total ascending')
    fig.update_xaxes(range=[0,10000000])

    return fig


def build_swallowed_vote_fig_3(swallowed_vote_df):
    print(f"in build_swallowed_vote_fig_3, swallowed_vote_df.head(): {swallowed_vote_df.head()}")

    # override hover_data
    hover_data = {'State': True, 'Candidate': True, 'EC Votes for Candidate': True, 'State: Candidate': False, 
                'Candidate: Outcome': False}

    category_orders = {'Candidate: Outcome': ['Biden: Win','Trump: Win','Biden: Loss','Trump: Loss']}
    color_discrete_sequence = ['Blue','Red','Gray','Gray']

    fig = px.bar(swallowed_vote_df, x="Popular Vote", y="State", 
                color='Candidate: Outcome', barmode='relative', hover_data=hover_data, width=1000, height=800,
                category_orders=category_orders, color_discrete_sequence=color_discrete_sequence)

    fig.update_layout(yaxis_categoryorder='total ascending')
    fig.update_xaxes(range=[0,18000000])

    return fig


def build_swallowed_vote_fig_4(swallowed_vote_df):
    distilled_svs = swallowed_vote_df.sort_values('EC Votes for Candidate', ascending=False)
    distilled_svs = distilled_svs[distilled_svs['EC Votes for Candidate'] != 0]
    
    print(f"in build_swallowed_vote_fig_4, swallowed_vote_df.head(): {swallowed_vote_df.head()}")

    # override hover_data
    hover_data = {'State': True, 'EC Votes for Candidate': True, 'State: Candidate': False}

    # assign group colors
    category_orders = {'Candidate': ['Biden','Trump']}
    color_discrete_sequence = ['Blue','Red']

    fig = px.bar(distilled_svs, x="EC Votes for Candidate", y="State", 
                color='Candidate', hover_data=hover_data, width=1000, height=800,
                category_orders=category_orders, color_discrete_sequence=color_discrete_sequence)

    fig.update_layout(yaxis_categoryorder='total ascending')

    return fig


def build_ivw_by_state_group_box_plot(year, pivot_on_year_df):
    # extract single-year data
    pivot_on_single_year = pivot_on_year_df[pivot_on_year_df[COL_YEAR] == year].sort_values(COL_PARTY, ascending=True)

    # display metadata
    category_orders = {COL_GROUP: GROUPS}
    color_discrete_sequence = [GROUP_COLORS[g] for g in GROUPS]
    box_title = f'{year} presidential election: voter impact by state grouping'

    # box plot
    box_data = pivot_on_single_year[[COL_GROUP, COL_VOTE_WEIGHT]]
    pivot = box_data.pivot(columns=COL_GROUP, values=COL_VOTE_WEIGHT)

    fig = px.box(pivot, color=COL_GROUP, 
                category_orders=category_orders, color_discrete_sequence=color_discrete_sequence,
                width=1000, height=600, log_y=True, title=box_title)

    # fig.add_trace(go.Scatter(x=flat_data['EC votes'], y=flat_data['Mean vote weight'], 
    #                          mode='lines', name=trace_name_natl_avg, line=dict(color='black', width=1)))

    fig.update_xaxes(title_text='')
    fig.update_yaxes(title_text='Range of individual voter impact within state grouping')
    fig.update_layout(title_x=0.46)
    return fig
