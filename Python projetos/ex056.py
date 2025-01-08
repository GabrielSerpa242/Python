somaidade = 0
mediaidade = 0
maioridade = 0
nomedomaisvelho = ''
totalmulher20 = 0
for p in range(1,5):
    print('---- {}ª PESSOA ----'.format(p))
    n = str(input('Nome: ')). strip()
    i = int(input('Idade: '))
    s = str(input('Sexo [M|F]:')).strip()
    somaidade += i 
    if p == 1 and s in 'Mm': 
        maioridadehomem = i
        nomedomaisvelho = n 
    if s in 'Mm' and i > maioridadehomem: 
        maioridadehomem = i
        nomedomaisvelho = n
    if s in 'Ff' and i < 20:
        totalmulher20 += 1

mediaidade = somaidade / 4 
print('A media do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho é {}'.format(nomedomaisvelho)) 
print('Ao todo tem {} mulheres menos de 20 anos'.format(totalmulher20))