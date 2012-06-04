import unittest
import time
import random
import exceptions

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

    def testEchoSuccess( self ):

        object = random.random( )
        question = Questions.EchoQuestion( object )
        answer = self.getAnswer( question )
        self.assertEqual( question.object, answer.object )

    def testEchoFail( self ):

        object = time
        question = Questions.EchoQuestion( object )
        if self.connection is localConnection:
            self.assertEqual( object, self.getAnswer( question ).object )
        else:
            self.assertRaises( exceptions.TypeError, self.getAnswer, question )

    def tearDown( self ): pass

class TestQuestionsSocket( TestQuestionsLocal ):

    def setUp( self ):
        
        self.connection = Connections.TCPConnection ()
    
if __name__ == '__main__':

    localConnection = Connections.LocalConnection ()
    socketServer = Servers.TCPServer( )
    unittest.main( exit=False )
    socketServer.shutdown( )
    
