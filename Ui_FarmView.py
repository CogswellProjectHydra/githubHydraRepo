# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_FarmView.ui'
#
# Created: Wed Mar 20 19:49:48 2013
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
        self.statusLabel = QtGui.QLabel(self.centralwidget)
        self.statusLabel.setText(_fromUtf8(""))
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.gridLayout.addWidget(self.statusLabel, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.fetchButton = QtGui.QPushButton(self.centralwidget)
        self.fetchButton.setObjectName(_fromUtf8("fetchButton"))
        self.horizontalLayout.addWidget(self.fetchButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
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
        self.onlineThisNodeButton = QtGui.QPushButton(self.layoutWidget)
        self.onlineThisNodeButton.setObjectName(_fromUtf8("onlineThisNodeButton"))
        self.verticalLayout.addWidget(self.onlineThisNodeButton)
        self.offlineThisNodeButton = QtGui.QPushButton(self.layoutWidget)
        self.offlineThisNodeButton.setObjectName(_fromUtf8("offlineThisNodeButton"))
        self.verticalLayout.addWidget(self.offlineThisNodeButton)
        self.getOffThisNodeButton = QtGui.QPushButton(self.layoutWidget)
        self.getOffThisNodeButton.setObjectName(_fromUtf8("getOffThisNodeButton"))
        self.verticalLayout.addWidget(self.getOffThisNodeButton)
        self.layoutWidget1 = QtGui.QWidget(self.thisNodeTab)
        self.layoutWidget1.setGeometry(QtCore.QRect(120, 20, 651, 87))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.formLayout = QtGui.QFormLayout(self.layoutWidget1)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.nodeNameLabelLabel = QtGui.QLabel(self.layoutWidget1)
        self.nodeNameLabelLabel.setObjectName(_fromUtf8("nodeNameLabelLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.nodeNameLabelLabel)
        self.nodeNameLabel = QtGui.QLabel(self.layoutWidget1)
        self.nodeNameLabel.setText(_fromUtf8(""))
        self.nodeNameLabel.setObjectName(_fromUtf8("nodeNameLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.nodeNameLabel)
        self.nodeStatusLabelLabel = QtGui.QLabel(self.layoutWidget1)
        self.nodeStatusLabelLabel.setObjectName(_fromUtf8("nodeStatusLabelLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.nodeStatusLabelLabel)
        self.nodeStatusLabel = QtGui.QLabel(self.layoutWidget1)
        self.nodeStatusLabel.setText(_fromUtf8(""))
        self.nodeStatusLabel.setObjectName(_fromUtf8("nodeStatusLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.nodeStatusLabel)
        self.taskIDLabelLabel = QtGui.QLabel(self.layoutWidget1)
        self.taskIDLabelLabel.setObjectName(_fromUtf8("taskIDLabelLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.taskIDLabelLabel)
        self.taskIDLabel = QtGui.QLabel(self.layoutWidget1)
        self.taskIDLabel.setText(_fromUtf8(""))
        self.taskIDLabel.setObjectName(_fromUtf8("taskIDLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.taskIDLabel)
        self.nodeVersionLabelLabel = QtGui.QLabel(self.layoutWidget1)
        self.nodeVersionLabelLabel.setObjectName(_fromUtf8("nodeVersionLabelLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.nodeVersionLabelLabel)
        self.nodeVersionLabel = QtGui.QLabel(self.layoutWidget1)
        self.nodeVersionLabel.setText(_fromUtf8(""))
        self.nodeVersionLabel.setObjectName(_fromUtf8("nodeVersionLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.nodeVersionLabel)
        self.layoutWidget2 = QtGui.QWidget(self.thisNodeTab)
        self.layoutWidget2.setGeometry(QtCore.QRect(120, 120, 221, 24))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.formLayout_2 = QtGui.QFormLayout(self.layoutWidget2)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.projectLabel = QtGui.QLabel(self.layoutWidget2)
        self.projectLabel.setObjectName(_fromUtf8("projectLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.projectLabel)
        self.projectComboBox = QtGui.QComboBox(self.layoutWidget2)
        self.projectComboBox.setObjectName(_fromUtf8("projectComboBox"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.projectComboBox)
        self.tabWidget.addTab(self.thisNodeTab, _fromUtf8(""))
        self.renderNodesTab = QtGui.QWidget()
        self.renderNodesTab.setObjectName(_fromUtf8("renderNodesTab"))
        self.gridLayout_6 = QtGui.QGridLayout(self.renderNodesTab)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.renderNodeTable = QtGui.QTableWidget(self.renderNodesTab)
        self.renderNodeTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.renderNodeTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.renderNodeTable.setObjectName(_fromUtf8("renderNodeTable"))
        self.renderNodeTable.setColumnCount(7)
        self.renderNodeTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Wingdings"))
        item.setFont(font)
        self.renderNodeTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.renderNodeTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.renderNodeTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.renderNodeTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.renderNodeTable.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.renderNodeTable.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.renderNodeTable.setHorizontalHeaderItem(6, item)
        self.renderNodeTable.horizontalHeader().setStretchLastSection(True)
        self.renderNodeTable.verticalHeader().setVisible(False)
        self.gridLayout_6.addWidget(self.renderNodeTable, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.onlineRenderNodesButton = QtGui.QPushButton(self.renderNodesTab)
        self.onlineRenderNodesButton.setObjectName(_fromUtf8("onlineRenderNodesButton"))
        self.horizontalLayout_2.addWidget(self.onlineRenderNodesButton)
        self.offlineRenderNodesButton = QtGui.QPushButton(self.renderNodesTab)
        self.offlineRenderNodesButton.setObjectName(_fromUtf8("offlineRenderNodesButton"))
        self.horizontalLayout_2.addWidget(self.offlineRenderNodesButton)
        self.getOffRenderNodesButton = QtGui.QPushButton(self.renderNodesTab)
        self.getOffRenderNodesButton.setObjectName(_fromUtf8("getOffRenderNodesButton"))
        self.horizontalLayout_2.addWidget(self.getOffRenderNodesButton)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
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
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
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
        self.projectLabel.setBuddy(self.projectComboBox)

        self.retranslateUi(FarmView)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(FarmView)

    def retranslateUi(self, FarmView):
        FarmView.setWindowTitle(_translate("FarmView", "FarmView", None))
        self.fetchButton.setText(_translate("FarmView", "Fetch", None))
        self.onlineThisNodeButton.setToolTip(_translate("FarmView", "<html><head/><body><p>Allow this node to accept render tasks</p></body></html>", None))
        self.onlineThisNodeButton.setText(_translate("FarmView", "Online", None))
        self.offlineThisNodeButton.setToolTip(_translate("FarmView", "<html><head/><body><p>Don\'t allow this node to accept any new jobs (it will still finish what it\'s working on)</p></body></html>", None))
        self.offlineThisNodeButton.setText(_translate("FarmView", "Offline", None))
        self.getOffThisNodeButton.setToolTip(_translate("FarmView", "<html><head/><body><p>Tell this node to stop the current job, put it back on the job board, and don\'t accept any more.</p></body></html>", None))
        self.getOffThisNodeButton.setText(_translate("FarmView", "Get Off!", None))
        self.nodeNameLabelLabel.setText(_translate("FarmView", "Node name:", None))
        self.nodeStatusLabelLabel.setText(_translate("FarmView", "Node status:", None))
        self.taskIDLabelLabel.setText(_translate("FarmView", "Task ID:", None))
        self.nodeVersionLabelLabel.setText(_translate("FarmView", "Version:", None))
        self.projectLabel.setText(_translate("FarmView", "Project:", None))
        self.projectComboBox.setWhatsThis(_translate("FarmView", "<html><head/><body><p><br/></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.thisNodeTab), _translate("FarmView", "This Node", None))
        self.renderNodeTable.setSortingEnabled(True)
        item = self.renderNodeTable.horizontalHeaderItem(0)
        item.setText(_translate("FarmView", "þ", None))
        item = self.renderNodeTable.horizontalHeaderItem(1)
        item.setText(_translate("FarmView", "Host", None))
        item = self.renderNodeTable.horizontalHeaderItem(2)
        item.setText(_translate("FarmView", "Status", None))
        item = self.renderNodeTable.horizontalHeaderItem(3)
        item.setText(_translate("FarmView", "Task ID", None))
        item = self.renderNodeTable.horizontalHeaderItem(4)
        item.setText(_translate("FarmView", "Project", None))
        item = self.renderNodeTable.horizontalHeaderItem(5)
        item.setText(_translate("FarmView", "Node Version", None))
        item = self.renderNodeTable.horizontalHeaderItem(6)
        item.setText(_translate("FarmView", "Last heartbeat", None))
        self.onlineRenderNodesButton.setText(_translate("FarmView", "Online", None))
        self.offlineRenderNodesButton.setText(_translate("FarmView", "Offline", None))
        self.getOffRenderNodesButton.setText(_translate("FarmView", "Get Off!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.renderNodesTab), _translate("FarmView", "Render Nodes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.jobsTab), _translate("FarmView", "Jobs", None))

