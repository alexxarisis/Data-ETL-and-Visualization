# Third party imports
import pandas as pd

# Local application imports
from model.dataFormatter import DataFormatter

def runTests():
    dataFormatter = DataFormatter()
    timelineOrBarDataTest(dataFormatter)
    timelineOrBarDataPer5YearsTest(dataFormatter)
    scatterDataTest(dataFormatter)
    scatterDataAllCountriesTest(dataFormatter)

def timelineOrBarDataTest(dataFormatter):
    expectedData = pd.DataFrame()
    expectedData["Angola - Taxes on exports (current LCU)"] = [144127641.0, 86822665.0,
                                                                71152438.0, 9732844.0,
                                                                7260164.0, 10715534.0]
    expectedData["Years"]=["2005","2006","2007","2008","2009","2010"]
    data  = dataFormatter.getBarOrTimelineData(["Taxes on exports (current LCU)"],
                                                    ["Angola"], 2005, 2010, 1)
    assert data.equals(expectedData) == True, "DataFormatter: Timeline/Bar data has wrong format"

def timelineOrBarDataPer5YearsTest(dataFormatter):
    expectedData = pd.DataFrame()
    expectedData["Angola - Taxes on exports (current LCU)"] = [63819150.4, 10715534.0]
    expectedData["Years"] = ["2005-2009","2010"]
    data = dataFormatter.getBarOrTimelineData(["Taxes on exports (current LCU)"],
                                                ["Angola"], 2005, 2010, 5)
    assert data.equals(expectedData) == True, "DataFormatter: Timeline/Bar data with time aggregation has wrong format"

def scatterDataTest(dataFormatter):
    expectedData = pd.DataFrame()
    expectedData["Access to electricity, rural (% of rural population)"]=[
                                                                None, 9.477077, 2.984414, 2.567459, 2.019035, 
                                                                1.324989, 0.965577, None, 6.609394, None, None] 
    expectedData["Access to electricity, urban (% of urban population)"]=[
                                                                None, 30.000000, 47.587940, 48.980316, 50.385216, 51.809338,
                                                                53.253960, 66.100000, 61.310000, 57.668503, 73.969627]
    data = dataFormatter.getScatterData(
                    ["Access to electricity, rural (% of rural population)",
                    "Access to electricity, urban (% of urban population)"],
                    ["Angola"], 2000, 2010, 1)
    # Comparing floats can produce wrong results, even if the numbers are the same, so
    # convert numbers to 6 decimal places (even if it is already at 6, it fixes the error)
    expectedData = expectedData.round(6)
    data = data.round(6)
    assert data.equals(expectedData) == True, "DataFormatter: Scatter data of single country has wrong format"

def scatterDataAllCountriesTest(dataFormatter):
    expectedData = pd.DataFrame()
    expectedData["Access to electricity, rural (% of rural population)"] = [1.324989, 92.308199, 100.000000,
                                                                            100.000000, 30.171858, 84.830535, 15.607157,
                                                                            88.872906, 88.000751, 89.649943, 99.097913,
                                                                            100.000000 ,70.715825, 100.000000, 57.015292,
                                                                            100.000000, 100.000000, 100.000000, 100.000000,
                                                                            100.000000, 100.000000, 100.000000, 89.163561,
                                                                            84.502870, 93.327609]  
    expectedData["Access to electricity, urban (% of urban population)"] = [51.809338, 97.382217, 100.000000,
                                                                            100.000000, 82.610000, 99.634816,
                                                                            80.981430, 99.300000, 99.625237,
                                                                            99.668752, 99.800000, 100.000000,
                                                                            93.576225, 100.000000, 91.488167,
                                                                            100.000000, 100.000000, 100.000000,
                                                                            100.000000, 100.000000, 100.000000,
                                                                            100.000000, 99.449341, 99.184151, 99.700363]
    data = dataFormatter.getScatterData(
                    ["Access to electricity, rural (% of rural population)",
                    "Access to electricity, urban (% of urban population)"],
                    [], 2005, 2005, 1)
    # Comparing floats can produce wrong results, even if the numbers are the same, so
    # convert numbers to 6 decimal places (even if it is already at 6, it fixes the error)
    expectedData = expectedData.round(6)
    data = data.round(6)
    assert data.equals(expectedData) == True, "DataFormatter: Scatter data of all countries has wrong format"