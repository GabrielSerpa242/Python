v = float(input('Digite a sua velocidade:'))
if v > 80:
    print('Parabens, vc foi multado o limite era de 80km, hehehe')
    multa = (v - 80) * 7
    print('Você deve pagar uma multa de {:.2f}, estou de olho em vc.'.format(multa))
else:
    print('Vc está na linha, parabens, continua assim.')