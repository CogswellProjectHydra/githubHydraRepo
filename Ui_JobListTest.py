# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_JobListTest.ui'
#
# Created: Wed Feb 20 16:18:40 2013
#      by: PyQt4 UI code generator 4.9.2
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
        MainWindow.resize(1138, 305)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.jobTableLabel = QtGui.QLabel(self.widget)
        self.jobTableLabel.setObjectName(_fromUtf8("jobTableLabel"))
        self.gridLayout.addWidget(self.jobTableLabel, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 2)
        self.jobTable = QtGui.QTableWidget(self.widget)
        self.jobTable.setObjectName(_fromUtf8("jobTable"))
        self.jobTable.setColumnCount(2)
        self.jobTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.jobTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.jobTable.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.jobTable, 1, 0, 1, 3)
        self.killJobButton = QtGui.QPushButton(self.widget)
        self.killJobButton.setObjectName(_fromUtf8("killJobButton"))
        self.gridLayout.addWidget(self.killJobButton, 2, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.widget1 = QtGui.QWidget(self.splitter)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget1)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.taskTableLabel = QtGui.QLabel(self.widget1)
        self.taskTableLabel.setObjectName(_fromUtf8("taskTableLabel"))
        self.gridLayout_2.addWidget(self.taskTableLabel, 0, 0, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        self.taskTable = QtGui.QTableWidget(self.widget1)
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
        self.gridLayout_2.addWidget(self.taskTable, 1, 0, 1, 4)
        self.killTaskButton = QtGui.QPushButton(self.widget1)
        self.killTaskButton.setObjectName(_fromUtf8("killTaskButton"))
        self.gridLayout_2.addWidget(self.killTaskButton, 2, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 1, 1, 1)
        self.refreshButton = QtGui.QPushButton(self.widget1)
        self.refreshButton.setObjectName(_fromUtf8("refreshButton"))
        self.gridLayout_2.addWidget(self.refreshButton, 2, 3, 1, 1)
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.jobTableLabel.setBuddy(self.jobTable)
        self.taskTableLabel.setBuddy(self.jobTable)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.jobTableLabel.setText(QtGui.QApplication.translate("MainWindow", "Job List", None, QtGui.QApplication.UnicodeUTF8))
        item = self.jobTable.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("MainWindow", "Job id", None, QtGui.QApplication.UnicodeUTF8))
        item = self.jobTable.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("MainWindow", "Job name", None, QtGui.QApplication.UnicodeUTF8))
        self.killJobButton.setText(QtGui.QApplication.translate("MainWindow", "Kill Job", None, QtGui.QApplication.UnicodeUTF8))
        self.taskTableLabel.setText(QtGui.QApplication.translate("MainWindow", "Task List (job: none selected)", None, QtGui.QApplication.UnicodeUTF8))
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
        self.killTaskButton.setText(QtGui.QApplication.translate("MainWindow", "Kill Task", None, QtGui.QApplication.UnicodeUTF8))
        self.refreshButton.setText(QtGui.QApplication.translate("MainWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))

