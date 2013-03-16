import sys
#import traceback
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

from MySQLSetup import Hydra_rendernode, Hydra_rendertask, transaction, READY, OFFLINE, IDLE
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
        QObject.connect(self.projectComboBox, SIGNAL("activated(int)"), self.projectSelectionHandler)
        
        self.thisNode = None
        self.lastProjectIndex = -1
        self.buttonsEnabled = True

    def getOff(self):
        """
        Offlines the node and sends a message to the render node server running on localhost to
        kill its current task
        """
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
            aboutBox(self, "Error", "The render node software is not running" 
                     " or has become unresponsive.")
            
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
            self.updateRenderNodeGrid()
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
            # update host/status labels
            self.nodeNameLabel.setText(self.thisNode.host)
            self.nodeStatusLabel.setText(codes[self.thisNode.status])
            
            # get RenderNodeMain version number if exists
            if self.thisNode.software_version:
                sw_ver = self.thisNode.software_version
                
                # case 1: executable in a versioned directory
                v = re.search("rendernodemain-dist-([0-9]+)", sw_ver, 
                                re.IGNORECASE)
                if v:
                    self.nodeVersionLabel.setText(v.group(1))
                
                # case 2: source code file
                elif re.search("rendernodemain.py$", sw_ver, re.IGNORECASE):
                    self.nodeVersionLabel.setText("Development source")
                
                # case 3: no freakin' clue
                else:
                    self.nodeVersionLabel.setText("Unrecognized version: " 
                                                  + sw_ver)
            else: 
                self.nodeVersionLabel.setText("None")
            
            # get task id, if exists
            if self.thisNode.task_id:
                self.taskIDLabel.setText(str(self.thisNode.task_id))
            else:
                self.taskIDLabel.setText("None")
            
            # set project selection based on node's current project setting
            idx = self.projectComboBox.findText(
                           self.thisNode.project, 
                           flags=Qt.MatchExactly|Qt.MatchCaseSensitive)
            self.projectComboBox.setCurrentIndex(idx)
            self.lastProjectIndex = idx
        else:
            QMessageBox.about(self, "Notice", "Information about this node"
                              " cannot be displayed because it is not"
                              " registered on the render farm. You may" 
                              " continue to use Farm View, but it must be"
                              " restarted after this node is registered if you"
                              " wish to see this node's information.")
            self.setButtonsEnabled(False)
    
    def setButtonsEnabled(self, choice):
        """Enables or disables buttons on the This Node tab"""
        
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
            
    def updateRenderNodeGrid(self):
        
        columns = [
            labelAttr( 'host' ),
            labelAttr( 'status' ),
            labelAttr( 'task_id' ),
            labelAttr ( 'project' ),
            getOffButton ("Get off!!!")]
        setup( Hydra_rendernode.fetch(order="order by host"), columns, 
               self.renderNodesGrid)

    def updateRenderTaskGrid(self):
        
        columns = [
            labelAttr( 'id' ),
            labelAttr( 'status' ),
            textAttr( 'logFile' ),
            labelAttr( 'host' ),
            labelAttr( 'project' ),
            labelAttr( 'command' ),
            labelAttr( 'startTime' ),
            labelAttr( 'endTime' ),
            labelAttr( 'exitCode' )]
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

# as above, but makes a specialized button to implement the GetOff function.            
class getOffButton (labelAttr):

    def dataWidget ( self, record ):
        w = QPushButton( self.name )

        # the click handler is the doGetOff method, but with the record 
        # argument already supplied. it's called a "partial application".
        handler = functools.partial (self.doGetOff, record=record)

        QObject.connect (w, SIGNAL("clicked()"), handler)
        return w

    def doGetOff (self, record):
        logger.debug('clobber %s', record.host)

if __name__ == '__main__':
    app = QApplication( sys.argv )
    window = FarmView( )

    window.show( )
    window.doFetch()
    retcode = app.exec_( )
    sys.exit( retcode )
