from maya import cmds
import subprocess

subprocess.check_call(['cmd', '/c', 'start', r'c:\python27\python.exe',
    r'\\flex2.cpc.local\projectHydra\githubHydraRepo\submitterMain.py',
#    r'u:\hydraRepo\submitterMain.py',
    '"' + cmds.file( query = True, location = True ) + '"',
    str( cmds.getAttr( 'defaultRenderGlobals.startFrame' ) ),
    str( cmds.getAttr( 'defaultRenderGlobals.endFrame' ) ),
    str( cmds.getAttr( 'defaultRenderGlobals.byFrame' ) ),
    ])
