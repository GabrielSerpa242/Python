s= 0
c = 0
for i in range(1,501,2): 
    if i %3==0:
        c = c +1
        s =s + i 
print("A soma dos valores",s,"e a quantidade contada é",c) 
