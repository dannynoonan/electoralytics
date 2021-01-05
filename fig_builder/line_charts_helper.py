import pandas as pd
import plotly.express as px

from metadata import Columns, FigDimensions, EVENTS, ERAS, YEAR_0, YEAR_N


cols = Columns()
fig_dims = FigDimensions()


def build_and_annotate_event_markers(fig, events, y_min, y_max, y_min2=None, y_max2=None):
    if not y_min2:
        y_min2 = y_min
    if not y_max2:
        y_max2 = y_max

    # build markers and labels marking events 
    event_markers = []
    for event in events:
        # add vertical line for each event date
        marker = dict(type='line', line_width=1, line_color='#888888', x0=event['year'], x1=event['year'], y0=y_min2, y1=y_max2)
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


def build_and_annotate_era_blocks(fig, eras, x_min, y_min, y_max, y_max2=None):
    if not y_max2:
        y_max2 = y_max

    # build shaded blocks designating eras
    era_blocks = []
    for era in eras:
        # add rectangle for each era date range
        block = dict(type='rect', line_width=0, x0=era['begin'], x1=era['end'], y0=y_min, y1=y_max, 
                    fillcolor=era['color'], opacity=0.12)
        era_blocks.append(block) 
        # add annotation for each era, centering text above rectangle
        era_begin = era['begin']
        if era_begin < x_min:
            era_begin = x_min
        era_mid = (era['end'] + era_begin) / 2
        era_name = f"<b>{era['name']}</b>"
        # special positioning for eras whose text would overlap
        if era['name'] in ['Civil War', 'Reconstruction']:
            if era['name'] == 'Civil War':
                xshift = -2
                yshift = 0
            if era['name'] == 'Reconstruction':
                xshift = 8
                yshift = -12
            fig.add_annotation(x=era_mid, y=y_max2, text=era_name, showarrow=True, arrowhead=2, xshift=xshift, yshift=yshift)
        # standard positioning for other eras
        else:
            yshift = 8
            fig.add_annotation(x=era_mid, y=y_max2, text=era_name, showarrow=False, yshift=yshift)

    return era_blocks