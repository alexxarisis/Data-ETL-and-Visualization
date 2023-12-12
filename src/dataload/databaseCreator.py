# Standard library imports
from os.path import join
import csv
import sys

# Third party imports
import mysql.connector

# Local application imports
import settings

class DBCreator:
    def __init__(self, pathFinder):
        self.pathFinder = pathFinder

    def createDB(self):
        print('DBCreator: ')
        self.__connect()
        self.__createDatabase()
        self.__createTables()

        self.cnx.commit()
        self.cnx.close()

    def __connect(self):
        print('\tConnecting... ', end=' ')
        try:
            self.cnx = mysql.connector.connect( 
                                host = settings.host,
                                user = settings.user,
                                password = settings.password,
                                port = settings.port
                                )
            self.cursor = self.cnx.cursor()
        except mysql.connector.Error as e:
                print(e)
                print("Connection not established.")
                sys.exit(-1)
        print('Done')

    def __createDatabase(self):
        print('\tCreating database...', end=' ')
        self.__executeQuery('DROP DATABASE IF EXISTS `%s`' % settings.database)
        self.__executeQuery('CREATE DATABASE %s' % settings.database)
        self.__executeQuery('USE %s' % settings.database)
        print('Done')

    def __createTables(self):
        print('\tCreating tables...', end=' ')
        createCountryTableQuery = '''
            CREATE TABLE Countries(
                country_code VARCHAR(3),
                region VARCHAR(64),
                income_group VARCHAR(64),
                country_name VARCHAR(64),
                special_notes TEXT,
                country_id INT NOT NULL AUTO_INCREMENT,
                PRIMARY KEY (country_id)
            )   ENGINE=InnoDB
            '''

        createStatsTableQuery = '''
            CREATE TABLE Stats(
                country_id INT NOT NULL,
                year YEAR NOT NULL,
                PRIMARY KEY (country_id, year),
                FOREIGN KEY (country_id) REFERENCES Countries(country_id)
            '''

        for header in self.__getHeaders():
            createStatsTableQuery += ',\n %s DOUBLE' % (header)
        createStatsTableQuery += ') ENGINE=InnoDB'

        createIndicatorTableQuery = '''
            CREATE TABLE Indicators(
                indicator_code VARCHAR(32),
                indicator_name TEXT,
                source_note TEXT,
                source_organization TEXT,
                indicator_id INT NOT NULL AUTO_INCREMENT,
                PRIMARY KEY (indicator_id)
            )   ENGINE=InnoDB
        '''
        self.__executeQuery(createCountryTableQuery)
        self.__executeQuery(createStatsTableQuery)
        self.__executeQuery(createIndicatorTableQuery)
        
        print('Done')
        
    def __getHeaders(self):
        with open(join(self.pathFinder.outputDir, settings.statsCsv), newline='') as file:
            reader = csv.reader(file)
            headers = next(reader)
            formattedHeaders = [header.replace('.', '_').lower() for header in headers]
            return formattedHeaders[2:]

    def __executeQuery(self, query):
        try:
            self.cursor.execute(query)
        except mysql.connector.Error as e:
            print(e)