# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DBViewer_UI.ui'
#
# Created: Wed Jul 04 04:30:28 2012
#      by: PyQt4 UI code generator 4.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DBWindow(object):
    def setupUi(self, DBWindow):
        DBWindow.setObjectName(_fromUtf8("DBWindow"))
        DBWindow.resize(869, 600)
        self.centralwidget = QtGui.QWidget(DBWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.fetchButton = QtGui.QPushButton(self.centralwidget)
        self.fetchButton.setObjectName(_fromUtf8("fetchButton"))
        self.gridLayout.addWidget(self.fetchButton, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 2)
        DBWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(DBWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 869, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        DBWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(DBWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        DBWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DBWindow)
        QtCore.QMetaObject.connectSlotsByName(DBWindow)

    def retranslateUi(self, DBWindow):
        DBWindow.setWindowTitle(QtGui.QApplication.translate("DBWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.fetchButton.setText(QtGui.QApplication.translate("DBWindow", "Fetch", None, QtGui.QApplication.UnicodeUTF8))

