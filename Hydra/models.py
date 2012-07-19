from django.db import models

"""Classes defining our MySQL database"""

class Job( models.Model ):
    """A submitted job"""
    
    createTime = models.DateTimeField( auto_now_add = True )
    
    pickledTicket = models.CharField( max_length = 1024, null = False )

class RenderTask( models.Model ):
    """A command to be executed by a render machine."""

    job = models.ForeignKey( Job, null = False )

    STATUS_CHOICES = [ ('R', 'Ready'),
                       ('A', 'Assigned'),
                       ('S', 'Started'),
                       ('F', 'Finished'),
                       ]
    status = models.CharField( max_length = 1,
                               choices = STATUS_CHOICES,
                               default = 'R',
                               )
    
    host = models.CharField( max_length = 32,
                             null = True
                             )

    command = models.CharField( max_length = 255,
                                null = True
                                )

    createTime = models.DateTimeField( auto_now_add = True )

    startTime = models.DateTimeField( null = True )

    endTime = models.DateTimeField( null = True )

    exitCode = models.IntegerField( null = True )

    logFile = models.CharField( max_length = 64,
                                null = True
                                )

    def __unicode__( self ):
        return "id %(id)s status %(status)s host %(host)s command %(command)r startTime %(startTime)s endTime %(endTime)s exitCode %(exitCode)s logFile %(logFile)s" % self.__dict__


class RenderNode( models.Model ):
    """A render machine's state."""

    host = models.CharField( max_length = 32,
                             primary_key = True
                             )
    
    STATUS_CHOICES = [ ('R', 'Ready'),
                       ('A', 'Assigned'),
                       ('S', 'Started'),
                       ('O', 'Offline'),
                       ]
    status = models.CharField( max_length = 1,
                               choices = STATUS_CHOICES,
                               default = 'O',
                               )

    task = models.OneToOneField( RenderTask , null = True )
    
