import random
n1 = input('Primeiro aluno:')
n2 = input('Segundo aluno:')
n3 = input('Terceiro aluno:')
n4 = input('Quarto aluno:')
Lista = [n1,n2,n3,n4]
A = random.choice(Lista)
print('O aluno sortudo é {}'.format(A))