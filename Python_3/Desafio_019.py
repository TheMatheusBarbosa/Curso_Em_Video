# Desenvolva um código que receba 4 nomes e sorteie um nome para que seja exibido

import random

nomes = input('Digite o 1º nome: '), input('Digite o 2º nome: '), input('Digite o 3º nome: '), input('Digite o 4º nome: ')

print('O nome sorteado foi {}'.format(random.choice(nomes)))