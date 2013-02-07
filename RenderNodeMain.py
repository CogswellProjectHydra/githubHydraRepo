import functools
import itertools
import os
from Constants import *
import datetime
import traceback
import subprocess

import Servers
from LoggingSetup import logger
import Utils
from Answers import RenderAnswer

from MySQLSetup import Hydra_rendernode, Hydra_rendertask, transaction, IDLE, READY, STARTED, FINISHED

class RenderTCPServer(Servers.TCPServer):
    
    def __init__(self, *arglist, **kwargs):
        Servers.TCPServer.__init__(self, *arglist, **kwargs) 
        self.childKilled = False
        
    def processRenderTasks(self):
        with transaction( ):
            self.childProcess = None
            
            [thisNode] = Hydra_rendernode.fetch ("where host = '%s'" % Utils.myHostName( ))
    
            # If this node is not idle, it's doing something, so it shouldn't pick another job
            if thisNode.status != IDLE:
                return
            
            # otherwise, get a job that's ready to be run and has a high enough priority level for this particular node
            render_tasks = Hydra_rendertask.fetch ("where status = '%s' and priority >= %s" % (READY, thisNode.minPriority), limit=1)
            if not render_tasks:
                return
            render_task = render_tasks[0]
            
            # create a log for this task and update the task entry in the database
            if not os.path.isdir( RENDERLOGDIR ):
                os.makedirs( RENDERLOGDIR )
            render_task.logFile = os.path.join( RENDERLOGDIR, '%010d.log.txt' % render_task.id )
            render_task.status = STARTED
            render_task.host = thisNode.host
            thisNode.status = STARTED
            thisNode.task_id = render_task.id
            render_task.startTime = datetime.datetime.now( )
            render_task.update( )
            thisNode.update( )
            
        log = file( render_task.logFile, 'w' )
            
        try:
            log.write( 'Hydra log file %s on %s\n' % ( render_task.logFile, render_task.host ) )
            log.write( 'Command: %s\n\n' % ( render_task.command ) )
            log.flush( )
            
            # run the render job and keep track of the process
            self.childProcess = subprocess.Popen( eval( render_task.command ),
                                                  stdout = log,
                                                  stderr = subprocess.STDOUT )
            render_task.exitCode = self.childProcess.wait()
            self.childProcess = None
            
            log.write( '\nProcess exited with code %d\n' % render_task.exitCode )
            return RenderAnswer( )
        except Exception, e:
            traceback.print_exc( e, log )
            raise
        finally: # mark the task as finished in the database and set state to idle
            if self.childKilled:
                render_task.status = READY
                render_task.startTime = None
            else:
                render_task.status = FINISHED # what if the process didn't run for some reason? we should check the status code
                render_task.endTime = datetime.datetime.now( )
                
            if thisNode.status == STARTED:
                thisNode.status = IDLE
            thisNode.task_id = None
            
            with transaction( ):
                render_task.update( )
                thisNode.update( )
    
            log.close( )
    
    def killCurrentJob(self):
        logger.debug("killing %r", self.childProcess)
        if self.childProcess:
            self.childProcess.kill()
            self.childKilled = True
        

def main ():
    [thisNode] = Hydra_rendernode.fetch( "where host = '%s'" % Utils.myHostName( ) )
    thisNode.status = 'I'
    thisNode.update( )
    socketServer = RenderTCPServer( )
#    socketServer.serverThread.join( )
    socketServer.createIdleLoop (5, socketServer.processRenderTasks ) # this is probably where we'll set up the code to kill a job

if __name__ == '__main__':
    main ()
