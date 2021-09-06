# Desenvolva um código que receba quatro nomes e ordene de maneira aleatória

import random

n1 = input('Digite o 1º nome: ')
n2 = input('Digite o 2º nome: ')
n3 = input('Digite o 3º nome: ')
n4 = input('Digite o 4º nome: ')

nomes = [n1, n2, n3, n4]

random.shuffle(nomes)

print('A ordem de nomes é: {}'.format(nomes))