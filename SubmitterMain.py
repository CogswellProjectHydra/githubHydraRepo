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

        scene, start, end, by = sys.argv[1:] # proper command line args would be nice
        self.sceneLabel.setText( scene )
        self.startSpinBox.setValue( eval (start ) )
        self.endSpinBox.setValue( eval( end ) )
        

    def doSubmit( self ):
        logger.debug ('doSubmit')

        sceneFile = str( self.sceneLabel.text( ) )
        startFrame = self.startSpinBox.value( )
        endFrame = self.endSpinBox.value( )
        batchSize = self.batchSizeSpinBox.value( )

        starts = range( startFrame, endFrame + 1, batchSize )
        ends = [min( start + batchSize - 1,
                     endFrame )
                for start in starts
                ]
        logger.debug( zip( starts, ends ) )
        for start, end in zip( starts, ends ):
            command = [
                        r'c:\program files\autodesk\maya2011\bin\render.exe',
                        '-mr:v', '5',
                        '-s', str( start ),
                        '-e', str( end ),
                        sceneFile
                      ]
            logger.debug( command )

if __name__ == '__main__':
    try:
        logger.debug(sys.argv)
        app = QApplication( sys.argv )
        
        window = SubmitterWindow( )

        window.show( )
        retcode = app.exec_( )
        sys.exit( retcode )        
    except Exception, e:
        logger.error( traceback.format_exc( e ) )
        raise
    
                      
