import time

from Answers import Answer, TimeAnswer, EchoAnswer

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
