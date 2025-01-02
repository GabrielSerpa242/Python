print('Pergunte o valor da casa, e o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.') 
casa = float(input('Qual o valor da casa:')) 
salario = float(input('Qual é o salario:')) 
anos = int(input('Em quantos voce pretende paga-la:')) 
prestacao = casa / (anos * 12) 
minimo = salario * 30 / 100
print('O valor da casa a ser pago R${:.2f} em {} anos, a prestacao sera de {:.2f}'.format(casa, anos, prestacao))
if prestacao <= minimo:
    print('EMPRESTIMO APROVADO') 
else:
    print('NÃO APROVADO')