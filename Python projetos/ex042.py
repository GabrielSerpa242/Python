pri = int(input('Primeiro segmento:')) 
seg = int(input('Segundo segmento:')) 
ter = int(input('Terceiro segmento:')) 

if pri < seg + ter and seg < pri + ter and ter < pri + seg: 
    if pri == seg == ter:
        print('Esse triangulo é Equilatero') 
    elif pri != seg != ter != pri:
        print('Esse triangulo é Escaleno')
    else:
        print('Esse triangulo é Isosceles')
else: 
    print('Não é um triangulo')



#equilatero= todos os lados são iguais
#isosceles= dois lados são iguais e um diferente 
#escaleno= todos os lados são diferentes