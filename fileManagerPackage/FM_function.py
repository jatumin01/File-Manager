import maya.cmds as cmds
import os 
import re
import time
import math
import getpass

class Function(object):
    def __init__(self):
        self.userPath = "C:/Users/%s/Documents"%(getpass.getuser())
        self.startProjectPath = ""
        self.realtimePath = ""
        self.projectPath = ""
        self.projectManagePath = ""
        self.sequences_categoryPath = ""
        self.shotsPath = ""
        self.taskPath = ""
        self.taskName = ""
        self.fileType = ['mayaAscii','mb']
        self.deptList = []
        self.nonee=["None"]
        self.clearOpen()

###################################
#                                 #
#           fileDisplay           # 
#                                 #
###################################
    def set_fileDisplay(self):
            self.fileName = os.path.basename(cmds.file(q=True,loc=True))
            self.fileTime = time.ctime(os.path.getmtime(self.realtimePath))
            self.fileSize = os.path.getsize(self.realtimePath)

    def convert_size(self,size_bytes):
       if size_bytes == 0:
           return "0B"
       self.size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
       self.i = int(math.floor(math.log(size_bytes, 1024)))
       self.p = math.pow(1024, self.i)
       self.s = round(size_bytes / self.p, 2)
       return "%s %s" % (self.s, self.size_name[self.i]) 

    def get_time(self):
        if self.taskName == "" :
            print "No File"
        else :
            return self.fileTime
    def get_size(self):
        return self.convert_size(self.fileSize)

###################################
#                                 #
#           returnPath            # 
#                                 #
###################################  
    def returnPath(self) :
        self.realtimePath = os.path.dirname(self.realtimePath) 

###################################
#                                 #
#          showRealtime           # 
#                                 #
###################################      
    def get_showRealtime(self):
        return self.realtimePath

###################################
#                                 #
#          searchFile             # 
#                                 #
###################################
    def searchFile(self,input = ""):
        self.fileFind = ""
        self.List = []
        self.searchAdetp = []
        for ix in input :
            self.searchAdetp+="["+ix+"]"

        for x in self.deptList :
            if re.findall("%s"%("".join(self.searchAdetp)),x) :
                self.fileFind+=x
                self.List.append(x)

        return self.List
       
###################################
#                                 #
#          set fileType           # 
#                                 #
###################################
    def set_fileType(self,input):
        self.fileType = input

###################################
#                                 #
#            openFile             # 
#                                 #
###################################
        
    def openfile(self):
        cmds.file(rename = "%s"%(self.realtimePath),open = True)

###################################
#                                 #
#           saveFile              # 
#                                 #
###################################
        
    def saveFile(self,input):
        cmds.file(rename = "%s/%s"%(self.realtimePath,input))
        cmds.file(save=True ,type=self.fileType)

###################################
#                                 #
#          defultSystax           # 
#                                 #
###################################
    def defultSystax(self):
        self.taskNaming = "_taskName_"
        if self.follow == 1 :
            if self.searchBox != "" :
                self.taskNaming = "_"+self.searchBox+"_"

        if self.taskName == "" :
            self.defultSystax = "None Syntax"
            return self.defultSystax 
        else :
            if self.projectManage == "sequences" :
                self.shotsName = self.shots_categery
                self.defultSystax = self.shotsName + "_" + self.dept + self.taskNaming + self.verstion +".ma"
            elif self.projectManage == "assets" :
                if self.sequences_category == "Character" :
                    self.shotsName = "Char"
                elif self.sequences_category == "Prop" :
                    self.shotsName = "Prop"
                self.defultSystax = self.shotsName + "_" + self.shots_categery +"_"+ self.dept +"_" + self.verstion +".ma"
            return self.defultSystax 

    def defultSystax_followTaskSearch(self,follow = 0):
        self.follow = follow
    def defultSystax_updateVersion(self,update = 0):
        self.update = update

###################################
#                                 #
#           clearOpen             # 
#                                 #
###################################
    def clearOpen(self):
        self.showstartProject = 1
        self.showProject = 0
        self.showProjectManage = 0
        self.showSequences_category = 0
        self.showShots = 0
        self.showDept = 0
        self.showTask = 0

###################################
#                                 #
#           checkOpen             # 
#                                 #
###################################
    def checkOpen(self):
        if self.showTask == 1:
            self.showDept = 1 
            self.showShots =  1
            self.showSequences_category = 1
            self.showProjectManage = 1
            self.showProject = 1
        elif  self.showDept == 1 :
            self.showShots = 1
            self.showSequences_category = 1
            self.showProjectManage = 1
            self.showProject = 1
        elif self.showShots == 1 :
            self.showSequences_category = 1
            self.showProjectManage = 1
            self.showProject = 1
        elif self.showSequences_category == 1 :
            self.showProject = 1
            self.showProjectManage = 1
        elif self.showProjectManage == 1 :
            self.showProject = 1
        elif self.showProject == 1 :
            pass
