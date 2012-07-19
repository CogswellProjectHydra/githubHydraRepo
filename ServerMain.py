import functools
import itertools

import Servers
from LoggingSetup import logger

import DjangoSetup
from Hydra.models import RenderTask, RenderNode
from django.db import transaction

@transaction.commit_on_success
def assignRenderTasks( ):
    for task, node in itertools.izip( RenderTask.objects.filter( status = 'R' ),
                                      RenderNode.objects.filter( status = 'I' )
                                      ):
        task.status = 'A'
        node.status = 'A'
        node.task = task
        task.host = node.host
        task.save( )
        node.save( )

if __name__ == '__main__':

    socketServer = Servers.TCPServer( )
#    socketServer.serverThread.join( )
    socketServer.createIdleLoop (5, assignRenderTasks )

