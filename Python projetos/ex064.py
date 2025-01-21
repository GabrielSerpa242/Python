num = cont = soma =0
num = int(input('Digite um numero [999 para parar]: '))
while num !=999:
    soma += num
    cont += 1
    num = int(input('Digite um numero [999 para parar]: ')) 
print('Voce digitou {} e a soma entre eles é {}'.format(cont, soma))