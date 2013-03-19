import sys
#import traceback
from exceptions import NotImplementedError
import datetime
import functools
import re
from socket import error as socketerror
from MySQLdb import Error as sqlerror

from LoggingSetup import logger

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_FarmView import Ui_FarmView

#import DjangoSetup
#from Hydra.models import RenderNode, RenderTask
#from django.db import transaction

from MySQLSetup import (Hydra_rendernode, Hydra_rendertask, transaction, READY, 
                        OFFLINE, IDLE, PENDING)
from Questions import KillCurrentJobQuestion
import Utils
from Connections import TCPConnection
from MessageBoxes import aboutBox, yesNoBox

codes = {'I': 'idle',
         'R': 'ready',
         'O': 'offline',
         'F': 'finished',
         'S': 'started'}

class FarmView( QMainWindow, Ui_FarmView ):

    def __init__( self ):
        
        QMainWindow.__init__( self )
        self.setupUi( self )

        QObject.connect(self.fetchButton, SIGNAL("clicked()"), self.doFetch)
        QObject.connect(self.onlineButton, SIGNAL("clicked()"), self.online)
        QObject.connect(self.offlineButton, SIGNAL("clicked()"), self.offline)
        QObject.connect(self.getOffButton, SIGNAL("clicked()"), self.getOff)
        QObject.connect(self.projectComboBox, SIGNAL("activated(int)"), 
                        self.projectSelectionHandler)
        
        self.thisNode = None
        self.lastProjectIndex = -1
        self.buttonsEnabled = True

    def getOff(self):
        """Offlines the node and sends a message to the render node server 
        running on localhost tokill its current task"""
        if not self.thisNode:
            aboutBox(self, "Error", "Node information not initialized. Do a "
                     "fetch first.")
            return
        
        self.offline()
        try:
            self.connection = TCPConnection()
            killed = self.getAnswer(KillCurrentJobQuestion(
                                        statusAfterDeath=READY))
            if not killed:
                logger.debug("There was a problem killing the task.")
                aboutBox(self, "Error", "There was a problem killing the task.")
        except socketerror:
            logger.debug(socketerror.message)
            aboutBox(self, "Error", "There was a problem communicating with the"
            "render node software. Either it's not running, or it has become"
            " unresponsive.")
            
        self.updateThisNodeInfo()
        
    def online(self):
        """Changes the local render node's status to online if it wasn't 
        on-line already"""
        
        if not self.thisNode:
            aboutBox(self, "Error", "Node information not initialized."
                     " Do a fetch first.")
            return
        
        if self.thisNode.status == OFFLINE:
            self.thisNode.status = IDLE
            with transaction() as t:
                self.thisNode.update(t)
        else:
            aboutBox(self, "Notice", "Node is already online.")
                
        self.updateThisNodeInfo()
            
    def offline(self):
        """Changes the local render node's status to offline"""
        
        if not self.thisNode:
            aboutBox(self, "Error", "Node information not initialized."
                     " Do a fetch first.")
            return
        
        if self.thisNode.task_id:
            self.thisNode.status = PENDING
        else:
            self.thisNode.status = OFFLINE
        with transaction() as t:
            self.thisNode.update(t)
            
        self.updateThisNodeInfo()
    
    def projectSelectionHandler(self, currentProjectIndex):
        """Checks to see if project selection has changed. If so, handles the 
        change. Else, does nothing."""
        
        if currentProjectIndex != self.lastProjectIndex:
            self.projectChangeHandler(currentProjectIndex)
        
    def projectChangeHandler(self, index):
        """Handler for the event where the project selection changed."""
       
        if not self.thisNode:
            aboutBox(self, "Error", "Node information not initialized. Do a"
            " fetch first.")
            return
        
        selectedProject = self.projectComboBox.itemText(index)
        choice = yesNoBox(self, "Change project", "Reassign this node to " + 
                          selectedProject + "? (will avoid jobs from other"
                          " projects)")
        if choice == QMessageBox.Yes:
            self.thisNode.project = self.projectComboBox.currentText()
            with transaction() as t:
                self.thisNode.update(t)
            self.lastProjectIndex = self.projectComboBox.currentIndex()
            aboutBox(self, "Success", "Node reassigned to " + selectedProject)
        else:
            aboutBox(self, "No changes", "This node will remain assigned to " + 
                     self.thisNode.project + ".")
            self.projectComboBox.setCurrentIndex(self.lastProjectIndex)

    # refresh the display, rebuilding every blessed widget.
    def doFetch( self ):
        """Aggregate method for updating all of the widgets."""
        
        try:
            self.updateThisNodeInfo()
            self.updateRenderNodeTable()
            self.updateRenderTaskGrid()
            self.updateStatusBar()
        except sqlerror:
            aboutBox(self, "Database Error", "There was a problem while trying"
                     " to fetch info from the database.")
        
    def updateThisNodeInfo(self):
        """Updates widgets on the "This Node" tab with the most recent 
        information available."""
        
        # if the buttons are disabled, don't bother
        if not self.buttonsEnabled:
            return
        
        # get the most current info from the database
        node = Hydra_rendernode.fetch ("where host = '%s'" % Utils.myHostName())
        if node:
            [self.thisNode] = node
        
        self.updateProjectComboBox()
        
        if self.thisNode:
            # update the labels
            self.nodeNameLabel.setText(self.thisNode.host)
            self.nodeStatusLabel.setText(codes[self.thisNode.status])
            self.updateTaskIDLabel()
            self.nodeVersionLabel.setText(
                        getSoftwareVersionText(self.thisNode.software_version))
            
            self.setCurrentProjectSelection()
            
        else:
            QMessageBox.about(self, "Notice", "Information about this node"
                              " cannot be displayed because it is not"
                              " registered on the render farm. You may" 
                              " continue to use Farm View, but it must be"
                              " restarted after this node is registered if you"
                              " wish to see this node's information.")
            self.setThisNodeButtonsEnabled(False)
    
    def setThisNodeButtonsEnabled(self, choice):
        """Enables or disables buttons on This Node tab"""
        
        self.onlineButton.setEnabled(choice)
        self.offlineButton.setEnabled(choice)
        self.getOffButton.setEnabled(choice)
        self.projectComboBox.setEnabled(choice)
        self.buttonsEnabled = choice
        
    def updateProjectComboBox(self):
        """Clears and refreshes the contents of the projects dropdown box."""
        
        # remove all items from the dropdown
        count = self.projectComboBox.count()
        while count:
            self.projectComboBox.removeItem(0)
            count = self.projectComboBox.count()
        
        # get current list of projects from the database
        tuples = None
        with transaction() as t:
            t.cur.execute("select * from Hydra_projects")
            tuples = t.cur.fetchall()
        
        # make flat list out of single-element tuples fetched from db
        projectsList = [t for (t,) in tuples]
        
        # refresh the dropdown
        for project in projectsList:
            self.projectComboBox.addItem(project)
    
    def updateTaskIDLabel(self):
        """Get task_id, if exists, update label on This Node tab."""
        
        if self.thisNode.task_id:
            self.taskIDLabel.setText(str(self.thisNode.task_id))
        else:
            self.taskIDLabel.setText("None")
    
    def setCurrentProjectSelection(self):
        """Set project selection based on node's current project setting."""
        
        idx = self.projectComboBox.findText(
                       self.thisNode.project, 
                       flags=Qt.MatchExactly|Qt.MatchCaseSensitive)
        self.projectComboBox.setCurrentIndex(idx)
        self.lastProjectIndex = idx
        
    def updateRenderNodeTable(self):
        rows = Hydra_rendernode.fetch(order="order by host")
        self.renderNodeTable.setRowCount (len (rows))
        columns = [
            lambda o: QTableWidgetItem(str(o.host)),
            lambda o: QTableWidgetItem(str(o.status)),
            lambda o: QTableWidgetItem(str(o.task_id)),
            lambda o: QTableWidgetItem(str(o.project)),
            lambda o: QTableWidgetItem(
                                getSoftwareVersionText(o.software_version)),
            lambda o: QTableWidgetItem_dt(o.pulse),
            ]
        for (rowIndex, row) in enumerate (rows):
            for (columnIndex, columnFun) in enumerate (columns):
                self.renderNodeTable.setItem (
                    rowIndex, columnIndex,
                    columnFun (row))

    def updateRenderTaskGrid(self):
        
        columns = [
            labelFactory( 'id' ),
            labelFactory( 'status' ),
            lineEditFactory( 'logFile' ),
            labelFactory( 'host' ),
            labelFactory( 'project' ),
            labelFactory( 'command' ),
            labelFactory( 'startTime' ),
            labelFactory( 'endTime' ),
            labelFactory( 'exitCode' )]
        setup( Hydra_rendertask.fetch (order = "order by id desc", 
                                       limit = self.limitSpinBox.value ()), 
                                       columns, self.jobsGrid)

    def updateStatusBar(self):
        
        with transaction() as t:
            t.cur.execute ("""select count(status), status 
                                from Hydra_rendernode
                                group by status""")
            counts = t.cur.fetchall ()
        logger.debug (counts)
        countString = ", ".join (["%d %s" % (count, codes[status])
                                  for (count, status) in counts])
        time = datetime.datetime.now().strftime ("%H:%M")
        msg = "%s as of %s" % (countString, time)
        self.statusLabel.setText (msg)

