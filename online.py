import os

import LoggingSetup
import Utils

from MySQLSetup import Hydra_rendernode

[thisNode] = Hydra_rendernode.fetch( "where host = '%s'" % Utils.myHostName( ) )
if thisNode.status == 'O':
    thisNode.status = 'I'
    thisNode.update( )
    
