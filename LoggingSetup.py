import logging
import logging.handlers
import os
from sys import argv

"""Sets up the logging instances with formatters and handlers,
for use in other modules, to make logging and debugging simple, easy and standardized."""

# create logger
logger = logging.getLogger()
# to use:

#from LoggingSetup import logger

# set logger level to DEBUG
logger.setLevel(logging.DEBUG)
"""Sets the logger to log all messages of level DEBUG and greater (e.g., all log messages.)"""

if argv[0]:
    # get the full path of the currently running process, split it into pieces, and get the last piece (the file name of the process)
    appname = argv[0].split('\\')[-1]
    
    # discard the file extension
    appname = os.path.splitext(appname)[0]
else:
    appname = "interpreter_output"

# set the log file path to C:\Hydra\Logs\appname.txt
logfileName = os.path.join( 'C:\\Hydra\\Logs\\', appname + '.txt')
"""Specifies where the log file will be saved. For now, the log file is saved in the OS's temp directory (essentially for junk files)
in a file named 'HydraLog.txt'. This behavior can later be changed to change how and where log messages are saved."""

# create handlers and set level to debug
for handler in [logging.StreamHandler(),
                logging.handlers.TimedRotatingFileHandler( logfileName, when='midnight' ),
                ]:
    handler.setLevel(logging.DEBUG)
    """Sets the handler to log all message levels from DEBUG upwards (so also INFO, WARN, ERROR, and CRITICAL."""

    # create formatter
    formatter = logging.Formatter("""
%(levelname)-9s%(message)s
%(pathname)s line %(lineno)s
%(asctime)s""")
    """Defines a logging.Formatter instance specifycing a standardized log
message format. "levelname" corresponds to the log message type (debug, warn, etc)
message refers to the argument passed as the log message (by the user), pathname refers
to the full path and filename where the log message occurred, lineno specifies the line number,
and asctime specifies the time when the log message occurred."""

    # add formatter to handler
    handler.setFormatter(formatter)
    """Specifies that our logger handler should format messages using the previously
defined Formatter instance."""

    # add handler to logger
    logger.addHandler(handler)
    """Lastly, adds our handler to the logger object, so the logger knows how to behave when
logging a log message using one of the library's pre-defined logging methods."""

# 'application' code
if __name__ == '__main__':
        logger.debug('debug message')
        logger.info('info message')
        logger.warn('warn message')
        logger.error('error message')
        logger.critical('critical message')
