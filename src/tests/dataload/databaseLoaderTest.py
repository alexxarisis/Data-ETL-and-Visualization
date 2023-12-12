# Third party imports
import mysql.connector

# Local application imports
from dataload.databaseLoader import DBLoader
import settings

def runTests(pathFinder):
    DBLoader(pathFinder).loadToMySQL()
    
    cnx, cursor = connect()
    countriesTableTest(cursor)
    indicatorsTableTest(cursor)
    statsTableTest(cursor)
    cnx.close()

def connect():
    try:
        cnx = mysql.connector.connect( host = '127.0.0.1',
                                user = settings.user, 
                                password = settings.password,
                                database = settings.database)
        cursor = cnx.cursor()
    except mysql.connector.Error as e:
            print(e)
            print("DBCreatorTest: Connection not established.")
    return cnx, cursor

def countriesTableTest(cursor):
    assert getTableRowCount(cursor, 'countries') == 25, 'DBLoader: Data missing on countries table.'

def indicatorsTableTest(cursor):
    assert getTableRowCount(cursor, 'indicators') == 55, 'DBLoader: Data missing on indicators table.'

def statsTableTest(cursor):
    assert getTableRowCount(cursor, 'stats') == 1525, 'DBLoader: Data missing on stats table.'

def getTableRowCount(cursor, tablename):
    cursor.execute(
            "SELECT count(*) FROM %s" % tablename)
    return cursor.fetchone()[0]