##################################
#                                #
#        run in maya             #
#                                #
##################################

import pipelineGameCard.CG_ClassCharacter 
import pipelineGameCard.CG_cardGame as C
import pipelineGameCard.CG_heroClass as H
import pipelineGameCard.CG_monsterClass as M

reload(pipelineGameCard.CG_ClassCharacter )
reload(C)
reload(H)
reload(M)


x= H.Hero('Hero')
y= M.Monster('Monster')
z= M.Monster('Boss')
c= C.CardGame(x,y,z)
c.GUI()


