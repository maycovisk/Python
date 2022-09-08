a = int(input('Primeiro valor:'))
b = int(input('Segundo valor: '))

if a > b:
    print('O maior numero e {}'.format(a))
else:
    print('O maior numero e {}'.format(b))

#--------------------------------------------------

a = int(input('Primeiro valor:'))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor:'))

if a > b and a > c:
    print('O maior numero e {}'.format(a))
elif b > a and b > c:
    print('O maior numero e {}'.format(b))
else:
    print('O maior numero e {}'.format(c))

#------------------------------------------------

a = int(input('Entre com um valor: '))

resto = a % 2
if resto == 0:
    print('O valor {} e par'.format(a))
else:
    print('O valor {} e impar'.format(a))

#------------------------------------------------

a = int(input('Entre o primeiro valor: '))
b = int(input('Entre o segundo valor: '))

restoA = a % 2
restoB = b % 2
if restoA == 0 or restoB == 0:  #or not inverte a condicao
    print('Foi digitado um numero par')
else:
    print('Nenhum numero par foi digitado')

#------------------------------------------------

a = int(input('Digite a nota 1: '))
b = int(input('Digite a nota 2: '))
c = int(input('Digite a nota 3: '))
d = int(input('Digite a nota 4: '))

media = (a + b + c + d) / 4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('Media: {}'.format(media))
else:
    print('Nota digitado com valor errado')

#------------------------------------------------

a = int(input('Digite a nota 1: '))
if a > 10:
    a = int(input('Voce digitou errado. Digite a nota 1: '))
b = int(input('Digite a nota 2: '))
if b > 10:
    b = int(input('Voce digitou errado. Digite a nota 2: '))
c = int(input('Digite a nota 3: '))
if c > 10:
    c = int(input('Voce digitou errado. Digite a nota 3: '))
d = int(input('Digite a nota 4: '))
if d > 10:
    d = int(input('Voce digitou errado. Digite a nota 4: '))

media = (a + b + c + d) / 4
print('Media: {}'.format(media))
