VERIFICAR SE O NUMERO E PRIMO
a = int(input('Entre um numero: '))

div = 0
for x in range(1, a + 1):
    resto = a % x
    print(x, resto)
    if resto == 0:
        div += 1

if div == 2:
    print('Numero {} e primo'.format(a))
else:
    print('Numero {} nao e primo'.format(a))

#...................................................
#IMPRIMIR TODOS OS NUMEROS PRIMOS DE 0 A 100
for num in range(101):
    div = 0
    for x in range(1, num + 1):
        resto = num % x
        if resto == 0:
            div += 1

    if div == 2:
        print(num)

#...................................................

a = 0
while a <= 10:
    print(a)
    a += 1

#...................................................

nota = int(input('Entre com a nota: '))
while nota > 10:
    nota = int(input('Nota invalida. Entre com a nota: '))
print(nota)

#...................................................

a = int(input('Digite a nota 1: '))
while a > 10:
    a = int(input('Voce digitou errado. Digite a nota 1: '))
b = int(input('Digite a nota 2: '))
while b > 10:
    b = int(input('Voce digitou errado. Digite a nota 2: '))
c = int(input('Digite a nota 3: '))
while c > 10:
    c = int(input('Voce digitou errado. Digite a nota 3: '))
d = int(input('Digite a nota 4: '))
while d > 10:
    d = int(input('Voce digitou errado. Digite a nota 4: '))

media = (a + b + c + d) / 4
print('Media: {}'.format(media))