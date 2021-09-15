# Desenvolva um código que faça uma contagem regressiva entre 10 e 0 com 1s entre eles

import time

for i in range(10, -1, -1):
    time.sleep(1)
    print(i)

print('BUM')