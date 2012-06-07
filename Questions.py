import time
import subprocess

from Answers import Answer, TimeAnswer, EchoAnswer, CMDAnswer

class Question:
    
    def computeAnswer( self, server ):
        return Answer( )
    
class TimeQuestion( Question ):
     
    def computeAnswer( self, server ):
        return TimeAnswer( time.localtime( ) )

class EchoQuestion( Question ):

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
