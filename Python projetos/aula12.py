nome = str(input('Qual é o seu nome:')) 
if nome == 'Gabriel': 
    print('Que nome legal') 
elif nome =='Fernando' or nome == 'Guilherme': 
    print('Nome razoável')
else:
    print('Seu nome é bem mais ou menos')
print('Tenha um belo dia, {}'.format(nome))