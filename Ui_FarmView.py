# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_FarmView.ui'
#
# Created: Thu Jul 26 15:04:44 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FarmView(object):
    def setupUi(self, FarmView):
        FarmView.setObjectName(_fromUtf8("FarmView"))
        FarmView.resize(800, 471)
        self.centralwidget = QtGui.QWidget(FarmView)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.fetchButton = QtGui.QPushButton(self.centralwidget)
        self.fetchButton.setObjectName(_fromUtf8("fetchButton"))
        self.horizontalLayout.addWidget(self.fetchButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.renderNodesTab = QtGui.QWidget()
        self.renderNodesTab.setObjectName(_fromUtf8("renderNodesTab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.renderNodesTab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.scrollArea = QtGui.QScrollArea(self.renderNodesTab)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 739, 335))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_3 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.renderNodesGrid = QtGui.QGridLayout()
        self.renderNodesGrid.setObjectName(_fromUtf8("renderNodesGrid"))
        self.gridLayout_3.addLayout(self.renderNodesGrid, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.renderNodesTab, _fromUtf8(""))
        self.jobsTab = QtGui.QWidget()
        self.jobsTab.setObjectName(_fromUtf8("jobsTab"))
        self.gridLayout_5 = QtGui.QGridLayout(self.jobsTab)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.scrollArea_2 = QtGui.QScrollArea(self.jobsTab)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 756, 335))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.jobsGrid = QtGui.QGridLayout()
        self.jobsGrid.setObjectName(_fromUtf8("jobsGrid"))
        self.gridLayout_2.addLayout(self.jobsGrid, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.jobsTab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        FarmView.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(FarmView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        FarmView.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(FarmView)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        FarmView.setStatusBar(self.statusbar)

        self.retranslateUi(FarmView)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(FarmView)

    def retranslateUi(self, FarmView):
        FarmView.setWindowTitle(QtGui.QApplication.translate("FarmView", "FarmView", None, QtGui.QApplication.UnicodeUTF8))
        self.fetchButton.setText(QtGui.QApplication.translate("FarmView", "Fetch", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.renderNodesTab), QtGui.QApplication.translate("FarmView", "Render Nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.jobsTab), QtGui.QApplication.translate("FarmView", "Jobs", None, QtGui.QApplication.UnicodeUTF8))

