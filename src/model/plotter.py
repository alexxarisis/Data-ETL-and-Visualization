# Third party imports
import matplotlib.pyplot as plt
import pandas as pd

class PlotMaker:
    def __init__(self):
        # settings
        plt.ion()
        plt.rc('legend', fontsize=8)
        plt.rc('figure', figsize=(12,6))

    def makeTimelinePlot(self, df:pd.DataFrame):
        # get all column names except 'Years'
        indicators = list(df).remove('Years')
        # plot
        df.plot(x="Years", y=indicators)
        # removes scientific scaling
        plt.ticklabel_format(style='plain', axis='y')
        # make everything visible/fit in the figure
        plt.tight_layout()

    def makeBarPlot(self, df:pd.DataFrame):
        # get all column names except 'Years'
        indicators = list(df).remove('Years')
        # plot
        df.plot(x="Years", y=indicators, kind="bar")
        # removes scientific scaling
        plt.ticklabel_format(style='plain', axis='y')
        # make everything visible/fit in the figure
        plt.tight_layout()

    def makeScatterPlot(self, df:pd.DataFrame, countries, year):
        # get all column names
        indicators = list(df)
        # plot
        df.plot.scatter(x=indicators[0], y=indicators[1])
        # title
        if (len(countries) == 1):
            plt.title('Correlation of %s for specified years' % (countries[0]))
        else:
            plt.title('Correlation of all countries in the year %d' % (year))
        # removes scientific scaling
        plt.ticklabel_format(style='plain')
        # make everything visible/fit in the figure
        plt.tight_layout()