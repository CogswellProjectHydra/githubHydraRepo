import sys
import traceback

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from submitter import Ui_MainWindow

import DjangoSetup
from Hydra.models import RenderTask
from django.db import transaction

from LoggingSetup import logger

class SubmitterWindow( QMainWindow, Ui_MainWindow ):

    def __init__( self ):
        
        QMainWindow.__init__( self )
        self.setupUi( self )

        QObject.connect(self.submitButton, SIGNAL("clicked()"), self.doSubmit)

        scene, start, end, by = sys.argv[1:]
        

    def doSubmit( self ):
        logger.debug ('doSubmit')

if __name__ == '__main__':
    logger.debug(sys.argv)
    app = QApplication( sys.argv )
    
    window = SubmitterWindow( )

    window.show( )
    retcode = app.exec_( )
    sys.exit( retcode )        
