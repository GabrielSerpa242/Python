from random import randint 
from time import sleep 
comp = randint (0, 5)
print('-=-'*20)
print('Vou pensar em um núermo de 0 a 5')
print('-=-'*20)
player = int(input('Em que numero eu pensei:'))
if player == comp: 
    print('Voce ganhou parabens') 
else: 
    print('eba eu ganhei de vc, kkkk, eu pensei no número {} e não no {}'.format(comp,player))