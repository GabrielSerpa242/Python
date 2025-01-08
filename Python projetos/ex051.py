print('PROGRESSÃO ARITMETICA')
p = int(input('Digite um número:')) 
r = int(input('Razao:')) 
d = p + (10-1) * r
for c in range (p , d + r , r): 
    print('{}'.format(c), end= ' -> ') 
print('ACABOU')