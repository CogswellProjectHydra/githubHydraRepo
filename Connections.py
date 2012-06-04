import exceptions
import socket
import pickle

import Servers
import Constants
import Answers

class Connection:

    def getAnswer( self, question ):

        raise exceptions.NotImplementedError

class LocalConnection( Connection ):

    def __init__( self,
                  localServer = Servers.Server( )
                  ):
        
        self.localServer = localServer

    def getAnswer( self, question ):
        
        return question.computeAnswer( self.localServer )

class TCPConnection( Connection ):

    def __init__( self,
                  hostname = Constants.HOSTNAME,
                  port = Constants.PORT
                  ):

        self.hostname = hostname
        self.port = port
    
    def getAnswer( self, question ):

        sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

        try:
            sock.connect( ( self.hostname, self.port ) )
            questionBytes = pickle.dumps( question )
            sock.sendall( questionBytes )
            sock.shutdown( socket.SHUT_WR)
        
            answerBytes = sock.recv( Constants.MANYBYTES)
            answer = pickle.loads( answerBytes )
 
        finally:
            sock.close( )
        
        return answer


