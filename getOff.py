import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Ui_getOff import Ui_MainWindow

import Servers
from Clients import Client
from Connections import TCPConnection
from Questions import KillCurrentJobQuestion
from MySQLSetup import transaction, Hydra_rendernode, IDLE, OFFLINE, READY
import Utils
from LoggingSetup import logger

codes = {'I': 'idle',
         'R': 'ready',
         'O': 'offline',
         'F': 'finished',
         'S': 'started'}

class getOffWindow(QMainWindow, Ui_MainWindow, Client):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        QObject.connect(self.onlineButton, SIGNAL("clicked()"), self.getOnline)
        QObject.connect(self.offlineButton, SIGNAL("clicked()"), self.getOffline)
        QObject.connect(self.getoffButton, SIGNAL("clicked()"), self.killRenderTask)
        
        self.server = Servers.Server()
    
    def updateRenderNodeInfo(self):
        with transaction():
            [thisNode] = Hydra_rendernode.fetch ("where host = '%s'" % Utils.myHostName( ))
            
        self.nameLabel.setText("Node name: " + thisNode.host)
        self.statusLabel.setText("Status: " + codes[thisNode.status])
        self.jobLabel.setText("Job id: " + thisNode.task_id)

    def killRenderTask(self):
        """Sends a message to the render node server running on localhost to kill its current task"""
        self.getOffline()
        self.connection = TCPConnection()
        killed = self.getAnswer(KillCurrentJobQuestion(statusAfterDeath=READY))
        if not killed:
            logger.debug("There was a problem killing the task.")
        
    def getOnline(self):
        """Changes the local render node's status to on-line if it wasn't on-line already"""
        with transaction():
            [thisNode] = Hydra_rendernode.fetch ("where host = '%s'" % Utils.myHostName( ))
            if thisNode.status == OFFLINE:
                thisNode.status = IDLE
                thisNode.update()
            else:
                logger.debug("Node is already online.")
            
    def getOffline(self):
        with transaction():
            [thisNode] = Hydra_rendernode.fetch ("where host = '%s'" % Utils.myHostName( ))
            thisNode.status = OFFLINE
            thisNode.update()
        
if __name__ == '__main__':
    app = QApplication( sys.argv )
    
    window = getOffWindow( )
    
    window.show( )
    # window.server.createIdleLoop(5, window.updateRenderNodeInfo) -- can't make it stop?
    retcode = app.exec_( )
    sys.exit( retcode )