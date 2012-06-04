import SocketServer
import threading
import pickle

import Constants

class Server: pass

class LocalServer( Server ): pass

class MySocketServer(  SocketServer.TCPServer ):

    allow_reuse_address = True

class TCPServer( Server ):


    def __init__( self, port = Constants.PORT ):

        MyTCPHandler.server = self
        
        self.serverObject = MySocketServer( ("localhost", port),
                                            MyTCPHandler)
        self.serverThread = threading.Thread( target = runTheServer,
                                              name = "server thread",
                                              args = ( self.serverObject, )
                                              )
        self.serverThread.start( )

    def shutdown( self ):
        self.serverObject.shutdown( )

def runTheServer( serverObject ):
    print "enter runTheServer"
    print "starting actual server"
    serverObject.serve_forever( )
    print "done runTheServer"
    
        
class MyTCPHandler( SocketServer.StreamRequestHandler ):

    server = None # the Hydra server object, NOT the SocketServer.

    def handle( self ):
        print "handle"
        questionBytes = self.rfile.read( )
        question = pickle.loads( questionBytes )
        
        answer = question.computeAnswer( self.server )

        answerBytes = pickle.dumps( answer )
        self.wfile.write( answerBytes )
        
