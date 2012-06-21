import sys

from PyQt4.QtGui import QMainWindow, QApplication, QTableWidgetItem
from PyQt4.QtCore import QObject, SIGNAL

from listExample import Ui_listMainWindow

class listExample( QMainWindow, Ui_listMainWindow ):
    def __init__( self ):
        QMainWindow.__init__( self )

        # Set up the user interface from Designer.
        self.setupUi( self )

        QObject.connect (self.tableWidget, SIGNAL('cellClicked(int,int)'), self.handleCellClicked)

        self.tableWidget.setRowCount( len( testData ))
        self.tableWidget.setColumnCount( len( testData[0] ))

        rowNumber = 0
        for row in testData:
            columnNumber = 0

            for datum in row:
                self.tableWidget.setItem( rowNumber,
                                          columnNumber,
                                          QTableWidgetItem( datum )
                                          )
                columnNumber += 1

            rowNumber += 1

    def handleCellClicked (self, r, c):
        self.label.setText( self.tableWidget.item( r, c ).text( ) )
        
testData = [ ("one", "this"),
             ("two", "that"),
             ("three", "the other"),
            ]

app = QApplication( sys.argv )
window = listExample( )

window.show( )
retcode = app.exec_( )
sys.exit( retcode )
