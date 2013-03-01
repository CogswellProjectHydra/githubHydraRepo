'''
Created on Feb 26, 2013

@author: Aaron Cohn
'''
from PyQt4.QtGui import QMessageBox

def aboutBox(qwidget, title, msg):
    QMessageBox.about(qwidget, title, msg)

def yesNoBox(qwidget, title, msg):
    return QMessageBox.question(qwidget, title, msg, buttons=(QMessageBox.Yes | QMessageBox.No), defaultButton=QMessageBox.Yes)