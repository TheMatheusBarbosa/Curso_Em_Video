# Desenvolva um código que recebe um valor entre 0 e 10 e compare com um numero gerado aleatoriamente, peça novamente o número até acertar

import random

vlr = -1
sor = random.randint(0, 10)
cont = 0

while(vlr != sor):
    cont += 1
    vlr = int(input('{}ª Tentativa. Advinhe qual numero o computador pensou entre 0 e 10: '.format(cont)))

print('Parabéns, você acertou na {}ª tentativa! O computador pensou no número {}'.format(cont, sor))