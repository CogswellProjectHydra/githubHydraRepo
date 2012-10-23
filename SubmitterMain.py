import sys
import traceback

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from submitter import Ui_MainWindow

from LoggingSetup import logger

from JobTicket import MayaTicket

class SubmitterWindow( QMainWindow, Ui_MainWindow ):

    def __init__( self ):
        """Initializes the Maya render job submission window."""
        
        QMainWindow.__init__( self )
        self.setupUi( self )

        QObject.connect(self.submitButton, SIGNAL("clicked()"), self.doSubmit)

        sys.argv.extend (['1', '1', '1'])
        scene, start, end, by = sys.argv[1:5] # proper command line args would be nice
        scene = scene.replace ('\\', '/')
        self.sceneLabel.setText( scene )
        if 'scenes' not in scene.split ('/'):
            self.errorLabel.setText ('<B>File not in a scene folder.</B>')
            self.submitButton.setVisible (False)
        if ':' in scene:
            self.errorLabel.setText ('<B>Use UNC paths, not mapped drives.</B>')
            self.submitButton.setVisible (False)
                                     
        self.startSpinBox.setValue( eval (start ) )
        self.endSpinBox.setValue( eval( end ) )
        

    def doSubmit( self ):
        """Submits a job ticket for this scene to be split into tasks and processed."""
        
        logger.debug ('doSubmit')

        sceneFile = str( self.sceneLabel.text( ) )
        startFrame = self.startSpinBox.value( )
        endFrame = self.endSpinBox.value( )
        batchSize = self.batchSizeSpinBox.value( )
        if 'scenes' in sceneFile.split ('/'):
            MayaTicket( sceneFile, startFrame, endFrame, batchSize ).submit( )
            self.errorLabel.setText ('Done. Close the window.')


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
    
                      
