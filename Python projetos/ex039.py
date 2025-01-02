print('Calculando o ano que vai fazer o alistamento militar') 
from datetime import date
atual = date.today() . year
ano = int(input('Digite o ano:')) 
idade = atual - ano
n1 =  18 - idade
n2 = idade - 18
n3 =  atual - n2
n4 = atual + n1
if idade == 18:
    print('Tem que se alistar você tem {} anos e nasceu no ano {}'.format(idade, ano))
elif idade > 18:
    print('Você se esqueceu de se alistar sua idade é {} e nasceu no ano {} e passou {} anos'.format(idade, ano, n2)) 
    print('E seu ano de alistamento foi em {}'.format(n3))
else: 
    print('Você tem {} anos e para você se alistar faltaria {} anos, não tenho pressa soldado a sua hora vai chegar, seu ano é {} e o ano de hoje é {}'.format(idade,n1,ano, atual))
    print('E seu ano para o alistamento vai ser em {}'.format(n4))