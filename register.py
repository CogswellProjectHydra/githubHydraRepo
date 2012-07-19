import os

import LoggingSetup
import DjangoSetup
import Utils

from Hydra.models import RenderNode

if RenderNode.objects.filter(  host = Utils.myHostName( ) ):
    raise Exception( 'already registered' )
RenderNode( host = Utils.myHostName( ) ).save( )
