import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Ui_getOff import Ui_MainWindow

from Clients import Client
from Connections import TCPConnection
from Questions import KillCurrentJobQuestion
from MySQLSetup import transaction, Hydra_rendernode, IDLE, OFFLINE
import Utils
from LoggingSetup import logger

class getOffWindow(QMainWindow, Ui_MainWindow, Client):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        QObject.connect(self.onlineButton, SIGNAL("clicked()"), self.getOnline)
        QObject.connect(self.offlineButton, SIGNAL("clicked()"), self.getOffline)
        QObject.connect(self.getoffButton, SIGNAL("clicked()"), self.killRenderTask)

    def killRenderTask(self):
        """Sends a message to the render node server running on localhost to kill its current task"""
        self.getOffline()
        self.connection = TCPConnection()
        self.getAnswer(KillCurrentJobQuestion())
        
    def getOnline(self):
        """Changes the local render node's status to  on-line if it wasn't on-line already"""
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
    retcode = app.exec_( )
    sys.exit( retcode )