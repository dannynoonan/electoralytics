

def validate_input(year_input, all_years):
    year = int(year_input)
    if year in all_years:
        return year
    else:
        return -1


def map_to_subdir(groupings_input, small_group_input):
    if groupings_input == 'Original':
        if small_group_input == 'Extract Small' or 'Extract Small' in small_group_input:
            return 'gen'
        else:
            return 'gen_noSmall'
    else:
        if small_group_input == 'Extract Small' or 'Extract Small' in small_group_input:
            return 'gen_altGroup'
        else:
            return 'gen_altGroupNoSmall'
