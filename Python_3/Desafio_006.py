from typing import Match


# Desenvolva um código que mostre o dobro, triplo e a raiz quadrada de um valor

import math

vlr = float(input('Digite um número: '))

print('O dobro de {} é {}'.format(vlr, vlr * 2))
print('O triplo de {} é {}'.format(vlr, vlr * 3))
print('A raiz quadrada de {} é {}'.format(vlr, math.sqrt(vlr)))