from MySQLSetup import Hydra_rendernode, Hydra_rendertask, transaction, IDLE, READY, STARTED, FINISHED
from LoggingSetup import logger

def unstick (taskID):
    [task] = Hydra_rendertask.fetch ("where id = %d" % taskID)
    hostMaybe = Hydra_rendernode.fetch ("where host = '%s'" % task.host)
    with transaction () as t:
        task.host = None
        task.status = READY
        task.startTime = None
        task.endTime = None
        if hostMaybe:
            [host] = hostMaybe
            host.task_id = None
            host.status = IDLE
            host.update (t)
        task.update (t)
