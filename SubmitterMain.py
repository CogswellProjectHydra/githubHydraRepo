import sys
import traceback
import math
import os

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_submitter import Ui_MainWindow

from LoggingSetup import logger
from JobTicket import MayaTicket
from MySQLSetup import transaction, Hydra_rendernode
import Utils
from MessageBoxes import aboutBox, yesNoBox

class SubmitterWindow( QMainWindow, Ui_MainWindow ):

    def __init__( self ):
        """Initializes the Maya render job submission window."""

        QMainWindow.__init__( self )
        self.setupUi( self ) #self, self

        QObject.connect(self.submitButton, SIGNAL("clicked()"), self.doSubmit)
        QObject.connect(self.browseButton, SIGNAL("clicked()"), 
                        self.setMayaProjectPath)

        sys.argv.extend (['1', '1', '1'])
        scene, start, end, by = sys.argv[1:5] # TODO: proper cmd line args
        scene = scene.replace ('\\', '/')
        self.sceneText.setText(scene)
        self.startSpinBox.setValue( eval (start ) )
        self.endSpinBox.setValue( eval( end ) )
        self.populateProjectComboBox()

    def populateProjectComboBox(self):
        """Clears and refreshes the contents of the projects dropdown box."""

        # get current list of projects from the database
        tuples = None
        with transaction() as t:
            t.cur.execute("select * from Hydra_projects")
            tuples = t.cur.fetchall()
        
        # make flat list out of single-element tuples fetched from db
        projectsList = [t for (t,) in tuples]
        
        # populate the dropdown
        for project in projectsList:
            self.projectComboBox.addItem(project)
        
        # show default project selection
        [thisNode] = Hydra_rendernode.fetch(
            "where host = '%s'" 
            % Utils.myHostName()
        )
        idx = self.projectComboBox.findText(
            thisNode.project, 
            flags = Qt.MatchExactly | Qt.MatchCaseSensitive
        )
        self.projectComboBox.setCurrentIndex(idx)
            
    # called by pressing the "submit" button in the Qt main window
    def doSubmit( self ):
        """Submits a job ticket for this scene to be split into tasks and 
        processed."""

        logger.debug ('doSubmit')

        sceneFile = str( self.sceneText.text() )
        startFrame = self.startSpinBox.value( )
        endFrame = self.endSpinBox.value( )
        numJobs = self.numJobsSpinBox.value( )
        batchSize = int(math.ceil((endFrame - startFrame + 1) / numJobs))
        priority = self.prioritySpinBox.value( )
        project = str(self.projectComboBox.currentText())
        
        mayaProjectPath = str(self.projectDirLineEdit.text())
        if os.path.exists(mayaProjectPath + "workspace.mel"):
            mayaProjectPath = self.getMayaProjectPath(sceneFile)
            choice = yesNoBox(self, "Confirm", "Maya project path set to:<br>"
                               + mayaProjectPath + "<br>Is this correct?")
            if choice == QMessageBox.No:
                aboutBox(self, "Abort", "Submission aborted.\
                         Please set the Maya project path manually.")
                return
            else:
                self.projectDirLineEdit.setText(mayaProjectPath)
                return
        
        if mayaProjectPath:
            MayaTicket(sceneFile, mayaProjectPath, startFrame, endFrame, 
                       batchSize, priority, project
            ).submit()
            aboutBox(self, "Success", "Job submitted. Please close the \
            submitter window.")
        else:
            logger.debug("workspace.mel not found")
            aboutBox(self, "Error", "The project path cannot be set because \
            workspace.mel could not be located. Please set the project path \
            manually.")

    def getMayaProjectPath(self, scenePath):
        """Walks up the file tree looking for workspace.mel, returns the path 
        if found"""
        
        dirList = scenePath.split('/')
        
        # remove "workspace.mel" from end of path
        dirList.pop()
        
        wrkspc = "workspace.mel"
        found = False; numDirs = len(dirList); i = 0
        while i < numDirs:
            if found:
                break
            mayaProjectPath = '/'.join(dirList) + '/'
            if os.path.exists(mayaProjectPath + wrkspc):
                found = True
            dirList.pop()
            i += 1
        
        if found:
            return mayaProjectPath
        
        return None
    
    def setMayaProjectPath(self):
        """Opens a file browser dialog for finding workspace.mel, tries to 
        start the user somewhere sensible"""
        
        currentDir = str( self.projectDirLineEdit.text() )
        projectDir = None
        if len(currentDir) == 0:
            sceneFile = str( self.sceneText.text() )
            projectDir = self.getMayaProjectPath(sceneFile)
            if not projectDir:
                projectDir = os.getcwd()
        else:
            projectDir = currentDir
            
        mayaProjectPath = QFileDialog.getOpenFileName(parent=self, 
                                          caption="Find workspace.mel", 
                                          directory=projectDir, 
                                          filter="workspace.mel")
        if mayaProjectPath:
            # remove "workspace.mel" from end of path
            mayaProjectPath = str(mayaProjectPath).split('/')
            mayaProjectPath.pop()
            mayaProjectPath = '/'.join(mayaProjectPath) + '/'
            self.projectDirLineEdit.setText(mayaProjectPath)
        
if __name__ == '__main__':
    try:
        logger.debug(sys.argv)
        app = QApplication( sys.argv )

        window = SubmitterWindow( )

        window.show( )
        retcode = app.exec_( )
        sys.exit( retcode )
    except Exception, e:
        logger.error( traceback.format_exc( e ) )
        raise
