import time

from Answers import Answer, TimeAnswer, EchoAnswer

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
