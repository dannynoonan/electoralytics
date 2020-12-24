# data dirs
BASE_DATA_DIR = 'data'
GEN_DATA_DIR = 'gen'
GEN_ALT_GROUP_DIR = 'gen_altGroup'
GEN_NO_SMALL_DIR = 'gen_noSmall'
GEN_ALT_GROUP_NO_SMALL_DIR = 'gen_altGroupNoSmall'
# data files
THE_ONE_RING_CSV = f'{BASE_DATA_DIR}/theOneRing.csv'
SWALLOWED_VOTE_2020_CSV = f'{BASE_DATA_DIR}/swallowedVoteSampler2020.csv'
GROUPS_BY_YEAR_CSV = 'groupsByYear.csv'
AVG_WEIGHT_BY_YEAR_CSV = 'avgWeightByYear.csv'
PIVOT_ON_YEAR_CSV = 'pivotOnYear.csv'
TOTALS_BY_YEAR_CSV = 'totalsByYear.csv'
GROUP_AGGS_BY_YEAR_CSV = 'groupAggsByYear.csv'

# data dir descriptions
DATA_DIR_DESCRIPTIONS = {
    GEN_DATA_DIR: 'Civil War Groupings, With \'Small\' States Extracted',
    GEN_ALT_GROUP_DIR: 'Regional Census Groupings, With \'Small\' States Extracted',
    GEN_NO_SMALL_DIR: 'Civil War Groupings',
    GEN_ALT_GROUP_NO_SMALL_DIR: 'Regional Census Groupings'
}

# state groupings
ACW_GROUPS = ['Union', 'Confederate', 'Border', 'Post-War', 'Small']
CENSUS_GROUPS = ['Northeast', 'South', 'Midwest', 'West', 'Small']
GROUP_COLORS = {
    'Union': 'MediumBlue',
    'Confederate': 'Red', 
    'Border': 'DarkSalmon', 
    'Post-War': 'Green', 
    'Northeast': 'MediumBlue',
    'South': 'Maroon', 
    'Midwest': 'Cyan',
    'West': 'SpringGreen',
    'Small': 'Gold', 
}

# parties
PARTIES = ['Democrat', 'Republican', 'Whig', 'Whig-Harrison', 'Whig-White', 'Whig-Webster', 'National Republican', 
        'Anti-Masonic', 'Constitutional Union', 'American', 'Democrat-Breckenridge', 'Democrat-Douglas', 
        'Democrat-Unpledged', 'Populist', 'Progressive', 'Dixiecrat', 'American Independent']

PARTY_COLORS = {
    'Democrat': 'Blue', 
    'Republican': 'Red', 
    'Whig': 'Orange',
    'Whig-Harrison': 'OrangeRed',
    'Whig-White': 'Tomato',
    'Whig-Webster': 'DarkOrange', 
    'National Republican': 'Crimson',
    'Anti-Masonic': 'ForestGreen',
    'Constitutional Union': 'Green',
    'American': 'SpringGreen',
    'Democrat-Breckenridge': 'LightBlue',
    'Democrat-Douglas': 'DodgerBlue',
    'Democrat-Unpledged': 'Cyan',
    'Populist': 'SeaGreen', 
    'Progressive': 'DarkGreen',
    'Dixiecrat': 'DarkTurquoise',
    'American Independent': 'LightSkyBlue',
}

# columns
COL_ABBREV = 'Abbrev'
COL_STATE = 'State'
COL_ACW_GROUP = 'Civil War Grouping'
COL_CENSUS_GROUP = 'Census Grouping'
COL_GROUP = 'Group'
COL_YEAR = 'Year'
COL_EC_VOTES = 'EC votes'
COL_EC_VOTES_NORM = 'EC votes normalized'
COL_VOTES_COUNTED = 'Votes counted'
COL_VOTES_COUNTED_NORM = 'Votes counted normalized'
COL_VOTES_COUNTED_PCT = 'Votes counted %'
COL_VOTE_WEIGHT = 'Vote weight'
COL_LOG_VOTE_WEIGHT = 'Vote weight (log)'
COL_AVG_WEIGHT = 'Average weight'
COL_PARTY = 'Party'
COL_POP_PER_EC = 'Population per EC vote'
COL_POP_PER_EC_SHORT = 'Pop per EC vote'
COL_STATE_COUNT = 'State count'
COL_MOST_EC_VOTES = 'Most EC votes'
COL_STATES_IN_GROUP = 'States in group'


# animations
FRAME_RATE = 1000
