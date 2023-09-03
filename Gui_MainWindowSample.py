# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui_MainWindowSample.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CryptoProject(object):
    def setupUi(self, CryptoProject):
        CryptoProject.setObjectName("CryptoProject")
        CryptoProject.resize(1209, 570)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CryptoProject.sizePolicy().hasHeightForWidth())
        CryptoProject.setSizePolicy(sizePolicy)
        CryptoProject.setMinimumSize(QtCore.QSize(1209, 570))
        CryptoProject.setMaximumSize(QtCore.QSize(1209, 570))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/Logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CryptoProject.setWindowIcon(icon)
        CryptoProject.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(CryptoProject)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget_siteList = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget_siteList.setGeometry(QtCore.QRect(6, 5, 120, 540))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.treeWidget_siteList.setFont(font)
        self.treeWidget_siteList.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.treeWidget_siteList.setAutoFillBackground(False)
        self.treeWidget_siteList.setStyleSheet("background-image: url(:/Crypto/SiteTreeBackground.png);")
        self.treeWidget_siteList.setMidLineWidth(0)
        self.treeWidget_siteList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeWidget_siteList.setDragEnabled(False)
        self.treeWidget_siteList.setAlternatingRowColors(False)
        self.treeWidget_siteList.setIconSize(QtCore.QSize(20, 20))
        self.treeWidget_siteList.setAutoExpandDelay(-1)
        self.treeWidget_siteList.setIndentation(4)
        self.treeWidget_siteList.setRootIsDecorated(True)
        self.treeWidget_siteList.setUniformRowHeights(False)
        self.treeWidget_siteList.setItemsExpandable(True)
        self.treeWidget_siteList.setAnimated(False)
        self.treeWidget_siteList.setAllColumnsShowFocus(False)
        self.treeWidget_siteList.setWordWrap(False)
        self.treeWidget_siteList.setHeaderHidden(False)
        self.treeWidget_siteList.setExpandsOnDoubleClick(True)
        self.treeWidget_siteList.setColumnCount(1)
        self.treeWidget_siteList.setObjectName("treeWidget_siteList")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.treeWidget_siteList.headerItem().setFont(0, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_siteList)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(True)
        item_0.setFont(0, font)
        item_0.setCheckState(0, QtCore.Qt.Checked)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/Myfin.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon1)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_siteList)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(True)
        item_0.setFont(0, font)
        item_0.setCheckState(0, QtCore.Qt.Unchecked)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/Kucoin.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_siteList)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        item_0.setFont(0, font)
        item_0.setCheckState(0, QtCore.Qt.Unchecked)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/Coinbase.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon3)
        self.treeWidget_siteList.header().setVisible(True)
        self.treeWidget_siteList.header().setCascadingSectionResizes(False)
        self.treeWidget_siteList.header().setHighlightSections(True)
        self.treeWidget_siteList.header().setMinimumSectionSize(10)
        self.treeWidget_siteList.header().setStretchLastSection(True)
        self.label_header = QtWidgets.QLabel(self.centralwidget)
        self.label_header.setGeometry(QtCore.QRect(131, 5, 1070, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_header.setFont(font)
        self.label_header.setAutoFillBackground(False)
        self.label_header.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.983, y2:0.227273, stop:0 rgba(227, 91, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_header.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_header.setText("")
        self.label_header.setScaledContents(False)
        self.label_header.setAlignment(QtCore.Qt.AlignCenter)
        self.label_header.setObjectName("label_header")
        self.tableWidget_mainResultWindow = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_mainResultWindow.setGeometry(QtCore.QRect(131, 30, 687, 374))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_mainResultWindow.sizePolicy().hasHeightForWidth())
        self.tableWidget_mainResultWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_mainResultWindow.setFont(font)
        self.tableWidget_mainResultWindow.setAutoFillBackground(False)
        self.tableWidget_mainResultWindow.setStyleSheet("")
        self.tableWidget_mainResultWindow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget_mainResultWindow.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget_mainResultWindow.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_mainResultWindow.setDragEnabled(False)
        self.tableWidget_mainResultWindow.setAlternatingRowColors(True)
        self.tableWidget_mainResultWindow.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget_mainResultWindow.setShowGrid(True)
        self.tableWidget_mainResultWindow.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_mainResultWindow.setWordWrap(True)
        self.tableWidget_mainResultWindow.setCornerButtonEnabled(True)
        self.tableWidget_mainResultWindow.setRowCount(13)
        self.tableWidget_mainResultWindow.setColumnCount(3)
        self.tableWidget_mainResultWindow.setObjectName("tableWidget_mainResultWindow")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        item.setFont(font)
        item.setBackground(QtGui.QColor(207, 207, 205))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_mainResultWindow.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_mainResultWindow.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_mainResultWindow.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_mainResultWindow.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(181, 181, 181))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.tableWidget_mainResultWindow.setItem(0, 1, item)
        self.tableWidget_mainResultWindow.horizontalHeader().setVisible(True)
        self.tableWidget_mainResultWindow.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_mainResultWindow.horizontalHeader().setDefaultSectionSize(228)
        self.tableWidget_mainResultWindow.horizontalHeader().setHighlightSections(False)
        self.tableWidget_mainResultWindow.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_mainResultWindow.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_mainResultWindow.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_mainResultWindow.verticalHeader().setVisible(False)
        self.tableWidget_mainResultWindow.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_mainResultWindow.verticalHeader().setDefaultSectionSize(27)
        self.tableWidget_mainResultWindow.verticalHeader().setHighlightSections(False)
        self.tableWidget_mainResultWindow.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_mainResultWindow.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_mainResultWindow.verticalHeader().setStretchLastSection(True)
        self.tableWidget_diagWindow = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_diagWindow.setGeometry(QtCore.QRect(131, 409, 687, 136))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(18)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.tableWidget_diagWindow.sizePolicy().hasHeightForWidth())
        self.tableWidget_diagWindow.setSizePolicy(sizePolicy)
        self.tableWidget_diagWindow.setBaseSize(QtCore.QSize(0, 0))
        self.tableWidget_diagWindow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget_diagWindow.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget_diagWindow.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_diagWindow.setAlternatingRowColors(True)
        self.tableWidget_diagWindow.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget_diagWindow.setRowCount(1)
        self.tableWidget_diagWindow.setColumnCount(1)
        self.tableWidget_diagWindow.setObjectName("tableWidget_diagWindow")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_diagWindow.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_diagWindow.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
        self.tableWidget_diagWindow.setItem(0, 0, item)
        self.tableWidget_diagWindow.horizontalHeader().setVisible(True)
        self.tableWidget_diagWindow.horizontalHeader().setDefaultSectionSize(689)
        self.tableWidget_diagWindow.horizontalHeader().setHighlightSections(False)
        self.tableWidget_diagWindow.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_diagWindow.verticalHeader().setVisible(False)
        self.tableWidget_diagWindow.verticalHeader().setDefaultSectionSize(0)
        self.tableWidget_diagWindow.verticalHeader().setHighlightSections(False)
        self.tableWidget_diagWindow.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_diagWindow.verticalHeader().setStretchLastSection(True)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(823, 30, 378, 515))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.label_coinChoice = QtWidgets.QLabel(self.frame)
        self.label_coinChoice.setGeometry(QtCore.QRect(50, 100, 131, 21))
        self.label_coinChoice.setObjectName("label_coinChoice")
        self.label_refreshTime = QtWidgets.QLabel(self.frame)
        self.label_refreshTime.setGeometry(QtCore.QRect(10, 30, 191, 16))
        self.label_refreshTime.setObjectName("label_refreshTime")
        self.spinBox_refreshTime = QtWidgets.QSpinBox(self.frame)
        self.spinBox_refreshTime.setEnabled(False)
        self.spinBox_refreshTime.setGeometry(QtCore.QRect(10, 50, 42, 22))
        self.spinBox_refreshTime.setObjectName("spinBox_refreshTime")
        self.checkBox_tgBotOn = QtWidgets.QCheckBox(self.frame)
        self.checkBox_tgBotOn.setEnabled(False)
        self.checkBox_tgBotOn.setGeometry(QtCore.QRect(30, 214, 161, 17))
        self.checkBox_tgBotOn.setObjectName("checkBox_tgBotOn")
        self.pushButton_EnableRefreshTime = QtWidgets.QPushButton(self.frame)
        self.pushButton_EnableRefreshTime.setEnabled(False)
        self.pushButton_EnableRefreshTime.setGeometry(QtCore.QRect(60, 50, 75, 23))
        self.pushButton_EnableRefreshTime.setObjectName("pushButton_EnableRefreshTime")
        self.label_setPanel = QtWidgets.QLabel(self.frame)
        self.label_setPanel.setGeometry(QtCore.QRect(113, 1, 171, 20))
        self.label_setPanel.setObjectName("label_setPanel")
        self.comboBox_quotationCoin = QtWidgets.QComboBox(self.frame)
        self.comboBox_quotationCoin.setGeometry(QtCore.QRect(9, 143, 100, 22))
        self.comboBox_quotationCoin.setObjectName("comboBox_quotationCoin")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_quotationCoin.addItem("")
        self.comboBox_basicCoin = QtWidgets.QComboBox(self.frame)
        self.comboBox_basicCoin.setEnabled(True)
        self.comboBox_basicCoin.setGeometry(QtCore.QRect(127, 142, 100, 22))
        self.comboBox_basicCoin.setInputMethodHints(QtCore.Qt.ImhNone)
        self.comboBox_basicCoin.setEditable(False)
        self.comboBox_basicCoin.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.comboBox_basicCoin.setObjectName("comboBox_basicCoin")
        self.comboBox_basicCoin.addItem("")
        self.comboBox_basicCoin.addItem("")
        self.comboBox_basicCoin.addItem("")
        self.comboBox_basicCoin.addItem("")
        self.comboBox_basicCoin.addItem("")
        self.line_settingPanel = QtWidgets.QFrame(self.frame)
        self.line_settingPanel.setGeometry(QtCore.QRect(30, 240, 311, 16))
        self.line_settingPanel.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_settingPanel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_settingPanel.setObjectName("line_settingPanel")
        self.pushButton_enableCoinChoice = QtWidgets.QPushButton(self.frame)
        self.pushButton_enableCoinChoice.setGeometry(QtCore.QRect(63, 173, 101, 23))
        self.pushButton_enableCoinChoice.setStyleSheet("background-color: rgb(126, 255, 112);")
        self.pushButton_enableCoinChoice.setObjectName("pushButton_enableCoinChoice")
        self.label_quotationCoin = QtWidgets.QLabel(self.frame)
        self.label_quotationCoin.setGeometry(QtCore.QRect(5, 120, 110, 20))
        self.label_quotationCoin.setObjectName("label_quotationCoin")
        self.label_basicCoin = QtWidgets.QLabel(self.frame)
        self.label_basicCoin.setGeometry(QtCore.QRect(136, 120, 110, 20))
        self.label_basicCoin.setObjectName("label_basicCoin")
        self.frame_settingPanelImg = QtWidgets.QFrame(self.frame)
        self.frame_settingPanelImg.setGeometry(QtCore.QRect(45, 282, 290, 180))
        self.frame_settingPanelImg.setAutoFillBackground(False)
        self.frame_settingPanelImg.setStyleSheet("background-image: url(:/Crypto/SettingsFone.bmp);")
        self.frame_settingPanelImg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_settingPanelImg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_settingPanelImg.setObjectName("frame_settingPanelImg")
        self.checkBox_circularRefresh = QtWidgets.QCheckBox(self.frame)
        self.checkBox_circularRefresh.setGeometry(QtCore.QRect(211, 53, 150, 17))
        self.checkBox_circularRefresh.setObjectName("checkBox_circularRefresh")
        self.pushButton_loadSiteData = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_loadSiteData.setGeometry(QtCore.QRect(11, 106, 110, 23))
        self.pushButton_loadSiteData.setStyleSheet("background-color: rgb(126, 255, 112);")
        self.pushButton_loadSiteData.setObjectName("pushButton_loadSiteData")
        CryptoProject.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CryptoProject)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1209, 21))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        self.menu_settings = QtWidgets.QMenu(self.menubar)
        self.menu_settings.setObjectName("menu_settings")
        CryptoProject.setMenuBar(self.menubar)
        self.action_mirrorsInput = QtWidgets.QAction(CryptoProject)
        self.action_mirrorsInput.setObjectName("action_mirrorsInput")
        self.action_additionalSettings = QtWidgets.QAction(CryptoProject)
        self.action_additionalSettings.setObjectName("action_additionalSettings")
        self.menu_settings.addAction(self.action_mirrorsInput)
        self.menu_settings.addAction(self.action_additionalSettings)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_settings.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(CryptoProject)
        QtCore.QMetaObject.connectSlotsByName(CryptoProject)

    def retranslateUi(self, CryptoProject):
        _translate = QtCore.QCoreApplication.translate
        CryptoProject.setWindowTitle(_translate("CryptoProject", "CryptoScanner"))
        self.treeWidget_siteList.setSortingEnabled(False)
        self.treeWidget_siteList.headerItem().setText(0, _translate("CryptoProject", "Выбор площадок"))
        __sortingEnabled = self.treeWidget_siteList.isSortingEnabled()
        self.treeWidget_siteList.setSortingEnabled(False)
        self.treeWidget_siteList.topLevelItem(0).setText(0, _translate("CryptoProject", "Myfin"))
        self.treeWidget_siteList.topLevelItem(1).setText(0, _translate("CryptoProject", "Kucoin"))
        self.treeWidget_siteList.topLevelItem(2).setText(0, _translate("CryptoProject", "Coinbase"))
        self.treeWidget_siteList.setSortingEnabled(__sortingEnabled)
        self.tableWidget_mainResultWindow.setSortingEnabled(False)
        item = self.tableWidget_mainResultWindow.horizontalHeaderItem(0)
        item.setText(_translate("CryptoProject", "Торговая площадка"))
        item = self.tableWidget_mainResultWindow.horizontalHeaderItem(1)
        item.setText(_translate("CryptoProject", "Валютная пара"))
        item = self.tableWidget_mainResultWindow.horizontalHeaderItem(2)
        item.setText(_translate("CryptoProject", "Котировка"))
        __sortingEnabled = self.tableWidget_mainResultWindow.isSortingEnabled()
        self.tableWidget_mainResultWindow.setSortingEnabled(False)
        self.tableWidget_mainResultWindow.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_diagWindow.horizontalHeaderItem(0)
        item.setText(_translate("CryptoProject", "Системные сообщения и дополнительная информация"))
        __sortingEnabled = self.tableWidget_diagWindow.isSortingEnabled()
        self.tableWidget_diagWindow.setSortingEnabled(False)
        self.tableWidget_diagWindow.setSortingEnabled(__sortingEnabled)
        self.label_coinChoice.setText(_translate("CryptoProject", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Выбор валют</span></p></body></html>"))
        self.label_refreshTime.setText(_translate("CryptoProject", "<html><head/><body><p>Время обновления данных парсеров</p></body></html>"))
        self.checkBox_tgBotOn.setText(_translate("CryptoProject", "Включение телеграмм-бота"))
        self.pushButton_EnableRefreshTime.setText(_translate("CryptoProject", "Установить"))
        self.label_setPanel.setText(_translate("CryptoProject", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Панель настроек</span></p></body></html>"))
        self.comboBox_quotationCoin.setItemText(0, _translate("CryptoProject", "Bitcoin"))
        self.comboBox_quotationCoin.setItemText(1, _translate("CryptoProject", "Ethereum"))
        self.comboBox_quotationCoin.setItemText(2, _translate("CryptoProject", "Tether"))
        self.comboBox_quotationCoin.setItemText(3, _translate("CryptoProject", "BNB"))
        self.comboBox_quotationCoin.setItemText(4, _translate("CryptoProject", "XRP"))
        self.comboBox_quotationCoin.setItemText(5, _translate("CryptoProject", "USD Coin"))
        self.comboBox_quotationCoin.setItemText(6, _translate("CryptoProject", "Cardano"))
        self.comboBox_quotationCoin.setItemText(7, _translate("CryptoProject", "Dogecoin"))
        self.comboBox_quotationCoin.setItemText(8, _translate("CryptoProject", "Solana"))
        self.comboBox_quotationCoin.setItemText(9, _translate("CryptoProject", "TRON"))
        self.comboBox_quotationCoin.setItemText(10, _translate("CryptoProject", "Ton"))
        self.comboBox_quotationCoin.setItemText(11, _translate("CryptoProject", "Dai"))
        self.comboBox_quotationCoin.setItemText(12, _translate("CryptoProject", "Polkadot"))
        self.comboBox_quotationCoin.setItemText(13, _translate("CryptoProject", "Polygon"))
        self.comboBox_quotationCoin.setItemText(14, _translate("CryptoProject", "Litecoin"))
        self.comboBox_quotationCoin.setItemText(15, _translate("CryptoProject", "SHIBA INU"))
        self.comboBox_quotationCoin.setItemText(16, _translate("CryptoProject", "Wrapped Bitcoin"))
        self.comboBox_quotationCoin.setItemText(17, _translate("CryptoProject", "Bitcoin Cash"))
        self.comboBox_quotationCoin.setItemText(18, _translate("CryptoProject", "UNUS SED LEO"))
        self.comboBox_quotationCoin.setItemText(19, _translate("CryptoProject", "Avalanche"))
        self.comboBox_quotationCoin.setItemText(20, _translate("CryptoProject", "TrueUSD"))
        self.comboBox_quotationCoin.setItemText(21, _translate("CryptoProject", "Chainlink"))
        self.comboBox_quotationCoin.setItemText(22, _translate("CryptoProject", "Stellar Lumens"))
        self.comboBox_quotationCoin.setItemText(23, _translate("CryptoProject", "Binance USD"))
        self.comboBox_quotationCoin.setItemText(24, _translate("CryptoProject", "Monero"))
        self.comboBox_quotationCoin.setItemText(25, _translate("CryptoProject", "Uniswap"))
        self.comboBox_quotationCoin.setItemText(26, _translate("CryptoProject", "Aave UNI V2"))
        self.comboBox_quotationCoin.setItemText(27, _translate("CryptoProject", "OKB"))
        self.comboBox_quotationCoin.setItemText(28, _translate("CryptoProject", "Cosmos"))
        self.comboBox_quotationCoin.setItemText(29, _translate("CryptoProject", "Ethereum Classic"))
        self.comboBox_quotationCoin.setItemText(30, _translate("CryptoProject", "Binance Chain Native Token"))
        self.comboBox_quotationCoin.setItemText(31, _translate("CryptoProject", "Crypto.com Coin"))
        self.comboBox_quotationCoin.setItemText(32, _translate("CryptoProject", "Hedera Hashgraph"))
        self.comboBox_quotationCoin.setItemText(33, _translate("CryptoProject", "THETA"))
        self.comboBox_quotationCoin.setItemText(34, _translate("CryptoProject", "Wrapped Bitcoin"))
        self.comboBox_quotationCoin.setItemText(35, _translate("CryptoProject", "IOTA"))
        self.comboBox_quotationCoin.setItemText(36, _translate("CryptoProject", "Bitcoin Cash"))
        self.comboBox_quotationCoin.setItemText(37, _translate("CryptoProject", "Stellar"))
        self.comboBox_quotationCoin.setItemText(38, _translate("CryptoProject", "Acala"))
        self.comboBox_quotationCoin.setItemText(39, _translate("CryptoProject", "XDC Mainnet"))
        self.comboBox_quotationCoin.setItemText(40, _translate("CryptoProject", "KuCoin Token"))
        self.comboBox_quotationCoin.setItemText(41, _translate("CryptoProject", "EOS"))
        self.comboBox_quotationCoin.setItemText(42, _translate("CryptoProject", "ZCash"))
        self.comboBox_quotationCoin.setItemText(43, _translate("CryptoProject", "NEO"))
        self.comboBox_quotationCoin.setItemText(44, _translate("CryptoProject", "DigitalCash"))
        self.comboBox_quotationCoin.setItemText(45, _translate("CryptoProject", "Verge"))
        self.comboBox_quotationCoin.setItemText(46, _translate("CryptoProject", "OmiseGo"))
        self.comboBox_quotationCoin.setItemText(47, _translate("CryptoProject", "NEM"))
        self.comboBox_quotationCoin.setItemText(48, _translate("CryptoProject", "DigiByte"))
        self.comboBox_quotationCoin.setItemText(49, _translate("CryptoProject", "Bitshares"))
        self.comboBox_basicCoin.setCurrentText(_translate("CryptoProject", "RUB"))
        self.comboBox_basicCoin.setItemText(0, _translate("CryptoProject", "RUB"))
        self.comboBox_basicCoin.setItemText(1, _translate("CryptoProject", "USDT"))
        self.comboBox_basicCoin.setItemText(2, _translate("CryptoProject", "USD"))
        self.comboBox_basicCoin.setItemText(3, _translate("CryptoProject", "EUR"))
        self.comboBox_basicCoin.setItemText(4, _translate("CryptoProject", "GBP"))
        self.pushButton_enableCoinChoice.setText(_translate("CryptoProject", "Применить"))
        self.label_quotationCoin.setText(_translate("CryptoProject", "Котируемая валюта"))
        self.label_basicCoin.setText(_translate("CryptoProject", "Базовая валюта"))
        self.checkBox_circularRefresh.setText(_translate("CryptoProject", "Циклическое обновление"))
        self.pushButton_loadSiteData.setText(_translate("CryptoProject", "Загрузить данные"))
        self.menu_file.setTitle(_translate("CryptoProject", "Файл"))
        self.menu_help.setTitle(_translate("CryptoProject", "Справка"))
        self.menu_settings.setTitle(_translate("CryptoProject", "Настройки"))
        self.action_mirrorsInput.setText(_translate("CryptoProject", "Ввод актульных зеркал сайтов"))
        self.action_additionalSettings.setText(_translate("CryptoProject", "Дополнительные настройки"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CryptoProject = QtWidgets.QMainWindow()
    ui = Ui_CryptoProject()
    ui.setupUi(CryptoProject)
    CryptoProject.show()
    sys.exit(app.exec_())
