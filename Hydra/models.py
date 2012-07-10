from django.db import models

# Create your models here.

class RenderTask( models.Model ):
    """A command to be executed by a render machine."""

    STATUS_CHOICES = [ ('R', 'Ready'),
                       ('S', 'Started'),
                       ('F', 'Finished'),
                       ]
    status = models.CharField( max_length = 1,
                               choices = STATUS_CHOICES,
                               default = 'R',
                               )
    
    host = models.CharField( max_length = 16,
                             null = True
                             )

    command = models.CharField( max_length = 255,
                                null = True
                                )

    startTime = models.DateTimeField( null = True )

    endTime = models.DateTimeField( null = True )

    exitCode = models.IntegerField( null = True )

    logFile = models.CharField( max_length = 64,
                                null = True
                                )

    def __unicode__( self ):
        return "id %(id)s status %(status)s host %(host)s command %(command)r startTime %(startTime)s endTime %(endTime)s exitCode %(exitCode)s logFile %(logFile)s" % self.__dict__
