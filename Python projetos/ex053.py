frase = str(input('Digite uma frase:')).strip().upper() 
sepa = frase.split()
juntar = ''.join(sepa)
inverso = ''
for letra in range(len(juntar) -1, -1, -1): 
    inverso += juntar[letra] 
print('O inverso de {} é {}'.format(juntar, inverso))
if inverso == juntar: 
    print('\033[32mÉ Palíndromo') 
else: 
    print('\033[31mNão é Palídromo')