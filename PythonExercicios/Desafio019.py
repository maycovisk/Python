#Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que
#ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolha = random.choice(lista)
print('O aluno escolhido foi o: {}'.format(escolha))