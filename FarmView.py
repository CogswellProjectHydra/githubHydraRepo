import sys
import traceback

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_FarmView import Ui_FarmView

import DjangoSetup
from Hydra.models import RenderNode, RenderTask
from django.db import transaction

class FarmView( QMainWindow, Ui_FarmView ):

    def __init__( self ):
        
        QMainWindow.__init__( self )
        self.setupUi( self )

        QObject.connect(self.fetchButton, SIGNAL("clicked()"), self.doFetch)

    @transaction.commit_on_success
    # we WANT a different answer every time this is called,
    # and if we leave django's implicit transaction open we'll
    # always get a consistent, unchanging result.
    def doFetch( self ):



        try:
            records = RenderNode.objects.all( )
            columns = [
                labelAttr( 'host' ),
                labelAttr( 'status' ),
                labelAttr( 'task' )]
            grid = self.renderNodesGrid
            
            for (column, attr) in enumerate( columns ):
                item = grid.itemAtPosition( 0, column )
                if item:
                    grid.removeItem( item )
                    item.widget( ).hide(  )
                grid.addWidget(attr.labelWidget( ) , 0, column )
            
            for (row, record) in enumerate( records ):
                for (column, attr) in enumerate( columns ):
                    item = grid.itemAtPosition( row + 1, column )
                    if item:
                        grid.removeItem( item )
                        item.widget( ).hide( )
                    grid.addWidget(attr.dataWidget( record ),
                                   row + 1,
                                   column,
                                   )
        except Exception, e:
            traceback.print_exc( e )
            raise
        

        try:
            records = RenderTask.objects.all( )
            columns = [
                labelAttr( 'id' ),
                labelAttr( 'status' ),
                textAttr( 'logFile' ),
                labelAttr( 'host' ),
                labelAttr( 'command' ),
                labelAttr( 'startTime' ),
                labelAttr( 'endTime' ),
                labelAttr( 'exitCode' )]
            grid = self.jobsGrid
            
            for (column, attr) in enumerate( columns ):
                item = grid.itemAtPosition( 0, column )
                if item:
                    grid.removeItem( item )
                    item.widget( ).hide(  )
                grid.addWidget( attr.labelWidget(  ), 0, column )
            
            for (row, record) in enumerate( records ):
                for (column, attr) in enumerate( columns ):
                    item = grid.itemAtPosition( row + 1, column )
                    if item:
                        grid.removeItem( item )
                        item.widget( ).hide( )
                    grid.addWidget(attr.dataWidget( record ),
                                   row + 1,
                                   column,
                                   )
        except Exception, e:
            traceback.print_exc( e )
            raise

class labelAttr:

    def __init__( self, name ):
        self.name = name

    def labelWidget( self ):
        return QLabel( '<b>' + self.name + '</b>' )

    def data( self, record ):
        return str( getattr( record, self.name ) )

    def dataWidget( self, record ):
        return QLabel( self.data( record ) )

class textAttr( labelAttr ):

    def dataWidget( self, record ):
        w = QLineEdit( )
        w.setText( self.data( record ) )
        w.setReadOnly( True )
        return w
            
if __name__ == '__main__':
    app = QApplication( sys.argv )
    window = FarmView( )

    window.show( )
    retcode = app.exec_( )
    sys.exit( retcode )

