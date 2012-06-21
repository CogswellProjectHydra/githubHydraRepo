# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listExample.ui'
#
# Created: Thu Jun 21 14:55:10 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_listMainWindow(object):
    def setupUi(self, listMainWindow):
        listMainWindow.setObjectName(_fromUtf8("listMainWindow"))
        listMainWindow.resize(593, 514)
        self.centralwidget = QtGui.QWidget(listMainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        listMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(listMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        listMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(listMainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        listMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(listMainWindow)
        QtCore.QMetaObject.connectSlotsByName(listMainWindow)

    def retranslateUi(self, listMainWindow):
        listMainWindow.setWindowTitle(QtGui.QApplication.translate("listMainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("listMainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

