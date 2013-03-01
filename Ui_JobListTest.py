# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_JobListTest.ui'
#
# Created: Thu Feb 28 23:35:50 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

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
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.jobTableLabel = QtGui.QLabel(self.layoutWidget)
        self.jobTableLabel.setObjectName(_fromUtf8("jobTableLabel"))
        self.gridLayout.addWidget(self.jobTableLabel, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 2)
        self.jobTable = QtGui.QTableWidget(self.layoutWidget)
        self.jobTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.jobTable.setObjectName(_fromUtf8("jobTable"))
        self.jobTable.setColumnCount(2)
        self.jobTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.jobTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.jobTable.setHorizontalHeaderItem(1, item)
        self.jobTable.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.jobTable, 1, 0, 1, 3)
        self.killJobButton = QtGui.QPushButton(self.layoutWidget)
        self.killJobButton.setObjectName(_fromUtf8("killJobButton"))
        self.gridLayout.addWidget(self.killJobButton, 2, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.taskTableLabel = QtGui.QLabel(self.layoutWidget1)
        self.taskTableLabel.setObjectName(_fromUtf8("taskTableLabel"))
        self.gridLayout_2.addWidget(self.taskTableLabel, 0, 0, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        self.taskTable = QtGui.QTableWidget(self.layoutWidget1)
        self.taskTable.setEnabled(True)
        self.taskTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.taskTable.setGridStyle(QtCore.Qt.SolidLine)
        self.taskTable.setObjectName(_fromUtf8("taskTable"))
        self.taskTable.setColumnCount(6)
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
        item = QtGui.QTableWidgetItem()
        self.taskTable.setHorizontalHeaderItem(5, item)
        self.gridLayout_2.addWidget(self.taskTable, 1, 0, 1, 4)
        self.killTaskButton = QtGui.QPushButton(self.layoutWidget1)
        self.killTaskButton.setEnabled(False)
        self.killTaskButton.setObjectName(_fromUtf8("killTaskButton"))
        self.gridLayout_2.addWidget(self.killTaskButton, 2, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 1, 1, 1)
        self.refreshButton = QtGui.QPushButton(self.layoutWidget1)
        self.refreshButton.setObjectName(_fromUtf8("refreshButton"))
        self.gridLayout_2.addWidget(self.refreshButton, 2, 3, 1, 1)
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.jobTableLabel.setBuddy(self.jobTable)
        self.taskTableLabel.setBuddy(self.jobTable)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.jobTableLabel.setText(_translate("MainWindow", "Job List", None))
        self.jobTable.setSortingEnabled(True)
        item = self.jobTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Job id", None))
        item = self.jobTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Job name", None))
        self.killJobButton.setText(_translate("MainWindow", "Kill Job", None))
        self.taskTableLabel.setText(_translate("MainWindow", "Task List (job: none selected)", None))
        self.taskTable.setSortingEnabled(True)
        item = self.taskTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Task ID", None))
        item = self.taskTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Host", None))
        item = self.taskTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status", None))
        item = self.taskTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Start Time", None))
        item = self.taskTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "End Time", None))
        item = self.taskTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Duration", None))
        self.killTaskButton.setText(_translate("MainWindow", "Kill Task", None))
        self.refreshButton.setText(_translate("MainWindow", "Refresh", None))

