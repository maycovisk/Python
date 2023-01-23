#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('O primeiro nome é {}'.format(n[0]))
print('O último nome é {}'.format(n[len(n)-1]))
