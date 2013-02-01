import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Ui_getOff import Ui_MainWindow

from Clients import Client
from Connections import TCPConnection

from Questions import KillCurrentJobQuestion

class getOffWindow(QMainWindow, Ui_MainWindow, Client):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        QObject.connect(self.pushButton, SIGNAL("clicked()"), self.killRenderTask)

    def killRenderTask(self):
        self.connection = TCPConnection()
        self.getAnswer(KillCurrentJobQuestion())
        
if __name__ == '__main__':
    app = QApplication( sys.argv ) # argv should be theoretically empty
    
    window = getOffWindow( )
    
    window.show( )
    retcode = app.exec_( )
    sys.exit( retcode )