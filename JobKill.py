'''
Created on Feb 16, 2013

@author: Aaron Cohn
@summary: Procedures for killing and resurrecting jobs and tasks
'''
from socket import error as socketerror
from MySQLSetup import Hydra_rendertask, transaction, KILLED, READY, STARTED
from Connections import TCPConnection
from Questions import KillCurrentJobQuestion
from LoggingSetup import logger
from sys import argv

def sendKillQuestion(renderhost):
    
    connection = TCPConnection(hostname=renderhost)
    answer = connection.getAnswer(
                            KillCurrentJobQuestion(statusAfterDeath=KILLED))
    
    if not answer.childKilled:
        logger.debug("%r tried to kill its job but failed for some reason." 
                        % renderhost)
    
    return not answer.childKilled
    
def killJob(job_id):
    """Kills every task associated with job_id. Killed tasks have status code 
    'K'. If a task was already started, an a kill request is sent to the host 
    running it.
    @return: False if no errors while killing started tasks, else True"""
    
    # mark all of the Ready tasks as Killed
    with transaction() as t:
        t.cur.execute("""update Hydra_rendernode set status = 'K' 
                        where job_id = '%d' and status = 'R'""" % job_id)
    
    # get hostnames for tasks that were already started
    tuples = None
    with transaction() as t:
        t.cur.execute("""select host from Hydra_rendertask 
                        where job_id = '%d' and status = 'S'""" % job_id)
        tuples = t.cur.fetchall()
    
    untuple = lambda h: h
    hosts = [untuple(*t) for t in tuples]
    
    # send a kill request to each host, note if any failures occurred
    error = False
    for host in hosts:
        try:
            error = error or sendKillQuestion(host)
        except socketerror:
            print "There was a problem communicating with {0:s}".format(host)
            error = True
    
    return error

def resurrectJob(job_id):
    """Resurrects job with the given id. Tasks marked 'K' or 'F' will have their 
    data cleared and their statuses set to 'R'"""
    
    with transaction() as t:
        t.cur.execute("""update Hydra_rendertask 
                        set status = 'R' 
                        where job_id = '%d' and 
                        status = 'K' or status = 'F'""" % job_id)

def killTask(task_id):
    """Kills the task with the specified id. If the task has been started, a 
    kill request is sent to the node running it.
    @return: False if there were no errors killing the task, else True."""
    
    [task] = Hydra_rendertask.fetch("where id = '%d'" % task_id)
    if task.status == READY:
        task.status = KILLED
        with transaction() as t:
            task.update(t)
    elif task.status == STARTED:
        try:
            error = sendKillQuestion(task.host)
        except socketerror:
            print ("There was a problem communicating with {0:s}"
                   .format(task.host))
            error = True
    
    return error

def resurrectTask(task_id, ignoreStarted = False):
    """Resurrects the task with the specified id. 
    @return: True if there was an error, such as when the user tries to 
             resurrect a task that is marked as Started, else False."""
    
    [task] = Hydra_rendertask.fetch("where id = '%d'" % task_id)
    if (
            task.status == 'K' or task.status == 'F' or 
            (task.status == 'S' and ignoreStarted == True)
        ):
        task.status = 'R'
        task.host = None
        task.startTime = None
        task.endTime = None
    else:
        return True

    with transaction() as t:
        task.update(t)
    
    return False

if __name__ == '__main__':
    if len(argv) == 3:
        cmd, job_id = argv[1], int(argv[2])
        if cmd == 'kill':
            killJob(job_id)
        elif cmd == 'resurrect':
            resurrectJob(job_id)
    else:
        print "Command line args: ['kill' or 'resurrect'] ['job_id']"
