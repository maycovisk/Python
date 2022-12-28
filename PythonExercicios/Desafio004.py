#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
#e todas informações possiveis sobre ele
x = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(x))
print('Só tem espaço', x.isspace())
print('É um numero', x.isnumeric())
print('É alfabeto', x.isalpha())
print('É alfanumerico', x.isalnum())
