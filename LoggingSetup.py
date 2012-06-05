import logging
import logging.handlers
import os

# create logger
logger = logging.getLogger()
# to use:

from LoggingSetup import logger

# set logger level to DEBUG
logger.setLevel(logging.DEBUG)

# log file goes in %TEMP%\HydraLog.txt
logfileName = os.path.join( os.getenv( 'TEMP' ), 'HydraLog.txt' )

# create handlers and set level to debug
for handler in [logging.StreamHandler(),
                logging.handlers.TimedRotatingFileHandler( logfileName, when='midnight' ),
                ]:
    handler.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter("""
%(levelname)-9s%(message)s
%(pathname)s line %(lineno)s
%(asctime)s""")

    # add formatter to handler
    handler.setFormatter(formatter)

    # add handler to logger
    logger.addHandler(handler)

# 'application' code
if __name__ == '__main__':
        logger.debug('debug message')
        logger.info('info message')
        logger.warn('warn message')
        logger.error('error message')
        logger.critical('critical message')
