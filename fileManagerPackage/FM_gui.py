import maya.cmds as cmds

def printNewMenuItem( item ):
	print item
	

if cmds.window('saveWindow' , q=True, ex=True):
    cmds.deleteUI('saveWindow' , window=True)
cmds.window('saveWindow' , t='Save / Open File')
cmds.columnLayout("colomnMain" , adj = True )
cmds.paneLayout("main", configuration='vertical2' )
cmds.paneLayout("main",e=True,ps=[1,10,10] )
cmds.paneLayout("project", configuration='horizontal2' )
cmds.frameLayout ("project", label = "Project" )
cmds.textScrollList( append=['one', 'two', 'three'],w=20 )
cmds.setParent('..')
cmds.frameLayout ("projectManager", label = "Project Manager" )
cmds.textScrollList( append=['one', 'two', 'three'] )
cmds.setParent('main')

################################################
cmds.columnLayout("path",adj=True)
cmds.rowLayout( 'pathLayout',numberOfColumns=3, 
    columnWidth3=(80, 75, 150), adjustableColumn=2, 
    columnAlign=(1, 'left')
    )
cmds.text('File Path :')
cmds.textField('taskName' , text = 'master')
cmds.button(l="return",w=100)
cmds.setParent('..')
cmds.paneLayout("main_task", configuration='vertical3' )
cmds.paneLayout("central", configuration='vertical2' )
cmds.frameLayout ("seq_cate", label = "seq / cate" )
cmds.textScrollList( append=['one', 'two', 'three'] )
###################################
#                                 #
#             Sences              # 
#                                 #
###################################
cmds.setParent('..')
cmds.paneLayout("project", configuration='horizontal2' )
cmds.frameLayout ("shot / name", label = "shot / name" )
cmds.textScrollList( append=['one', 'two', 'three'] )
cmds.setParent('..')
cmds.frameLayout ("dept", label = "dept" )
cmds.textScrollList( append=['one', 'two', 'three'] )
cmds.setParent('main_task')

cmds.columnLayout("taskColumn",adj=True)
###################################
#                                 #
#         Sences  task            # 
#                                 #
###################################
cmds.frameLayout ("task", label = "Scenes Task" )
cmds.rowLayout( 'taskLayout',numberOfColumns=3, 
    columnWidth3=(80, 75, 150), adjustableColumn=2, 
    columnAlign=(1, 'left'), columnAttach=[(1, 'left', 0), 
    (2, 'left', 0), (3, 'left', 0)] 
    )
cmds.text('search : ')
cmds.textField('taskName' , text = 'master')
cmds.button()
cmds.setParent('..')
cmds.paneLayout("task_detail", configuration='vertical3', )

###################################
#                                 #
#             Sences              # 
#                                 #
###################################
cmds.frameLayout ("Sences", label = "Sences" )
cmds.textScrollList( append=['one', 'two', 'three'],w=200,h=400 )
cmds.setParent('..')
cmds.frameLayout ("Date Modified", label = "Date Modified" )
cmds.textScrollList( append=['one', 'two', 'three'] ,w=100,h=400 )
cmds.setParent('..')
cmds.frameLayout ("Size", label = "Size" )
cmds.textScrollList( append=['one', 'two', 'three'],w=100,h=400 )
cmds.setParent('colomnMain')
cmds.rowColumnLayout
###############################################
cmds.paneLayout("rowColumnSave_open",configuration='vertical2')
cmds.paneLayout("rowColumnSave_open",e=True ,ps=[1,60,10] )
cmds.columnLayout("file_type" , adj =True)
cmds.rowLayout( 'fileName',numberOfColumns=3, 
    columnWidth3=(40,10,30), adjustableColumn=2, 
    columnAlign=(1, 'left'), columnAttach=[(1, 'left', 0), 
    (2, 'left', 0), (3, 'left', 0)] 
    )
cmds.text( ' Search : ')
cmds.textField('taskName' , text = 'master')
cmds.button(l="DefultSyntax",w=100)
cmds.setParent('..')

cmds.rowLayout( ' Type',numberOfColumns=3, 
    columnWidth3=(20, 75, 150), adjustableColumn=2, 
    columnAlign=(1, 'left'), 
    columnAttach=[(1, 'left', 0), 
    (2, 'left', 0), (3, 'left', 0)] 
    )
cmds.optionMenu( label='Type    :',w=500 ,changeCommand=printNewMenuItem )
cmds.menuItem( label='Yellow' )
cmds.menuItem( label='Purple' )
cmds.menuItem( label='Orange' )
cmds.columnLayout("check" , adj =True)
cmds.checkBox( label = "follow Search", 
    onCommand = "on_func", 
    offCommand = "off_func",
    value =1
    )
cmds.checkBox( label = "update Version", 
    onCommand = "on_func", 
    offCommand = "off_func",
    value =1
    )
cmds.setParent('rowColumnSave_open')
cmds.columnLayout("ColumnSave_open" ,adj=True)
cmds.rowLayout( 'open_save',numberOfColumns=2, 
    columnWidth=(80, 75) 
    )

cmds.button(l="Save")
cmds.button(l="Open")
cmds.window('saveWindow' , e=True, wh=[1000,600])
cmds.columnLayout("colomnMain" ,e=True , h=200, w=1000)
cmds.showWindow()
