import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_ParentChildTest import Ui_ParentChildTest
from ParentChild import ExampleParentChild

class ParentChildTest( QMainWindow, Ui_ParentChildTest ):

    def __init__( self ):
        
        QMainWindow.__init__( self )
        self.setupUi( self )
        
        for i in range( 333 ):
            pc = ExampleParentChild( )
            self.widgetLayout.addWidget( pc )
            pc.addParentWidget( QLabel( '<a href="toggle">parent %d</a>' % i) )
        
if __name__ == '__main__':
    app = QApplication( sys.argv )
    window = ParentChildTest( )

    window.show( )
    retcode = app.exec_( )
    sys.exit( retcode )
