# Desenvolva um código que gere cinco números aleatórios, mostre os números gerados e indique qual foi o menor e maior número

import random

sor = []

for i in range(5):
    sor.append(random.randint(0, 100))

print('Os números sorteados foram: {}'.format(sor))

sor.sort()

print('O maior valor é {}'.format(sor[4]))
print('O menor valor é {}'.format(sor[0]))