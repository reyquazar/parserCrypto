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
logger = logging.getLogger('parserCrypto.parserCryptoGui')

class parserCryptoGui(QMainWindow):
    """Класс-обертка для основного окна приложения"""
    path = os.getcwd().replace('\\', '\\\\') + '\\\\'  # директория, из которой запускается программа
    pathImg = path.replace("\\", '/')
    selectedQuotationCoin = 'XRP'
    selectedBasicCoin = 'USDT'

    def __init__(self):
        super(parserCryptoGui, self).__init__()
        self.ui = Ui_CryptoProject()
        self.ui.setupUi(self)

        self.ui.treeWidget_siteList.setStyleSheet(f"background-image: url({parserCryptoGui.pathImg}/img/SiteTreeBackground.png)")
        self.ui.frame_settingPanelImg.setStyleSheet(f"background-image: url({parserCryptoGui.pathImg}/img/SettingsFone.bmp)")
        self.ui.icon = QtGui.QIcon()
        self.ui.icon.addPixmap(QtGui.QPixmap(f"url({parserCryptoGui.pathImg}/img/Logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.add_guiFunctions()

    def add_guiFunctions(self):
        self.ui.pushButton_loadSiteData.clicked.connect(self.startParsingThread)
        self.ui.pushButton_enableCoinChoice.clicked.connect(self.enableCoinChoice)

    def enableCoinChoice(self):
        self.selectedQuotationCoin = self.ui.comboBox_quotationCoin.currentText()
        self.selectedBasicCoin = self.ui.comboBox_basicCoin.currentText()

    def startParsingThread(self):
        try:
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
            unfilledRowNumber = 0

            self.ui.tableWidget_mainResultWindow.clearContents()
            self.ui.tableWidget_mainResultWindow.setRowCount(13)
            self.ui.tableWidget_mainResultWindow.setColumnCount(3)

            with open("JSON/cryptoDictCOINBASE.json", "r") as file:
                cryptoMarkets.append('COINBASE')
                cryptoMarketsData.append(json.loads(file.read()))
            with open("JSON/cryptoDictKUCOIN.json", "r") as file:
                cryptoMarkets.append('KUCOIN')
                cryptoMarketsData.append(json.loads(file.read()))
            with open("JSON/cryptoDictMYFIN.json", "r") as file:
                cryptoMarkets.append('MYFIN')
                cryptoMarketsData.append(json.loads(file.read()))
            for cryptoMarket, cryptoMarketData in zip(cryptoMarkets, cryptoMarketsData):
                self.fillResultWindow(unfilledRowNumber, cryptoMarket, cryptoMarketData)
                unfilledRowNumber += 1
        except Exception as ex:
            logger.error(ex)

    def fillResultWindow(self, unfilledRowNumber, cryptoMarket, cryptoMarketData):
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignCenter)
        item.setText(cryptoMarket)
        self.ui.tableWidget_mainResultWindow.setItem(unfilledRowNumber, 0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignCenter)
        item.setText(f'{self.selectedQuotationCoin}/{self.selectedBasicCoin}')
        self.ui.tableWidget_mainResultWindow.setItem(unfilledRowNumber, 1, item)

        if self.selectedQuotationCoin in cryptoMarketData:
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignCenter)
            item.setText(str(cryptoMarketData.get(self.selectedQuotationCoin)))
            self.ui.tableWidget_mainResultWindow.setItem(unfilledRowNumber, 2, item)
        else:
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignCenter)
            item.setText('Котировка отсутствует')
            self.ui.tableWidget_mainResultWindow.setItem(unfilledRowNumber, 2, item)

class ParsThread(QObject):
    """Класс получения данных с сайтов криптоплощадок в отдельном потоке"""
    finishSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(ParsThread, self).__init__()

    def start(self):
        try:
            main()
        except Exception as ex:
            logger.error(ex)
        self.finishSignal.emit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = parserCryptoGui()
    w.show()
    sys.exit(app.exec_())