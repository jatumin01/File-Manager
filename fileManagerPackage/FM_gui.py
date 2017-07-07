import sys
import getpass
userProfile = "C:/Users/"+getpass.getuser() + "/Documents/FileManager_louise"
if not userProfile in sys.path:
    sys.path.append(userProfile)

import fileManagerPackage.FM_function as function
reload(function)

test = function.Function()



test.userPath

test.defultSystax_followTaskSearch(1)
test.defultSystax_updateVersion(1)
test.set_startProject("yggintern")
'''
test.set_project("YIT")

test.set_projectManage("sequences")

test.set_sequences_category("Y01")

test.set_shots("Y01_0020")
test.set_dept("Animation")

test.set_projectManage("assets")

test.set_sequences_category("Prop")
test.set_shots("weapon")
test.set_sequences_category("Character")
test.set_shots("norman")
test.set_dept("Model")

test.set_task("Char_Norman_A1_v010.mb")

test.set_projectManage("sequences")

test.set_sequences_category("Y01")
test.set_shots("Y01_0020")
test.set_dept("Animation")

test.set_task("Y01_0020_Animation_master.v001.ma")


'''


class Louise_Gui(object):
    
    def __init__(self):
        self.window = 'Louise_Window';
        self.title = 'Louise_Gui';
        self.size = (1000, 600);
        self.supportsToolAction = False;

    
    def commonMenu(self):
    
        self.editMenu = cmds.menu(label='Edit');
        self.editMenuSave = cmds.menuItem(
            label='Save Settings',
            command=self.editMenuSaveCmd                                     
        );
        self.editMenuReset = cmds.menuItem(
            label='Reset Settings',
            command=self.editMenuResetCmd 
        );
        self.editMenuDiv = cmds.menuItem(d=True);
        self.editMenuRadio = cmds.radioMenuItemCollection();
        self.editMenuTool = cmds.menuItem(
            label='As Tool',
            radioButton=True,
            enable=self.supportsToolAction,
            command=self.editMenuActionCmd
        );
        self.editMenuAction = cmds.menuItem(
            label='As Action',
            radioButton=True,
            enable=self.supportsToolAction,
            command=self.editMenuActionCmd
        );
        
        self.helpMenu = cmds.menu(label='Help');
        self.helpMenuItem = cmds.menuItem(
            label='Help on %s'%self.title,
            command=self.helpMenuCmd 
        );

       		    ###################################
				#                                 #
#################         commonButtons           ###########################
				#                                 #
				################################### 
        
    def commonButtons(self):
        self.colomnMain = cmds.columnLayout("colomnMain" , adj = True )
        self.paneMain = cmds.paneLayout("main", configuration='vertical2' ) #create paneMain
        cmds.paneLayout(self.paneMain,e=True,ps=[1,10,10] ) 

				###################################
				#                                 #
#################            left Pane            ###########################
				#                                 #
				###################################
        
###################################
#                                 #
#            project              # 
#                                 #
###################################
        self.paneProject = cmds.paneLayout("paneProject",configuration='horizontal2' )
        cmds.frameLayout ("project", label = "Project" )
        self.listProject = cmds.textScrollList( "listProjects" ,
        	append=self.loadlist(test.get_startProject()),
        	w=20 ,p = "project" ,
        	)
        cmds.textScrollList(self.listProject,e=True,sc = self.secList_project )


###################################
#                                 #
#         projectManager          # 
#                                 #
###################################
        cmds.setParent(self.paneProject)
        cmds.frameLayout ("projectManager", label = "Project Manager" )
        self.projectManage = cmds.textScrollList( 
        	append=self.loadlist(test.get_project()),
        	p="projectManager" ,sc=self.secList_projectManage)
                

        
				###################################
				#                                 #
#################         centarl Pane            ###########################
				#                                 #
				###################################
        cmds.setParent(self.paneMain)
        cmds.columnLayout("Path",adj=True)
        cmds.rowLayout( 'pathLayout',numberOfColumns=3, 
            columnWidth3=(80, 75, 150), adjustableColumn=2, 
            columnAlign=(1, 'left')
            )
        self.texts = cmds.text('File Path :')
        cmds.textField('taskName' , text = "%s"%(test.realtimePath))
        cmds.button(l="return",w=100)
        
        
###################################
#                                 #
#           seq / cate            # 
#                                 #
###################################
        cmds.setParent('..')
        cmds.paneLayout("main_task", configuration='vertical3' )
        cmds.paneLayout("central", configuration='vertical2' )
        cmds.frameLayout ("seq_cate", label = "seq / cate" )
        self.seq_cate = cmds.textScrollList( 
        	append=self.loadlist(test.get_projectManage()),
        	w=20 ,p = "seq_cate" , 
        	sc = self.secList_seqCate )
        
        
###################################
#                                 #
#           shot / dept           # 
#                                 #
###################################
        cmds.setParent('..')
        cmds.paneLayout("project", configuration='horizontal2' )
        cmds.frameLayout ("shot_name", label = "shot / name" )
        self.shots = cmds.textScrollList( append=self.loadlist(test.get_sequences_category()),
        	w=20 ,p = "shot_name" ,
        	sc = self.secList_dept )
        cmds.setParent('..')
        cmds.frameLayout ("dept", label = "dept" )
        self.dept = cmds.textScrollList( append=self.loadlist(test.get_shots()),
        	w=20 ,p = "dept" ,
        	sc = self.secList_task )
        cmds.setParent('main_task')
        
        cmds.columnLayout("TaskColumn",adj=True)

				###################################
				#                                 #
