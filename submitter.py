# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'submitter.ui'
#
# Created: Thu Jul 26 15:05:51 2012
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
        MainWindow.resize(794, 174)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.sceneLabel = QtGui.QLabel(self.centralwidget)
        self.sceneLabel.setObjectName(_fromUtf8("sceneLabel"))
        self.gridLayout.addWidget(self.sceneLabel, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.startSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.startSpinBox.setMaximum(99999)
        self.startSpinBox.setObjectName(_fromUtf8("startSpinBox"))
        self.gridLayout.addWidget(self.startSpinBox, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(652, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.endSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.endSpinBox.setMaximum(99999)
        self.endSpinBox.setObjectName(_fromUtf8("endSpinBox"))
        self.gridLayout.addWidget(self.endSpinBox, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(652, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.batchSizeSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.batchSizeSpinBox.setMaximum(999)
        self.batchSizeSpinBox.setProperty("value", 10)
        self.batchSizeSpinBox.setObjectName(_fromUtf8("batchSizeSpinBox"))
        self.gridLayout.addWidget(self.batchSizeSpinBox, 3, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(652, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 2, 1, 1)
        self.submitButton = QtGui.QPushButton(self.centralwidget)
        self.submitButton.setObjectName(_fromUtf8("submitButton"))
        self.gridLayout.addWidget(self.submitButton, 4, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Submitter", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "scene:", None, QtGui.QApplication.UnicodeUTF8))
        self.sceneLabel.setText(QtGui.QApplication.translate("MainWindow", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbccccccccccccccccccccccc", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "start frame:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "end frame:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "batch size:", None, QtGui.QApplication.UnicodeUTF8))
        self.submitButton.setText(QtGui.QApplication.translate("MainWindow", "Submit", None, QtGui.QApplication.UnicodeUTF8))

