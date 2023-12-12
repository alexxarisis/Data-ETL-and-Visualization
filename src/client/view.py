# Standard library imports
from functools import partial
from re import search
import sys

# Third party imports
from PyQt5 import QtCore, QtGui, QtWidgets

class ClientView(object):
    def __init__(self, controller):
        app = QtWidgets.QApplication(sys.argv)

        self.initializeValues(controller)
        self.setupIndicators()
        self.setupCountries()
        self.setupYears()
        self.setupPlotArea()
        self.decorateUI()
        self.updateButtons()
        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self.Dialog)
        self.Dialog.show()
        sys.exit(app.exec_())

    def initializeValues(self, controller):
        # Gui related
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(1115, 830)
        self.translate = QtCore.QCoreApplication.translate
        # Variables
        self.controller = controller
        self.selectedIndicators = []
        self.selectedCountries = []

    def setupIndicators(self):
        # Create Vertical Layout containing all checkboxes
        self.indicatorsLayout = QtWidgets.QVBoxLayout()
        for indicator in self.controller.getIndicators():
            checkBox = QtWidgets.QCheckBox()
            checkBox.setText(self.translate("Dialog", indicator))
            checkBox.stateChanged.connect(partial(self.indicatorStateChanged, checkBox))
            self.indicatorsLayout.addWidget(checkBox)

        # Widget containing the checkboxes
        self.indicatorsWidget = QtWidgets.QWidget()
        self.indicatorsWidget.setGeometry(QtCore.QRect(0, 0, 472, 729))
        self.indicatorsWidget.setObjectName("indicatorsWidget")
        self.indicatorsWidget.setLayout(self.indicatorsLayout)
        # Scroll Area Properties
        self.indicatorsScrollArea = QtWidgets.QScrollArea(self.Dialog)
        self.indicatorsScrollArea.setGeometry(QtCore.QRect(20, 80, 450, 700))
        self.indicatorsScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.indicatorsScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.indicatorsScrollArea.setWidgetResizable(True)
        self.indicatorsScrollArea.setObjectName("indicatorsScrollArea")
        self.indicatorsScrollArea.setWidget(self.indicatorsWidget)
        # Add label
        self.chooseIndLabel = QtWidgets.QLabel(self.Dialog)
        self.chooseIndLabel.setGeometry(QtCore.QRect(20, 50, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.chooseIndLabel.setFont(font)
        self.chooseIndLabel.setObjectName("chooseIndLabel")

    def setupCountries(self):
        # Create Vertical Layout containing all checkboxes
        self.countriesLayout = QtWidgets.QVBoxLayout()
        for country_name in self.controller.getCountries():
            checkBox = QtWidgets.QCheckBox()
            checkBox.setText(self.translate("Dialog", country_name))
            checkBox.stateChanged.connect(partial(self.countryStateChanged, checkBox))
            self.countriesLayout.addWidget(checkBox)

        # Widget containing the checkboxes
        self.countriesWidget = QtWidgets.QWidget()
        self.countriesWidget.setGeometry(QtCore.QRect(0, 0, 452, 289))
        self.countriesWidget.setObjectName("countriesWidget")
        self.countriesWidget.setLayout(self.countriesLayout)
        # Scroll Area Properties
        self.countriesScrollArea = QtWidgets.QScrollArea(self.Dialog)
        self.countriesScrollArea.setGeometry(QtCore.QRect(580, 220, 471, 291))
        self.countriesScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.countriesScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.countriesScrollArea.setWidgetResizable(True)
        self.countriesScrollArea.setObjectName("countriesScrollArea")
        self.countriesScrollArea.setWidget(self.countriesWidget)

        # Add label
        self.chooseCountriesLabel = QtWidgets.QLabel(self.Dialog)
        self.chooseCountriesLabel.setGeometry(QtCore.QRect(580, 180, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.chooseCountriesLabel.setFont(font)
        self.chooseCountriesLabel.setObjectName("chooseCountriesLabel")

    def setupYears(self):
        # Labels
        self.toYearLabel = QtWidgets.QLabel(self.Dialog)
        self.toYearLabel.setGeometry(QtCore.QRect(750, 90, 21, 16))
        self.toYearLabel.setObjectName("toYearLabel")
        self.fromYearLabel = QtWidgets.QLabel(self.Dialog)
        self.fromYearLabel.setGeometry(QtCore.QRect(580, 90, 31, 16))
        self.fromYearLabel.setObjectName("fromYearLabel")
        self.perYearsLabel = QtWidgets.QLabel(self.Dialog)
        self.perYearsLabel.setGeometry(QtCore.QRect(900, 90, 21, 16))
        self.perYearsLabel.setObjectName("perYearsLabel")
        self.chooseYearsLabel = QtWidgets.QLabel(self.Dialog)
        self.chooseYearsLabel.setGeometry(QtCore.QRect(580, 50, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.chooseYearsLabel.setFont(font)
        self.chooseYearsLabel.setObjectName("chooseYearsLabel")
    
        # Combo boxes
        self.fromYearComboBox = QtWidgets.QComboBox(self.Dialog)
        self.fromYearComboBox.setGeometry(QtCore.QRect(610, 90, 91, 20))
        self.fromYearComboBox.setObjectName("fromYearComboBox")
        self.toYearComboBox = QtWidgets.QComboBox(self.Dialog)
        self.toYearComboBox.setGeometry(QtCore.QRect(770, 90, 91, 20))
        self.toYearComboBox.setObjectName("toYearComboBox")
        self.perYearCombobox = QtWidgets.QComboBox(self.Dialog)
        self.perYearCombobox.setGeometry(QtCore.QRect(930, 90, 91, 20))
        self.perYearCombobox.setObjectName("perYearCombobox")

        # Assign values
        years = list(map(str, self.controller.getYears()))
        self.fromYearComboBox.addItems(years)
        self.toYearComboBox.addItems(years)
        self.toYearComboBox.setCurrentText(years[-1])
        self.perYearCombobox.addItems(['1 Year', '5 Years', '10 Years'])

        # Events
        self.fromYearComboBox.currentTextChanged.connect(self.updateButtons)
        self.toYearComboBox.currentTextChanged.connect(self.updateButtons)
        self.perYearCombobox.currentTextChanged.connect(self.updateButtons)

    def setupPlotArea(self):
        # Label
        self.plotLabel = QtWidgets.QLabel(self.Dialog)
        self.plotLabel.setGeometry(QtCore.QRect(680, 600, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.plotLabel.setFont(font)
        self.plotLabel.setObjectName("plotLabel")

        # Pushbuttons
        self.timelinePushbutton = QtWidgets.QPushButton(self.Dialog)
        self.timelinePushbutton.setGeometry(QtCore.QRect(770, 660, 121, 21))
        self.timelinePushbutton.setObjectName("timelinePushbutton")
        self.timelinePushbutton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.barPushbutton = QtWidgets.QPushButton(self.Dialog)
        self.barPushbutton.setGeometry(QtCore.QRect(770, 690, 121, 21))
        self.barPushbutton.setObjectName("barPushbutton")
        self.barPushbutton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scatterPushbutton = QtWidgets.QPushButton(self.Dialog)
        self.scatterPushbutton.setGeometry(QtCore.QRect(770, 720, 121, 21))
        self.scatterPushbutton.setObjectName("scatterPushbutton")
        self.scatterPushbutton.setFocusPolicy(QtCore.Qt.NoFocus)

        # Events
        self.timelinePushbutton.clicked.connect(self.timelinePlotClicked)
        self.barPushbutton.clicked.connect(self.barPlotClicked)
        self.scatterPushbutton.clicked.connect(self.scatterPlotClicked)

    def decorateUI(self):
        # lines
        self.line = QtWidgets.QFrame(self.Dialog)
        self.line.setGeometry(QtCore.QRect(550, 540, 561, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.Dialog)
        self.line_2.setGeometry(QtCore.QRect(530, 50, 31, 791))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.Dialog)
        self.line_3.setGeometry(QtCore.QRect(550, 140, 561, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

    def retranslateUi(self):
        self.Dialog.setWindowTitle(self.translate("Dialog", "Data ETL and Visualization"))
        self.toYearLabel.setText(self.translate("Dialog", "To:"))
        self.fromYearLabel.setText(self.translate("Dialog", "From:"))
        self.chooseIndLabel.setText(self.translate("Dialog", "Choose indicators:"))
        self.chooseYearsLabel.setText(self.translate("Dialog", "Choose years:"))
        self.perYearsLabel.setText(self.translate("Dialog", "Per:"))
        self.chooseCountriesLabel.setText(self.translate("Dialog", "Choose countries:"))
        self.plotLabel.setText(self.translate("Dialog", "Choose an available type of plot:"))
        self.timelinePushbutton.setText(self.translate("Dialog", "Timeline"))
        self.barPushbutton.setText(self.translate("Dialog", "Bar"))
        self.scatterPushbutton.setText(self.translate("Dialog", "Scatter"))

    ######## On click events ########
    def indicatorStateChanged(self, checkBox):
        if (checkBox.isChecked()):
            self.selectedIndicators.append(checkBox.text())
        else:
            self.selectedIndicators.remove(checkBox.text())
        self.updateButtons()

    def countryStateChanged(self, checkBox):
        if (checkBox.isChecked()):
            self.selectedCountries.append(checkBox.text())
        else:
            self.selectedCountries.remove(checkBox.text())
        self.updateButtons()

    # PushButtons on/off
    def updateButtons(self):
        self.__updateTimelineButton()
        self.__updateBarButton()
        self.__updateScatterButton()

    def __isInvalidYearRange(self):
        return (
            int(self.fromYearComboBox.currentText()) >
            int(self.toYearComboBox.currentText()))

    def __updateTimelineButton(self):
        if (not self.selectedIndicators or not self.selectedCountries or
                self.__isInvalidYearRange()):
            self.timelinePushbutton.setDisabled(True)
            return

        self.timelinePushbutton.setEnabled(True)

    def __updateBarButton(self):
        if (not self.selectedIndicators or not self.selectedCountries or
                self.__isInvalidYearRange()):
            self.barPushbutton.setDisabled(True)
            return

        self.barPushbutton.setEnabled(True)

    def __updateScatterButton(self):
        if (not self.selectedIndicators or self.__isInvalidYearRange()):
            self.scatterPushbutton.setDisabled(True)
            return

        fromYear = int(self.fromYearComboBox.currentText())
        toYear = int(self.toYearComboBox.currentText())
        yearDifference = toYear - fromYear
        
        if (len(self.selectedIndicators) != 2 or
            (len(self.selectedCountries) != 1 and yearDifference != 0) or
            (len(self.selectedCountries) != 0 and yearDifference == 0)):
                self.scatterPushbutton.setDisabled(True)
                return
        
        self.scatterPushbutton.setEnabled(True)

    ## Displaying plots
    def timelinePlotClicked(self):
        self.controller.makeTimelinePlot(
                        self.selectedIndicators,
                        self.selectedCountries,
                        int(self.fromYearComboBox.currentText()),
                        int(self.toYearComboBox.currentText()),
                        int(search(r'\d+', 
                            self.perYearCombobox.currentText()).group())
                        )

    def barPlotClicked(self):
        self.controller.makeBarPlot(
                        self.selectedIndicators,
                        self.selectedCountries,
                        int(self.fromYearComboBox.currentText()),
                        int(self.toYearComboBox.currentText()),
                        int(search(r'\d+', 
                            self.perYearCombobox.currentText()).group())
                        )

    def scatterPlotClicked(self):
        self.controller.makeScatterPlot(
                        self.selectedIndicators,
                        self.selectedCountries,
                        int(self.fromYearComboBox.currentText()),
                        int(self.toYearComboBox.currentText()),
                        int(search(r'\d+', 
                            self.perYearCombobox.currentText()).group())
                        )