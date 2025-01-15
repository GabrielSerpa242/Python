sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Digite novamnete o seu gênero: ')).strip().upper()[0]
print('O seu gênero {} está registrado com sucesso'.format(sexo))