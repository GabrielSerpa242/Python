nome = str(input('Digite seu nome completo:')).strip()
print('Verificando seu nome...')
print('Seu nome em maiúscula {}'.format(nome.upper()))
print('Seu nome em minúsculo {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

separa = nome.split()
print ('''Seu primeiro nome é {} e ele tem {} letras,
Seu nome do meio é {} e ele tem {} letras, 
Seu ultimo nome é {} e ele tem {} letras. '''.format(separa[0],len(separa[0]),separa[1],len(separa[1]),separa[2],len(separa[2])))