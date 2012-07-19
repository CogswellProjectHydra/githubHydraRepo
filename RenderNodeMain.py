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

@transaction.commit_on_success
def processRenderTasks( ):
    thisNode = RenderNode.objects.get( host = Utils.myHostName )
    for render_task in RenderTask.objects.filter( status = 'A',
                                                  host = thisNode.host ,
                                                  ):
        if not os.path.isdir( RENDERLOGDIR ):
            os.makedirs( RENDERLOGDIR )
        render_task.logFile = os.path.join( RENDERLOGDIR, '%010d.log.txt' % render_task.id )
        render_task.status = 'S'
        thisNode.status = 'S'
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
            render_task.save( )
            thisNode.status = 'I'
            thisNode.save( )

            log.close( )

if __name__ == '__main__':

    socketServer = Servers.TCPServer( )
#    socketServer.serverThread.join( )
    socketServer.createIdleLoop (5, processRenderTasks )

