import DjangoSetup

from Hydra.models import RenderTask

RenderTask( command = 'blammo' ).save( )
for rt in RenderTask.objects.all( ):
    print rt
print RenderTask.objects.count( ), 'objects found'
print RenderTask.objects.get( id = 3 )

