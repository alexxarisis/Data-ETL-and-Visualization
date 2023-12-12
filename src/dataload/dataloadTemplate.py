# Local application imports
from dataload.finalCsvsWriter import CsvWriter
from dataload.databaseCreator import DBCreator
from dataload.databaseLoader import DBLoader
from dataload.pathFinder import PathFinder

class DataLoader():
    def __init__(self):
        self.pathFinder = PathFinder()

    def createAndLoadData(self):
        CsvWriter(self.pathFinder).createCsvs()
        DBCreator(self.pathFinder).createDB()
        DBLoader(self.pathFinder).loadToMySQL()
        print('Data loaded successfully...')