# Standard library imports
from os import getcwd
from os.path import join
from pathlib import Path

class PathFinder():
    def __init__(self):
        self.__getInputOutputDirectories()

    def __getInputOutputDirectories(self):
        # Get to csv's directory
        currentPath = Path(getcwd())
        dataDir = join(currentPath.parent.absolute(), 'data')
        originalCsvsDir = join(dataDir, 'original')
        # Input csvs directories
        self.countriesDir = join(originalCsvsDir, 'countries')
        self.statsDir = join(originalCsvsDir, 'stats')
        self.indicatorsDir = join(originalCsvsDir, 'indicators')
        # Output directory
        self.outputDir = join(dataDir, 'final')