import pipelineGameCard.CG_ClassCharacter as m
reload(m)
class Monster(m.Character):
    
   def __init__(self,name):
       super(Monster,self).__init__(name)
       if self.name == 'Boss':
           self.hp = 300
           self.atk = 40
           self.deff = 30
           self.brk = 50
           self.hel = 30
       else :
           self.hp = 150
           self.atk = 30
           self.deff = 20
           self.brk = 40
           self.hel = 30



