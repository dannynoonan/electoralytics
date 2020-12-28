# data dirs
class DataDirs():
    def __init__(self):
        self.BASE = 'data'
        self.GEN = 'gen'
        self.ACW = 'acw'
        self.CENSUS = 'census' 
        self.NO_SMALL = 'noSmall'
        self.SMALL_3 = 'small3'
        self.SMALL_4 = 'small4'
        self.SMALL_5 = 'small5'

data_dirs = DataDirs()

# data files
THE_ONE_RING_CSV = f'{data_dirs.BASE}/theOneRing.csv'
SWALLOWED_VOTE_2020_CSV = f'{data_dirs.BASE}/swallowedVoteSampler2020.csv'
GROUPS_BY_YEAR_CSV = 'groupsByYear.csv'
AVG_WEIGHT_BY_YEAR_CSV = 'avgWeightByYear.csv'
PIVOT_ON_YEAR_CSV = 'pivotOnYear.csv'
TOTALS_BY_YEAR_CSV = 'totalsByYear.csv'
GROUP_AGGS_BY_YEAR_CSV = 'groupAggsByYear.csv'

class DataFiles():
    data_dirs = DataDirs()
    def __init__(self, data_dirs):
        self.THE_ONE_RING = f'{data_dirs.BASE}/theOneRing.csv'
        self.SWALLOWED_VOTE_2020 = f'{data_dirs.BASE}/swallowedVoteSampler2020.csv'
        self.GROUPS_BY_YEAR = 'groupsByYear.csv'
        self.AVG_WEIGHT_BY_YEAR = 'avgWeightByYear.csv'
        self.PIVOT_ON_YEAR = 'pivotOnYear.csv'
        self.TOTALS_BY_YEAR = 'totalsByYear.csv'
        self.GROUP_AGGS_BY_YEAR = 'groupAggsByYear.csv'

# state groupings
ACW_GROUPS = ['Union', 'Confederate', 'Border', 'Postbellum']
CENSUS_GROUPS = ['Northeast', 'South', 'Midwest', 'West']
GROUP_LABEL_SMALL_3 = 'Small (3 ECV)'
GROUP_LABEL_SMALL_4 = 'Small (3-4 ECV)'
GROUP_LABEL_SMALL_5 = 'Small (3-5 ECV)'
DATA_DIR_TO_SMALL_GROUP_LABELS = {
    data_dirs.SMALL_3: GROUP_LABEL_SMALL_3,
    data_dirs.SMALL_4: GROUP_LABEL_SMALL_4,
    data_dirs.SMALL_5: GROUP_LABEL_SMALL_5
}
GROUPS_FOR_DIR = {
    data_dirs.ACW: ACW_GROUPS,
    data_dirs.CENSUS: CENSUS_GROUPS
}
GROUP_COLORS_PLOTLY = {
    'Union': '#636EFA',
    'Confederate': '#FECB52',
    'Border': '#00CC96',
    'Postbellum': '#AB63FA',
    'Northeast': '#FFA15A',
    'South': '#19D3F3',
    'Midwest': '#FF6692',
    'West': '#B6E880',
    'Extra': '#FF97FF',
    'Small': '#EF553B'
}
GROUP_COLORS = {
    # ACW
    'Union': '#5378BE',
    'Confederate': '#E3B061',
    'Border': '#69B190', 
    'Postbellum': '#DC5A48',
    # Census
    'Northeast': '#19D3F3',
    # 'Northeast': '#636EFA',
    'South': '#FFA15A',
    # 'South': '#FECB52',
    'Midwest': '#00CC96',
    # 'Midwest': '#B6E880',
    'West': '#EB637A',
    # 'West': '#FF6692',
    # 'West': '#FF97FF',
    GROUP_LABEL_SMALL_3: '#AAAAAA',
    GROUP_LABEL_SMALL_4: '#AAAAAA',
    GROUP_LABEL_SMALL_5: '#AAAAAA',
    # 'Small': '#AAAAAA', # '#EF553B'
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

# columns in csv files
class Columns():
    def __init__(self):
        self.ABBREV = 'Abbrev'
        self.STATE = 'State'
        self.ACW_GROUP = 'Civil War Grouping'
        self.CENSUS_GROUP = 'Census Grouping'
        self.GROUP = 'Group'
        self.YEAR = 'Year'
        self.EC_VOTES = 'EC votes'
        self.EC_VOTES_NORM = 'EC votes normalized'
        self.VOTES_COUNTED = 'Votes counted'
        self.VOTES_COUNTED_NORM = 'Votes counted normalized'
        self.VOTES_COUNTED_PCT = 'Votes counted %'
        self.VOTE_WEIGHT = 'Vote weight'
        self.LOG_VOTE_WEIGHT = 'Vote weight (log)'
        self.AVG_WEIGHT = 'Average weight'
        self.PARTY = 'Party'
        self.POP_PER_EC = 'Population per EC vote'
        self.POP_PER_EC_SHORT = 'Pop per EC vote'
        self.STATE_COUNT = 'State count'
        self.MOST_EC_VOTES = 'Most EC votes'
        self.STATES_IN_GROUP = 'States in group'

# animations
FRAME_RATE = 1000
