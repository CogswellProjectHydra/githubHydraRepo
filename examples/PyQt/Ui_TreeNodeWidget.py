# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_TreeNodeWidget.ui'
#
# Created: Sat Jul 14 22:42:38 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TreeNodeWidget(object):
    def setupUi(self, TreeNodeWidget):
        TreeNodeWidget.setObjectName(_fromUtf8("TreeNodeWidget"))
        TreeNodeWidget.resize(470, 331)
        self.gridLayout_2 = QtGui.QGridLayout(TreeNodeWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.nodeWidgetLayout = QtGui.QVBoxLayout()
        self.nodeWidgetLayout.setSpacing(0)
        self.nodeWidgetLayout.setObjectName(_fromUtf8("nodeWidgetLayout"))
        self.verticalLayout_2.addLayout(self.nodeWidgetLayout)
        self.childContainerWidget = QtGui.QWidget(TreeNodeWidget)
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

        self.retranslateUi(TreeNodeWidget)
        QtCore.QMetaObject.connectSlotsByName(TreeNodeWidget)

    def retranslateUi(self, TreeNodeWidget):
        TreeNodeWidget.setWindowTitle(QtGui.QApplication.translate("TreeNodeWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))

