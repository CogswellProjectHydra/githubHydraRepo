__doc__ = """The Answers module represents any answer that is given."""
class Answer: pass


class TimeAnswer( Answer ):
    """An answer class that returns the time."""

    def __init__( self, time ):
        self.time = time


class EchoAnswer( Answer ):
    """An answer class that returns the original quesion from the Client
    as an answer."""
    
    def __init__( self, object ):
        self.object = object

class CMDAnswer( Answer ):
    def __init__( self, output ):
        self.output = output
        
        
