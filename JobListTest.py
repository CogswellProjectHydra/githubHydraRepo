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

codes = {'I': 'idle',
         'R': 'ready',
         'O': 'offline',
         'F': 'finished',
         'S': 'started'}

class JobListWindow(QMainWindow, Ui_MainWindow, Client):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        # register buttons
        # start a thread to refresh the job table every now and then
        
if __name__ == '__main__':
    app = QApplication( sys.argv )
    
    window = JobListWindow( )
    
    window.show( )
    retcode = app.exec_( )
    sys.exit( retcode )