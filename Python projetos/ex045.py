from random import randint 
from time import sleep
itens = ('Pedra','Papel', 'Tesoura')
cp = randint(0,2) 
print(''' OPÇÕES
    [0] Pedra
    [1] Papel
    [2] Tesoura''') 
player = int(input(('Escolha uma das opções:'))) 
print('JO') 
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(2)
print('-='*10)
print('o player jogou {}'.format(itens [player]))
print('o computador jogou {}'.format(itens[cp]))
print('-='*10) 
if cp == 0:
    if player == 0:
        print('EMPATE')
    elif player == 1:
        print('O computador ganhou') 
    elif player == 2: 
        print('Ele perdeu') 
    else:
        print('TRAPECEIRO')

elif cp == 1:
    if player == 0: 
        print('Ganhei')
    elif player ==1:
        print('EMPATE')
    elif player == 2: 
        print('Perde')
    else:
        print('Trapaceiro')

elif cp ==2:
    if player == 0:
        print('Perde')
    elif player == 1:
        print('Ganhei')
    elif player == 2: 
        print('EMPATE')
    else:
        print('TRAPACEIRO')
