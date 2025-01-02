a = int(input('Primerio valor:'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))
#verificando o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O menor valor è {}'.format(menor))
#verificando o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior valor é {}'.format(maior)) 
