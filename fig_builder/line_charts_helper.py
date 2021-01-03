import pandas as pd
import plotly.express as px

from metadata import Columns, FigDimensions, EVENTS, ERAS, YEAR_0, YEAR_N


cols = Columns()
fig_dims = FigDimensions()


# def add_national_average_line(group_aggs_by_year_df, totals_by_year_df):
#     year = YEAR_0
#     while year <= YEAR_N:
#         # extract year data from totals_by_year
#         year_totals = totals_by_year_df[totals_by_year_df[cols.YEAR] == year]
#         # init and populate new df for year matching column structure for group_aggs_by_year_df
#         df = pd.DataFrame(columns=[cols.GROUP, cols.YEAR, cols.EC_VOTES, cols.VOTES_COUNTED, cols.VOTES_COUNTED_NORM, cols.VOTES_COUNTED_PCT,
#                         cols.EC_VOTES_NORM, cols.POP_PER_EC, cols.AVG_WEIGHT, cols.STATE_COUNT, cols.STATES_IN_GROUP])
#         df[cols.GROUP] = "Nat'l Average"
#         df[cols.YEAR] = year
#         df[cols.EC_VOTES] = year_totals[cols.EC_VOTES].item()
#         df[cols.VOTES_COUNTED] = year_totals[cols.VOTES_COUNTED].item()
#         df[cols.VOTES_COUNTED_NORM] = year_totals[cols.VOTES_COUNTED].item()
#         df[cols.VOTES_COUNTED_PCT] = 100
#         df[cols.EC_VOTES_NORM] = year_totals[cols.EC_VOTES].item()
#         df[cols.POP_PER_EC] = year_totals[cols.POP_PER_EC].item()
#         df[cols.AVG_WEIGHT] = 1.0 
#         df[cols.STATE_COUNT] = year_totals[cols.STATE_COUNT].item() 
#         df[cols.STATES_IN_GROUP] = f"All {year_totals[cols.STATE_COUNT].item()}"
#         # concat single year df to group_aggs_by_year_df
#         group_aggs_by_year_df = pd.concat([group_aggs_by_year_df, df], ignore_index=True, sort=False)

#         year = year + 4

#     return group_aggs_by_year_df


def build_and_annotate_event_markers(fig, events, y_min, y_max, y_min2=None, y_max2=None):
    if not y_min2:
        y_min2 = y_min
    if not y_max2:
        y_max2 = y_max2

    # build markers and labels marking events 
    event_markers = []
    for event in events:
        # add vertical line for each event date
        marker = dict(type='line', line_width=1, x0=event['year'], x1=event['year'], y0=y_min2, y1=y_max2)
        event_markers.append(marker)
        # add annotation for each event name and description
        event_name = event['name']
        if str(event['year']) not in event['name']: 
            event_name = f"{event_name} ({event['year']})"
        fig.add_annotation(x=event['year'], y=y_max, text=event_name, showarrow=False, 
            yshift=-2, xshift=-7, textangle=-90, align='right', yanchor='top')
        if event.get('desc'):
            event_desc = f"<i>{event['desc']}</i>"
            fig.add_annotation(x=event['year'], y=y_min, text=event_desc, showarrow=False, 
                yshift=2, xshift=6, textangle=-90, align='left', yanchor='bottom')

    return event_markers


def build_and_annotate_era_blocks(fig, eras, x_min, y_min, y_max):
    # build shaded blocks designating eras
    era_blocks = []
    for era in eras:
        # add rectangle for each era date range
        block = dict(type='rect', line_width=0, x0=era['begin'], x1=era['end'], y0=y_min, y1=y_max, 
                    fillcolor=era['color'], opacity=0.1)
        era_blocks.append(block) 
        # add annotation for each era
        era_begin = era['begin']
        if era_begin < x_min:
            era_begin = x_min
        era_len = era['end'] - era_begin
        era_mid = (era['end'] + era_begin) / 2
        showarrow = False
        yshift = 8
        if era_len < 10:
            showarrow = True
            yshift = 0
        
        era_name = f"<b>{era['name']}</b>"
        fig.add_annotation(x=era_mid, y=y_max, text=era_name, showarrow=showarrow, yshift=yshift)

    return era_blocks