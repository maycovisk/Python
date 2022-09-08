#DESAFIO1: Crie um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas
#de acordo com o valor digitado
nome = input('Digite seu nome: ')
print('Seja bem vindo(a)', nome, '! Prazer em te conhecer!')

#DESAFIO2: Crie um programa que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre
#uma mensagem com a data formatada.
dia = input('Digite seu dia de nascimento: ')
mes = input('Digite seu mes de nascimento: ')
ano = input('Digite seu ano de nascimento: ')
print('Você nasceu dia', dia, 'de', mes, 'de', ano)

#DESAFIO3: Crie um programa que leia dois numeros e tente mostra a soma entre eles.
num1 = input('Digite um primeiro número: ')
num2 = input('Digite um segundo número: ')
#soma = int(num1) + int(num2)
print('A soma de', num1, '+', num2, 'é igual a', (int(num1) + int(num2)))