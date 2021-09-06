# Desenvolva um código que receba os dois catetos de um triângulo retângulo e calcule o comprimento da hipotenusa

import math

n1 = float(input('Digite o comprimento do cateto oposto:    '))
n2 = float(input('Digite o comprimento do cateto adjacente: '))

print('O comprimento da hiponenusa do triângulo retângulo é de {:.2f}'.format(math.hypot(n1, n2)))