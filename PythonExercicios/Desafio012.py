#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
p = float(input('Digite o preço: '))
d = p - (p * 0.05)
print('O preço de R${:.2f} com 5% de desconto é R${:.2f}'.format(p, d))
