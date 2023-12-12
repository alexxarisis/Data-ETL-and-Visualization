# Local application imports
from model.databaseConnector import DatabaseConnector

def runTests():
    dbConnector = DatabaseConnector()
    getAllYearsTest(dbConnector)
    getRangeOfYearsTest(dbConnector)
    getAllCountriesTest(dbConnector)
    getAllIndicatorsTest(dbConnector)
    selectBasedOnMultipleVariablesTest(dbConnector)
    selectBasedOnYearTest(dbConnector)

def getAllYearsTest(dbConnector):
    expectedYears = list(range(1960, 2021))
    allYears = dbConnector.getYears()
    assert allYears == expectedYears, "DatabaseConnector: Some years are missing"

def getRangeOfYearsTest(dbConnector):
    expectedYears = list(range(2000, 2011))
    years = dbConnector.getYearsInRange(2000, 2010)
    assert years == expectedYears, "DatabaseConnector: Some years in range are missing"

def getAllCountriesTest(dbConnector):
    countries = dbConnector.getCountries()
    expectedCountries = ['Angola', 'Argentina', 'Australia', 
                'Austria', 'Bangladesh', 'Brazil', 'Cameroon', 
                'Colombia', 'Cuba', 'Ecuador', 'Egypt, Arab Rep.', 
                'Fiji', 'Greece', 'India', 'Japan', 'Netherlands', 
                'Poland', 'Portugal', 'Russian Federation', 
                'Singapore', 'Spain', 'Sweden', 'Thailand', 
                'Uruguay', 'Venezuela, RB']
    assert countries == expectedCountries, "DatabaseConnector: Some countries are missing or wrong"

def selectBasedOnMultipleVariablesTest(dbConnector):
    data = dbConnector.selectBasedOnMultipleVariables(
        'Alternative and nuclear energy (% of total energy use)', 'Angola', 2000, 2002)
    expectedData = [0.873405083422169, 0.933955926843142, 1.00205331935022]
    assert data == expectedData, "DatabaseConnector: Returning data based on multiple criteria is wrong"

def selectBasedOnYearTest(dbConnector):
    data = dbConnector.selectBasedOnYear(
        'Alternative and nuclear energy (% of total energy use)', 2005)
    expectedData = [1.60962521879031, 6.42423543130273, 1.12978575094151, 
                    9.35971193459465, 0.237191873724245, 13.3373502658831, 
                    3.79673277205908, 9.78572149880052, 0.0431740774273123, 
                    5.43716613863573, 1.56398839796882, 12.692517767956, None, 
                    1.95185036099807, 2.19468590160713, 16.6844052248879, 1.92628896630913, 
                    0.211845174886823, 2.3407833754253, 7.5842606503736, 0.177019219940105, 
                    47.2381867277524, 0.462170298679137, 16.4273167099346, 7.97143615363316]
    assert data == expectedData, "DatabaseConnector: Returning data based on year is wrong"

def getAllIndicatorsTest(dbConnector):
    indicators = dbConnector.getIndicators()
    expectedIndicators = getAllExpectedIndicators()
    assert indicators == expectedIndicators, "DatabaseConnector: Some indicators are missing or wrong"

def getAllExpectedIndicators():
    return ['Access to clean fuels and technologies for cooking (% of population)', 
                'Access to electricity (% of population)', 
                'Access to electricity, rural (% of rural population)', 
                'Access to electricity, urban (% of urban population)', 
                'Alternative and nuclear energy (% of total energy use)', 
                'Charges for the use of intellectual property, payments (BoP, current US$)', 
                'Combustible renewables and waste (% of total energy)', 
                'Communications, computer, etc. (% of service imports, BoP)', 
                'Customs and other import duties (% of tax revenue)', 
                'Customs and other import duties (current LCU)', 
                'Electric power consumption (kWh per capita)', 
                'Electric power transmission and distribution losses (% of output)', 
                'Electricity production from coal sources (% of total)', 
                'Electricity production from hydroelectric sources (% of total)', 
                'Electricity production from natural gas sources (% of total)', 
                'Electricity production from nuclear sources (% of total)', 
                'Electricity production from oil sources (% of total)', 
                'Electricity production from oil, gas and coal sources (% of total)', 
                'Electricity production from renewable sources, excluding hydroelectric (% of total)', 
                'Electricity production from renewable sources, excluding hydroelectric (kWh)', 
                'Energy imports, net (% of energy use)', 
                'Energy intensity level of primary energy (MJ/$2011 PPP GDP)', 
                'Energy use (kg of oil equivalent per capita)', 
                'Energy use (kg of oil equivalent) per $1,000 GDP (constant 2017 PPP)', 
                'Foreign direct investment, net outflows (% of GDP)', 
                'Foreign direct investment, net outflows (BoP, current US$)', 
                'Fossil fuel energy consumption (% of total)', 
                'GDP per unit of energy use (constant 2017 PPP $ per kg of oil equivalent)', 
                'GDP per unit of energy use (PPP $ per kg of oil equivalent)', 
                'Goods imports (BoP, current US$)', 
                'Imports of goods and services (BoP, current US$)', 
                'Imports of goods, services and primary income (BoP, current US$)', 
                'Insurance and financial services (% of service imports, BoP)', 
                'Other taxes (% of revenue)', 'Other taxes (current LCU)', 
                'Personal remittances, paid (current US$)', 
                'Primary income payments (BoP, current US$)', 
                'Renewable electricity output (% of total electricity output)', 
                'Renewable energy consumption (% of total final energy consumption)', 
                'Secondary income, other sectors, payments (BoP, current US$)', 
                'Service imports (BoP, current US$)', 
                'Tax revenue (% of GDP)', 
                'Tax revenue (current LCU)', 
                'Taxes on exports (% of tax revenue)', 
                'Taxes on exports (current LCU)', 
                'Taxes on goods and services (% of revenue)', 
                'Taxes on goods and services (% value added of industry and services)', 
                'Taxes on goods and services (current LCU)', 
                'Taxes on income, profits and capital gains (% of revenue)', 
                'Taxes on income, profits and capital gains (% of total taxes)', 
                'Taxes on income, profits and capital gains (current LCU)', 
                'Taxes on international trade (% of revenue)', 
                'Taxes on international trade (current LCU)', 
                'Transport services (% of service imports, BoP)', 
                'Travel services (% of service imports, BoP)']