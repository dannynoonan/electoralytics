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


# data files
class DataFiles():
    def __init__(self):
        data_dirs = DataDirs()
        # source files
        self.THE_ONE_RING = f'{data_dirs.BASE}/theOneRing.csv'
        self.SWALLOWED_VOTE_2020 = f'{data_dirs.BASE}/swallowedVoteSampler2020.csv'
        self.TOTALS_BY_YEAR = f'{data_dirs.BASE}/totalsByYear.csv'
        # generated files
        self.STATE_VOTE_WEIGHTS_PIVOT = 'stateVoteWeightsPivot.csv'
        self.STATE_SWING_WEIGHTS_PIVOT = 'stateSwingWeightsPivot.csv'
        self.GROUP_AGG_WEIGHTS_PIVOT = 'groupAggWeightsPivot.csv'
        self.AVG_WEIGHT_BY_YEAR = 'avgWeightByYear.csv'


# columns in data files
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
        self.VOTES_COUNTED_PCT_TOTAL_POP = 'Votes counted as % of total population'
        self.TOTAL_POP = 'Total population'
        self.STATE_COUNT = 'State count'
        self.STATES_IN_GROUP = 'States in group'
        self.MOST_EC_VOTES = 'Most EC votes'


# figure dimensions
class FigDimensions():
    def __init__(self):
        self.MD5 = 660
        self.MD6 = 800
        self.MD7 = 940
        self.MD8 = 1080
        self.MD12 = 1640

    def square(self, width):
        return width

    def crt(self, width):
        return width * .75

    def wide_door(self, width):
        return width * 1.25


data_dirs = DataDirs()


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
        'Democrat-Unpledged', 'Populist', 'Progressive', 'Dixiecrat', 'American Independent', 'split']

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
    'split': 'Gray'
}

COLORS_PLOTLY = [
    '#636EFA',
    '#FECB52',
    '#00CC96',
    '#AB63FA',
    '#FFA15A',
    '#19D3F3',
    '#FF6692',
    '#B6E880',
    '#FF97FF',
    '#EF553B'
]

# years
YEAR_0 = 1824
YEAR_N = 2020

# animations
FRAME_RATE = 1000
