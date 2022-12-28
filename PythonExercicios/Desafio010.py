#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
#quantos dolares ela pode comprar
#Considere US$1,00 = R$3,27
v = float(input('Digite o valor em reais: '))
c = float(3.27)
d = v / c
print('Com R${:.2f} voce poderá comprar US${:.2f}'.format(v, d))
