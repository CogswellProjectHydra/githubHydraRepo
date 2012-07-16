import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from RenderLayerPseudowidget import RenderLayerPseudowidget
from Ui_SubmissionWindow import Ui_SubmissionWindow

class SubmissionWindow( QMainWindow, Ui_SubmissionWindow ):
    """A demo of a tree built with the SubmissionWindow widget.
The main window has a scroller with a vertical layout called widgetLayout,
that's where the test widgets go."""
    def __init__( self ):
        
        QMainWindow.__init__( self )
        self.setupUi( self )
        self.layerPseudowidgets = []

        RenderLayerPseudowidget( ).makeHeaders( self )
##        # make a master control
##        RenderLayerPseudowidget( layerName = "" ).makeWidgets( self, 1 )
        # make a bunch of layers
        for row in range( 1, 6 ):
            rl = RenderLayerPseudowidget( layerName = 'layer_%d' % row )
            rl.makeWidgets( self, row )
            
        
if __name__ == '__main__':
    app = QApplication( sys.argv )
    window = SubmissionWindow( )

    window.show( )
    retcode = app.exec_( )
    sys.exit( retcode )
