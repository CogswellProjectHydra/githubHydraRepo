import re

from MySQLSetup import transaction, Hydra_rendertask

badTasks = Hydra_rendertask.fetch ("where command like '%QString%'")
print len(badTasks)
for task in badTasks:
    task.command = re.sub (r"PyQt4.QtCore.QString\(u(.*)\)", r'\1', task.command)
    with transaction () as t:
        task.update (t)
        
    
