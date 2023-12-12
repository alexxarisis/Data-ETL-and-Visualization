# Standard library imports
from os import listdir
from os.path import join

# Third party imports
import pandas as pd

# Local application imports
import settings

class CsvWriter:
    def __init__(self, pathFinder):
        # list of countries, in the order read
        self.countries = []
        self.pathFinder = pathFinder

    def createCsvs(self):
        print('CsvWriter: ')
        print('\tCreating csv\'s...', end=" ")
        self.__createCountriesCsv()
        self.__createStatsCsv()
        self.__createIndicatorsCsv()
        print('Done')

    def __createCountriesCsv(self):
        finalDf = pd.DataFrame()
        for filename in listdir(self.pathFinder.countriesDir):
            df = pd.read_csv(join(self.pathFinder.countriesDir, filename))
            finalDf = pd.concat([finalDf, df])

        # Drop unnecessary columns 
        finalDf = finalDf.drop(['Unnamed: 5', 'Unnamed: 4'], axis=1)
        # save countries code in order read
        self.countries = finalDf['Country Code'].to_list()
        # Export
        self.__exportToCsv(finalDf, settings.countriesCsv)

    def __createStatsCsv(self):
        finalDf = pd.DataFrame()

        for filename in listdir(self.pathFinder.statsDir):
            df = pd.read_csv(join(self.pathFinder.statsDir, filename), skiprows=4)
            # Get specific ID of country based on country code
            code = df['Country Code'].drop_duplicates().loc[0]
            id = self.countries.index(code) + 1

            # Invert dataframe and drop unnessecary columns
            df = df.T
            df = df.drop(['Country Name', 'Country Code', 'Indicator Name', 'Unnamed: 65'])
            # Name headers based on each 'Indicator Code'
            df = df.rename(columns=df.iloc[0]).drop(df.index[0])
            # Make Years from index to a column
            df = df.reset_index()
            df = df.rename(columns={'index': 'Year'})

            # Keep only codes starting with the given strings
            wantedColumns = ('Year', 'BM', 'EG', 'GC.TAX')
            columnFilter = [col for col in df if col.startswith(wantedColumns)]
            df = df[columnFilter]

            # insert ID column based on country code
            df.insert(0, 'Country ID', id)
            finalDf = pd.concat([finalDf, df])
        # Export
        self.__exportToCsv(finalDf, settings.statsCsv)

    def __createIndicatorsCsv(self):
        finalDf = pd.DataFrame()

        for filename in listdir(self.pathFinder.indicatorsDir):
            df = pd.read_csv(join(self.pathFinder.indicatorsDir, filename))
            df = df.drop(['Unnamed: 4'], axis = 1)
            finalDf = pd.concat([finalDf, df])

        # Keep specified non-duplicated columns
        finalDf = finalDf.drop_duplicates()
        finalDf = finalDf[finalDf['INDICATOR_CODE'].str.startswith('BM') | 
                            finalDf['INDICATOR_CODE'].str.startswith('EG') |
                            finalDf['INDICATOR_CODE'].str.startswith('GC.TAX') ]
        # Export
        self.__exportToCsv(finalDf, settings.indicatorsCsv)

    def __exportToCsv(self, df, outputFileName):
        df.to_csv(join(self.pathFinder.outputDir, outputFileName), na_rep='NULL', index = False)