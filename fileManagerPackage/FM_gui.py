import maya.cmds as cmds

cmds.window()
cmds.paneLayout( configuration='quad' )
cmds.button()
cmds.frameLayout ("Name", label = "Name" )
cmds.textScrollList( append=['one', 'two', 'three'] )
cmds.scrollField()
cmds.scrollLayout()
cmds.columnLayout()
cmds.button()
cmds.button()
cmds.button()
cmds.showWindow()