# loading
from dataload.dataloadTemplate import DataLoader
# model
from model.databaseConnector import DatabaseConnector
from model.dataFormatter import DataFormatter
from model.plotter import PlotMaker
# controller
from controller.controller import Controller
# client
from client import view

if __name__ == '__main__':
    print('Starting ETL procedure...')
    DataLoader().createAndLoadData()
    print('Opening App...')
    myController = Controller(
        DatabaseConnector(),
        DataFormatter(), 
        PlotMaker()
    )
    view.ClientView(myController)