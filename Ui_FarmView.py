# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_FarmView.ui'
#
# Created: Thu Feb 21 11:04:05 2013
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
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.statusLabel = QtGui.QLabel(self.centralwidget)
        self.statusLabel.setText(_fromUtf8(""))
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.gridLayout.addWidget(self.statusLabel, 1, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.thisNodeTab = QtGui.QWidget()
        self.thisNodeTab.setObjectName(_fromUtf8("thisNodeTab"))
        self.layoutWidget = QtGui.QWidget(self.thisNodeTab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 95, 100))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.onlineButton = QtGui.QPushButton(self.layoutWidget)
        self.onlineButton.setObjectName(_fromUtf8("onlineButton"))
        self.verticalLayout.addWidget(self.onlineButton)
        self.offlineButton = QtGui.QPushButton(self.layoutWidget)
        self.offlineButton.setObjectName(_fromUtf8("offlineButton"))
        self.verticalLayout.addWidget(self.offlineButton)
        self.getOffButton = QtGui.QPushButton(self.layoutWidget)
        self.getOffButton.setObjectName(_fromUtf8("getOffButton"))
        self.verticalLayout.addWidget(self.getOffButton)
        self.layoutWidget1 = QtGui.QWidget(self.thisNodeTab)
        self.layoutWidget1.setGeometry(QtCore.QRect(120, 20, 641, 64))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.formLayout = QtGui.QFormLayout(self.layoutWidget1)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.nodeNameLabelLabel = QtGui.QLabel(self.layoutWidget1)
        self.nodeNameLabelLabel.setObjectName(_fromUtf8("nodeNameLabelLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.nodeNameLabelLabel)
        self.nodeNameLabel = QtGui.QLabel(self.layoutWidget1)
        self.nodeNameLabel.setObjectName(_fromUtf8("nodeNameLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.nodeNameLabel)
        self.nodeStatusLabelLabel = QtGui.QLabel(self.layoutWidget1)
        self.nodeStatusLabelLabel.setObjectName(_fromUtf8("nodeStatusLabelLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.nodeStatusLabelLabel)
        self.nodeStatusLabel = QtGui.QLabel(self.layoutWidget1)
        self.nodeStatusLabel.setObjectName(_fromUtf8("nodeStatusLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.nodeStatusLabel)
        self.taskIDLabelLabel = QtGui.QLabel(self.layoutWidget1)
        self.taskIDLabelLabel.setObjectName(_fromUtf8("taskIDLabelLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.taskIDLabelLabel)
        self.taskIDLabel = QtGui.QLabel(self.layoutWidget1)
        self.taskIDLabel.setObjectName(_fromUtf8("taskIDLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.taskIDLabel)
        self.tabWidget.addTab(self.thisNodeTab, _fromUtf8(""))
        self.renderNodesTab = QtGui.QWidget()
        self.renderNodesTab.setObjectName(_fromUtf8("renderNodesTab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.renderNodesTab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.scrollArea = QtGui.QScrollArea(self.renderNodesTab)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 98, 31))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_3 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.renderNodesGrid = QtGui.QGridLayout()
        self.renderNodesGrid.setObjectName(_fromUtf8("renderNodesGrid"))
        self.gridLayout_3.addLayout(self.renderNodesGrid, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 1, 1)
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
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 98, 62))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.limitSpinBox = QtGui.QSpinBox(self.scrollAreaWidgetContents_2)
        self.limitSpinBox.setMaximum(999)
        self.limitSpinBox.setProperty("value", 100)
        self.limitSpinBox.setObjectName(_fromUtf8("limitSpinBox"))
        self.gridLayout_2.addWidget(self.limitSpinBox, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 2, 0, 1, 1)
        self.jobsGrid = QtGui.QGridLayout()
        self.jobsGrid.setObjectName(_fromUtf8("jobsGrid"))
        self.gridLayout_2.addLayout(self.jobsGrid, 1, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.jobsTab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        FarmView.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(FarmView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        FarmView.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(FarmView)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        FarmView.setStatusBar(self.statusbar)

        self.retranslateUi(FarmView)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FarmView)

    def retranslateUi(self, FarmView):
        FarmView.setWindowTitle(_translate("FarmView", "FarmView", None))
        self.fetchButton.setText(_translate("FarmView", "Fetch", None))
        self.onlineButton.setText(_translate("FarmView", "Online", None))
        self.offlineButton.setText(_translate("FarmView", "Offline", None))
        self.getOffButton.setText(_translate("FarmView", "Get Off!", None))
        self.nodeNameLabelLabel.setText(_translate("FarmView", "Node name:", None))
        self.nodeNameLabel.setText(_translate("FarmView", "(empty)", None))
        self.nodeStatusLabelLabel.setText(_translate("FarmView", "Node status:", None))
        self.nodeStatusLabel.setText(_translate("FarmView", "(empty)", None))
        self.taskIDLabelLabel.setText(_translate("FarmView", "Task ID:", None))
        self.taskIDLabel.setText(_translate("FarmView", "(empty)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.thisNodeTab), _translate("FarmView", "This Node", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.renderNodesTab), _translate("FarmView", "Render Nodes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.jobsTab), _translate("FarmView", "Jobs", None))

