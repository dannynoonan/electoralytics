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

# historical events/eras/descriptions 
EVENTS = [
    {'year': 1788, 'name': 'Nation\'s founding', 'desc': 'State legislatures/property-owning white males can vote'},
    # {'year': 1800, 'name': 'Jeffersonian democracy'},
    {'year': 1828, 'name': 'Jacksonian democracy begins', 'desc': 'Most tax/property-based voting restrictions eliminated'},
    # {'year': 1857, 'name': 'Dred Scott v Sandford'},
    {'year': 1861, 'name': '11 of 15 slave states secede, Civil War begins'},
    # {'year': 1863, 'name': 'Emancipation Proclamation'},
    {'year': 1865, 'name': 'Civil War ends, 13th Amendment', 'desc': 'Slavery abolished'},
    # {'year': 1868, 'name': '14th Amendment'},
    {'year': 1870, 'name': '15th Amendment', 'desc': 'Black male suffrage'},
    {'year': 1877, 'name': 'Compromise of 1877', 'desc': 'Federal troops leave South, \'Redeemer\' govts take power'},
    {'year': 1887, 'name': 'Dawes Act', 'desc': 'Suffrage to Native Americans who leave tribes'},
    {'year': 1896, 'name': 'Plessy v Ferguson:', 'desc': '\'Separate but equal\' segregation in the South'},
    # {'year': 1915, 'name': 'Second KKK reborn in Georgia'},
    {'year': 1920, 'name': '19th Amendment', 'desc': 'Women\'s suffrage'},
    # {'year': 1921, 'name': 'Tulsa race massacre'},
    {'year': 1924, 'name': 'Indian Citizenship Act', 'desc': 'Suffrage to Native Americans'},
    # {'year': 1925, 'name': 'KKK peak membership at 4-5 million (15% of eligible population)'},
    # {'year': 1932, 'name': 'Tuskegee Syphilis Study'},
    {'year': 1943, 'name': 'Magnuson Act', 'desc': 'Suffrage to Chinese immigrants'},
    {'year': 1954, 'name': 'Brown v Board of Education'},
    # {'year': 1955, 'name': 'Emmett Till lynching, Montgomery bus boycott'},
    # {'year': 1960, 'name': 'Sit-ins'},
    # {'year': 1961, 'name': '23rd Amendment', 'desc': 'Washington DC citizens can vote for President'}, 
    # {'year': 1964, 'name': 'Civil Rights Act, 24th Amendment abolishes poll taxes'}, 
    {'year': 1965, 'name': 'Voting Rights Act', 'desc': 'Voting protections for racial minorities'},
    {'year': 1971, 'name': '26th Amendment', 'desc': 'Suffrage extended to 18-year-olds'},
    {'year': 2006, 'name': 'Voting Rights Act extended for last time'},
    {'year': 2013, 'name': 'Shelby County v Holder', 'desc': 'Voting Rights Act loses oversight power'},
]

ERAS = [
    {'begin': 1788, 'end': 1861, 'name': 'Antebellum Period', 'color': '#636EFA'},
    {'begin': 1861, 'end': 1865, 'name': 'Civil War', 'color': '#FECB52'},
    {'begin': 1865, 'end': 1877, 'name': 'Reconstruction', 'color': '#00CC96'},
    {'begin': 1877, 'end': 1896, 'name': 'Redemption', 'color': '#AB63FA'},
    {'begin': 1896, 'end': 1954, 'name': 'Jim Crow Era', 'color': '#FFA15A'},
    {'begin': 1954, 'end': 1965, 'name': 'Civil Rights Era', 'color': '#19D3F3'},
    {'begin': 1965, 'end': YEAR_N, 'name': 'Post Voting Rights Act', 'color': '#FF6692'},
]
