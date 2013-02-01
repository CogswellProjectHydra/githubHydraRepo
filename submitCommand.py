from sys import argv
from JobTicket import CMDTicket

"""Create a command ticket to plant an arbitrary command in the database as opposed to a standard render job"""

if len(argv) > 1:
    CMDTicket(argv[1:]).submit()