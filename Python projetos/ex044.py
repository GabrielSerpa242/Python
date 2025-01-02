print('{:=^40}'.format(' LOJA BIRD ')) 
preço =  (float(input('Preço das compras:'))) 
print(''' FORMAS DE PAGAMENTO:
     [1] Á vista ou chueque
     [2] Á vista no cartão
     [3] Em até 2 vezes no cartão 
     [4] 3 vezes ou mais no cartão''')
opção = (float(input('Escolha uma das opções acima:'))) 
if opção == 1: 
    total = preço - (preço * 10/100) 
elif opção == 2: 
    total = preço - (preço * 5/100)
elif opção ==3: 
    total = preço 
    parcela = total /2
    print('Parcelando a sua em 2x a sua compra vai ser {:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20/100)
    totalparc = int(input('Em quantas parcelas:'))
    parcela = total / totalparc
    print('Parcelando em mais de {}x o valor vai ficar {:.2f}'.format(totalparc, parcela))
else:
    total = 0
    print('OPÇÃO INVALIDA DE PAGAMENTO. TENTE NOVAMENTE')
print('O valor anterior {}'.format(total))