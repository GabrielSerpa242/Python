n = int(input('Digite um número:')) 
tant = 0
for c in range(1, n + 1):
    if n % c ==0:
        print('\033[32m', end = '') 
        tant += 1
    else:
        print('\033[31m', end= '')
    print('{}'.format(c), end = ' ') 
print('\n\033[mO numero {} foi divisivel {} vezes'. format(n, tant)) 
if tant ==2:
    print('Ele é primo') 
else: 
    print('Ele não é primo')