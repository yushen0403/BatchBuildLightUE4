# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindows.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(573, 510)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.levelsLayout = QtWidgets.QVBoxLayout()
        self.levelsLayout.setObjectName("levelsLayout")
        self.toolsLevelsLayout = QtWidgets.QHBoxLayout()
        self.toolsLevelsLayout.setObjectName("toolsLevelsLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.toolsLevelsLayout.addItem(spacerItem)
        self.pushLevelsSelect = QtWidgets.QPushButton(self.groupBox)
        self.pushLevelsSelect.setObjectName("pushLevelsSelect")
        self.toolsLevelsLayout.addWidget(self.pushLevelsSelect)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.toolsLevelsLayout.addItem(spacerItem1)
        self.pushLevelsDeselect = QtWidgets.QPushButton(self.groupBox)
        self.pushLevelsDeselect.setObjectName("pushLevelsDeselect")
        self.toolsLevelsLayout.addWidget(self.pushLevelsDeselect)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.toolsLevelsLayout.addItem(spacerItem2)
        self.toolLevelsEdit = QtWidgets.QToolButton(self.groupBox)
        self.toolLevelsEdit.setObjectName("toolLevelsEdit")
        self.toolsLevelsLayout.addWidget(self.toolLevelsEdit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.toolsLevelsLayout.addItem(spacerItem3)
        self.levelsLayout.addLayout(self.toolsLevelsLayout)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.levelsLayout.addWidget(self.line)
        self.listLevels = QtWidgets.QListView(self.groupBox)
        self.listLevels.setObjectName("listLevels")
        self.levelsLayout.addWidget(self.listLevels)
        self.gridLayout.addLayout(self.levelsLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.toolsLayout = QtWidgets.QHBoxLayout()
        self.toolsLayout.setObjectName("toolsLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.toolsLayout.addItem(spacerItem4)
        self.pushToolsBuils = QtWidgets.QPushButton(self.centralwidget)
        self.pushToolsBuils.setObjectName("pushToolsBuils")
        self.toolsLayout.addWidget(self.pushToolsBuils)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.toolsLayout.addItem(spacerItem5)
        self.pushToolsCache = QtWidgets.QPushButton(self.centralwidget)
        self.pushToolsCache.setObjectName("pushToolsCache")
        self.toolsLayout.addWidget(self.pushToolsCache)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.toolsLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.toolsLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 573, 21))
        self.menubar.setObjectName("menubar")
        self.menu_Fichier = QtWidgets.QMenu(self.menubar)
        self.menu_Fichier.setObjectName("menu_Fichier")
        self.menuSetup = QtWidgets.QMenu(self.menubar)
        self.menuSetup.setObjectName("menuSetup")
        self.menuLog = QtWidgets.QMenu(self.menubar)
        self.menuLog.setObjectName("menuLog")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNouveau_Setup = QtWidgets.QAction(MainWindow)
        self.actionNouveau_Setup.setObjectName("actionNouveau_Setup")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionPaths = QtWidgets.QAction(MainWindow)
        self.actionPaths.setObjectName("actionPaths")
        self.actionNetworks = QtWidgets.QAction(MainWindow)
        self.actionNetworks.setObjectName("actionNetworks")
        self.actionCSV = QtWidgets.QAction(MainWindow)
        self.actionCSV.setObjectName("actionCSV")
        self.actionShow_log_folder = QtWidgets.QAction(MainWindow)
        self.actionShow_log_folder.setObjectName("actionShow_log_folder")
        self.actionClean_Log = QtWidgets.QAction(MainWindow)
        self.actionClean_Log.setObjectName("actionClean_Log")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionUpdates = QtWidgets.QAction(MainWindow)
        self.actionUpdates.setObjectName("actionUpdates")
        self.actionShortcut = QtWidgets.QAction(MainWindow)
        self.actionShortcut.setObjectName("actionShortcut")
        self.actionOuvrir = QtWidgets.QAction(MainWindow)
        self.actionOuvrir.setObjectName("actionOuvrir")
        self.menu_Fichier.addAction(self.actionNouveau_Setup)
        self.menu_Fichier.addAction(self.actionOuvrir)
        self.menu_Fichier.addSeparator()
        self.menu_Fichier.addAction(self.actionExit)
        self.menuSetup.addAction(self.actionPaths)
        self.menuSetup.addAction(self.actionNetworks)
        self.menuSetup.addAction(self.actionCSV)
        self.menuLog.addAction(self.actionShow_log_folder)
        self.menuLog.addAction(self.actionClean_Log)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionUpdates)
        self.menuHelp.addAction(self.actionShortcut)
        self.menubar.addAction(self.menu_Fichier.menuAction())
        self.menubar.addAction(self.menuSetup.menuAction())
        self.menubar.addAction(self.menuLog.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Levels"))
        self.pushLevelsSelect.setText(_translate("MainWindow", "Select all Levels"))
        self.pushLevelsDeselect.setText(_translate("MainWindow", "Deselect all Levels"))
        self.toolLevelsEdit.setText(_translate("MainWindow", "..."))
        self.pushToolsBuils.setText(_translate("MainWindow", "Builds Levels"))
        self.pushToolsCache.setText(_translate("MainWindow", "Clean Cache"))
        self.menu_Fichier.setTitle(_translate("MainWindow", "&Fichier"))
        self.menuSetup.setTitle(_translate("MainWindow", "Setup"))
        self.menuLog.setTitle(_translate("MainWindow", "Log"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNouveau_Setup.setText(_translate("MainWindow", "New Setup"))
        self.actionNouveau_Setup.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionPaths.setText(_translate("MainWindow", "Paths"))
        self.actionNetworks.setText(_translate("MainWindow", "Networks"))
        self.actionCSV.setText(_translate("MainWindow", "CSV"))
        self.actionShow_log_folder.setText(_translate("MainWindow", "Show log folder"))
        self.actionClean_Log.setText(_translate("MainWindow", "Clean Log"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionUpdates.setText(_translate("MainWindow", "Updates"))
        self.actionShortcut.setText(_translate("MainWindow", "Shortcut"))
        self.actionOuvrir.setText(_translate("MainWindow", "Open Setup"))
        self.actionOuvrir.setShortcut(_translate("MainWindow", "Ctrl+O"))

