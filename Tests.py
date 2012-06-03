import unittest
import time

import Questions
import Answers

class TestQuestions( unittest.TestCase ):

    def setUp( self ): pass

    def testQA( self ):
        
        question = Questions.Question( )
        answer = question.computeAnswer( )
        self.assertEqual( answer.__class__, Answers.Answer )

    def testTime( self ):
        
        time1 = time.localtime( )
        
        question = Questions.TimeQuestion( )
        answer = question.computeAnswer( )
        time2 = answer.time

        self.assertEqual( time1, time2 )

    def tearDown( self ): pass
    
if __name__ == '__main__':
    unittest.main( exit=False )
    
