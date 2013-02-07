# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'getOff.ui'
#
# Created: Wed Feb 06 21:20:06 2013
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
        MainWindow.resize(319, 122)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 95, 101))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.onlineButton = QtGui.QPushButton(self.widget)
        self.onlineButton.setObjectName(_fromUtf8("onlineButton"))
        self.verticalLayout.addWidget(self.onlineButton)
        self.offlineButton = QtGui.QPushButton(self.widget)
        self.offlineButton.setObjectName(_fromUtf8("offlineButton"))
        self.verticalLayout.addWidget(self.offlineButton)
        self.getoffButton = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.getoffButton.sizePolicy().hasHeightForWidth())
        self.getoffButton.setSizePolicy(sizePolicy)
        self.getoffButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.getoffButton.setObjectName(_fromUtf8("getoffButton"))
        self.verticalLayout.addWidget(self.getoffButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "GET OFF!", None))
        self.onlineButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Set render node status to ONLINE. The node will begin looking for new render jobs to do.</p></body></html>", None))
        self.onlineButton.setText(_translate("MainWindow", "Online", None))
        self.offlineButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Set render node status to OFFLINE. The render node will complete its current job, if any, and stop looking for new jobs.</p></body></html>", None))
        self.offlineButton.setText(_translate("MainWindow", "Offline", None))
        self.getoffButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Kill the current job and set render node status to OFFLINE. The render node will not look for new jobs until its put back on-line.</p></body></html>", None))
        self.getoffButton.setText(_translate("MainWindow", "Get Off!", None))

