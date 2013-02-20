import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Ui_JobListTest import Ui_MainWindow

import Servers
from Clients import Client
from Connections import TCPConnection
from Questions import KillCurrentJobQuestion
from MySQLSetup import transaction, Hydra_rendernode, IDLE, OFFLINE
import Utils
from LoggingSetup import logger
import pickle
import JobTicket

from MySQLSetup import Hydra_rendernode, Hydra_rendertask, Hydra_job, transaction, cur


codes = {'I': 'idle',
         'R': 'ready',
         'O': 'offline',
         'F': 'finished',
         'S': 'started'}

class JobListWindow(QMainWindow, Ui_MainWindow, Client):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        QObject.connect (self.refreshButton, SIGNAL("clicked()"), self.refreshHandler)
        # register buttons
        # start a thread to refresh the job table every now and then

    def refreshHandler (self, *args):
        jobs = Hydra_job.fetch ()
        self.jobTable.setRowCount (len (jobs))
        for pos, job in enumerate (jobs):
            ticket = pickle.loads(job.pickledTicket)
            self.jobTable.setItem (pos, 0, QTableWidgetItem(ticket.sceneFile))

            self.jobTable.setItem (pos, 1, QTableWidgetItem(str(job.id)))
        
if __name__ == '__main__':
    app = QApplication( sys.argv )
    
    window = JobListWindow( )
    
    window.show( )
    retcode = app.exec_( )
    sys.exit( retcode )
