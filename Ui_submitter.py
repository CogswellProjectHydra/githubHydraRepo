# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'submitter.ui'
#
# Created: Wed Jan 23 18:11:36 2013
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
        MainWindow.resize(901, 215)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(652, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        self.endSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.endSpinBox.setMaximum(99999)
        self.endSpinBox.setObjectName(_fromUtf8("endSpinBox"))
        self.gridLayout.addWidget(self.endSpinBox, 3, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(652, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.startSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.startSpinBox.setMaximum(99999)
        self.startSpinBox.setObjectName(_fromUtf8("startSpinBox"))
        self.gridLayout.addWidget(self.startSpinBox, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.sceneLabel = QtGui.QLabel(self.centralwidget)
        self.sceneLabel.setObjectName(_fromUtf8("sceneLabel"))
        self.gridLayout.addWidget(self.sceneLabel, 0, 1, 1, 2)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.batchSizeSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.batchSizeSpinBox.setMaximum(999)
        self.batchSizeSpinBox.setProperty("value", 10)
        self.batchSizeSpinBox.setObjectName(_fromUtf8("batchSizeSpinBox"))
        self.gridLayout.addWidget(self.batchSizeSpinBox, 4, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(652, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 2, 1, 1)
        self.submitButton = QtGui.QPushButton(self.centralwidget)
        self.submitButton.setObjectName(_fromUtf8("submitButton"))
        self.gridLayout.addWidget(self.submitButton, 6, 2, 1, 1)
        self.errorLabel = QtGui.QLabel(self.centralwidget)
        self.errorLabel.setText(_fromUtf8(""))
        self.errorLabel.setObjectName(_fromUtf8("errorLabel"))
        self.gridLayout.addWidget(self.errorLabel, 1, 1, 1, 2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.prioritySpinBox = QtGui.QSpinBox(self.centralwidget)
        self.prioritySpinBox.setProperty("value", 50)
        self.prioritySpinBox.setObjectName(_fromUtf8("prioritySpinBox"))
        self.gridLayout.addWidget(self.prioritySpinBox, 5, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 901, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Submitter", None))
        self.label_4.setText(_translate("MainWindow", "batch size:", None))
        self.label_3.setText(_translate("MainWindow", "end frame:", None))
        self.label_2.setText(_translate("MainWindow", "start frame:", None))
        self.sceneLabel.setText(_translate("MainWindow", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbccccccccccccccccccccccc", None))
        self.label.setText(_translate("MainWindow", "scene:", None))
        self.submitButton.setText(_translate("MainWindow", "Submit", None))
        self.label_5.setText(_translate("MainWindow", "priority:", None))

