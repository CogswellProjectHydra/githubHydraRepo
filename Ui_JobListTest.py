# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_JobListTest.ui'
#
# Created: Wed Feb 20 08:23:41 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(847, 305)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.jobTableLabel = QtGui.QLabel(self.centralwidget)
        self.jobTableLabel.setGeometry(QtCore.QRect(30, 20, 53, 16))
        self.jobTableLabel.setObjectName(_fromUtf8("jobTableLabel"))
        self.jobTable = QtGui.QTableWidget(self.centralwidget)
        self.jobTable.setGeometry(QtCore.QRect(30, 40, 261, 192))
        self.jobTable.setObjectName(_fromUtf8("jobTable"))
        self.jobTable.setColumnCount(2)
        self.jobTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.jobTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.jobTable.setHorizontalHeaderItem(1, item)
        self.taskTable = QtGui.QTableWidget(self.centralwidget)
        self.taskTable.setGeometry(QtCore.QRect(300, 40, 511, 192))
        self.taskTable.setObjectName(_fromUtf8("taskTable"))
        self.taskTable.setColumnCount(5)
        self.taskTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.taskTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.taskTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.taskTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.taskTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.taskTable.setHorizontalHeaderItem(4, item)
        self.taskTableLabel = QtGui.QLabel(self.centralwidget)
        self.taskTableLabel.setGeometry(QtCore.QRect(300, 20, 511, 16))
        self.taskTableLabel.setObjectName(_fromUtf8("taskTableLabel"))
        self.killJobButton = QtGui.QPushButton(self.centralwidget)
        self.killJobButton.setGeometry(QtCore.QRect(30, 240, 93, 28))
        self.killJobButton.setObjectName(_fromUtf8("killJobButton"))
        self.killTaskButton = QtGui.QPushButton(self.centralwidget)
        self.killTaskButton.setGeometry(QtCore.QRect(300, 240, 93, 28))
        self.killTaskButton.setObjectName(_fromUtf8("killTaskButton"))
        self.refreshButton = QtGui.QPushButton(self.centralwidget)
        self.refreshButton.setGeometry(QtCore.QRect(730, 240, 75, 31))
        self.refreshButton.setObjectName(_fromUtf8("refreshButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.jobTableLabel.setBuddy(self.jobTable)
        self.taskTableLabel.setBuddy(self.jobTable)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.jobTableLabel.setText(QtGui.QApplication.translate("MainWindow", "Job List", None, QtGui.QApplication.UnicodeUTF8))
        item = self.jobTable.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("MainWindow", "Job name", None, QtGui.QApplication.UnicodeUTF8))
        item = self.jobTable.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("MainWindow", "Job id", None, QtGui.QApplication.UnicodeUTF8))
        item = self.taskTable.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("MainWindow", "Task ID", None, QtGui.QApplication.UnicodeUTF8))
        item = self.taskTable.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("MainWindow", "Host", None, QtGui.QApplication.UnicodeUTF8))
        item = self.taskTable.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("MainWindow", "Status", None, QtGui.QApplication.UnicodeUTF8))
        item = self.taskTable.horizontalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("MainWindow", "Start Time", None, QtGui.QApplication.UnicodeUTF8))
        item = self.taskTable.horizontalHeaderItem(4)
        item.setText(QtGui.QApplication.translate("MainWindow", "End Time", None, QtGui.QApplication.UnicodeUTF8))
        self.taskTableLabel.setText(QtGui.QApplication.translate("MainWindow", "Task List (job: none selected)", None, QtGui.QApplication.UnicodeUTF8))
        self.killJobButton.setText(QtGui.QApplication.translate("MainWindow", "Kill Job", None, QtGui.QApplication.UnicodeUTF8))
        self.killTaskButton.setText(QtGui.QApplication.translate("MainWindow", "Kill Task", None, QtGui.QApplication.UnicodeUTF8))
        self.refreshButton.setText(QtGui.QApplication.translate("MainWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))

