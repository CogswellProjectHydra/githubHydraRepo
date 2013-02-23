'''
Created on Feb 16, 2013

@author: Aaron Cohn
'''
from socket import error as socketerror
from MySQLSetup import Hydra_rendertask, transaction, KILLED, READY
from Connections import TCPConnection
from Questions import KillCurrentJobQuestion
from LoggingSetup import logger
from sys import argv

def sendKillQuestion(renderhost):
    connection = TCPConnection(hostname=renderhost)
    killed = connection.getAnswer(KillCurrentJobQuestion(statusAfterDeath=KILLED))
    if not killed:
        logger.debug("%r tried to kill its job but failed for some reason." % renderhost)
    return killed
    
def kill(job_id):
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
        
    #with transaction():
    # mark all of the ready tasks complete
    readyTasks = [finish(task) for task in Hydra_rendertask.fetch("where status = 'R' and job_id = %s" % job_id)]
    for task in readyTasks:
        task.update()
            
    startedTasks = Hydra_rendertask.fetch("where status = 'S' and job_id = %s" % job_id)
    error = False
    for host in [getHost(task) for task in startedTasks]:
        try:
            error = error or sendKillQuestion(host)
        except socketerror:
            print "There was a problem communicating with {0:s}".format(host)
            error = True
    if error:
        print "Some jobs could not be killed."

def resurrect(job_id):
    #with transaction():
    killedTasks = Hydra_rendertask.fetch("where status = 'K' and job_id = %s" % job_id)
    for task in killedTasks:
        task.status = READY
        task.update()

def main(args):
    if len(args) == 3:
        cmd, job_id = args[1], int(args[2])
        if cmd == 'kill':
            kill(job_id)
        elif cmd == 'resurrect':
            resurrect(job_id)
    else:
        print "Command line args: ['kill' or 'resurrect'] ['job_id']"

if __name__ == '__main__':
    main(argv)
