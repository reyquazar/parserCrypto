from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.QtCore import QThread, QObject
from PyQt5.QtGui import QColor
from Gui_MainWindowSample import Ui_CryptoProject
from main_async import main
import os
import sys
import logging
import json


def init_logger(name):
    logger = logging.getLogger(name)
    FORMAT = "%(asctime)s -- %(name)s -- %(lineno)s -- %(levelname)s -- %(message)s"
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(FORMAT))
    sh.setLevel(logging.DEBUG)
    fh = logging.FileHandler(filename="Logs.txt", encoding="UTF-8")
    fh.setFormatter(logging.Formatter(FORMAT))
    fh.setLevel(logging.DEBUG)
    logger.addHandler(sh)
    logger.addHandler(fh)
    logger.debug('logger was initialized')

init_logger('parserCrypto')
logger = logging.getLogger('parserCrypto.ParserCryptoGui')

class ParserCryptoGui(QMainWindow):
    """Класс-обертка для основного окна приложения"""
    path = os.getcwd().replace('\\', '\\\\') + '\\\\'  # директория, из которой запускается программа
    pathImg = path.replace("\\", '/')
    selectedQuotationCoin = 'Bitcoin'
    selectedBasicCoin = 'RUB'
    circularRefreshOn = False
    refreshTime = 0
    startParsButtonClicked = False
    unfilledRowNumber = 0

    def __init__(self):
        super(ParserCryptoGui, self).__init__()
        self.ui = Ui_CryptoProject()
        self.ui.setupUi(self)

        self.ui.treeWidget_siteList.setStyleSheet(f"background-image: url({ParserCryptoGui.pathImg}/img/SiteTreeBackground.png)")
        self.ui.frame_settingPanelImg.setStyleSheet(f"background-image: url({ParserCryptoGui.pathImg}/img/SettingsFone.bmp)")
        self.ui.icon = QtGui.QIcon()
        self.ui.icon.addPixmap(QtGui.QPixmap(f"url({ParserCryptoGui.pathImg}/img/Logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.add_guiFunctions()

    def add_guiFunctions(self):
        self.ui.pushButton_enableCoinChoice.clicked.connect(self.enableCoinChoice)
        self.ui.checkBox_circularRefresh.clicked.connect(self.circularRefreshSwitcher)
        self.ui.checkBox_allCoinsRender.clicked.connect(self.allCoinsRenderSwitcher)
        self.ui.pushButton_loadSiteData.clicked.connect(self.startParsingThread)
        self.ui.pushButton_coinSearch.clicked.connect(self.startCoinSearch)
        self.ui.pushButton_addNewCoin.clicked.connect(self.addNewCoin)
        self.ui.pushButton_deleteCoin.clicked.connect(self.deleteCoin)

    def enableCoinChoice(self):
        self.selectedQuotationCoin = self.ui.comboBox_quotationCoin.currentText()
        self.selectedBasicCoin = self.ui.comboBox_basicCoin.currentText()

    def circularRefreshSwitcher(self):
        if self.ui.checkBox_circularRefresh.isChecked():
            self.ui.label_refreshTime.setDisabled(False)
            self.ui.spinBox_refreshTime.setDisabled(False)
            self.ui.pushButton_EnableRefreshTime.setDisabled(False)
            ParserCryptoGui.circularRefreshOn = True
            ParserCryptoGui.refreshTime = self.ui.spinBox_refreshTime.value()
            if self.startParsButtonClicked:
                self.startParsingThread()
        else:
            self.ui.label_refreshTime.setDisabled(True)
            self.ui.spinBox_refreshTime.setDisabled(True)
            self.ui.pushButton_EnableRefreshTime.setDisabled(True)
            ParserCryptoGui.circularRefreshOn = False

    def allCoinsRenderSwitcher(self):
        if self.ui.checkBox_allCoinsRender.isChecked():
            self.ui.label_coinSearch.setDisabled(True)
            self.ui.lineEdit_coinSearch.setDisabled(True)
            self.ui.pushButton_coinSearch.setDisabled(True)
            self.ui.comboBox_quotationCoin.setDisabled(True)
            self.ui.label_quotationCoin.setDisabled(True)
            self.ui.pushButton_addNewCoin.setDisabled(True)
            self.ui.pushButton_deleteCoin.setDisabled(True)
        else:
            self.ui.label_coinSearch.setDisabled(False)
            self.ui.lineEdit_coinSearch.setDisabled(False)
            self.ui.pushButton_coinSearch.setDisabled(False)
            self.ui.comboBox_quotationCoin.setDisabled(False)
            self.ui.label_quotationCoin.setDisabled(False)
            self.ui.pushButton_addNewCoin.setDisabled(False)
            self.ui.pushButton_deleteCoin.setDisabled(False)

    def startParsingThread(self):
        try:
            self.startParsButtonClicked = True
            self.parsThread = ParsThread()
            self.computeThread = QThread()
            self.parsThread.moveToThread(self.computeThread)
            self.computeThread.started.connect(self.parsThread.start)
            self.parsThread.finishSignal.connect(self.computeThread.quit)
            self.parsThread.finishSignal.connect(self.renderParsResult)
            self.computeThread.start()
        except Exception as ex:
            logger.info(ex)

    def renderParsResult(self):
        try:
            cryptoMarkets = []
            cryptoMarketsData = []
            rowsCount = 0
            self.unfilledRowNumber = 0

            self.ui.tableWidget_mainResultWindow.clearContents()
            self.ui.tableWidget_mainResultWindow.setRowCount(13)

            if self.ui.treeWidget_siteList.topLevelItem(0).checkState(0) == 2:
                with open("JSON/cryptoDictMYFIN.json", "r") as file:
                    cryptoMarkets.append('MYFIN')
                    cryptoMarketsData.append(json.loads(file.read()))
            if self.ui.treeWidget_siteList.topLevelItem(1).checkState(0) == 2:
                with open("JSON/cryptoDictKUCOIN.json", "r") as file:
                    cryptoMarkets.append('KUCOIN')
                    cryptoMarketsData.append(json.loads(file.read()))
            if self.ui.treeWidget_siteList.topLevelItem(2).checkState(0) == 2:
                with open("JSON/cryptoDictCOINBASE.json", "r") as file:
                    cryptoMarkets.append('COINBASE')
                    cryptoMarketsData.append(json.loads(file.read()))

            if self.ui.checkBox_allCoinsRender.isChecked():
                for cryptoMarketData in cryptoMarketsData:
                    rowsCount += len(cryptoMarketData)
                self.ui.tableWidget_mainResultWindow.setRowCount(rowsCount)

            for cryptoMarket, cryptoMarketData in zip(cryptoMarkets, cryptoMarketsData):
                self.fillResultWindow(cryptoMarket, cryptoMarketData)
        except Exception as ex:
            logger.error(ex)

    def fillResultWindow(self, cryptoMarket, cryptoMarketData):

        def addTableItem(text):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignCenter)
            item.setText(text)
            return item
        item = addTableItem

        if not self.ui.checkBox_allCoinsRender.isChecked():  # рендеринг котировок одной выбранной криптомонеты
            self.ui.tableWidget_mainResultWindow.setItem(self.unfilledRowNumber, 0, item(cryptoMarket))
            self.ui.tableWidget_mainResultWindow.setItem(self.unfilledRowNumber, 1, item(
                f'{self.selectedQuotationCoin}/{self.selectedBasicCoin}'))
            for key in cryptoMarketData:
                if self.selectedQuotationCoin.lower() in key.lower():
                    self.ui.tableWidget_mainResultWindow.setItem(self.unfilledRowNumber, 2, item(
                        str(cryptoMarketData.get(key))))
                    self.unfilledRowNumber += 1
                    return
            self.ui.tableWidget_mainResultWindow.setItem(self.unfilledRowNumber, 2, item('Котировка отсутствует'))
            self.unfilledRowNumber += 1
        else:  # рендеринг котировок всех криптомонет
            for key in cryptoMarketData:
                self.ui.tableWidget_mainResultWindow.setItem(self.unfilledRowNumber, 0, item(cryptoMarket))
                self.ui.tableWidget_mainResultWindow.setItem(self.unfilledRowNumber, 1, item(
                    f'{key}/{self.selectedBasicCoin}'))
                self.ui.tableWidget_mainResultWindow.setItem(self.unfilledRowNumber, 2, item(
                    str(cryptoMarketData.get(key))))
                self.unfilledRowNumber += 1

    def startCoinSearch(self):
        enteredCoinName = self.ui.lineEdit_coinSearch.text()
        try:
            for row in range(self.ui.comboBox_quotationCoin.count()):
                cboxCoinName = self.ui.comboBox_quotationCoin.itemText(row).lower().replace(' ', '').replace('.', '')
                if enteredCoinName.lower().replace(' ', '').replace('.', '') in cboxCoinName or \
                        cboxCoinName in enteredCoinName.lower().replace(' ', '').replace('.', ''):
                    self.ui.comboBox_quotationCoin.setCurrentIndex(row)
                    self.selectedQuotationCoin = self.ui.comboBox_quotationCoin.currentText()
                    return
            self.ui.comboBox_quotationCoin.setCurrentText(enteredCoinName)
        except Exception as ex:
            logger.error(ex)

    def addNewCoin(self):
        try:
            j = 0
            for symbol in self.ui.lineEdit_coinSearch.text():
                j += 1
                if (symbol != '') and (symbol != ' '):
                    self.ui.comboBox_quotationCoin.addItem(self.ui.lineEdit_coinSearch.text()[j:])
                    self.ui.comboBox_quotationCoin.setCurrentIndex(self.ui.comboBox_quotationCoin.count()-1)
                    return
            self.ui.lineEdit_coinSearch.clear()
        except Exception as ex:
            logger.error(ex)

    def deleteCoin(self):
        self.model = self.ui.comboBox_quotationCoin.model()
        self.model.removeRow(self.ui.comboBox_quotationCoin.currentIndex())
        self.ui.comboBox_quotationCoin.setCurrentIndex(0)

class ParsThread(QObject):
    """Класс получения данных с сайтов криптоплощадок в отдельном потоке"""
    finishSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(ParsThread, self).__init__()

    def start(self):
        try:
            while True:
                main()
                self.finishSignal.emit()
                if not ParserCryptoGui.circularRefreshOn:
                    break
                QThread.sleep(ParserCryptoGui.refreshTime)
        except Exception as ex:
            logger.error(ex)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = ParserCryptoGui()
    w.show()
    sys.exit(app.exec_())