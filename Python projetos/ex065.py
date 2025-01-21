resp = 'S'
soma = media = quant = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant +=1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Você quer continuar [S/N]: ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a media é {}'.format(quant, media))
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))