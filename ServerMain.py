import functools
import Servers
from LoggingSetup import logger

if __name__ == '__main__':

    socketServer = Servers.TCPServer( )
#    socketServer.serverThread.join( )
    socketServer.createIdleLoop (5, functools.partial ( logger.info, "idle") )
