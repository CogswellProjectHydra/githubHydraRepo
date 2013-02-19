'''
Created on Feb 16, 2013

@author: Aaron Cohn
'''
from MySQLSetup import Hydra_rendertask, transaction, KILLED, READY
from Connections import TCPConnection
from Questions import KillCurrentJobQuestion
from LoggingSetup import logger

def sendKillQuestion(renderhost):
    connection = TCPConnection(hostname=renderhost)
    killed = connection.getAnswer(KillCurrentJobQuestion(statusAfterDeath=KILLED))
    if not killed:
        logger.debug("There was a problem killing the task running on %r" % renderhost)

def killjob(job_id):
    # open transaction -- no race condition
    #    fetch all of the tasks with the corresponding job id
    #    mark the Ready tasks complete
    #    update
    # close transaction
    # for each Started task:
    #    send the kill question to the node running it
    #    wait until the answer arrives
    #    open transaction:
    #        mark the task Finished
    #        update
    #    close transaction
    def finish(rendertask):
        rendertask.status = KILLED
        return rendertask
    
    def getHost(rendertask):
        return rendertask.host
        
    with transaction():
        # mark all of the ready tasks complete
        readyTasks = [finish(task) for task in Hydra_rendertask.fetch("where status = 'R' and job_id = %s" % job_id)]
        for task in readyTasks:
            task.update()
            
    startedTasks = Hydra_rendertask.fetch("where status = 'S' and job_id = %s" % job_id)
    for host in [getHost(task) for task in startedTasks]:
        sendKillQuestion(host)

def resurrectJob(job_id):
    with transaction():
        killedTasks = Hydra_rendertask.fetch("where status = 'K' and job_id = %s" % job_id)
        for task in killedTasks:
            task.status = READY
            task.update()
