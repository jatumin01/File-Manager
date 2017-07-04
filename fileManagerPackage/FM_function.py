import maya.cmds as cmds
import os 
import re
import time
import math
import getpass

class Function(object):
    def __init__(self):
        self.userPath = "C:/Users/%s/Documents/yggintern"%(getpass.getuser())
        self.realtimePath = ""
        self.projectPath = ""
        self.projectManagePath = ""
        self.sequencesPath = ""
        self.shotsPath = ""
        self.taskPath = ""
        self.taskName = ""
        self.fileType = 'mayaAscii'
        self.deptList = []
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

    def get_fileDisplay(self):
        if self.taskName == "" :
            print "No File"
        else :
            print "File Name     : " +self.fileName
            print "Date Modified : " +self.fileTime
            print "Size          : " +self.convert_size(self.fileSize)

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
    def searchFile(self,input):
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
        if self.taskName == "" :
            self.defultSystax = "None Syntax"
            return self.defultSystax 
        else :
            self.defultSystax = "AAAA"
            if self.projectManage == "sequences" :
                self.shotsName = self.shots_categery
            elif self.projectManage == "assets" :
                if self.sequences == "Character" :
                    self.shotsName = "Char"
                elif self.sequences == "Prop" :
                    self.shotsName = "Prop"
            self.defultSystax = self.shotsName + "_" + self.dept + "_taskName_v000.ma"
            return self.defultSystax 

###################################
#                                 #
#           clearOpen             # 
#                                 #
###################################
    def clearOpen(self):
        self.showProject = 0
        self.showProjectManage = 0
        self.showSequences = 0
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
            self.showSequences = 1
            self.showProjectManage = 1
            self.showProject = 1
        elif  self.showDept == 1 :
            self.showShots = 1
            self.showSequences = 1
            self.showProjectManage = 1
            self.showProject = 1
        elif self.showShots == 1 :
            self.showSequences = 1
            self.showProjectManage = 1
            self.showProject = 1
        elif self.showSequences == 1 :
            self.showProject = 1
            self.showProjectManage = 1
        elif self.showProjectManage == 1 :
            self.showProject = 1
        elif self.showProject == 1 :
            pass

    



###################################
#                                 #
#            Project              # 
#                                 #
###################################
    def set_project(self,input):
        self.clearOpen()
        self.showProject = 1
        self.checkOpen()
        self.projectPath = '%s/%s'%(self.userPath,input)
        self.realtimePath = self.projectPath
        self.projectList = os.listdir(self.projectPath)
    def get_project(self):
        if self.showProject == 1 :
            return self.projectList
        else :
            print "[Project]"

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
            print "[ProjectManage]"
###################################
#                                 #
#        sequences/assets         # 
#                                 #
###################################  
    def set_sequences(self,input):
        self.clearOpen()
        self.showSequences = 1
        self.checkOpen()
        self.sequencesPath = '%s/%s'%(self.projectManagePath,input)
        self.sequences = input
        self.realtimePath = self.sequencesPath
        self.sequencesList = os.listdir(self.sequencesPath)
    def get_sequences(self):
        if self.showSequences == 1 :
            return self.sequencesList
        else :
            print "[Sequences]"

###################################
#                                 #
#         shots / categery        # 
#                                 #
################################### 
    def set_shots(self,input):
        self.clearOpen()
        self.showShots = 1
        self.checkOpen()
        self.shotsPath = '%s/%s'%(self.sequencesPath,input)
        self.shots_categery = input
        self.realtimePath = self.shotsPath
        self.shotsList = os.listdir(self.shotsPath)
    def get_shots(self):
        if self.showShots == 1 :
            return self.shotsList
        else :
            print "[Shots]"


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
    def get_dept(self):
        if self.showDept == 1 :
            return self.deptList
        else :
            print "[Dept]"
        

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
            print "[Task]"     
###################################
#                                 #
#           test Get              # 
#                                 #
################################### 
    def testGet(self):
        print "project      : " + str(test.get_project())
        print "projectManage: " + str(test.get_projectManage())
        print "sequences    : " + str(test.get_sequences())
        print "Shots        : " + str(test.get_shots())
        print "Dept         : " + str(test.get_dept())
        print "Task         : " + str(test.get_task())
        print "Realtime     : " + str(test.get_showRealtime())
        test.set_fileDisplay()
        test.get_fileDisplay()
        print "defultSystax : " + str(test.defultSystax())


test = Function()
print test.userPath

test.set_project("YIT")
test.set_projectManage("sequences")
test.set_sequences("Y01")
test.set_shots("Y01_0020")
test.set_dept("Animation")

test.set_projectManage("assets")
'''
test.set_sequences("Prop")
test.set_shots("weapon")
test.set_sequences("Character")
test.set_shots("norman")
test.set_dept("Model")
test.set_task("Char_Norman_A1_v010.mb")

test.set_projectManage("sequences")
test.set_sequences("Y01")
test.set_shots("Y01_0020")
test.set_dept("Animation")
test.set_task("Y01_0020_Animation_master.v001.ma")
'''
#########################
test.testGet()



