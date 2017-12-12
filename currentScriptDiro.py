import os
import inspect 

#here the two functions the first one gave the path for the current running script
def currentScriptPath():
    return os.path.abspath(inspect.getsourcefile(lambda:0))
# the second the directory that the current running script file is on
def currentScriptDiro():
    return os.path.dirname(currentScriptPath())

CURRENT_SCRIPT_DIRO = currentScriptDiro()
CURRENT_SCRIPT_PATH = currentScriptPath()

print("CURRENT_SCRIPT_DIRO=>", CURRENT_SCRIPT_DIRO)
print("CURRENT_SCRIPT_PATH=>", CURRENT_SCRIPT_PATH)

