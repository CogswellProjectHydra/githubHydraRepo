import os

import LoggingSetup
import Utils

from MySQLSetup import Hydra_rendernode, OFFLINE, IDLE

[thisNode] = Hydra_rendernode.fetch( "where host = '%s'" % Utils.myHostName( ) )
if thisNode.status == OFFLINE:
    thisNode.status = IDLE
    thisNode.update( )
    
