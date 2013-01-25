"""Classes representing submitted jobs. These contain extra information that's
not strictly necessary to getting the jobs executed."""

import pickle
from LoggingSetup import logger

from MySQLSetup import Hydra_job, Hydra_rendertask

class JobTicket:
    """A generic job ticket"""

    def submit( self ):
        job = self.createJob( )
        self.createTasks( job )

    def createJob( self ):
        job = Hydra_job( pickledTicket = pickle.dumps( self ) )
        job.insert( )
        return job

    def createTasks( self, job ):
        raise NotImplemented

class MayaTicket( JobTicket ):

    def __init__( self, sceneFile, startFrame, endFrame, batchSize, priority ):
        self.sceneFile = sceneFile
        self.startFrame = startFrame
        self.endFrame = endFrame
        self.batchSize = batchSize
        self.priority = priority

    def createTasks( self, job ):
        starts = range( self.startFrame, self.endFrame + 1, self.batchSize )
        ends = [min( start + self.batchSize - 1,
                     self.endFrame )
                for start in starts
                ]
        for start, end in zip( starts, ends ):
            command = [
                        r'c:\program files\autodesk\maya2011\bin\render.exe',
                        '-mr:v', '5',
                        '-s', str( start ),
                        '-e', str( end ),
                        self.sceneFile
                      ]
            path = self.sceneFile.split( '/' )
            if 'scenes' in path:
                project = '/'.join( path[ : path.index( 'scenes' ) ])
                command[-1:-1] = ['-proj', project]
                                    
            logger.debug( command )
            Hydra_rendertask( status = READY,
                              command = repr( command ),
                              job_id = job.id, priority = self.priority).insert( ) # the keys here represent columns in the database table
