'''
Created on Feb 16, 2013

@author: Aaron Cohn
@summary: Procedures for killing and resurrecting jobs and tasks
'''
from socket import error as socketerror
from MySQLSetup import Hydra_rendertask, transaction, KILLED, READY, STARTED
from Connections import TCPConnection
from Questions import CMDQuestion
from LoggingSetup import logger
from sys import argv

def sendRebootQuestion(renderhost):
    
    connection = TCPConnection(hostname=renderhost)
    answer = connection.getAnswer(CMDQuestion("shutdown /r /t 0"))
    return answer    

if __name__ == '__main__':
    if len(argv) == 2:
        host = argv[1]
        print sendRebootQuestion (host).output
    else:
        print "Command line args: hostName"
