#Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros
m = int(input('Digite um valor em metro: '))
c = m * 100
ml = m * 1000
print('{} metros convertido em centimetros é {} e em milimetros é {}'.format(m, c, ml))
