from time import sleep
n1 = int(input('Primeiro valor: ')) 
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('''      [ 1 ] Somar
      [ 2 ] Multiplicar
      [ 3 ] Maior
      [ 4 ] Novos números 
      [ 5 ] Sair do programa''') 
    op = int(input('>>>>>> Digite uma opção: '))
    if op == 1:
        soma = n1 + n2
        print('A soma do {} + {} é {}'.format(n1,n2,soma))
    elif op == 2:
        multi = n1 * n2
        print('A multiplicação entre {} X {} é {}'.format(n1,n2,multi))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior dentre deles é {}'.format(n1,n2, maior))
    elif op == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando o programa')
    else:
        print('Opção inválida, digite novamente')
    print('=-='*20)
    sleep(2)
print('Fim do programa! Volte Sempre ! :)')