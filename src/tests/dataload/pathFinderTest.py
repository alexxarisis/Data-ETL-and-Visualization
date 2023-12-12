# Standard library imports
from os import getcwd
from os.path import join
from pathlib import Path

# Local application imports
from dataload.pathFinder import PathFinder

def runTests():
    pathFinder = PathFinder()
    dbmsDirectory = Path(getcwd()).parent
    countriesDirectory = join(dbmsDirectory, 'data\original\countries')
    statsDirectory = join(dbmsDirectory, 'data\original\stats')
    indicatorsDirectory = join(dbmsDirectory, 'data\original\indicators')
    outputDirectory = join(dbmsDirectory, 'data\\final')
    
    countriesDirectoryTest(countriesDirectory, pathFinder)
    statsDirectoryTest(statsDirectory, pathFinder)
    indicatorsDirectoryTest(indicatorsDirectory, pathFinder)
    outputFilesDirectoryTest(outputDirectory, pathFinder)
    return pathFinder

def countriesDirectoryTest(countriesDirectory, pathFinder):
    assert countriesDirectory == pathFinder.countriesDir, "PathFinder: Countries data directory not found or is wrong"

def statsDirectoryTest(statsDirectory, pathFinder):
    assert statsDirectory == pathFinder.statsDir, "PathFinder: Stats data directory not found or is wrong"

def indicatorsDirectoryTest(indicatorsDirectory, pathFinder):
    assert indicatorsDirectory == pathFinder.indicatorsDir, "PathFinder: Indicators data directory not found or is wrong"

def outputFilesDirectoryTest(outputDirectory, pathFinder):
    assert outputDirectory == pathFinder.outputDir, "PathFinder: Output data directory not found or is wrong"