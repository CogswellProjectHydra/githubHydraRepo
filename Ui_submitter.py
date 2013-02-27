# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_submitter.ui'
#
# Created: Wed Feb 27 01:12:40 2013
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
        MainWindow.resize(280, 273)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.sceneLabel = QtGui.QLabel(self.centralwidget)
        self.sceneLabel.setObjectName(_fromUtf8("sceneLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.sceneLabel)
        self.sceneText = QtGui.QLineEdit(self.centralwidget)
        self.sceneText.setText(_fromUtf8(""))
        self.sceneText.setReadOnly(True)
        self.sceneText.setObjectName(_fromUtf8("sceneText"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.sceneText)
        self.projectDirLabel = QtGui.QLabel(self.centralwidget)
        self.projectDirLabel.setObjectName(_fromUtf8("projectDirLabel"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.projectDirLabel)
        self.projectDirLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.projectDirLineEdit.setReadOnly(True)
        self.projectDirLineEdit.setObjectName(_fromUtf8("projectDirLineEdit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.projectDirLineEdit)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.startFrameLabel = QtGui.QLabel(self.centralwidget)
        self.startFrameLabel.setObjectName(_fromUtf8("startFrameLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.startFrameLabel)
        self.startSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.startSpinBox.setMaximum(99999)
        self.startSpinBox.setObjectName(_fromUtf8("startSpinBox"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.startSpinBox)
        self.endFrameLabel = QtGui.QLabel(self.centralwidget)
        self.endFrameLabel.setObjectName(_fromUtf8("endFrameLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.endFrameLabel)
        self.endSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.endSpinBox.setMaximum(99999)
        self.endSpinBox.setObjectName(_fromUtf8("endSpinBox"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.endSpinBox)
        self.renderNodesLabel = QtGui.QLabel(self.centralwidget)
        self.renderNodesLabel.setObjectName(_fromUtf8("renderNodesLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.renderNodesLabel)
        self.numJobsSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.numJobsSpinBox.setMaximum(999)
        self.numJobsSpinBox.setProperty("value", 1)
        self.numJobsSpinBox.setObjectName(_fromUtf8("numJobsSpinBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.numJobsSpinBox)
        self.priorityLabel = QtGui.QLabel(self.centralwidget)
        self.priorityLabel.setObjectName(_fromUtf8("priorityLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.priorityLabel)
        self.prioritySpinBox = QtGui.QSpinBox(self.centralwidget)
        self.prioritySpinBox.setProperty("value", 50)
        self.prioritySpinBox.setObjectName(_fromUtf8("prioritySpinBox"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.prioritySpinBox)
        self.projectLabel = QtGui.QLabel(self.centralwidget)
        self.projectLabel.setObjectName(_fromUtf8("projectLabel"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.projectLabel)
        self.projectComboBox = QtGui.QComboBox(self.centralwidget)
        self.projectComboBox.setMinimumSize(QtCore.QSize(171, 22))
        self.projectComboBox.setObjectName(_fromUtf8("projectComboBox"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.projectComboBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.submitButton = QtGui.QPushButton(self.centralwidget)
        self.submitButton.setObjectName(_fromUtf8("submitButton"))
        self.verticalLayout.addWidget(self.submitButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.startFrameLabel.setBuddy(self.startSpinBox)
        self.endFrameLabel.setBuddy(self.endSpinBox)
        self.renderNodesLabel.setBuddy(self.numJobsSpinBox)
        self.priorityLabel.setBuddy(self.prioritySpinBox)
        self.projectLabel.setBuddy(self.projectComboBox)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.startSpinBox, self.endSpinBox)
        MainWindow.setTabOrder(self.endSpinBox, self.numJobsSpinBox)
        MainWindow.setTabOrder(self.numJobsSpinBox, self.prioritySpinBox)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Submitter", None))
        self.sceneLabel.setText(_translate("MainWindow", "scene:", None))
        self.sceneText.setPlaceholderText(_translate("MainWindow", "scene name here", None))
        self.projectDirLabel.setText(_translate("MainWindow", "project dir:", None))
        self.projectDirLineEdit.setToolTip(_translate("MainWindow", "If Submitter failed to locate your project directory automatically, double-click in the text box to set it manually.", None))
        self.projectDirLineEdit.setPlaceholderText(_translate("MainWindow", "click to set project directory", None))
        self.startFrameLabel.setText(_translate("MainWindow", "start frame:", None))
        self.endFrameLabel.setText(_translate("MainWindow", "end frame:", None))
        self.renderNodesLabel.setText(_translate("MainWindow", "<html><head/><body><p># of render<br/>nodes to use:</p></body></html>", None))
        self.priorityLabel.setText(_translate("MainWindow", "priority:", None))
        self.projectLabel.setText(_translate("MainWindow", "Project:", None))
        self.submitButton.setText(_translate("MainWindow", "Submit", None))

