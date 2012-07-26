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

import DjangoSetup
from Hydra.models import RenderTask, RenderNode
from django.db import transaction

def processRenderTasks( ):

    with transaction.commit_on_success( ):

        thisNode = RenderNode.objects.get( host = Utils.myHostName( ) )
        if thisNode.status != 'I':
            return
        
        render_tasks = RenderTask.objects.filter( status = 'R' )
        if render_tasks.count( ) == 0:
            return
        render_task = render_tasks[0]
        
        if not os.path.isdir( RENDERLOGDIR ):
            os.makedirs( RENDERLOGDIR )
        render_task.logFile = os.path.join( RENDERLOGDIR, '%010d.log.txt' % render_task.id )
        render_task.status = 'S'
        render_task.node = thisNode.host
        thisNode.status = 'S'
        thisNode.task = render_task
        render_task.startTime = datetime.datetime.now( )
        render_task.save( )
        thisNode.save( )
        
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
        
        with transaction.commit_on_success( ):
            render_task.save( )
            thisNode.save( )

        log.close( )

if __name__ == '__main__':

    thisNode = RenderNode.objects.get( host = Utils.myHostName( ) )
    thisNode.status = 'I'
    thisNode.save( )
    socketServer = Servers.TCPServer( )
#    socketServer.serverThread.join( )
    socketServer.createIdleLoop (5, processRenderTasks )

