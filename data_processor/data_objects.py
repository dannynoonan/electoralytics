import pandas as pd

from metadata import BASE_DATA_DIR, PIVOT_ON_YEAR_CSV


PIVOT_ON_YEAR_CSV = f"{BASE_DATA_DIR}/{PIVOT_ON_YEAR_CSV}"


class DataObject():

    def __init__(self):
        self.pivot_on_year_df = None
        self.melted_pivot_on_year_df = None
        self.all_years = None

    # load pivot_on_year data from csv
    def load_pivot_on_year(self):
        print(f'loading {PIVOT_ON_YEAR_CSV}')

        self.pivot_on_year_df = pd.read_csv(PIVOT_ON_YEAR_CSV)
        self.pivot_on_year_df.drop('Unnamed: 0', axis=1, inplace=True)
        # rename pop per EC vote
        self.pivot_on_year_df.rename(columns={'Population per EC vote': 'Pop per EC vote'}, inplace=True)

        # extract valid election years (for request validation)
        self.all_years = self.pivot_on_year_df['Year'].unique()

    def melt_pivot_on_year(self):
        print(f'melting {PIVOT_ON_YEAR_CSV}')

        pivot_on_year_mod = self.pivot_on_year_df.rename(
            columns={'EC votes': 'EC votes: Actual', 'EC votes normalized': 'ECV: Adjusted for population'})

        self.melted_pivot_on_year_df = pd.melt(
            pivot_on_year_mod, 
            id_vars=['Abbrev', 'State', 'Group', 'Year', 'Votes counted', 'Votes counted %', 'Pop per EC vote',
                    'Vote weight', 'Party'],
            var_name='Actual vs Adjusted EC votes^',
            value_name='EC votes^'
        )
