print('Gerador de PA') 
print('-='*10)
pri = int(input('Primeiro termo: '))
razao = int(input('Razão: ')) 
termo = pri
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end = '')
    termo += razao
    cont += 1
print('FIM')
print('-='*10)