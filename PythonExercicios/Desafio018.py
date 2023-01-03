#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math

ang = float(input('Digite o ângulo que voce deseja: '))
seno = math.sin(math.radians(ang))
print('O ângulo de {} tem o seno de {:.2f}'.format(ang, seno))
coss = math.cos(math.radians(ang))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ang, coss))
tang = math.tan(math.radians(ang))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ang, tang))