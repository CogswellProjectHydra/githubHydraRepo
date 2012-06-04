class Answer: pass

class TimeAnswer( Answer ):

    def __init__( self, time ):
        self.time = time
        
class EchoAnswer( Answer ):
    def __init__( self, object ):
        self.object = object
