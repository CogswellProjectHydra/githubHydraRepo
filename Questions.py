import time
import subprocess
import traceback
import exceptions
import os
import datetime

import DjangoSetup
from Hydra.models import RenderTask

from Answers import Answer, TimeAnswer, EchoAnswer, CMDAnswer, RenderAnswer

from LoggingSetup import logger

from Constants import RENDERLOGDIR

__doc__ = """This class is the base class of both the TimeQuestion and
EchoQuestion class. The Quesiton class represents of how any answer is
returned."""
class Question:
    
    def computeAnswer( self, server ):
        return Answer( )

class TimeQuestion( Question ):
    """TimeQuestion corresponds with TimeAnswer in the Answers module,
    returning the answer."""
     
    def computeAnswer( self, server ):
        return TimeAnswer( time.localtime( ) )


class EchoQuestion( Question ):
    """EchoQuestion corresponds with EchoAnswer in the Answers module,
    returning the answer."""

    def __init__( self, object ):
        self.object = object

    def computeAnswer( self, server ):
        return EchoAnswer( self.object )

class CMDQuestion( Question ):
    
    def __init__( self, args ):
        self.args = args

    def computeAnswer( self, server ):
        output = subprocess.check_output( self.args,
                                          stderr=subprocess.STDOUT )
        return CMDAnswer( output )

class RenderQuestion( Question ):

    def __init__(self, render_task_id ):

        self.render_task_id = render_task_id

    def computeAnswer( self, server ):
        render_task = RenderTask.objects.get( id = self.render_task_id )
        render_task.host = os.getenv( 'COMPUTERNAME' )
        if not os.path.isdir( RENDERLOGDIR ):
            os.makedirs( RENDERLOGDIR )
        render_task.logFile = os.path.join( RENDERLOGDIR, '%010d.log.txt' % render_task.id )
        render_task.status = 'S'
        render_task.startTime = datetime.datetime.now( )
        render_task.save( )
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

            log.close( )
            
