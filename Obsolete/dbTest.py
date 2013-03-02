import DjangoSetup

from Hydra.models import RenderTask

for rt in RenderTask.objects.all( ):
    print rt
    
