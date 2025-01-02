n = int(input('Digite um número:'))
r = n % 2
if r == 0:
    print('O número é par {}'.format(n))
else:
    print('O número é ímpar'.format(n))