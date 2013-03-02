# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_SubmissionWindow.ui'
#
# Created: Sun Jul 15 13:50:40 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SubmissionWindow(object):
    def setupUi(self, SubmissionWindow):
        SubmissionWindow.setObjectName(_fromUtf8("SubmissionWindow"))
        SubmissionWindow.resize(391, 190)
        self.centralwidget = QtGui.QWidget(SubmissionWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 369, 132))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.widgetGridLayout = QtGui.QGridLayout()
        self.widgetGridLayout.setObjectName(_fromUtf8("widgetGridLayout"))
        self.gridLayout_2.addLayout(self.widgetGridLayout, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        SubmissionWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SubmissionWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 391, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        SubmissionWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(SubmissionWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SubmissionWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SubmissionWindow)
        QtCore.QMetaObject.connectSlotsByName(SubmissionWindow)

    def retranslateUi(self, SubmissionWindow):
        SubmissionWindow.setWindowTitle(QtGui.QApplication.translate("SubmissionWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))

