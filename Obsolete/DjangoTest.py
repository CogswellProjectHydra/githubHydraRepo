import DjangoSetup

from Hydra.models import RenderTask

RenderTask( command = 'blammo' ).save( )

for rt in RenderTask.objects.all( ):
    print rt

print RenderTask.objects.count( ), 'objects found'

RenderTask.objects.filter( command__contains = 'blammo' ).delete( )

