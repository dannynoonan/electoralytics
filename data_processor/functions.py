from metadata import FRAME_RATE


def validate_input(year_input, all_years):
    year = int(year_input)
    if year in all_years:
        return year
    else:
        return -1


def map_to_subdir(groupings_input, small_group_input):
    if groupings_input == 'Civil War':
        if small_group_input == 'Extract Small' or 'Extract Small' in small_group_input:
            return 'gen'
        else:
            return 'gen_noSmall'
    else:
        if small_group_input == 'Extract Small' or 'Extract Small' in small_group_input:
            return 'gen_altGroup'
        else:
            return 'gen_altGroupNoSmall'


def get_era_for_year(year):
    if year <= 1860:
        return 'Antebellum Period'
    elif year == 1864:
        return 'Civil War'
    elif year <= 1876:
        return 'Reconstruction'
    elif year <= 1900:
        return 'Redemption / Early Jim Crow'
    elif year <= 1948:
        return 'Jim Crow Era'
    elif year <= 1964:
        return 'Late Jim Crow / Civil Rights Era'
    else:
        return 'Post Voting Rights Act'


def apply_animation_settings(fig, base_fig_title, frame_rate=None):
    if not frame_rate:
        frame_rate = FRAME_RATE

    fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = frame_rate
        
    for button in fig.layout.updatemenus[0].buttons:
        button["args"][1]["frame"]["redraw"] = True
        
    for step in fig.layout.sliders[0].steps:
        step["args"][1]["frame"]["redraw"] = True

    for k in range(len(fig.frames)):
        year = 1828 + (k*4)
        era = get_era_for_year(year)
        fig.frames[k]['layout'].update(title_text=f'{base_fig_title}: {year} ({era})')

    # return fig