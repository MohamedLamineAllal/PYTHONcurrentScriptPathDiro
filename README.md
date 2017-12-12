# PYTHONcurrentScriptPathDiro
This is a meme, a code snippet that detecte and give the current running script path and dironame, there is two files, the code itself, and also a .json file that containe a snippet configuration for VSCODE, and it will work or can be modified to work with all others editors that have the same format. Working with snippet boost your productivity and your work time.

the code snippet is as fellow:
########################################"
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
####################################################

you may need to read about how to add snippet to vscode. (google it)


