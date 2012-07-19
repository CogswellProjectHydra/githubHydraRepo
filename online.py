import os

import LoggingSetup
import DjangoSetup
import Utils

from Hydra.models import RenderNode

thisNode = RenderNode.objects.get( host = Utils.myHostName( ) )
if thisNode.status == 'O':
    thisNode.status = 'I'
    thisNode.save( )
    
