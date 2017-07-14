import sys
import getpass
import maya.cmds as cmds
userProfile = "C:/Users/"+getpass.getuser() + "/Documents/FileManager_louise"
if not userProfile in sys.path:
    sys.path.append(userProfile)
    
import tictactoePackage.tictactoe_GUI as ttt
import fileManagerPackage.FM_gui as gui
import cardGamePackage.CG_masterCompiled as runCG
    

def tictactoe(*args):
    reload(ttt)

def fileManager(*args):
    reload(gui)

def cardGame(*args):
    reload(runCG)
        
import maya.mel as mel
main = mel.eval('$main = $gMainWindow')

if cmds.menu("Menu",q=True,ex=True):
    cmds.deleteUI("Menu")
    
cmds.menu("Menu",l="Louise_menuBar",p=main,tearOff = True)
cmds.menuItem(p="Menu",l="Reload")
cmds.menuItem(p="Menu",l="FileManager",c=fileManager)
cmds.menuItem(p="Menu",divider=True)
cmds.menuItem(p="Menu",l="Tactactoe",c=tictactoe)
cmds.menuItem(p="Menu",l="CardGame",c=cardGame)
