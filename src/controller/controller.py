
class Controller:
    def __init__(self, dbConnector, dataFormatter, plotMaker):
        self.dbConnector = dbConnector
        self.dataFormatter = dataFormatter
        self.plotMaker = plotMaker

    def getIndicators(self):
        return self.dbConnector.getIndicators()

    def getCountries(self):
        return self.dbConnector.getCountries()

    def getYears(self):
        return self.dbConnector.getYears()

    def makeTimelinePlot(self, indicators, countries, fromYear, toYear, perYears):
        # data
        data =  self.dataFormatter.getBarOrTimelineData(indicators, countries,
                                                        fromYear, toYear, perYears)
        # plot
        self.plotMaker.makeTimelinePlot(data)

    def makeBarPlot(self, indicators, countries, fromYear, toYear, perYears):
        #data
        data =  self.dataFormatter.getBarOrTimelineData(indicators, countries,
                                                        fromYear, toYear, perYears)
        # plot
        self.plotMaker.makeBarPlot(data)

    def makeScatterPlot(self, indicators, countries, fromYear, toYear, perYears):
        # data
        data = self.dataFormatter.getScatterData(indicators, countries,
                                                        fromYear, toYear, perYears)
        # plot
        self.plotMaker.makeScatterPlot(data, countries, toYear)