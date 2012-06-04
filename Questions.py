import time

from Answers import Answer, TimeAnswer

class Question:
    
    def computeAnswer( self, server ):
        return Answer( )
    
class TimeQuestion( Question ):
    
    def computeAnswer( self, server ):
        return TimeAnswer( time.localtime( ) )
