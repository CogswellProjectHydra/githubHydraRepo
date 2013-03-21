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

from tableHelpers import *

from Ui_FarmView import Ui_FarmView

#import DjangoSetup
#from Hydra.models import RenderNode, RenderTask
#from django.db import transaction

from MySQLSetup import (Hydra_rendernode, Hydra_rendertask, transaction, READY, 
                        OFFLINE, IDLE, PENDING, STARTED,
                        niceNames)
from Questions import KillCurrentJobQuestion
import Utils
from Connections import TCPConnection
from MessageBoxes import aboutBox, yesNoBox

class FarmView( QMainWindow, Ui_FarmView ):

    def __init__( self ):
        
        QMainWindow.__init__( self )
        self.setupUi( self )

        self.renderNodeTable.setColumnWidth(0, 30)
        self.renderNodeTable.setColumnWidth(1, 200)
        self.renderNodeTable.setColumnWidth(2, 70)
        self.renderNodeTable.setColumnWidth(3, 70)
        self.renderNodeTable.setColumnWidth(5, 100)
        self.renderNodeTable.setColumnWidth(6, 150)

        # Buttons on the This Node tab
        QObject.connect(self.fetchButton, SIGNAL("clicked()"), self.doFetch)
        QObject.connect(self.onlineThisNodeButton, SIGNAL("clicked()"), 
                        self.onlineThisNodeButtonClicked)
        QObject.connect(self.offlineThisNodeButton, SIGNAL("clicked()"), 
                        self.offlineThisNodeButtonClicked)
        QObject.connect(self.getOffThisNodeButton, SIGNAL("clicked()"), 
                        self.getOffThisNodeButtonClicked)
        QObject.connect(self.projectComboBox, SIGNAL("activated(int)"), 
                        self.projectSelectionHandler)
        
        # Buttons on the Render Nodes tab
        QObject.connect(self.onlineRenderNodesButton, SIGNAL("clicked()"), 
                        self.onlineRenderNodesButtonClicked)
        QObject.connect(self.offlineRenderNodesButton, SIGNAL("clicked()"),
                        self.offlineRenderNodesButtonClicked)
        QObject.connect(self.getOffRenderNodesButton, SIGNAL("clicked()"),
                        self.getOffRenderNodesButtonClicked)
        
        # internal variables
        self.lastProjectIndex = -1
        self.thisNodeButtonsEnabled = True
        
        # other stuff
        # TODO: test sqlErrorBox
        self.sqlErrorBox = (
            functools.partial(aboutBox, 
                        parent=self, 
                        title="Error", 
                        msg="There was a problem while trying to fetch info"
                        " from the database. Check the FarmView log file for"
                        " more details about the error.")
        )
        
        # let there be data
        self.doFetch()

    def getThisNodeData(self):
        
        [thisNode] = Hydra_rendernode.fetch("where host = '%s'" 
                                            % Utils.myHostName())
        return thisNode
    
    def offlineNode(self, thisNode):
        if thisNode.status == OFFLINE:
                return
        elif thisNode.task_id:
            thisNode.status = PENDING
        else:
            thisNode.status = OFFLINE
        with transaction() as t:
                thisNode.update(t)
                
    def getOffThisNodeButtonClicked(self):
        """Offlines the node and sends a message to the render node server 
        running on localhost to kill its current task"""
        #TODO: test getOffThisNodeButtonClicked
        thisNode = None
        try:
            thisNode = self.getThisNodeData()
        except sqlerror as err:
            logger.debug(str(err))
            self.sqlErrorBox()
            return
        
        choice = yesNoBox(self, "Confirm", "All progress on the current job"
                          " will be lost. Are you sure you want to stop it?")
        if choice == QMessageBox.No:
            aboutBox(self, "Abort", "No action taken.")
            return
        
        if thisNode:
            self.offlineNode(thisNode)
                
            if thisNode.task_id:
                try:
                    # TODO: use JobKill for getOff instead of doing it manually
                    connection = TCPConnection()
                    killed = connection.getAnswer(KillCurrentJobQuestion(
                                                statusAfterDeath=READY))
                    if not killed:
                        logger.debug("There was a problem killing the task.")
                        aboutBox(self, "Error", "There was a problem killing"
                                 " the task.")
                except socketerror:
                    logger.debug(socketerror.message)
                    aboutBox(self, "Error", "There was a problem communicating"
                             " with the render node software. Either it's not"
                             " running, or it has become unresponsive.")
            else:
                aboutBox(self, "Offline", "No job was running. Node offlined.")
                
        self.doFetch()
        
    def onlineThisNodeButtonClicked(self):
        """Changes the local render node's status to online if it was offline,
        goes back to started if it was pending offline."""
        
        # get most current info from the database
        thisNode = None
        try:
            thisNode = self.getThisNodeData()
        except sqlerror as err:
            logger.debug(str(err))
            self.sqlErrorBox()
            return
        
        if thisNode:
            if thisNode.status == IDLE:
                return
            elif thisNode.status == OFFLINE:
                thisNode.status = IDLE
            elif thisNode.status == PENDING and thisNode.task_id:
                thisNode.status = STARTED
            with transaction() as t:
                thisNode.update(t)
        
        self.doFetch()
            
    def offlineThisNodeButtonClicked(self):
        """Changes the local render node's status to offline if it was idle,
        pending if it was working on something."""
        
        # get the most current info from the database
        thisNode = None
        try:
            thisNode = self.getThisNodeData()
        except sqlerror as err:
            logger.debug(str(err))
            self.sqlErrorBox()
            return
        
        if thisNode:
            self.offlineNode(thisNode)
            
        self.doFetch()
    
    def getCheckedItems(self, table, itemColumn, checkBoxColumn):
        nRows = table.rowCount()
        checks = list()
        for rowIndex in range(0, nRows - 1):
            item = str(table.item(rowIndex, itemColumn).text())
            checkState = table.item(rowIndex, checkBoxColumn).checkState()
            if checkState:
                checks.append(item)
        return checks
    
    def onlineRenderNodesButtonClicked(self):
        
        hosts = self.getCheckedItems(table=self.renderNodeTable, itemColumn=0, 
                                checkBoxColumn=6)
        if len(hosts) == 0:
            aboutBox(self, "None checked", "No nodes have been selected. Use"
                     " the check boxes on the right side of the table to"
                     " select render nodes.")
            return
        
        choice = yesNoBox(self, "Confirm", "Are you sure you want to online"
                          " these nodes? <br>" + str(hosts))
        
        if choice == QMessageBox.Yes:
            with transaction() as t:
                rendernode_rows = Hydra_rendernode.fetch(explicitTransaction=t)
                for node_row in rendernode_rows:
                    if node_row.host in hosts:
                        if node_row.status == OFFLINE:
                            node_row.status = IDLE
                            node_row.update(t)
                        else:
                            logger.info(node_row.host + " was already online.")
            self.doFetch()
        else:
            aboutBox(self, "Aborted", "No action taken.")
                    
    def offlineRenderNodesButtonClicked(self):
        """For all nodes with boxes checked in the render nodes table, changes
        status to offline if idle, or pending if started."""
        
        hosts = self.getCheckedItems(table=self.renderNodeTable, itemColumn=0, 
                                checkBoxColumn=6)
        if len(hosts) == 0:
            aboutBox(self, "None checked", "No nodes have been selected. Use"
                     " the check boxes on the right side of the table to"
                     " select render nodes.")
            return
        
        choice = yesNoBox(self, "Confirm", "Are you sure you want to online"
                          " these nodes? <br>" + str(hosts))
        
        if choice == QMessageBox.Yes:
            with transaction() as t:
                rendernode_rows = Hydra_rendernode.fetch(explicitTransaction=t)
                for node_row in rendernode_rows:
                    if node_row.host in hosts:
                        if node_row.status == STARTED:
                            node_row.status = PENDING
                        else:
                            node_row.status = OFFLINE
                        node_row.update(t)
            self.doFetch()
        else:
            aboutBox(self, "Aborted", "No action taken.")
    
    def getOffRenderNodesButtonClicked(self):
        pass
    
    def projectSelectionHandler(self, currentProjectIndex):
        """Checks to see if project selection has changed. If so, handles the 
        change. Else, does nothing."""
        
        if currentProjectIndex != self.lastProjectIndex:
            self.projectChangeHandler(currentProjectIndex)
        
    def projectChangeHandler(self, index):
        """Handler for the event where the project selection changed."""
        
        selectedProject = self.projectComboBox.itemText(index)
        choice = yesNoBox(self, "Change project", "Reassign this node to " + 
                          selectedProject + "? (will avoid jobs from other"
                          " projects)")
        
        if choice == QMessageBox.No:
            aboutBox(self, "No changes", "This node will remain assigned to " + 
                     self.thisNode.project + ".")
            self.projectComboBox.setCurrentIndex(self.lastProjectIndex)
            return
        
        # get the most up to date info from the database
        thisNode = None
        try:
            thisNode = self.getThisNodeData()
        except sqlerror as err:
            logger.debug(str(err))
            self.sqlErrorBox()
            return
        
        thisNode.project = self.projectComboBox.currentText()
        with transaction() as t:
            thisNode.update(t)
        self.lastProjectIndex = self.projectComboBox.currentIndex()
        aboutBox(self, "Success", "Node reassigned to " + selectedProject)

    def doFetch( self ):
        """Aggregate method for updating all of the widgets."""
        
        try:
            self.updateThisNodeInfo()
            self.updateRenderNodeTable()
            self.updateRenderTaskGrid()
            self.updateStatusBar()
        except sqlerror as err:
            logger.debug(str(err))
            self.sqlErrorBox()
        
    def updateThisNodeInfo(self):
        """Updates widgets on the "This Node" tab with the most recent 
        information available."""
        
        # if the buttons are disabled, don't bother
        if not self.thisNodeButtonsEnabled:
            return
        
        # get the most current info from the database
        thisNode = None
        try:
            thisNode = self.getThisNodeData()
            self.updateProjectComboBox()
        except sqlerror as err:
            logger.debug(str(err))
            self.sqlErrorBox()
        
        if thisNode:
            # update the labels
            self.nodeNameLabel.setText(thisNode.host)
            self.nodeStatusLabel.setText(niceNames[thisNode.status])
            self.updateTaskIDLabel(thisNode.task_id)
            self.nodeVersionLabel.setText(
                        getSoftwareVersionText(thisNode.software_version))
            
            self.setCurrentProjectSelection(thisNode.project)
            
        else:
            QMessageBox.about(self, "Notice", 
                "Information about this node cannot be displayed because it is"
                "not registered on the render farm. You may continue to use"
                " Farm View, but it must be restarted after this node is "
                "registered if you wish to see this node's information.")
            self.setThisNodeButtonsEnabled(False)
    
    def setThisNodeButtonsEnabled(self, choice):
        """Enables or disables buttons on This Node tab"""
        
        self.onlineThisNodeButton.setEnabled(choice)
        self.offlineThisNodeButton.setEnabled(choice)
        self.getOffThisNodeButton.setEnabled(choice)
        self.projectComboBox.setEnabled(choice)
        self.thisNodeButtonsEnabled = choice
        
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
    
    def updateTaskIDLabel(self, task_id):
        
        if task_id:
            self.taskIDLabel.setText(str(task_id))
        else:
            self.taskIDLabel.setText("None")
    
    def setCurrentProjectSelection(self, project):
        """Set project selection based on node's current project setting."""
        
        
        idx = self.projectComboBox.findText(project, 
                       flags=Qt.MatchExactly|Qt.MatchCaseSensitive)
        self.projectComboBox.setCurrentIndex(idx)
        self.lastProjectIndex = idx
        
    def updateRenderNodeTable(self):
        
        # clear the table (note: this is done to avoid duplication of items)
        self.renderNodeTable.clearContents()
        self.renderNodeTable.setRowCount(0)
        
        # prevent rows from being sorted while table is populating
        self.renderNodeTable.setSortingEnabled(False)
        
        rows = Hydra_rendernode.fetch(order="order by host")
        self.renderNodeTable.setRowCount (len (rows))
        columns = [
            lambda o: TableWidgetItem_check(),
            lambda o: TableWidgetItem(str(o.host)),
            lambda o: TableWidgetItem(str(niceNames[o.status])),
            lambda o: TableWidgetItem(str(o.task_id)),
            lambda o: TableWidgetItem(str(o.project)),
            lambda o: TableWidgetItem(
                                getSoftwareVersionText(o.software_version)),
            lambda o: TableWidgetItem_dt(o.pulse),
            ]
        for (rowIndex, row) in enumerate (rows):
            for (columnIndex, columnFun) in enumerate (columns):
                columnFun (row).setIntoTable (self.renderNodeTable,
                                              rowIndex, columnIndex)
        
        self.renderNodeTable.setSortingEnabled(True)
                
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
        countString = ", ".join (["%d %s" % (count, niceNames[status])
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

class TableWidgetItem_dt(TableWidgetItem):
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
    retcode = app.exec_( )
    sys.exit( retcode )
