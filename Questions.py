import time

from Answers import Answer, TimeAnswer

class Question:
    def computeAnswer (self):
        return Answer ()
    
class TimeQuestion (Question):
    def computeAnswer (self):
        return TimeAnswer (time.time ())
