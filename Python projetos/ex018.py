import math
a = float(input('Digite um ângulo:'))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('''O seno é {:.2f} 
O Cosseno è {:.2f}
A tangente é {:.2f} '''.format(s,c,t))