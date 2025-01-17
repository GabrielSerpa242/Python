from random import randint 
comp = randint (0, 10)
print('-=-'*20)
print('Vou pensar em um núermo de 0 a 10')
print('-=-'*20)
acertou = False
palpites = 0
while not acertou:
    player = int(input('Qual é seu palpite? '))
    palpites += 1
    if player == comp:
        acertou = True
    else:
        if player < comp:
            print('Hum... um pouco mais')
        elif player > comp:
            print('Um pouco menos') 
print('Você teve {} tentativas, para acertar.'.format(palpites))