#################            right Pane            ###########################
				#                                 #
				###################################
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
        self.taskSences = cmds.textScrollList( append=self.loadlist(test.get_dept()),
            w=200,h=400 ,p="Sences")
        cmds.setParent('..')
        self.date = cmds.frameLayout ("Date Modified", label = "Date Modified" )
        cmds.textScrollList( append=['one', 'two', 'three'] ,w=100,h=400 )
        cmds.setParent('..')
        cmds.frameLayout ("Size", label = "Size" )
        self.size = cmds.textScrollList( append=['one', 'two', 'three'],w=100,h=400 )
        cmds.setParent('colomnMain')
        cmds.rowColumnLayout


				###################################
				#                                 #
#################          Bottom pane            ###########################
				#                                 #
				###################################

###################################
#                                 #
#         taskNameBox             # 
#                                 #
###################################
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
        
###################################
#                                 #
#         Type & checkbox         # 
#                                 #
###################################
        cmds.setParent('..')
        cmds.rowLayout( ' Type',numberOfColumns=3, 
            columnWidth3=(20, 75, 150), adjustableColumn=2, 
            columnAlign=(1, 'left'), 
            columnAttach=[(1, 'left', 0), 
            (2, 'left', 0), (3, 'left', 0)] 
            )
        cmds.optionMenu( label='Type    :',w=500 ,changeCommand=self.printNewMenuItem )
        self.menuItemList(test.fileType)
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
        cmds.formLayout("formLayout",numberOfDivisions=300)
        b1 = cmds.button(l="Save",w=150,h=30)
        b2 = cmds.button(l="Open",w=150,h=30)
        cmds.formLayout( "formLayout", edit=True, attachForm=[
            (b1, 'top', 25), (b1, 'left', 25), 
            (b2, 'top', 25), (b2, 'right', 25) ]
            )
        cmds.columnLayout(self.colomnMain ,e=True , h=200, w=1000)

				###################################
				#                                 #
#################          feature in GUI         ###########################
				#                                 #
				###################################

    def loadlist(self,List):
    	self.findList = []
    	for x in List :
    		self.findList.append(x) 

    	return self.findList


    def secList_project(self,*args) :
    	self.sec = cmds.textScrollList( "listProjects" ,q = True , selectItem = True)
    	test.set_project(self.sec[0])
    	cmds.textField('taskName' ,e=True, text = "%s"%(test.realtimePath))
    	cmds.textScrollList( self.projectManage, e=True,ra=True,
        	append=self.loadlist(test.get_project()),
        	)
    def secList_projectManage(self,*args) :
    	self.sec = cmds.textScrollList( self.projectManage ,q = True , selectItem = True)
    	test.set_projectManage(self.sec[0])
    	cmds.textField('taskName' ,e=True, text = "%s"%(test.realtimePath))
    	cmds.textScrollList( self.seq_cate, e=True,ra=True,
        	append=self.loadlist(test.get_projectManage()),
        	)
    def secList_seqCate(self,*args) :
    	self.sec = cmds.textScrollList( self.seq_cate,q = True , selectItem = True)
    	test.set_sequences_category(self.sec[0])
    	cmds.textField('taskName' ,e=True, text = "%s"%(test.realtimePath))
    	cmds.textScrollList( self.shots, e=True,ra=True,
        	append=self.loadlist(test.get_sequences_category()),
        	)
    def secList_dept(self,*args) :
    	self.sec = cmds.textScrollList( self.shots,q = True , selectItem = True)
    	test.set_shots(self.sec[0])
    	cmds.textField('taskName' ,e=True, text = "%s"%(test.realtimePath))
    	cmds.textScrollList( self.dept, e=True,ra=True,
        	append=self.loadlist(test.get_shots()),
        	)

    def secList_task(self,*args) :
    	self.sec = cmds.textScrollList( self.dept,q = True , selectItem = True)
    	test.set_dept(self.sec[0])
    	cmds.textField('taskName' ,e=True, text = "%s"%(test.realtimePath))
    	cmds.textScrollList( self.taskSences, e=True,ra=True,
        	append=self.loadlist(test.get_dept()),
        	)
'''
    	cmds.textScrollList( self.date, e=True,ra=True,
        	append=self.loadlist(test.get_time()),
        	)
    	cmds.textScrollList( self.size, e=True,ra=True,
        	append=self.loadlist(test.get_size()),
        	)
'''

    def menuItemList(self,menuList):
    	for x in menuList:
    		cmds.menuItem(l="%s"%(x))

    def printNewMenuItem(self,item=""):
	    print item

    def helpMenuCmd(self, *args): 
        cmds.launch(web='http://docs.python.org/2/library/');
    def editMenuSaveCmd(self, *args): pass 
    def editMenuResetCmd(self, *args): pass
    def editMenuToolCmd(self, *args): pass
    def editMenuActionCmd(self, *args): pass
    def displayOptions(self): pass 


###################################
#                                 #
#             Create              # 
#                                 #
###################################
    def create(self): 
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window, window=True);
        self.window = cmds.window(
            self.window,
            title=self.title,
            widthHeight=self.size,
            menuBar=True
        );
        self.commonMenu();
        self.commonButtons();
        self.optionsBorder = cmds.tabLayout( 
            scrollable=True,
            tabsVisible=False,
            height=1
        );

        
        self.displayOptions();
        cmds.showWindow();
            
        
testWindow = Louise_Gui();
testWindow.create();


cmds.showWindow()
