import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_TreeNodeWidgetTest import Ui_TreeNodeWidgetTest
from TreeNodeWidget import ExampleTreeNodeWidget

class TreeNodeWidgetTest( QMainWindow, Ui_TreeNodeWidgetTest ):
    """A demo of a tree built with the TreeNodeWidget widget.
The main window has a scroller with a vertical layout called widgetLayout,
that's where the test widgets go."""
    def __init__( self ):
        
        QMainWindow.__init__( self )
        self.setupUi( self )
        
        # make a ton of nodes
        for i in range( 666 ):
            pc = ExampleTreeNodeWidget( )
            
            self.widgetLayout.addWidget( pc )
            # put a label in as the main part of the node, and have it fire the toggle method when clicked.
            pc.addNodeWidget( QLabel( '<a href="toggle">parent %d</a>' % i) )
        
if __name__ == '__main__':
    app = QApplication( sys.argv )
    window = TreeNodeWidgetTest( )

    window.show( )
    retcode = app.exec_( )
    sys.exit( retcode )
