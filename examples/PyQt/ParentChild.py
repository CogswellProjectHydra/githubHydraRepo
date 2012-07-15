from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_ParentChild import Ui_ParentChild

class ParentChild( QWidget, Ui_ParentChild ):

    def __init__( self ):
        
        QWidget.__init__( self )
        self.setupUi( self )
        
        self.needsChildren = True        
        self.childContainerWidget.setVisible( False )

    def addParentWidget( self, parentWidget ):
        
        self.parentWidget = parentWidget
        self.parentWidgetLayout.addWidget( parentWidget )
        QObject.connect(parentWidget, SIGNAL("linkActivated(QString)"), self.dispatchOnLink)

    def addChildWidget( self, childWidget ):

        self.childContainerLayout.addWidget( childWidget )

    def dispatchOnLink( self, anchor ):
        
        method = getattr( self, str( anchor ) )
        method ( )

    def toggle( self ):
        
        self.childContainerWidget.setVisible( not self.childContainerWidget.isVisible( ) )

        if self.needsChildren and self.childContainerWidget.isVisible( ):
            self.generateChildren( )
            self.needsChildren = False

    def generateChildren( self ):
        pass
        
class ExampleParentChild( ParentChild ):

    def generateChildren( self ):
        for j in range( 1, 9 ):
            self.addChildWidget( QLabel( "%s.%d" % (self.parentWidget.text( ),j) ) )
        
