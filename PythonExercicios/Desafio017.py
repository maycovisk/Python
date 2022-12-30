#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
#calcule e mostre o comprimento da hipotenusa.
from math import hypot
catopost = int(input('Digite o valor do cateto oposto: '))
catadjac = int(input('Digite o valor do cateto adjacente: '))
print(hypot(catopost, catadjac))