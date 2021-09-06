# Desenvolva um código que receba quatro nomes e ordene de maneira aleatória

import random

nomes = input('Digite o 1º nome: '), input('Digite o 2º nome: '), input('Digite o 3º nome: '), input('Digite o 4º nome: ')

for i in range(4):
    pos = random.randint(i, 3)
    aux = nomes[pos]

    nomes[pos] = nomes[i]
    nomes[i] = aux
print(nomes)