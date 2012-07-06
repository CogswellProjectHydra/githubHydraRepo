import time
import subprocess
import traceback
import exceptions
import os

import DjangoSetup
from Hydra.models import RenderTask

from Answers import Answer, TimeAnswer, EchoAnswer, CMDAnswer, RenderAnswer

from LoggingSetup import logger

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

    def __init__(self, command, log_file ):
        render_task = RenderTask( )
        render_task.status = 'R'
        render_task.logFile = log_file
        render_task.host = os.getenv( 'COMPUTERNAME' )
        render_task.command = repr( command )
        render_task.save( )

        logger.debug(render_task)

        self.render_task_id = render_task.id
        self.command = command
        self.log_file = log_file

    def computeAnswer( self, server ):
        render_task = RenderTask.objects.get( id = self.render_task_id )
        log = file( render_task.logFile, 'w' )
        
        try:
            log.write( 'Hydra log file %s on %s\n' % ( render_task.logFile, render_task.host ) )
            log.write( 'Command: %s\n\n' % ( render_task.command ) )
            
            render_CMDQuestion = CMDQuestion( eval( render_task.command ) )
            render_CMDAnswer = render_CMDQuestion.computeAnswer( render_task.host )

            log.write( 'Render Output:\n\n%s\n\n' % ( render_CMDAnswer.output ) )
            log.flush ( )

            render_task.status = 'D'
            render_task.save( )

            return render_CMDAnswer
        except Exception, e:
            traceback.print_exc( e, log )
            raise
        finally:
            log.close( )
            
