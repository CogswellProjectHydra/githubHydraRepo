import os

import LoggingSetup
import Utils

from MySQLSetup import Hydra_rendernode, OFFLINE

import ConfigParser

config = ConfigParser.RawConfigParser ()
config.read ("C:/Hydra/hydraSettings.cfg")

me = Utils.myHostName( )
minJobPriority = config.get(section="rendernode", option="minJobPriority")

if Hydra_rendernode.fetch( "where host = '%s'" % me ):
    raise Exception( 'already registered' )
Hydra_rendernode ( host = me, status = OFFLINE, minPriority = minJobPriority).insert( )
