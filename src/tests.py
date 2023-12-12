# Standard library imports
import os, sys

# Local application imports
# dataload
from tests.dataload import (finalCsvWriterTest, 
                            databaseCreatorTest,
                            databaseLoaderTest, 
                            pathFinderTest)
# model
from tests.model import dataFormatterTest, databaseControllerTest

def runDataloadTests():
    pathFinder = pathFinderTest.runTests()
    finalCsvWriterTest.runTests(pathFinder)
    databaseCreatorTest.runTests(pathFinder)
    databaseLoaderTest.runTests(pathFinder)

def runModelTests():
    databaseControllerTest.runTests()
    dataFormatterTest.runTests()

if __name__ == "__main__":
    print('Running tests...')
    # disable printing
    original_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    # run tests
    runDataloadTests()
    runModelTests()
    # enable printing
    sys.stdout.close()
    sys.stdout = original_stdout
    print('All tests completed successfully.')