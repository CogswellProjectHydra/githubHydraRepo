import sys
import traceback
import datetime
import functools

from LoggingSetup import logger

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_FarmView import Ui_FarmView

#import DjangoSetup
#from Hydra.models import RenderNode, RenderTask
#from django.db import transaction

from MySQLSetup import Hydra_rendernode, Hydra_rendertask, Hydra_job, transaction, cur

codes = {'I': 'idle',
         'R': 'ready',
         'A': 'assigned',
         'O': 'offline',
         'F': 'finished',
         'S': 'started'}

class FarmView( QMainWindow, Ui_FarmView ):

    def __init__( self ):
        
        QMainWindow.__init__( self )
        self.setupUi( self )

        QObject.connect(self.fetchButton, SIGNAL("clicked()"), self.doFetch)

    # refresh the display, rebuilding every blessed widget.
    def doFetch( self ):

        with transaction ():
            columns = [
                labelAttr( 'host' ),
                labelAttr( 'status' ),
                labelAttr( 'task_id' ),
                getOffButton ("Get off!!!")]
            setup( Hydra_rendernode.fetch (), columns, self.renderNodesGrid)        

            columns = [
                labelAttr( 'id' ),
                labelAttr( 'status' ),
                textAttr( 'logFile' ),
                labelAttr( 'host' ),
                labelAttr( 'command' ),
                labelAttr( 'startTime' ),
                labelAttr( 'endTime' ),
                labelAttr( 'exitCode' )]
            setup( Hydra_rendertask.fetch (order = "order by id desc",
                                           limit = self.limitSpinBox.value ()), columns, self.jobsGrid)

            cur.execute ("""
select count(status), status from Hydra_rendernode
group by status
""")
            counts = cur.fetchall ()
            logger.debug (counts)
            countString = ", ".join (["%d %s" % (count, codes[status])
                                      for (count, status) in counts]) # KeyError 'S'
            time = datetime.datetime.now().strftime ("%H:%M")
            msg = "%s as of %s" % (countString, time)
            self.statusLabel.setText (msg)

# populate a data grid. The "columns"
# are like widget factory objects.
def setup( records, columns, grid):
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

# labelAttr: a widget factory object for making a label.
# the object's name is the name of a database column.
# to make a label widget, given a record, extract the
# named attribute from the record and use that as the label
# text.
# the labelWidget method makes a widget suitable for the heading
# (first) row of the display.
# the dataWidget method makes a widget that displays actual data.
class labelAttr:

    def __init__( self, name ):
        self.name = name

    def labelWidget( self ):
        return QLabel( '<b>' + self.name + '</b>' )

    def data( self, record ):
        return str( getattr (record, self.name) )
    
    def dataWidget( self, record ):
        return QLabel( self.data( record ) )

# like labelAttr, but makes a read-only text field instead of a label.
class textAttr( labelAttr ):

    def dataWidget( self, record ):
        w = QLineEdit( )
        w.setText( self.data( record ) )
        w.setReadOnly( True )
        return w

# as above, but makes a specialized button to implement the GetOff!!! functionality.            
class getOffButton (labelAttr):

    def dataWidget ( self, record ):
        w = QPushButton( self.name )

        # the click handler is the doGetOff method, but with the record argument already supplied.
        # it's called a "partial application".
        handler = functools.partial (self.doGetOff, record=record)

        QObject.connect (w, SIGNAL("clicked()"), handler)
        return w

    def doGetOff (self, record):
        logger.debug('clobber %s', record.host)

if __name__ == '__main__':
    app = QApplication( sys.argv )
    window = FarmView( )

    window.show( )
    retcode = app.exec_( )
    sys.exit( retcode )