###################################
#                                 #
#         updateVersion           # 
#                                 #
###################################  
    def updateVersion(self,taskFile):
        self.verstion = "v001"
        if taskFile != [] :
            if self.update == 1 :
                self.verstionList = []
                for x in taskFile :
                    self.verstionList += re.findall("[v][0-9]{3}",x)
                print self.verstionList[-1]
                self.verstionNew = self.verstionList[-1].split("v")
                self.convertNumVerstion = int(self.verstionNew[-1])+1
                self.verstion = "v%03d"%(self.convertNumVerstion) 

        return self.verstion


###################################
#                                 #
#           startProject          # 
#                                 #
###################################
    def set_startProject(self,input):
        self.clearOpen()
        self.startProjectPath = '%s/%s'%(self.userPath,input)
        self.realtimePath = self.startProjectPath
        self.startProjectList = os.listdir(self.startProjectPath)
    def get_startProject(self):
        if self.showstartProject == 1 :
            return self.startProjectList
        else :
            return self.nonee
###################################
#                                 #
#            Project              # 
#                                 #
###################################
    def set_project(self,input):
        self.clearOpen()
        self.showProject = 1
        self.checkOpen()
        self.projectPath = '%s/%s'%(self.startProjectPath,input)
        self.realtimePath = self.projectPath
        self.projectList = os.listdir(self.projectPath)
    def get_project(self):
        if self.showProject == 1 :
            return self.projectList
        else :
            return self.nonee

###################################
#                                 #
#         projectManage           # 
#                                 #
###################################     
    def set_projectManage(self,input):
        self.clearOpen()
        self.showProjectManage = 1
        self.checkOpen()
        self.projectManagePath = '%s/%s'%(self.projectPath,input)
        self.projectManage = input
        self.realtimePath = self.projectManagePath
        self.projectManageList = os.listdir(self.projectManagePath)
    def get_projectManage(self):
        if self.showProjectManage == 1 :
            return self.projectManageList
        else :
            return self.nonee
###################################
#                                 #
#        sequences/assets         # 
#                                 #
###################################  
    def set_sequences_category(self,input):
        self.clearOpen()
        self.showSequences_category = 1
        self.checkOpen()
        self.sequences_categoryPath = '%s/%s'%(self.projectManagePath,input)
        self.sequences_category = input
        self.realtimePath = self.sequences_categoryPath
        self.sequences_categoryList = os.listdir(self.sequences_categoryPath)
    def get_sequences_category(self):
        if self.showSequences_category == 1 :
            return self.sequences_categoryList
        else :
            return self.nonee

###################################
#                                 #
#         shots / categery        # 
#                                 #
################################### 
    def set_shots(self,input):
        self.clearOpen()
        self.showShots = 1
        self.checkOpen()
        self.shotsPath = '%s/%s'%(self.sequences_categoryPath,input)
        self.shots_categery = input
        self.realtimePath = self.shotsPath
        self.shotsList = os.listdir(self.shotsPath)
    def get_shots(self):
        if self.showShots == 1 :
            return self.shotsList
        else :
            return self.nonee


###################################
#                                 #
#              Dept               # 
#                                 #
###################################  
    def set_dept(self,input):
        self.clearOpen()
        self.showDept = 1
        self.checkOpen()
        self.deptPath = '%s/%s/scenes'%(self.shotsPath,input)
        self.dept = input
        self.realtimePath = self.deptPath
        self.deptList = os.listdir(self.deptPath) 
    def get_dept(self,inputSearch=""):
        self.searchBox = inputSearch
        if self.showDept == 1 :
            if self.searchBox != "" : 
                self.updateVersion(self.searchFile(inputSearch))
                return self.searchFile(inputSearch)
            else :
                self.updateVersion(self.deptList)
                return self.deptList

        else :
            return self.nonee
        

###################################
#                                 #
#              task               # 
#                                 #
################################### 
    def set_task(self,input):
        self.clearOpen()
        self.showTask = 1
        self.checkOpen()
        self.taskPath = '%s/%s'%(self.deptPath,input)
        self.realtimePath = self.taskPath
        self.taskName = os.path.basename(self.realtimePath)     
    def get_task(self):
        if self.showTask  == 1 :
             return   self.taskName
        else :
            return self.nonee

###################################
#                                 #
#           test Get              # 
#                                 #
################################### 
'''
    def testGet(self):
        print "project      : " + str(get_project())
        print "projectManage: " + str(get_projectManage())
        print "seq / cate   : " + str(get_sequences_category())
        print "Shots        : " + str(get_shots())
        print "Dept         : " + str(get_dept())
        print "Task         : " + str(get_task())
        print "Realtime     : " + str(get_showRealtime())
        set_fileDisplay()
        get_fileDisplay()
        print "defultSystax : " + str(defultSystax())


test = Function()
print test.userPath

test.defultSystax_followTaskSearch(1)
test.defultSystax_updateVersion(1)

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



#########################
test.testGet()

'''

