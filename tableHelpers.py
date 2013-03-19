from PyQt4.QtGui import *

class TableWidgetItem (QTableWidgetItem):

    def setIntoTable (self, table, row, column):
        table.setItem (row, column, self)

class WidgetForTable:

    def setIntoTable (self, table, row, column):
        table.setCellWidget (row, column, self)

class LabelForTable (QLabel, WidgetForTable): pass
