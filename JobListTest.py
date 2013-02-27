import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Ui_JobListTest import Ui_MainWindow

import Servers
from Clients import Client
from Connections import TCPConnection
from Questions import KillCurrentJobQuestion
from MySQLSetup import transaction, Hydra_job, Hydra_rendertask, Hydra_rendernode, IDLE, OFFLINE
import Utils
from LoggingSetup import logger
import pickle
import JobTicket
from JobKill import kill
from MessageBoxes import msgBox, yesNoMsgBox

codes = {'I': 'idle',
         'R': 'ready',
         'O': 'offline',
         'F': 'finished',
         'S': 'started'}

class JobListWindow(QMainWindow, Ui_MainWindow, Client):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.refreshHandler()

        QObject.connect (self.refreshButton, SIGNAL("clicked()"), self.refreshHandler)
        QObject.connect (self.jobTable, SIGNAL ("cellClicked(int,int)"), self.jobCellClickedHandler)
        QObject.connect (self.killJobButton, SIGNAL ("clicked()"), self.killJobButtonHandler)
        QObject.connect (self.killTaskButton, SIGNAL ("clicked()"), self.killTaskButtonHandler)
        
    def refreshHandler (self, *args):
        jobs = Hydra_job.fetch ()
        self.jobTable.setRowCount (len (jobs))
        for pos, job in enumerate (jobs):
            ticket = pickle.loads(job.pickledTicket)
            self.jobTable.setItem (pos, 0, QTableWidgetItem(str(job.id)))
            self.jobTable.setItem (pos, 1, QTableWidgetItem(ticket.name ()))

    def jobCellClickedHandler (self, row, column):
        # populate the task table widget
        item = self.jobTable.item (row, 0)
        taskId = int (item.text ())
        tasks = Hydra_rendertask.fetch ("where job_id = %d" % taskId)
        self.taskTable.setRowCount (len (tasks))
        for pos, task in enumerate (tasks):
            self.taskTable.setItem (pos, 0, QTableWidgetItem (str (task.id)))
            self.taskTable.setItem (pos, 1, QTableWidgetItem (str (task.host)))
            self.taskTable.setItem (pos, 2, QTableWidgetItem (str (task.status)))
            self.taskTable.setItem (pos, 3, QTableWidgetItem (str (task.startTime)))
            self.taskTable.setItem (pos, 4, QTableWidgetItem (str (task.endTime)))

    def killJobButtonHandler (self):
        item = self.jobTable.currentItem ()
        if item and item.isSelected ():
            row = self.jobTable.currentRow ()
            id = int (self.jobTable.item (row, 0).text ())
            choice = yesNoMsgBox(self, "Confirm", "Are you sure you want to kill job " + str(id) + "?")
            if choice == QMessageBox.Yes:
                kill(id)
                self.refreshHandler()
            else:
                msgBox(self, "Abort", "Job " + str(id) + " remains on the farm.")

    def killTaskButtonHandler (self):
        item = self.taskTable.currentItem ()
        if item and item.isSelected ():
            row = self.taskTable.currentRow ()
            id = int (self.taskTable.item (row, 0).text ())
            choice = yesNoMsgBox(self, "Confirm", "Are you sure you want to kill task " + str(id) + "?")
            if choice == QMessageBox.Yes:
                print ('kill task', id)
            else:
                print ('don\'t kill task', id)

                       
if __name__ == '__main__':
    app = QApplication( sys.argv )
    
    window = JobListWindow( )
    
    window.show( )
    retcode = app.exec_( )
    sys.exit( retcode )
