class Answer: pass

class TimeAnswer( Answer ):

    def __init__( self, time ):
        self.time = time
        
class EchoAnswer( Answer ):
    def __init__( self, object ):
        self.object = object

class CMDAnswer( Answer ):
    def __init__( self, output ):
        self.output = output
        
