from PyQt4.QtGui import *
from PyQt4.QtCore import *

class RenderLayerPseudowidget( ):

    def __init__( self,
                  layerName = "undefined",
                  render = True,
                  startFrame = 0, endFrame = 0, batchSize = 0,
                  ):
        self.layerName = layerName
        self.render = render
        self.startFrame = startFrame
        self.endFrame = endFrame
        self.batchSize = batchSize

    nColumns = 5
    def widgetData( self ):
        # list of (colum name, column data, column number)
        return [('Name', QLabel( self.layerName ), 0),
                ('Render', makeCheckBox( self.render ), 1),
                ('Start', makeSpinBox( self.startFrame ), 2),
                ('End', makeSpinBox( self.endFrame ), 3),
                ('Batch', makeSpinBox( self.batchSize ), 4),
                ]

    def makeHeaders( self, submissionWindow ):
        for name, _, column in self.widgetData( ):
            label = QLabel( '<u>%s</u>' % name )
            submissionWindow.widgetGridLayout.addWidget( label, 0, column )
    
    def makeWidgets( self, submissionWindow, row):
        for name, widget, column in self.widgetData( ):
            submissionWindow.widgetGridLayout.addWidget( widget, row, column )
            submissionWindow.layerPseudowidgets.append( self )
    
def makeSpinBox( i, min = 0, max = 99999 ):
    box = QSpinBox( )
    box.setMinimum( min )
    box.setMaximum( max )
    box.setValue( i )
    return box

def makeCheckBox( b ):
    box = QCheckBox( "" )
    box.setChecked( b )
    return box


