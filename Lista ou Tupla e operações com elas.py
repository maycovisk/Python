lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']
print(lista_animal[1])  #print(type(lista)) verificar o tipo da variavel - utilizar o type

for x in lista_animal:
    print(x)

#..............................................

lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']

soma = 0
for x in lista:
    print(x)
    soma += x
print(soma)

#..............................................

lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']
print(sum(lista))     #SOMA

#..............................................

lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']
print(max(lista))     #IMPRIME O MAIOR
print(min(lista))     #IMPRIME O MENOR

#..............................................

lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']

if 'gato' in lista_animal:
    print('existe um gato na lista')
else:
    print('nao existe um gato na lista')


#..............................................

lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']

nova_lista = lista_animal * 3
print(nova_lista)

 #..............................................

lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']

if 'lobo' in lista_animal:
    print('existe esse animal na lista')
else:
    print('nao existe esse animal na lista')
    lista_animal.append('lobo')   #INCLUIR
    print(lista_animal)

lista_animal.pop(1)               #REMOVER O ULTIMO DA LISTA
print(lista_animal)

 #..............................................

lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']

if 'lobo' in lista_animal:
    print('existe esse animal na lista')
else:
    print('nao existe esse animal na lista')
    lista_animal.append('lobo')   #INCLUIR
    print(lista_animal)

lista_animal.remove('elefante')   #REMOVER
print(lista_animal)

#..............................................

lista = [12, 10, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

lista.sort()            #ORDENA DO MENOR PARA MAIOR
lista_animal.sort()
print(lista)
print(lista_animal)

#..............................................

lista = [12, 10, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

lista.reverse()            #ORDENA DO ULTIMO DA LISTA PARA O PRIMEIRO
lista_animal.reverse()
print(lista)
print(lista_animal)

..............................................

lista = [12, 10, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

tupla = (1,10,12,14)    #TUPLA E IMUTAVEL
print(len(tupla))       #LEN retorna quanto tem na lista

tupla_animal = tuple(lista_animal)      #TUPLE CONVERTE LISTA EM TUPLA
print(type(tupla_animal))               #IMPRIME O TIPO
print(tupla_animal)

lista_numerica = list(tupla)            #LIST CONVERTE TUPLA PARA LISTA
print(type(lista_numerica))             #IMPRIME O TIPO
print(lista_numerica)