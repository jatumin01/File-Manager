import maya.cmds as mc
import os 
import re
import sys

class Function(object):
    def __init__(self):
        self.userPath = "C:/Users/eur/Documents/yggintern"
        self.realtimePath = ""
        self.projectPath = ""
        self.projectManagePath = ""
        self.sequencesPath = ""
        self.shotsPath = ""
        self.fileType = 'mayaAscii'
        self.deptList = []
    
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
       
        
    def set_fileType(self,input):
        self.fileType = input
        
    def openfile(self):
        cmds.file(rename = "%s"%(self.realtimePath),open = True)
        
    def saveFile(self,input):
        cmds.file(rename = "%s/%s"%(self.realtimePath,input))
        cmds.file(save=True ,type=self.fileType)

    def set_project(self,input):
        self.projectPath = '%s/%s'%(self.userPath,input)
        self.realtimePath = self.projectPath
        self.projectList = os.listdir(self.projectPath)

        
    def set_projectManage(self,input):
        self.projectManagePath = '%s/%s'%(self.projectPath,input)
        self.realtimePath = self.projectManagePath
        self.projectManageList = os.listdir(self.projectManagePath)

        
    def set_sequences(self,input):
        self.sequencesPath = '%s/%s'%(self.projectManagePath,input)
        self.realtimePath = self.sequencesPath
        self.sequencesList = os.listdir(self.sequencesPath)

    
    def set_shots(self,input):
        self.shotsPath = '%s/%s'%(self.sequencesPath,input)
        self.realtimePath = self.shotsPath
        self.shotsList = os.listdir(self.shotsPath)

        
    def set_dept(self,input):
        self.deptPath = '%s/%s/scenes'%(self.shotsPath,input)
        self.realtimePath = self.deptPath
        self.deptList = os.listdir(self.deptPath)

    def get_project(self):
        return self.projectList
        
    def get_projectManage(self):
        return self.projectManageList
        
    def get_sequences(self):
        return self.sequencesList
    
    def get_shots(self):
        return self.shotsList
        
    def get_dept(self):
        return self.deptList
    
    def get_showRealtime(self):
        return self.realtimePath



        
test = Function()
print test.userPath

test.set_project("YIT")
test.set_projectManage("sequences")
test.set_sequences("Y01")
test.set_shots("Y01_0020")
test.set_dept("Animation")
print test.get_project()
print test.get_projectManage()
print test.get_sequences()
print test.get_shots()
print test.get_dept()
print test.get_showRealtime()
print test.searchFile("v002")





