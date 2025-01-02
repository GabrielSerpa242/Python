n = str(input('Qual é o seu nome:')).strip()
print('Seu nome tem serpa? {}'.format('SERPA'in n.upper()))
print('Seu nome tem {} letras'.format(len(n)))