import random
import maya.cmds as cmds
class CardGame(object):
    def __init__(self,Hero,Monster,Boss):
        super(CardGame,self).__init__()
        self.hero = Hero
        self.monster = Monster
        self.boss = Boss
        self.cardHero = [0,0,0]
         
    
    def randomCard(self,x):
        x.selectCard = random.randint(0,3)
        self.monsterName = 'Mons'
        if self.state == 2 :
            self.monsterName = 'Boss'

        if x.selectCard == 0 :
            cmds.iconTextButton("cardMon",e=True, image='a%s.png'%(self.monsterName))
        elif x.selectCard == 1 :
            cmds.iconTextButton("cardMon",e=True, image='d%s.png'%(self.monsterName))
        elif x.selectCard == 2 :
            cmds.iconTextButton("cardMon",e=True, image='b%s.png'%(self.monsterName))
        else :
            cmds.iconTextButton("cardMon",e=True, image='heal.png')
    
    def randomCardHero(self):
        for x in range(3):
            self.cardHero[x] = random.randint(0,3)
        print 'Draw Card : ' + str(self.cardHero)
        
    def chooseCard(self):
        print 'You Have Card ' + str(self.cardHero)
        if self.hero.selectCard == 0 :
            cmds.iconTextButton("cardHero",e=True, image='aHero.png')
        elif self.hero.selectCard == 1 :
            cmds.iconTextButton("cardHero",e=True, image='dHero.png')
        elif self.hero.selectCard == 2 :
            cmds.iconTextButton("cardHero",e=True, image='bHero.png')
        else :
            cmds.iconTextButton("cardHero",e=True, image='heal.png')
                       
                   
    def imageHero(self):
        self.count = 0
                
        for x in self.cardHero :
            if x == 0 :
                cmds.iconTextButton("button%s"%(self.count),e=True, image='aHero.png')
            elif x == 1 :
                cmds.iconTextButton("button%s"%(self.count),e=True, image='dHero.png')
            elif x == 2 :
                cmds.iconTextButton("button%s"%(self.count),e=True, image='bHero.png')
            else :
                cmds.iconTextButton("button%s"%(self.count),e=True, image='heal.png')
            self.count+=1     
    def action(self):
        self.fineMonster = 1
        
             
        if self.state != 3 :            
            if self.hero.hp >0 and self.monsterType.hp >0 :
                
                print '--------- Turn ' + str(self.turn) +' -------------'
                
                self.imageHero()
                
                self.randomCard(self.monsterType)       
                self.chooseCard()
                print 'Hero SelectCard == ' + str(self.hero.selectCard) + '\nMonster SelectCard == ' + str(self.monsterType.selectCard)
                if self.hero.selectCard == 0 and self.monsterType.selectCard == 0 :
                    self.hero.hp -= self.monsterType.atk
                    self.monsterType.hp -= self.hero.atk
                    cmds.text("event",e=True, label ='Hero Attack : ' +str(self.hero.atk) +'\n'+ self.monsterType.name + ' Attack : ' +str(self.monsterType.atk) )
                    print 'Hero Attack : ' +str(self.hero.atk)
                    print self.monsterType.name + ' Attack : ' +str(self.monsterType.atk)
                elif self.hero.selectCard == 0 and self.monsterType.selectCard == 1 :
                    self.monsterType.hp -= (self.hero.atk - self.monsterType.deff)
                    cmds.text("event",e=True,label ='Hero Attack : ' +str(self.hero.atk)+'\n'+self.monsterType.name + ' Deffend : ' +str(self.monsterType.deff))
                    print 'Hero Attack : ' +str(self.hero.atk)
                    print self.monsterType.name + ' Deffend : ' +str(self.monsterType.deff)
                elif self.hero.selectCard == 0 and self.monsterType.selectCard == 2 :
                    self.monsterType.hp -= self.hero.atk
                    cmds.text("event",e=True,label ='Hero Attack : ' + str(self.hero.atk) +'\n'+self.monsterType.name + ' Break  : Break Fail ')
                    print 'Hero Attack : ' + str(self.hero.atk)
                    print self.monsterType.name + ' Break  : Break Fail '
                elif self.hero.selectCard == 0 and self.monsterType.selectCard == 3 :
                    self.monsterType.hp -= (self.hero.atk-self.monsterType.hel)
                    cmds.text("event",e=True,label ='Hero Attack : ' +str(self.hero.atk) +'\n'+self.monsterType.name + ' Heal : ' +str(self.monsterType.hel))
                    print 'Hero Attack : ' +str(self.hero.atk)
                    print self.monsterType.name + ' Heal : ' +str(self.monsterType.hel)
                elif self.hero.selectCard == 1 and self.monsterType.selectCard == 0 :
                    self.hero.hp -= ( self.monsterType.atk - self.hero.deff )
                    cmds.text("event",e=True,label ='Hero Deffend : ' +str(self.hero.deff)+'\n'+self.monsterType.name + ' Attack : ' +str(self.monsterType.atk) )
                    print 'Hero Deffend : ' +str(self.hero.deff)
                    print self.monsterType.name + ' Attack : ' +str(self.monsterType.atk)            
                elif self.hero.selectCard == 1 and self.monsterType.selectCard == 1 :
                    cmds.text("event",e=True,label ='Hero Deffend : ' +str(self.hero.deff)+'\n'+self.monsterType.name + ' Deffend : ' +str(self.monsterType.deff) +'\n'+  'Nothing' )
                    print 'Hero Deffend : ' +str(self.hero.deff)
                    print self.monsterType.name + ' Deffend : ' +str(self.monsterType.deff)   
                    print 'Nothing'
                elif self.hero.selectCard == 1 and self.monsterType.selectCard == 2 :
                    self.hero.hp -= self.monsterType.brk
                    cmds.text("event",e=True,label ='Hero Deffend : Deffend Fail'+'\n'+self.monsterType.name + ' Break : ' +str(self.monsterType.brk)   )
                    print 'Hero Deffend : Deffend Fail'
                    print self.monsterType.name + ' Break : ' +str(self.monsterType.brk)  
                elif self.hero.selectCard == 1 and self.monsterType.selectCard == 3 :
                    self.monsterType.hp += self.monsterType.hel
                    cmds.text("event",e=True,label ='Hero Deffend : ' +str(self.hero.deff) +'\n'+self.monsterType.name + ' Heal : ' +str(self.monsterType.hel)  )
                    print 'Hero Deffend : ' +str(self.hero.deff)
                    print self.monsterType.name + ' Heal : ' +str(self.monsterType.hel)  
                elif self.hero.selectCard == 2 and self.monsterType.selectCard == 0 :
                    self.hero.hp -= self.monsterType.atk
                    cmds.text("event",e=True,label = 'Hero Break : Break Fail' +'\n'+self.monsterType.name + ' Attack : ' +str(self.monsterType.atk) )
                    print 'Hero Break : Break Fail' 
                    print self.monsterType.name + ' Attack : ' +str(self.monsterType.atk) 
                elif self.hero.selectCard == 2 and self.monsterType.selectCard == 1 :
                    self.monsterType.hp -= self.hero.brk
                    cmds.text("event",e=True,label = 'Hero Break : ' +str(self.hero.brk) +'\n'+self.monsterType.name + ' Deffend : Deffend Fail')
                    print 'Hero Break : ' +str(self.hero.brk)
                    print self.monsterType.name + ' Deffend : Deffend Fail'
                elif self.hero.selectCard == 2 and self.monsterType.selectCard == 2 :
                    self.hero.hp -= self.monsterType.brk
                    self.monsterType.hp -= self.hero.brk
                    cmds.text("event",e=True,label ='Hero Break : ' +str(self.hero.brk) +'\n'+self.monsterType.name + ' Break : ' +str(self.monsterType.brk))
                    print 'Hero Break : ' +str(self.hero.brk)
                    print self.monsterType.name + ' Break : ' +str(self.monsterType.brk)
                elif self.hero.selectCard == 2 and self.monsterType.selectCard == 3 :
                    self.monsterType.hp -= (self.hero.brk-self.monsterType.hel)
                    cmds.text("event",e=True,label ='Hero Break : ' +str(self.hero.brk) +'\n'+self.monsterType.name + ' Heal : ' +str(self.monsterType.hel))
                    print 'Hero Break : ' +str(self.hero.brk)
                    print self.monsterType.name + ' Heal : ' +str(self.monsterType.hel)
                elif self.hero.selectCard == 3 and self.monsterType.selectCard == 0 :
                    self.hero.hp -= (self.monsterType.atk-self.hero.hel)
                    cmds.text("event",e=True,label ='Hero Heal : ' +str(self.hero.hel) +'\n'+self.monsterType.name + ' Attack : ' +str(self.monsterType.atk))
                    print 'Hero Heal : ' +str(self.hero.hel)
                    print self.monsterType.name + ' Attack : ' +str(self.monsterType.atk)
                elif self.hero.selectCard == 3 and self.monsterType.selectCard == 1 :
                    self.hero.hp += self.hero.hel
                    cmds.text("event",e=True,label =' Hero Heal : ' +str(self.hero.hel) +'\n'+self.monsterType.name + ' Deffend ')
                    print 'Hero Heal : ' +str(self.hero.hel)
                    print self.monsterType.name + ' Deffend '
                elif self.hero.selectCard == 3 and self.monsterType.selectCard == 2 :
                    self.hero.hp -= (self.monsterType.brk-self.hero.hel)
                    cmds.text("event",e=True,label ='Hero Heal : ' +str(self.hero.hel) +'\n'+self.monsterType.name + ' Break : ' +str(self.monsterType.brk)) 
                    print 'Hero Heal : ' +str(self.hero.hel)
                    print self.monsterType.name + ' Break : ' +str(self.monsterType.brk)
                elif self.hero.selectCard == 3 and self.monster.selectCard == 3 :
                    self.monsterType.hp += self.monsterType.hel
                    self.hero.hp += self.hero.hel
                    cmds.text("event",e=True,label ='Hero Heal : ' +str(self.hero.hel) +'\n'+self.monsterType.name + ' Heal : ' +str(self.monsterType.hel)) 
                    print 'Hero Heal : ' +str(self.hero.hel)
                    print self.monsterType.name + ' Heal : ' +str(self.monsterType.hel)

                if self.hero.hp > 300 :
                    self.hero.hp = 300
                if self.monster.hp > 150 :
                    self.monsterType.hp = 150
                if self.boss.hp > 300 :
                    self.boss.hp = 300

                print self.hero.name + ' HP : ' + str(self.hero.hp)
                print self.monsterType.name + '  HP : ' + str(self.monsterType.hp)


                if self.state == 1:
                    cmds.text("MHp",e=True, label = "Monster HP %s/150"%(self.monsterType.hp))
  
                elif self.state == 2 :
                    cmds.text("MHp",e=True, label = "Boss HP %s/300"%(self.monsterType.hp))  
                cmds.text("HHp",e=True, label = "Hero HP %s/300"%(self.hero.hp)) 
                
                self.checkHPbar()
                self.turn+=1
                
        if self.state == 1 :
            if self.hero.hp <= 0 :
                cmds.text("event",e=True, label = 'Monster Win \n----------- End Game ------------ ' )
                print '-------- Monster Win -----------'
                self.end()
            elif self.monster.hp <= 0 :
                self.state+=1
                cmds.text("event",e=True, label = ' Hero Win  \n----------- Next State (Boss)  ------------ ' )
                print '-------- Hero Win --------------'
                print '-------- Next State (Boss) ----------'
                self.monsterType = self.boss  
                cmds.iconTextButton('Monsterss',e=True,image='charBoss.png')   
                cmds.iconTextButton('cardMon',e=True,image='backCard.png') 
                cmds.iconTextButton('cardHero',e=True,image='backCard.png')     
                cmds.text("MHp",e=True, label = "Boss HP 300/300") 
        elif self.state == 2 :
            if self.hero.hp <= 0 :
                cmds.text("event",e=True, label = ' Boss Win \n----------- End Game ------------ ' )
                print '-------- Boss Win -----------'
                print '--------- End Game ----------'
                self.end()
            elif self.monsterType.hp <= 0 :
                cmds.text("event",e=True, label = ' Hero Win  \n----------- End Game  ------------ ' )
                print '-------- Hero Win --------------'
            
                print '--------- End Game ----------'
                self.end()

    def end (self,*args):
        cmds.columnLayout('menu',e=True, backgroundColor =[0.4, 0.4, 0.4])
        cmds.iconTextButton( 'Monsterss',e=1,en=0,backgroundColor = [0.4, 0.4, 0.4])
        cmds.iconTextButton("cardMon",e=1,en=0,backgroundColor = [0.4, 0.4, 0.4]) 
        cmds.iconTextButton('HeroChar',e=1,en=0,backgroundColor = [0.4, 0.4, 0.4])
        cmds.iconTextButton("cardHero",e=1,en=0 ,backgroundColor = [0.4, 0.4, 0.4])
        cmds.iconTextButton("button0", e=1,en=0,backgroundColor = [0.4, 0.4, 0.4])
        cmds.iconTextButton("button1",e=1,en=0 ,backgroundColor = [0.4, 0.4, 0.4])
        cmds.iconTextButton("button2",e=1,en=0 ,backgroundColor = [0.4, 0.4, 0.4])

    def checkHPbar(self):

        if self.hero.hp <= 0 :
            self.hero.hp = 0
        if self.monster.hp <= 0 :
           self.monster.hp = 0
        if self.boss.hp <= 0 :
          self.boss.hp = 0

        self.rHero = 0.00
        self.gHero = 0.00
        self.rMonster = 0.00
        self.gMonster = 0.00
        self.rBoss = 0.00
        self.gBoss = 0.00
        self.Hpercent = self.hero.hp*100 /300.00
        self.Mpercent = (self.monster.hp/150.00) * 100.00
        self.Bpercent = (self.boss.hp/300.00) * 100.00

        self.gHero = self.Hpercent*1.00 /100.00
        self.rHero = 1.00 - self.gHero 
        self.gMonster = (self.Mpercent/100.00) * 1.00
        self.rMonster = 1.00 - self.gMonster 
        self.gBoss = (self.Bpercent/100.00) * 1.00
        self.rBoss = 1.00 - self.gBoss 
        print self.gMonster
        print self.rMonster
        print self.Mpercent

        if self.state == 1 :
            if self.monster.hp == 0 :
                cmds.button('mhpBar',e=True,w=self.boss.hp*2,backgroundColor =[self.rBoss, self.gBoss ,0])
            elif self.monster.hp > 0 :
                cmds.button('mhpBar',e=True,w=self.monster.hp*4,backgroundColor = [self.rMonster, self.gMonster,0])
        elif self.state == 2 :
            if self.boss.hp == 0 :
                cmds.button('mhpBar',e=True,w=600 ,backgroundColor = [0.1, 0.1, 0.1])
            else :
                cmds.button('mhpBar',e=True,w=self.boss.hp*2,backgroundColor = [self.rBoss, self.gBoss ,0])

        if self.hero.hp == 0 :
            cmds.button('hhpBar',e=True,w=600 ,backgroundColor = [0.1, 0.1, 0.1])
        else :
            cmds.button('hhpBar',e=True,w=self.hero.hp*2,backgroundColor = [self.rHero, self.gHero ,0])


    def rematch(self,*args):
        self.state = 1
        self.hero.hp = 300
        self.boss.hp = 300
        self.monster.hp = 150
        self.GUI()
        
            
    def GUI(self):

        if cmds.window('cardGame' , q=True, ex=True):
                cmds.deleteUI('cardGame' , window=True)
        cmds.window('cardGame' , t='Card Game')
        cmds.columnLayout('menu' ,w=20)
        cmds.button('mhpBar', backgroundColor = [0, 255, 0 ],w=600)
        cmds.text("MHp", label = "Monster HP 150/150", height = 30, backgroundColor = [0.2, 0.2, 0.2],p='menu',w=600)
        cmds.gridLayout( 'Monster',numberOfRowsColumns=(1,2), cellWidthHeight=(200,150),p='menu' )
        cmds.iconTextButton( 'Monsterss',image='charMons.png',p='Monster')
        cmds.iconTextButton("cardMon", image='backCard.png',p='Monster')
        cmds.text("event", label = "Start Game", height = 50, backgroundColor = [0.2, 0.2, 0.2],p='menu',w=600)
        cmds.gridLayout( 'Hero',numberOfRowsColumns=(1,2), cellWidthHeight=(200,150),p='menu' )
        cmds.iconTextButton('HeroChar',image='charHero.png',p='Hero')
        cmds.iconTextButton("cardHero", image='backCard.png',p='Hero')
        cmds.text("HHp", label = "Hero HP 300/300", height = 30, backgroundColor = [0.2, 0.2, 0.2],p='menu',w=600)
        cmds.button('hhpBar', backgroundColor = [0, 255, 0 ],w=600,p='menu')
        cmds.gridLayout( 'name',numberOfRowsColumns=(1,3), cellWidthHeight=(200,200),p='menu' )
        cmds.iconTextButton("button0", image='backCard.png',c=self.buttonCard0)
        cmds.iconTextButton("button1", image='backCard.png',c=self.buttonCard1)
        cmds.iconTextButton("button2", image='backCard.png',c=self.buttonCard2)
        cmds.button("tryAgian",l='Reset Match' , h = 50 ,p='menu',c=self.rematch,w=600)
        cmds.showWindow('cardGame')
        self.state = 1
        self.turn = 1
        self.monsterType = self.monster 
        self.randomCardHero()
        self.imageHero()
    def buttonCard0(self,*agrs):
        if self.cardHero[0] == 0 :
            self.hero.selectCard = 0
        elif self.cardHero[0] == 1 :
            self.hero.selectCard = 1
        elif self.cardHero[0] == 2 :
            self.hero.selectCard = 2
        else  :
            self.hero.selectCard = 3
        self.cardHero[0]=random.randint(0,3)
        self.action()
        
    def buttonCard1(self,*agrs):
        if self.cardHero[1] == 0 :
            self.hero.selectCard = 0
        elif self.cardHero[1] == 1 :
            self.hero.selectCard = 1
        elif self.cardHero[1] == 2 :
            self.hero.selectCard = 2
        else  :
            self.hero.selectCard = 3
        self.cardHero[1]=random.randint(0,3)
        self.action()
        
    def buttonCard2(self,*agrs):
        if self.cardHero[2] == 0 :
            self.hero.selectCard = 0
        elif self.cardHero[2] == 1 :
            self.hero.selectCard = 1
        elif self.cardHero[2] == 2 :
            self.hero.selectCard = 2
        else  :
            self.hero.selectCard = 3
        self.cardHero[2]=random.randint(0,3)
        self.action()


