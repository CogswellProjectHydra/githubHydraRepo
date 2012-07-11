import sys
from random import random, randint

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from DBViewer_UI import Ui_DBWindow

import DjangoSetup
from Hydra.models import RenderTask

class DBWindow( QMainWindow, Ui_DBWindow ):

    def __init__( self ):
        
        QMainWindow.__init__( self )
        self.setupUi( self )

        QObject.connect(self.fetchButton, SIGNAL("clicked()"), self.doFetch)

    
    def doFetch( self ):
        
        print( "Fetching record" )
        
        try:
            records = RenderTask.objects.all( )
            print( len( records ) )
            columns = [
                'id',
                'status',
                'logFile',
                'host',
                'command',
                'startTime',
                'endTime',
                'exitCode']
            table = self.tableWidget
            table.setRowCount( len( records)  )
            table.setColumnCount( len( columns ) )
            
            for (column, attr) in enumerate( columns ):
                self.tableWidget.setHorizontalHeaderItem( column, QTableWidgetItem( attr ) )
            
            for (row, record) in enumerate( records ):
                for (column, attr) in enumerate( columns ):
                    table.setItem( row,
                                   column,
                                   QTableWidgetItem( str( getattr( record, attr ) ) )
                                   )
            table.resizeColumnsToContents( )
        except Exception, e:
            traceback.print_exc( e )
            raise
        
class Record( ):
 
    columns = ['x', 'y', 'z']
    nColumns = len( columns )
    
    def __init__( self ):
        for column in self.columns:
            setattr( self, column, random( ) )
            
if __name__ == '__main__':
    app = QApplication( sys.argv )
    window = DBWindow( )

    window.show( )
    retcode = app.exec_( )
    sys.exit( retcode )

