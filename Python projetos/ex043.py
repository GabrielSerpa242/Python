peso = float(input('Digite seu peso (KG)')) 
alt = float(input('Digite sua altura (M)')) 
IMC = peso / (alt ** 2) 
print('Seu peso em IMC é {:.1f}'.format(IMC)) 
if IMC <  18.5: 
    print('Abaixo do peso') 
elif  18.5 <= IMC < 25: 
    print('Peso Ideal') 
elif 25 <= IMC < 30: 
    print('Sobrepeso') 
elif 30 <= IMC < 40: 
    print('Obesidade') 
else:
    print('Obesidade morbida')