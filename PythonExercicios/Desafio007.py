#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media
n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota : '))
m = (n1+n2) / 2
print('As notas digitadas foram: \n{}\n{} \nE a média é {:.2f}'.format(n1, n2, m))