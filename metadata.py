# data dirs
BASE_DATA_DIR = 'data'
GEN_DATA_DIR = f'{BASE_DATA_DIR}/gen'
GEN_ALT_GROUP_DIR = f'{BASE_DATA_DIR}/gen_altGroup'
GEN_NO_SMALL_DIR = f'{BASE_DATA_DIR}/gen_noSmall'
GEN_ALT_GROUP_NO_SMALL_DIR = f'{BASE_DATA_DIR}/gen_altGroupNoSmall'
# data files
THE_ONE_RING_CSV = f'{BASE_DATA_DIR}/theOneRing.csv'
SWALLOWED_VOTE_2020_CSV = f'{BASE_DATA_DIR}/swallowedVoteSampler2020.csv'
GROUPS_BY_YEAR_CSV = 'groupsByYear.csv'
AVG_WEIGHT_BY_YEAR_CSV = 'avgWeightByYear.csv'
PIVOT_ON_YEAR_CSV = 'pivotOnYear.csv'
TOTALS_BY_YEAR_CSV = 'totalsByYear.csv'
GROUP_AGGS_BY_YEAR_CSV = 'groupAggsByYear.csv'


# state groupings
GROUPS = ['Small', 'Confederate', 'Border', 'Northeast', 'Midwest', 'West']
ALT_GROUPS = ['Small', 'Confederate', 'Border', 'Union', 'West']


# columns
COL_ABBREV = 'Abbrev'
COL_STATE = 'State'
COL_GROUP = 'Group'
COL_ALT_GROUP = 'Alt Group'
COL_YEAR = 'Year'
COL_EC_VOTES = 'EC votes'
COL_EC_VOTES_NORM = 'EC votes normalized'
COL_VOTES_COUNTED = 'Votes counted'
COL_VOTES_COUNTED_PCT = 'Votes counted %'
COL_VOTE_WEIGHT = 'Vote weight'
COL_AVG_WEIGHT = 'Average weight'
COL_PARTY = 'Party'
COL_POP_PER_EC = 'Population per EC vote'
COL_POP_PER_EC_SHORT = 'Pop per EC vote'
COL_STATE_COUNT = 'State count'
COL_MOST_EC_VOTES = 'Most EC votes'
COL_STATES_IN_GROUP = 'States in group'
