import os

import LoggingSetup
import Utils

from MySQLSetup import Hydra_rendernode

[thisNode] = Hydra_rendernode.fetch( "where host = '%s'" % Utils.myHostName( ) )
thisNode.status = 'O'
thisNode.update( )
    
