#Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua area
#e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta
#uma area de 2m²
al = float(input('Digite a altura : '))
la = float(input('Digite a largura: '))
ar = al * la
t = ar / 2
print('Para uma area de {}m² serão necessario(s) {} litros de tinta'.format(ar, t))