print('===Ex 5===')
n = int(input('Digite um número?'))
n1 = n - 1
n2 = n + 1
print('O seu número é {} e o seu antecessor é {} e sucessor é {}'.format(n,n1,n2))

print('===Ex 6===')
n = int(input('Digite um númeo?'))
n1 = (n*2)
n2 = (n*3)
n3 = (n**(1/2))
print('O dobro desse número é {}\n,o seu triplo é {}\n e a sua raiz quadrada é {:.3f}'.format(n1,n2,n3))

print('===Ex 7===')
n = float(input('Digite sua nota:'))
n1 = float(input('Digite sua nota:'))
s = n +n1
m = s/2
print('Sua média é {}'.format(m))
print('===Ex 8===')
p = int(input('Digite um número qualquer:'))
m = p * 1
cm = p*100
mm = p*1000
print('O seu {}m, em {}cm e em {}mm, convertidos'.format(m,cm,mm))
print('===Ex 9===')
num = int(input('Digite um número para ver sua tabuada:'))
u = num * 1
d = num * 2
t = num * 3
q = num * 4
c = num * 5
se = num * 6
set = num * 7
o = num * 8
n =num * 9
dez = num * 10
print('{} x 1 = {}\n'
      '{} x 2 = {}\n'
      '{} x 3 = {}\n'
      '{} x 4 = {}\n'
      '{} x 5 = {}\n'
      '{} x 6 = {}\n'
      '{} x 7 = {}\n'
      '{} x 8 = {}\n'
      '{} x 9 = {}\n'
      '{} x 10= {} '.format(num,u,num,d,num,t,num,q,num,c,num,se,num,set,num,o,num,n,num,dez))

print('===Ex 10===')
din = float(input('Digite um valor pode ser em virgula:R$'))
dolar = din / 3.27
print('Seu dinheiro em dolar é ${:.2f}'.format(dolar))

print('===Ex 11===')
larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
area = larg * alt
print(' Sua parede tem sua largura é {}m e a sua altura é {} a sua area é {}m²'.format(larg,alt,area))
tinta = area / 2
print('E para pintar essa parede vai precisar de {}L de tinta'.format(tinta))

print('===Ex 12===')
g = float(input('Qual o preço do produto? R$'))
pr = g * 5/100
no = g - pr
print('É esse é o novo preço do produto R${:.2f} com 5% de desconto'.format(no))

print('===Ex 13===')
s = float(input('Qual é seu salario? R$'))
r = s + (s*15/100)
print(' seu salario é R${:.2f}, seu reajuste de 15% de aumento vai ser R${:.2f}'.format(s,r))

print('===Ex 14===')
c = float(input('Qual a temperatura? c°'))
f = ((9 * c) / 5) + 32
print('A temperatura em {}C° corresponde em {}F°'.format(c,f))

print('===Ex 15===')
dias = int(input('Dias alugados?'))
km = int(input('Quantos km?'))
p = (dias * 60) + (km * 0.15)
print('O total a pagar é R${}'.format(p))
