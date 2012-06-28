import time
import subprocess
import DjangoSetup

from Hydra.models import RenderTask

from Answers import Answer, TimeAnswer, EchoAnswer, CMDAnswer, RenderAnswer

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
        output = subprocess.check_output( self.args, stderr=subprocess.STDOUT )
        return CMDAnswer( output )

class RenderQuestion( Question ):

    def __init__(self, render_task_id ):
        self.render_task_id = render_task_id

    def computeAnswer( self, server ):
        task = RenderTask.objects.get( id = self.render_task_id )
        
        print(task)
        return RenderAnswer( )
