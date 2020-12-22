

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


def get_era_for_year(year):
    if year <= 1860:
        return 'Antebellum Period'
    elif year == 1864:
        return 'Civil War'
    elif year <= 1876:
        return 'Reconstruction'
    elif year <= 1900:
        return 'Early Jim Crow'
    elif year <= 1952:
        return 'Jim Crow'
    elif year <= 1964:
        return 'Late Jim Crow'
    else:
        return 'Post Voting Rights Act'
