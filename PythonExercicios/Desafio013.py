#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento
s = float(input('Digite o salario: '))
a = s + (s * 0.15)
print('O salaria R${:.2f} com 15% de aumento passa a ser: R${:.2f}'.format(s, a))