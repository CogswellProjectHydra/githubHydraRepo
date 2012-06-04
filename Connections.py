import exceptions

import Servers
import Constants
import Answers

class Connection:

    def sendQuestionToServer( self, question ):

        raise exceptions.NotImplementedError

class LocalConnection( Connection ):

    def __init__( self,
                  localServer = Servers.Server( )
                  ):
        
        self.localServer = localServer

    def sendQuestionToServer( self, question ):
        
        return question.computeAnswer( self.localServer )

class SocketConnection( Connection ):

    def __init__( self,
                  hostname = Constants.HOSTNAME,
                  port = Constants.PORT
                  ):

        self.hostname = hostname
        self.port = port
    
    def sendQuestionToServer( self, question ):
        
        sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

        try:
            sock.connect( ( self.hostname, self.port ) )
            questionBytes = pickle.dumps( question )
            sock.sendall( questionBytes )
        
            answerBytes = sock.recv( Constants.MANYBYTES)
            answer = pickle.loads( answerBytes )
 
        finally:
            sock.close( )

        return answer


