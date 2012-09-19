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

from MySQLSetup import Hydra_rendernode, Hydra_rendertask, transaction

def processRenderTasks( ):

    with transaction( ):

        [thisNode] = Hydra_rendernode.fetch ("where host = '%s'" % Utils.myHostName( ))
        #RenderNode.objects.get( host = Utils.myHostName( ) )

        if thisNode.status != 'I':
            return
        
        render_tasks = Hydra_rendertask.fetch ("where status = 'R'", limit=1)
        # RenderTask.objects.filter( status = 'R' )
        if not render_tasks:
            return
        render_task = render_tasks[0]
        
        if not os.path.isdir( RENDERLOGDIR ):
            os.makedirs( RENDERLOGDIR )
        render_task.logFile = os.path.join( RENDERLOGDIR, '%010d.log.txt' % render_task.id )
        render_task.status = 'S'
        render_task.host = thisNode.host
        thisNode.status = 'S'
        thisNode.task_id = render_task.id
        render_task.startTime = datetime.datetime.now( )
        render_task.update( )
        thisNode.update( )
        
    log = file( render_task.logFile, 'w' )
        
    try:
        log.write( 'Hydra log file %s on %s\n' % ( render_task.logFile, render_task.host ) )
        log.write( 'Command: %s\n\n' % ( render_task.command ) )
        log.flush( )
        
        render_task.exitCode = subprocess.call( eval( render_task.command ),
                                                stdout = log,
                                                stderr = subprocess.STDOUT )
        log.write( '\nProcess exited with code %d\n' % render_task.exitCode )
        return RenderAnswer( )
    except Exception, e:
        traceback.print_exc( e, log )
        raise
    finally:
        render_task.status = 'D'
        render_task.endTime = datetime.datetime.now( )
        thisNode.status = 'I'
        thisNode.task_id = None
        
        with transaction( ):
            render_task.update( )
            thisNode.update( )

        log.close( )


def main ():
    [thisNode] = Hydra_rendernode.fetch( "where host = '%s'" % Utils.myHostName( ) )
    thisNode.status = 'I'
    thisNode.update( )
    socketServer = Servers.TCPServer( )
#    socketServer.serverThread.join( )
    socketServer.createIdleLoop (5, processRenderTasks )

if __name__ == '__main__':
    main ()
