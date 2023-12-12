# Standard library imports
from os import listdir
from os.path import join

# Third party imports
import pandas as pd

# Local application imports
import settings
from dataload.pathFinder import PathFinder
from dataload.finalCsvsWriter import CsvWriter

def runTests(pathFinder: PathFinder):
    CsvWriter(pathFinder).createCsvs()
    
    filesCreatedTest(pathFinder)
    countriesCsvTest(pathFinder)
    indicatorsCsvTest(pathFinder)
    statsCsvTest(pathFinder)

def filesCreatedTest(pathFinder):
    files = [f for f in listdir(pathFinder.outputDir)]
    assert 'countries.csv' in files, 'CsvWriter: countries.csv not found or created.'
    assert 'indicators.csv' in files, 'CsvWriter: indicators.csv not found or created.'
    assert 'stats.csv' in files, 'CsvWriter: stats.csv not found or created.'

def countriesCsvTest(pathFinder):
    countryCsv = pd.read_csv(join(pathFinder.outputDir, settings.countriesCsv))
    expectedColumnHeaders = ['Country Code', 'Region', 'IncomeGroup', 'TableName', 'SpecialNotes']
    columnHeaders = [str(x) for x in countryCsv.columns]
    assert expectedColumnHeaders == columnHeaders, 'CsvWriter: countries.csv has wrong column headers/names.'
    assert not (len(countryCsv.index) <  25), 'CsvWriter: countries.csv | Data is missing'
    assert not (len(countryCsv.index) >  25), 'CsvWriter: countries.csv | Data is more than expected'

def indicatorsCsvTest(pathFinder):
    indicatorsCsv = pd.read_csv(join(pathFinder.outputDir, settings.indicatorsCsv))
    expectedColumnHeaders = ['INDICATOR_CODE', 'INDICATOR_NAME', 'SOURCE_NOTE', 'SOURCE_ORGANIZATION']
    columnHeaders = [str(x) for x in indicatorsCsv.columns]
    assert expectedColumnHeaders == columnHeaders, 'CsvWriter: indicators.csv has wrong column headers/names.'
    assert not (len(indicatorsCsv.index) <  55), 'CsvWriter: indicators.csv | Data is missing'
    assert not (len(indicatorsCsv.index) >  55), 'CsvWriter: indicators.csv | Data is more than expected'
    
def statsCsvTest(pathFinder):
    # load indicators from the indicators'csv
    indicatorsCsv = pd.read_csv(join(pathFinder.outputDir, settings.indicatorsCsv))
    indicators = [str(x) for x in indicatorsCsv['INDICATOR_CODE']]
    # load the stats csv
    statsCsv = pd.read_csv(join(pathFinder.outputDir, settings.statsCsv))
    expectedColumnHeaders = ['Country ID', 'Year'] + indicators
    columnHeaders = [str(x) for x in statsCsv.columns]
    assert expectedColumnHeaders == columnHeaders, 'CsvWriter: stats.csv has wrong column headers/names.'
    assert not (len(statsCsv.index) <  1525), 'CsvWriter: stats.csv | Data is missing'
    assert not (len(statsCsv.index) >  1525), 'CsvWriter: stats.csv | Data is more than expected'