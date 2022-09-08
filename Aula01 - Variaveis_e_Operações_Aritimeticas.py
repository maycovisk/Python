#a = 10
a = int(input('Entre um valor: '))
#b = 5
b = int(input('Entre um valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(resto)
print('soma: ' + str(soma))
print('soma: {}'.format(soma))
print('soma: {}, subtracao: {}'.format(soma, subtracao))
print('Soma: {soma}. \nSubtracao: {subtracao}.'
      '\nMultiplicacao: {multiplicacao}'
      '\nDivisao: {divisao}'
      '\nResto: {resto}'.format(soma = soma,
                                subtracao = subtracao,
                                resto = resto,
                                multiplicacao = multiplicacao,
                                divisao = divisao))
