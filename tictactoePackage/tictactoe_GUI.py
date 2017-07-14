import maya.cmds as cmds
class tictactoe(object):
    
    def __init__(self):
        self.turn = 0
        self.ix = 1
        self.tictactoe = ['0','1','2','3','4','5','6','7','8','9']
    def tictactoeWindow(self,*agrs):    
        if cmds.window('tictactoeWindow' , q=True, ex=True):
                cmds.deleteUI('tictactoeWindow' , window=True)
        cmds.window('tictactoeWindow' , t='TIC TAC TOE GAME')
        cmds.columnLayout('menu' ,adjustableColumn = True,w=200)
        cmds.gridLayout( numberOfColumns=3, cellWidthHeight=(200,200) )
        cmds.iconTextButton("button1", image='blank.png',c=self.choosenum1)
        cmds.iconTextButton("button2", image='blank.png',c=self.choosenum2)
        cmds.iconTextButton("button3", image='blank.png',c=self.choosenum3)
        cmds.iconTextButton("button4", image='blank.png',c=self.choosenum4)
        cmds.iconTextButton("button5", image='blank.png',c=self.choosenum5)
        cmds.iconTextButton("button6", image='blank.png',c=self.choosenum6)
        cmds.iconTextButton("button7", image='blank.png',c=self.choosenum7)
        cmds.iconTextButton("button8", image='blank.png',c=self.choosenum8)
        cmds.iconTextButton("button9", image='blank.png',c=self.choosenum9)
        cmds.button("tryAgian",l='Reset Match' , h = 50 ,p='menu', c = self.resetMatch)
        cmds.showWindow('tictactoeWindow')
    def resetMatch(self,*args):
        self.turn = 0
        self.ix = 1
        self.tictactoe = ['0','1','2','3','4','5','6','7','8','9']
        self.tictactoeWindow()   
        
    def choosenum1(self,*agrs):
        self.UI(1)
        if self.turn%2==0:
            cmds.iconTextButton("button1",e=True,image='O.png',command = self.err)
        else :
            cmds.iconTextButton("button1",e=True,image='X.png',command = self.err)
        self.turn+=1
            
    def choosenum2(self,*agrs):
        self.UI(2)
        if self.turn%2==0:
            cmds.iconTextButton("button2",e=True,image='O.png',command = self.err)
        else :
            cmds.iconTextButton("button2",e=True,image='X.png',command = self.err)
        self.turn+=1
            
    def choosenum3(self,*agrs):
        self.UI(3)
        if self.turn%2==0:
            cmds.iconTextButton("button3",e=True,image='O.png',command = self.err)
        else :
            cmds.iconTextButton("button3",e=True,image='X.png',command = self.err)
        self.turn+=1
            
    def choosenum4(self,*agrs):
        self.UI(4)
        if self.turn%2==0:
            cmds.iconTextButton("button4",e=True,image='O.png',command = self.err)
        else :
            cmds.iconTextButton("button4",e=True,image='X.png',command = self.err)
        self.turn+=1
            
    def choosenum5(self,*agrs):
        self.UI(5)
        if self.turn%2==0:
            cmds.iconTextButton("button5",e=True,image='O.png',command = self.err)
        else :
            cmds.iconTextButton("button5",e=True,image='X.png',command = self.err)
        self.turn+=1
            
    def choosenum6(self,*agrs):
        self.UI(6)
        if self.turn%2==0:
            cmds.iconTextButton("button6",e=True,image='O.png',command = self.err)
        else :
            cmds.iconTextButton("button6",e=True,image='X.png',command = self.err)
        self.turn+=1
                        
    def choosenum7(self,*agrs):
        self.UI(7)
        if self.turn%2==0:
            cmds.iconTextButton("button7",e=True,image='O.png',command = self.err)
        else :
            cmds.iconTextButton("button7",e=True,image='X.png',command = self.err)
        self.turn+=1
                        
    def choosenum8(self,*agrs):
        self.UI(8)
        if self.turn%2==0:
            cmds.iconTextButton("button8",e=True,image='O.png',command = self.err)
        else :
            cmds.iconTextButton("button8",e=True,image='X.png',command = self.err)
        self.turn+=1
        
    def choosenum9(self,*agrs):
        self.UI(9)
        if self.turn%2==0:
            cmds.iconTextButton("button9",e=True,image='O.png',command = self.err)
        else :
            cmds.iconTextButton("button9",e=True,image='X.png',command = self.err)
        self.turn+=1
            
    def err(self,*args):
        print "Error pls try again."
    
    def play_tictactoe(self,position,player):    
        self.mask =''
        if player%2 == 1:
            self.mask = 'O'
        else :
            self.mask = 'X' 
        if position == 1 and self.tictactoe[1] == '1':
            self.tictactoe[position] =self. mask
        elif position == 2 and self.tictactoe[2] == '2':
            self.tictactoe[position] = self.mask
        elif position == 3 and self.tictactoe[3] == '3':
            self.tictactoe[position] = self.mask
        elif position == 4 and self.tictactoe[4] == '4':
            self.tictactoe[position] = self.mask
        elif position == 5 and self.tictactoe[5] == '5':
            self.tictactoe[position] = self.mask
        elif position == 6 and self.tictactoe[6] == '6':
            self.tictactoe[position] = self.mask
        elif position == 7 and self.tictactoe[7] == '7':
            self.tictactoe[position] = self.mask
        elif position == 8 and self.tictactoe[8] == '8':
            self.tictactoe[position] = self.mask
        elif position == 9 and self.tictactoe[9] == '9':
            self.tictactoe[position] = self.mask
        else :
            self.c = ' Error input pls try agian'
            return self.c
        print self.show_state() 
        self.i = self.checkwin()
        if self.i == 1 :
            self.i = 'Tic tac toe is Over \n Winner is player ' + self.mask
            cmds.iconTextButton("button1",e=True,en=False)
            cmds.iconTextButton("button2",e=True,en=False)
            cmds.iconTextButton("button3",e=True,en=False)
            cmds.iconTextButton("button4",e=True,en=False)
            cmds.iconTextButton("button5",e=True,en=False)
            cmds.iconTextButton("button6",e=True,en=False)
            cmds.iconTextButton("button7",e=True,en=False)
            cmds.iconTextButton("button8",e=True,en=False)
            cmds.iconTextButton("button9",e=True,en=False)
        elif self.i == 0 :
            self.i = 'Tic tac Toe in Progress' 
        else :
            self.i = 'Tic Tac Toe is Draw' 
            cmds.iconTextButton("button1",e=True,en=False)
            cmds.iconTextButton("button2",e=True,en=False)
            cmds.iconTextButton("button3",e=True,en=False)
            cmds.iconTextButton("button4",e=True,en=False)
            cmds.iconTextButton("button5",e=True,en=False)
            cmds.iconTextButton("button6",e=True,en=False)
            cmds.iconTextButton("button7",e=True,en=False)
            cmds.iconTextButton("button8",e=True,en=False)
            cmds.iconTextButton("button9",e=True,en=False)
        return self.i
            
    def show_state(self):
        self.asset = '\nPlayer 1 is [X] Player 2 is [O]\n'
        self.asset += self.tictactoe[1] + ' | ' + self.tictactoe[2] + ' | ' + self.tictactoe[3]
        self.asset += '\n'+ self.tictactoe[4] + ' | ' + self.tictactoe[5] + ' | ' + self.tictactoe[6] 
        self.asset += '\n' + self.tictactoe[7] + ' | ' + self.tictactoe[8] + ' | ' + self.tictactoe[9]
        return self.asset 
    
    def checkwin(self):
        if   self.tictactoe[1] == self.tictactoe[2] and self.tictactoe[2] == self.tictactoe[3]:
            return 1
        elif self.tictactoe[4] == self.tictactoe[5] and self.tictactoe[5] == self.tictactoe[6]:
            return 1
        elif self.tictactoe[7] == self.tictactoe[8] and self.tictactoe[8] == self.tictactoe[9]:
            return 1
        elif self.tictactoe[1] == self.tictactoe[4] and self.tictactoe[4] == self.tictactoe[7]:
            return 1
        elif self.tictactoe[2] == self.tictactoe[5] and self.tictactoe[5] == self.tictactoe[8]:
            return 1
        elif self.tictactoe[3] == self.tictactoe[6] and self.tictactoe[6] == self.tictactoe[9]:
            return 1
        elif self.tictactoe[7] == self.tictactoe[5] and self.tictactoe[5] == self.tictactoe[3]:
            return 1
        elif self.tictactoe[1] == self.tictactoe[5] and self.tictactoe[5] == self.tictactoe[9]:
            return 1
        elif self.tictactoe[1] != '1' and self.tictactoe[2] != '2' and self.tictactoe[3] != '3' and self.tictactoe[4] != '4' and self.tictactoe[5] != '5' and self.tictactoe[6] != '6' and self.tictactoe[7] != '7' and self.tictactoe[8] != '8' and self.tictactoe[9] != '9' :
            return -1
        else :
            return 0
            
        
    def UI(self,num):
        self.pos = num
        self.x = self.play_tictactoe(self.pos,self.ix)
        if self.x == ' Error input pls try agian':
            print self.x
        elif self.x =='Tic tac toe is Over \n Winner is player X' or  self.x =='Tic tac toe is Over \n Winner is player O' :
            print self.x
        elif self.x == 'Tic Tac Toe is Draw' :
            print self.x
        print self.x
        self.ix+=1

a = tictactoe()
a.tictactoeWindow()
