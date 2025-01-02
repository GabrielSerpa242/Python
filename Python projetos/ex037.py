print('Conversor de bases numericas para binario, octal e hexadecimal') 
num = int(input('Digite um número inteiro:')) 
print('''Escolha uma dessas opções abaixo:
      [ 1 ] Binario
      [ 2 ] Octal
      [ 3 ] Hexadecimal''') 
opção = int(input('Sua opção:')) 
if opção == 1:
    print('O numero {} para binario é {}'.format(num, bin(num)[2:]))
elif opção == 2: 
    print('O numero {} para Octal é {}'.format(num, oct(num)[2:])) 
elif opção == 3:
    print('O numero {} para Hexadecimal é {}'.format(num, hex(num)[2:])) 
else:
    print('Não existe')