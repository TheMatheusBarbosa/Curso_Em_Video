# Desenvolva um código que recebe o valor de um ângulo e informe o seno, cosseno e tangente desse ângulo

import math

vlr = float(input('informe o ângulo: '))

print('O seno de {}° é {:.4f}'.format(vlr, math.sin(math.radians(vlr))))
print('O cosseno de {}° é {:.4f}'.format(vlr, math.cos(math.radians(vlr))))
print('A tangente de {}° é {:.4f}'.format(vlr, math.tan(math.radians(vlr))))