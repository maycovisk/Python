#lista utiliza []
#tupla utiliza ()
#cojunto utiliza {}

conjunto = {1,2,3,4}    #CONJUNTO NAO ACEITA DUPLICIDADE
print(type(conjunto))
print(conjunto)

conjunto = {1,2,3,4}
conjunto.add(5)         #ADICIONAR
conjunto.discard(2)     #REMOVER
print(conjunto)

................................................

conjunto = {1,2,3,4,5}
conjunto2 = {5,6,7,8}

conjunto_uniao = conjunto.union(conjunto2)                      #UNIR AMBOS CONJUNTOS
print('União: {}'.format(conjunto_uniao))

conjunto_interseccao = conjunto.intersection(conjunto2)         #SOMENTE O QUE TEM EM AMBOS
print('Intersecção: {}'.format(conjunto_interseccao))

conjunto_diferenca = conjunto.difference(conjunto2)             #DIFERENÇA DO 1 COM O 2
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca))
conjunto_diferenca2 = conjunto2.difference(conjunto)            #DIFERENÇA DO 2 COM O 1
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))

conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)  #DIFERENCA SIMETRICA, SOMENTE O QUE TEM NO 1 E NO 2
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))

.........................................

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}

conjunto_subset = conjunto_a.issubset(conjunto_b)           #VERIFICA SE CONJUNTO A ESTA DENTRO DE B
print('A é subconjunto de B: {}'.format(conjunto_subset))

conjunto_superset = conjunto_b.issuperset(conjunto_a)       #VERIFICAR SE CONJUNTO B TEM TODOS OS ELEMENTOS DE A
print('B é superconjunto de A: {}'.format(conjunto_superset))

...........................................

lista = ['cachorro','cachorro','gato','gato','elefante']
conjunto_animais = set(lista)                               #CONVERTER LISTA EM CONJUNTO
print(conjunto_animais)
lista_animais = list(conjunto_animais)                      #CONVERTER CONJUNTO EM LISTA
print(lista_animais)