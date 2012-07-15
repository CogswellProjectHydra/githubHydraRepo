# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_TreeNodeWidgetTest.ui'
#
# Created: Sat Jul 14 22:47:56 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TreeNodeWidgetTest(object):
    def setupUi(self, TreeNodeWidgetTest):
        TreeNodeWidgetTest.setObjectName(_fromUtf8("TreeNodeWidgetTest"))
        TreeNodeWidgetTest.resize(800, 600)
        self.centralwidget = QtGui.QWidget(TreeNodeWidgetTest)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 778, 542))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.widgetLayout = QtGui.QVBoxLayout()
        self.widgetLayout.setSpacing(0)
        self.widgetLayout.setObjectName(_fromUtf8("widgetLayout"))
        self.gridLayout.addLayout(self.widgetLayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        TreeNodeWidgetTest.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(TreeNodeWidgetTest)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        TreeNodeWidgetTest.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(TreeNodeWidgetTest)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        TreeNodeWidgetTest.setStatusBar(self.statusbar)

        self.retranslateUi(TreeNodeWidgetTest)
        QtCore.QMetaObject.connectSlotsByName(TreeNodeWidgetTest)

    def retranslateUi(self, TreeNodeWidgetTest):
        TreeNodeWidgetTest.setWindowTitle(QtGui.QApplication.translate("TreeNodeWidgetTest", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))

