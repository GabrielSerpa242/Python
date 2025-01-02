ano = int(input('Ano de nascimento:')) 
from datetime import date
atual = date.today(). year 
idade = atual - ano 
print('Voce tem {} anos'.format(idade)) 
if idade <=9: 
    print('Sua categoria é MIRIM') 
elif idade <=14: 
    print('Sua categoria é INFANTIL') 
elif idade <=19: 
    print('Sua categoria é JUNIOR') 
elif idade <=25: 
    print('Sua categoria é SENIOR') 
elif idade >26: 
    print('Sua categoria é MASTER')