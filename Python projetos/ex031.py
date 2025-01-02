v = float(input('Digite a distancia da sua viagem:'))
r = v * 0.45
r1 = v * 0.50
if v > 200:
    print('A sua distância é {}km e o preço vai ser R${:.2f}'.format(v,r))
else:
    print('A sua distância é {}km preço vai ser R${:.2f}'.format(v,r1))