from datetime import date
atual = date.today().year
totalmaoir = 0
totalmenor = 0
for p in range(1,8):
    ano = int(input('Em que ano a {}ª pessoa nasceu?'.format(p)))
    idade = atual - ano
    if idade >= 21:
        totalmaoir += 1
    else:
        totalmenor += 1 
print('Ao total tivemos {} maiores de idade'.format(totalmaoir)) 
print('E tivemos {} menores de idade'.format(totalmenor))