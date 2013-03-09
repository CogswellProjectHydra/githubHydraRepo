import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Ui_JobListTest import Ui_MainWindow
from TaskSearchDialog import TaskSearchDialog

import Servers
from Clients import Client
from Connections import TCPConnection
from MySQLSetup import (transaction, Hydra_job, Hydra_rendertask, 
                        Hydra_rendernode, IDLE, OFFLINE)
from MySQLdb import Error as sqlerror
import Utils
from LoggingSetup import logger
import pickle
import JobTicket
from JobKill import killJob, killTask
from MessageBoxes import aboutBox, yesNoBox
from datetime import datetime as dt


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

        QObject.connect (self.refreshButton, SIGNAL("clicked()"), 
                         self.refreshHandler)
        QObject.connect (self.jobTable, SIGNAL ("cellClicked(int,int)"), 
                         self.jobCellClickedHandler)
        QObject.connect (self.killJobButton, SIGNAL ("clicked()"), 
                         self.killJobButtonHandler)
        QObject.connect (self.killTaskButton, SIGNAL ("clicked()"), 
                         self.killTaskButtonHandler)
        QObject.connect (self.advancedSearchButton, SIGNAL ("clicked()"),
                         self.advancedSearchButtonClicked)
        
    def refreshHandler (self, *args):
        try:
            jobs = Hydra_job.fetch ()
            self.jobTable.setRowCount (len (jobs))
            for pos, job in enumerate (jobs):
                ticket = pickle.loads(job.pickledTicket)
                self.jobTable.setItem (pos, 0, 
                                       QTableWidgetItem_int(str(job.id)))
                self.jobTable.setItem (pos, 1, 
                                       QTableWidgetItem(ticket.name ()))
        except sqlerror as err:
            logger.debug(str(err))
            aboutBox(self, "SQL error", str(err))

    def jobCellClickedHandler (self, row, column):
        # populate the task table widget
        item = self.jobTable.item (row, 0)
        job_id = int (item.text ())
        self.taskTableLabel.setText("Task List (job: " + item.text() + ")")
        try:
            tasks = Hydra_rendertask.fetch ("where job_id = %d" % job_id)
            self.taskTable.setRowCount (len (tasks))
            for pos, task in enumerate (tasks):
                # calcuate time difference
                tdiff = None
                if task.endTime:
                    tdiff = task.endTime - task.startTime
                elif task.startTime:
                    tdiff = dt.now().replace(microsecond=0) - task.startTime
                
                # populate table
                self.taskTable.setItem(pos, 0, 
                                       QTableWidgetItem_int(str(task.id)))
                self.taskTable.setItem(pos, 1, 
                                       QTableWidgetItem(str(task.host)))
                self.taskTable.setItem(pos, 2, 
                                       QTableWidgetItem(str(task.status)))
                self.taskTable.setItem(pos, 3, 
                                       QTableWidgetItem_dt(task.startTime))
                self.taskTable.setItem(pos, 4, 
                                       QTableWidgetItem_dt(task.endTime))
                self.taskTable.setItem(pos, 5, QTableWidgetItem(str(tdiff)))
        except sqlerror as err:
            aboutBox(self, "SQL Error", str(err))
            
    def advancedSearchButtonClicked(self):
        TaskSearchDialog.create()

    def killJobButtonHandler (self):
        item = self.jobTable.currentItem ()
        if item and item.isSelected ():
            row = self.jobTable.currentRow ()
            id = int (self.jobTable.item (row, 0).text ())
            choice = yesNoBox(self, "Confirm", "Really kill job {:d}?"
                              .format(id))
            if choice == QMessageBox.Yes:
                try:
                    if killJob(id):
                        aboutBox(self, "Error", "Some nodes couldn't kill their"
                                 + " tasks.")
                    self.jobCellClickedHandler(self.taskTable.currentRow(), 0)
                except sqlerror as err:
                    logger.debug(str(err))
                    aboutBox(self, "SQL Error", str(err))

    def killTaskButtonHandler (self):
        item = self.taskTable.currentItem ()
        if item and item.isSelected ():
            row = self.taskTable.currentRow ()
            id = int (self.taskTable.item (row, 0).text ())
            choice = yesNoBox(self, "Confirm", "Really kill task {:d}?"
                              .format(id))
            if choice == QMessageBox.Yes:
                if killTask(id):
                    aboutBox(self, "Error", "Task couldn't be killed.")

class QTableWidgetItem_int(QTableWidgetItem):
    """A QTableWidgetItem which holds integer data and sorts it properly."""
    
    def __init__(self, stringValue):
        QTableWidgetItem.__init__(self, stringValue)
    
    def __lt__(self, other):
        return int(self.text()) < int(other.text())

class QTableWidgetItem_dt(QTableWidgetItem):
    """A QTableWidgetItem which holds datetime data and sorts it properly."""

    def __init__(self, dtValue):
        QTableWidgetItem.__init__(self, str(dtValue))
        self.dtValue = dtValue
    
    def __lt__(self, other):
        return self.dtValue - other.dtValue
                       
if __name__ == '__main__':
    app = QApplication( sys.argv )
    
    window = JobListWindow( )
    
    window.show( )
    retcode = app.exec_( )
    sys.exit( retcode )
