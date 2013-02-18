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
        self.childProcess = None
        self.childKilled = False
        
    def processRenderTasks(self):
        
        with transaction( ):
            
            [thisNode] = Hydra_rendernode.fetch ("where host = '%s'" % Utils.myHostName( ))
            
            logger.debug("This render node is: %r\nrender node status: %r", thisNode.host, thisNode.status)
            
            # If this node is not idle, it must be OFFLINE, so don't try to find a new job
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
            
            # run the job and keep track of the process
            self.childProcess = subprocess.Popen( eval( render_task.command ),
                                                  stdout = log,
                                                  stderr = subprocess.STDOUT )
            
            # wait until the job is finished or terminated
            render_task.exitCode = self.childProcess.wait()
            
            log.write( '\nProcess exited with code %d\n' % render_task.exitCode )
            return RenderAnswer( )
        
        except Exception, e:
            traceback.print_exc( e, log )
            raise
        
        finally:
            # get the latest info about this render node
            with transaction():
                [thisNode] = Hydra_rendernode.fetch ("where host = '%s'" % Utils.myHostName( ))
            
            # check if the job was killed, then update the job board accordingly
            if self.childKilled:
                # reset the task in the job board so another render node can pick it up
                render_task.status = READY
                render_task.startTime = None
                render_task.host = None
                self.childKilled = False
            else:
                # report that the job was finished
                render_task.status = FINISHED # note: what if the process didn't run for some reason? maybe we should check the status code
                render_task.endTime = datetime.datetime.now( )
            
            # if nobody set status to OFFLINE, return to IDLE and continue to look for new jobs    
            if thisNode.status == STARTED:
                logger.debug("status: %r", thisNode.status)
                thisNode.status = IDLE
            thisNode.task_id = None
            
            # open a connection to the database and update the records
            with transaction( ):
                render_task.update( )
                thisNode.update( )
    
            log.close( )
            
            # discard info about the previous child process
            self.childProcess = None
            
    def killCurrentJob(self):
        """Kills the render node's current job if it's running one."""
        logger.debug("killing %r", self.childProcess)
        if self.childProcess:
            self.childProcess.kill()
            self.childProcess.poll()
            if self.childProcess.returncode:
                self.childKilled = True
        else:
            logger.debug("no process was running.")
        

def main ():
    socketServer = RenderTCPServer( )
#    socketServer.serverThread.join( )
    socketServer.createIdleLoop (5, socketServer.processRenderTasks )

if __name__ == '__main__':
    main ()
