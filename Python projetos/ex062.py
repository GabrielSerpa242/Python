print('Gerador de PA') 
print('-='*10)
pri = int(input('Primeiro termo: '))
razao = int(input('Razão: ')) 
termo = pri
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end = '')
        termo += razao
        cont += 1
    print('PAUSA') 
    mais = int(input('Quantos termos você quer mostrar a mais? ')) 
print('FIM') 
print('Progreção finalizada com {} termos mostrados'.format(total))
print('-='*10)