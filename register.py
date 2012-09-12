import os

import LoggingSetup
import Utils

from MySQLSetup import Hydra_rendernode

me = Utils.myHostName( )
if Hydra_rendernode.fetch( "where host = '%s'" % me ):
    raise Exception( 'already registered' )
Hydra_rendernode ( host = me, status = 'O' ).insert( )
