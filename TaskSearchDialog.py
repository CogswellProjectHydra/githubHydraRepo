'''
Created on Mar 9, 2013

@author: Aaron Cohn
'''
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import QObject, SIGNAL
from Ui_TaskSearchDialog import Ui_taskSearchDialog

class TaskSearchDialog(QDialog, Ui_taskSearchDialog):
    """A dialog box for running queries on Hydra_rendertask."""

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        QObject.connect(self.cancelBtn, SIGNAL("clicked()"), 
                        self.cancelBtnClicked)
        QObject.connect(self.searchBtn, SIGNAL("clicked()"),
                        self.searchBtnClicked)
        
    def getValues(self):
        task_id = str(self.idBox.text())
        host = str(self.hostnameBox.text())
        status = str(self.statusBox.text())
        cmd = str(self.cmdBox.text())
        return (task_id, host, status, cmd)
    
    def cancelBtnClicked(self):
        self.close()
        return None
    
    def searchBtnClicked(self):
        self.close()
        return self.getValues()
    
    @classmethod
    def create(cls):
        dialog = TaskSearchDialog()
        if dialog.exec_():
            values = dialog.getValues()
        return values