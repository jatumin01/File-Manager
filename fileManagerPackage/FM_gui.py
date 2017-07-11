import getpass
import os 
import maya.cmds as cmds
import fileManagerPackage.FM_function as function
reload(function)

test = function.Function()



test.userPath
test.set_startProject("yggintern")



class Louise_Gui(object):
    
    def __init__(self):
        self.window = 'Louise_Window';
        self.title = 'Louise_Gui';
        self.size = (1000, 600);
        self.supportsToolAction = False;
        self.ix = 0

    
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

   			######################################################
			#                                 ####################
        	#         commonButtons           ####################
			#                                 ####################
			######################################################
        
    def commonButtons(self):
        self.colomnMain = cmds.columnLayout("colomnMain" , adj = True )
        self.paneMain = cmds.paneLayout("main", configuration='vertical2' ) #create paneMain
        cmds.paneLayout(self.paneMain,e=True,ps=[1,10,10] ) 
        
			######################################################
			#                                 ####################
        	#           left Pane             ####################
			#                                 ####################
			######################################################
                
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
                
        

			######################################################
			#                                 ####################
        	#         centarl Pane            ####################
			#                                 ####################
			######################################################
        cmds.setParent(self.paneMain)
        cmds.columnLayout("Path",adj=True)
        cmds.rowLayout( 'pathLayout',numberOfColumns=3, 
            columnWidth3=(80, 75, 150), adjustableColumn=2, 
            columnAlign=(1, 'left')
            )
        self.texts = cmds.text('File Path :')
        cmds.textField('taskName' ,en=False,text = "%s"%(test.realtimePath))
        #cmds.button(l="return",w=100)
                
                
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
        
			######################################################
			#                                 ####################
        	#           right Pane            ####################
			#                                 ####################
			######################################################
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
        self.searchBox = cmds.textField(ec=self.searchButton)
        self.searchButton = cmds.button(l = "Find" ,c=self.searchButton)
        cmds.setParent('..')
        cmds.paneLayout("task_detail", configuration='vertical3', )
                
        	###################################
        	#                                 #
        	#             Sences              # 
        	#                                 #
        	###################################
        cmds.frameLayout ("Sences", label = "Sences" )
        self.taskSences = cmds.textScrollList( append=self.loadlist(test.get_dept()),
            w=200,h=400 ,p="Sences",sc = self.taskNameBox)
        cmds.setParent('..')
        cmds.frameLayout ("Date Modified", label = "Date Modified" )
        self.Date = cmds.textScrollList( w=100,h=400 )
        cmds.setParent('..')
        cmds.frameLayout ("Size", label = "Size" )
        self.Size = cmds.textScrollList( w=100,h=400 )
        cmds.setParent('colomnMain')
        cmds.rowColumnLayout
        
        
			######################################################
			#                                 ####################
            #         Bottom pane             ####################
			#                                 ####################
			######################################################
        
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
        self.taskName = cmds.textField('taskFile' )
        self.defultSyntax = cmds.button(l="DefultSyntax",w=100,c=self.DefultSyntax)
        	        
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
            onCommand = self.followTaskSearch_on, 
            offCommand = self.followTaskSearch_off,
            value =0
            )
        cmds.checkBox( label = "update Version", 
            onCommand = self.updateVersion_on, 
            offCommand = self.updateVersion_off,
            value =0 
            )
        cmds.setParent('rowColumnSave_open')
        cmds.formLayout("formLayout",numberOfDivisions=300)
        self.b1 = cmds.button(l="Save",w=150,h=30,en=False,c=self.saveFuciton)
        self.b2 = cmds.button(l="Open",w=150,h=30,en=False,c=self.openFuciton)
        cmds.formLayout( "formLayout", edit=True, attachForm=[
            (self.b1, 'top', 25), (self.b1, 'left', 25), 
            (self.b2, 'top', 25), (self.b2, 'right', 25) ]
            )
        cmds.columnLayout(self.colomnMain ,e=True , h=200, w=1000)














			######################################################
			#                                 ####################
        	#          feature in GUI         ####################
			#                                 ####################
			######################################################

    def DefultSyntax(self,*args):
    	self.searchName = cmds.textField(self.searchBox,q=True,text = True)
    	test.searchBox = self.searchName
    	self.defultAttr = test.defultSystax()
    	cmds.textField('taskFile',e=True ,text=self.defultAttr)

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

    def searchButton(self,*args):
    	self.searchName = cmds.textField(self.searchBox,q=True,text = True)
        cmds.textScrollList( self.taskSences, e=True,ra=True,append=self.loadlist(test.get_dept(self.searchName)))
        test.set_fileDisplay(self.searchName)
        cmds.textScrollList( self.Date, e=True,ra=True,append=self.loadlist(test.get_time()))
        cmds.textScrollList( self.Size, e=True,ra=True,append=self.loadlist(test.get_size()))

    def secList_task(self,*args) :
        cmds.button(self.b1,e=True,en=True)
        cmds.button(self.b2,e=True,en=True)
        self.saveList = []
        self.savePath = []
        self.sec = cmds.textScrollList( self.dept,q = True , selectItem = True)
        test.set_dept(self.sec[0])
        cmds.textField('taskName' ,e=True, text = "%s"%(test.realtimePath))
        self.showTask()

    def showTask(self):
        cmds.textScrollList( self.taskSences, e=True,ra=True,append=self.loadlist(test.get_dept()))
        test.set_fileDisplay()
        cmds.textScrollList( self.Date, e=True,ra=True,append=self.loadlist(test.get_time()))
        cmds.textScrollList( self.Size, e=True,ra=True,append=self.loadlist(test.get_size()))

    def taskNameBox(self,*args):
    	self.sec = cmds.textScrollList( self.taskSences ,q = True , selectItem = True)
    	test.set_task(self.sec[0])
    	cmds.textField('taskName' ,e=True, text = "%s"%(test.realtimePath))
    	cmds.textField(self.taskName , e=True , text = "%s"%(self.sec[0]))

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

    def saveFuciton(self,*args):
    	self.fileName = cmds.textField(self.taskName , q=True ,text=True )
    	self.rename = os.path.dirname(test.realtimePath)
    	test.saveFile("%s/%s"%(test.deptPath,self.fileName))
    	self.secList_task()
    	print test.realtimePath
    def openFuciton(self,*args):
    	self.fileName = cmds.textField(self.taskName , q=True ,text=True )
    	test.openFile()
    def followTaskSearch_on(self,*args):
    	test.defultSystax_followTaskSearch(1)
    	print "Task 1"
    def followTaskSearch_off(self,*args):
    	test.defultSystax_followTaskSearch(0)
    	print "Task 0"
    def updateVersion_on(self,*args) :
    	test.defultSystax_updateVersion(1)
    	print "version 1"
    def updateVersion_off(self,*args) :
    	test.defultSystax_updateVersion(0)
    	print "version 0"
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
