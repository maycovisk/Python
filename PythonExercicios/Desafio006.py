#Crie um algoritmo que leia um numero e mostre seu dobro, triplo e raiz quadrada
n1 = int(input('Digite um numero: '))
d = n1**2
t = n1**3
r = n1**(1/2)
print('O dobro de {} é {} \nSeu triplo é {} \nSua raiz quadrada é {:.2f}'.format(n1, d, t, r))