def getSoftwareVersionText(sw_ver):
    """Given the software_version attribute of a Hydra_rendernode row, returns
    a string suitable for display purposes."""
    
    # get RenderNodeMain version number if exists
    if sw_ver:
        
        # case 1: executable in a versioned directory
        v = re.search("rendernodemain-dist-([0-9]+)", sw_ver, 
                        re.IGNORECASE)
        if v:
            return v.group(1)
        
        # case 2: source code file
        elif re.search("rendernodemain.py$", sw_ver, re.IGNORECASE):
            return "Development source"
        
        # case 3: no freakin' clue
        return sw_ver
    
    else: 
        return "None"

def setup(records, columns, grid):
    """Populate a data grid. "colums" is a list of widget factory objects."""
    
    # build the header row
    for (column, attr) in enumerate( columns ):
        item = grid.itemAtPosition( 0, column )
        if item:
            grid.removeItem( item )
            item.widget().hide()
        grid.addWidget( attr.headerWidget(), 0, column )
    
    # build the data rows
    for (row, record) in enumerate( records ):
        for (column, attr) in enumerate( columns ):
            item = grid.itemAtPosition( row + 1, column )
            if item:
                grid.removeItem( item )
                item.widget().hide()
            grid.addWidget(attr.dataWidget( record ),
                           row + 1,
                           column,
                           )

