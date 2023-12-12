# Standard library imports
import sys

# Third party imports
import mysql.connector

# Local application imports
import settings

class DatabaseConnector:
    def __init__(self):
        self.__connect()

    def __del__(self):
        self.cnx.commit()
        self.cnx.close()
        
    def __connect(self):
        try:
            self.cnx = mysql.connector.connect( 
                                host = settings.host,
                                user = settings.user, 
                                password = settings.password,
                                port = settings.port,
                                database = settings.database
                                )
            self.cursor = self.cnx.cursor()
        except mysql.connector.Error as e:
                print(e)
                print("Connection not established.")
                sys.exit(-1)

    #### For Gui initialization ####
    def getIndicators(self):
        self.__executeQuery(
            "SELECT indicator_name FROM Indicators ORDER BY indicator_name ASC")
        return [ind[0] for ind in self.cursor.fetchall()]

    def getCountries(self):
        self.__executeQuery(
            "SELECT country_name FROM Countries ORDER BY country_name ASC")
        return [ind[0] for ind in self.cursor.fetchall()]

    def getYears(self):
        self.__executeQuery(
            "SELECT DISTINCT year FROM Stats ORDER BY year ASC")
        return [ind[0] for ind in self.cursor.fetchall()]

    #### For plots ####
    def __getCountryID(self, country_name):
        self.__executeQuery(
            "SELECT country_id FROM Countries WHERE country_name='%s'" 
            % (country_name))
        return self.cursor.fetchone()[0]

    def __getIndicatorCode(self, indicator_name):
        self.__executeQuery(
            "SELECT indicator_code FROM Indicators WHERE indicator_name='%s'" 
            % (indicator_name))
        return self.cursor.fetchone()[0].replace('.', '_').lower()

    def selectBasedOnMultipleVariables(self, indicatorName, countryName, fromYear, toYear):
        indicatorCode = self.__getIndicatorCode(indicatorName)
        countryID = self.__getCountryID(countryName)
        self.__executeQuery(
            "SELECT %s FROM Stats WHERE country_id = %d && year BETWEEN %d AND %d" 
            % (indicatorCode, countryID, fromYear, toYear))
        return [ind[0] for ind in self.cursor.fetchall()]

    def selectBasedOnYear(self, indicatorName, year):
        indicatorCode = self.__getIndicatorCode(indicatorName)
        self.__executeQuery(
            "SELECT %s FROM Stats WHERE year = %d" 
            % (indicatorCode, year))
        return [ind[0] for ind in self.cursor.fetchall()]

    def getYearsInRange(self, fromYear, toYear):
        self.__executeQuery(
            "SELECT DISTINCT year FROM Stats WHERE year BETWEEN %s AND %s" 
            % (fromYear, toYear)
            )
        return [ind[0] for ind in self.cursor.fetchall()]

    ########################
    ### STILL IN PROGRESS ###
    # bar plot

    ########################
    def __executeQuery(self, query):
        try:
            self.cursor.execute(query)
        except mysql.connector.Error as e:
            print(e)