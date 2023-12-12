# Third party imports
import pandas as pd

# Local application imports
from model.databaseConnector import DatabaseConnector

class DataFormatter():
    def __init__(self):
        self.dbConnector = DatabaseConnector()

    # Returns a dataframe with 1 year and multiple indicator columns
    def getBarOrTimelineData(self, indicators, countries, fromYear, toYear, perYears):
        df = pd.DataFrame()
        # populate dataFrame with values
        for indicator in indicators:
            for country in countries:
                columnName = country + ' - ' + indicator
                df[columnName] = self.dbConnector.selectBasedOnMultipleVariables(
                    indicator, country, fromYear, toYear)
        # groudby aggregated time
        if (perYears != 1):
            df = df.groupby(df.index//perYears).mean()
        # get specified years
        years = self.dbConnector.getYearsInRange(fromYear, toYear)
        years = self.__getYearsByPeriod(years, perYears)
        df['Years'] = years

        # remove rows with all NaN values (dont count 'Years' column)
        columnsToCheck = [n for n in df if n != 'Years']
        df.dropna(how='all', subset=columnsToCheck, inplace=True)
        return df
    
    # Returns a dataframe with 2 indicator columns
    def getScatterData(self, indicators, countries, fromYear, toYear, perYears):
        df = pd.DataFrame()
        # populate dataFrame with values
        for indicator in indicators:
            # Choose either values of all countries for specific year
            if (fromYear == toYear):
                df[indicator] = self.dbConnector.selectBasedOnYear(indicator, fromYear)
            # Or values of one country for range of years
            else:
                df[indicator] = self.dbConnector.selectBasedOnMultipleVariables(
                                            indicator, countries[0], fromYear, toYear)
        
        # groudby aggregated time if its on different years
        if (fromYear != toYear) and (perYears != 1):
            df = df.groupby(df.index//perYears).mean()
        return df

    def __getYearsByPeriod(self, years, yearsPeriod):
        # Return it as string, if no changes needed
        if (yearsPeriod == 1):
            return [str(x) for x in years]

        # List containing the new years
        newYears = []
        # Years in periods of 5, 10, etc...
        periods = years[::yearsPeriod]
        # Make the years' labels
        for i in periods:
            newYears.append(str(i) + '-' + str(i+yearsPeriod-1))
        # Change the last one if its the same
        if (periods[-1] == years[-1]):
            newYears[-1] = str(periods[-1])
        # or if the label is calculated wrongly
        else:
            newYears[-1] = str(periods[-1]) + '-' + str(years[-1])

        return newYears