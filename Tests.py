import unittest
import time

import Questions
import Answers
import Connections
import Clients
import Servers

class TestQuestionsLocal( unittest.TestCase, Clients.Client ):

    def setUp( self ):

        self.connection = localConnection
        
    def testQA( self ):
        
        question = Questions.Question( )
        answer = self.getAnswer( question )
        self.assertEqual( answer.__class__, Answers.Answer )

    def testTime( self ):
        
        time1 = time.localtime( )
        
        question = Questions.TimeQuestion( )
        answer = self.getAnswer( question )
        time2 = answer.time

        self.assertEqual( time1, time2 )

    def tearDown( self ): pass

class TestQuestionsSocket( TestQuestionsLocal ):

    def setUp( self ):
        
        self.connection = Connections.TCPConnection ()
    
if __name__ == '__main__':

    localConnection = Connections.LocalConnection ()
    socketServer = Servers.TCPServer( )
    unittest.main( exit=False )
    socketServer.shutdown( )
    
