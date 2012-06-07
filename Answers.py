class Answer: pass

__doc__ = """An answer class that returns the time."""
class TimeAnswer( Answer ):

    def __init__( self, time ):
        self.time = time

__doc__ = """An answer class that returns the original quesion from the Client
as an answer."""
class EchoAnswer( Answer ):
    
    def __init__( self, object ):
        self.object = object
