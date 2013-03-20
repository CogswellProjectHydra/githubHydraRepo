'''
Created on Feb 26, 2013

@author: Aaron Cohn
'''
from PyQt4.QtGui import QMessageBox

def aboutBox(qwidget, title, msg):
    """Creates a message box with an OK button, suitable for displaying short 
    messages to the user."""
    
    QMessageBox.about(qwidget, title, msg)

def yesNoBox(qwidget, title, msg):
    """Creates a message box with Yes and No buttons. Returns QMessageBox.Yes 
    if the user clicked Yes, or QMessageBox.No otherwise."""
    
    return QMessageBox.question(qwidget, title, msg, 
                                buttons=(QMessageBox.Yes | QMessageBox.No), 
                                defaultButton=QMessageBox.Yes)