class widgetFactory():
    """A widget building class intended to be subclassed for building particular 
    types of widgets. 'name' must be the name of a database column."""
    
    def __init__(self, name):
        self.name = name
    
    def headerWidget(self):
        """Makes a label for the header row of the display."""
        
        return QLabel('<b>' + self.name + '</b>')
    
    def data(self, record):
        
        return str(getattr(record, self.name))
    
    def dataWidget(self, record):
        """Create a QWidget instance and return a reference to it. To make a 
        widget, given a record, extract the named attribute from the record
        with the data method, and use that as the widget's text/data."""
        
        raise NotImplementedError

class labelFactory(widgetFactory):
    """A label widget factory. The object's name is the name of a database 
    column."""
    
    def dataWidget( self, record ):
        
        return QLabel( self.data( record ) )

class lineEditFactory(widgetFactory):
    """like labelFactory, but makes a read-only text field instead of a 
    label."""
    
    def dataWidget( self, record ):
        
        w = QLineEdit( )
        w.setText( self.data( record ) )
        w.setReadOnly( True )
        return w

class versionLabelFactory(widgetFactory):
    """Builds a label specially for the software_version column in the render
    node table, trimming out non-essential information in the process."""
    
    def dataWidget (self, record ):
        
        sw_version_text = getSoftwareVersionText(self.data(record))
        return QLabel(sw_version_text)

class getOffButton(widgetFactory):
    """As above, but makes a specialized button to implement the GetOff 
    function."""
    
    def dataWidget ( self, record ):
        
        w = QPushButton( self.name )

        # the click handler is the doGetOff method, but with the record 
        # argument already supplied. it's called a "partial application".
        handler = functools.partial (self.doGetOff, record=record)

        QObject.connect (w, SIGNAL("clicked()"), handler)
        return w

    def doGetOff (self, record):
        
        logger.debug('clobber %s', record.host)

class QTableWidgetItem_dt(QTableWidgetItem):
    """A QTableWidgetItem which holds datetime data and sorts it properly."""

    def __init__(self, dtValue):
        QTableWidgetItem.__init__(self, str(dtValue))
        self.dtValue = dtValue
    
    def __lt__(self, other):
        if self.dtValue and other.dtValue:
            return self.dtValue < other.dtValue
        elif self.dtValue and not other.dtValue:
            return True
        else:
            return False

if __name__ == '__main__':
    app = QApplication( sys.argv )
    window = FarmView( )

    window.show( )
    window.doFetch()
    retcode = app.exec_( )
    sys.exit( retcode )
