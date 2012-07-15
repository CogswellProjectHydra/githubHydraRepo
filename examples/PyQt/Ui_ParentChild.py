# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_parentChild.ui'
#
# Created: Sat Jul 14 21:29:20 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ParentChild(object):
    def setupUi(self, ParentChild):
        ParentChild.setObjectName(_fromUtf8("ParentChild"))
        ParentChild.resize(470, 331)
        self.gridLayout_2 = QtGui.QGridLayout(ParentChild)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.parentWidgetLayout = QtGui.QVBoxLayout()
        self.parentWidgetLayout.setSpacing(0)
        self.parentWidgetLayout.setObjectName(_fromUtf8("parentWidgetLayout"))
        self.verticalLayout_2.addLayout(self.parentWidgetLayout)
        self.childContainerWidget = QtGui.QWidget(ParentChild)
        self.childContainerWidget.setObjectName(_fromUtf8("childContainerWidget"))
        self.gridLayout = QtGui.QGridLayout(self.childContainerWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(-1, 0, 0, 0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.childContainerLayout = QtGui.QVBoxLayout()
        self.childContainerLayout.setSpacing(0)
        self.childContainerLayout.setMargin(0)
        self.childContainerLayout.setObjectName(_fromUtf8("childContainerLayout"))
        self.gridLayout.addLayout(self.childContainerLayout, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.childContainerWidget)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(ParentChild)
        QtCore.QMetaObject.connectSlotsByName(ParentChild)

    def retranslateUi(self, ParentChild):
        ParentChild.setWindowTitle(QtGui.QApplication.translate("ParentChild", "Form", None, QtGui.QApplication.UnicodeUTF8))

