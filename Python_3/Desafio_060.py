# Desenvolva um código que receba um número e mostre seu fatorial

import math

vlr = int(input('Digite um número: '))
fat = 1

print('Fatorial de {} usando a biblioteca math: {}'.format(vlr, math.factorial(vlr)))

for i in range(vlr, 0, -1):
    fat *= i

print('Fatorial de {} usando for: {}'.format(vlr, fat))

fat = 1
i = vlr

while(i > 0):
    fat *= i
    i -= 1

print('Fatorial de {} usando while: {}'.format(vlr, fat))