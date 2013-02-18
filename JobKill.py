'''
Created on Feb 16, 2013

@author: Aaron Cohn
'''
from MySQLSetup import Hydra_job, Hydra_rendertask, transaction
from Connections import TCPConnection
from Questions import KillCurrentJobQuestion
from LoggingSetup import logger

def sendKillQuestion(renderhost):
    connection = TCPConnection(host=renderhost)
    killed = connection.getAnswer(KillCurrentJobQuestion())
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
        rendertask.status = 'F'
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