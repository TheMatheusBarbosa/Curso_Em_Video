# Desenvolva um código que recebe um valor entre 0 e 5 e compare com um numero gerado aleatoriamente, informando se foi o mesmo numero ou não

import random

vlr = int(input('Advinhe qual numero o computador pensou entre 0 e 5: '))
sor = random.randint(0, 5)

if(vlr == sor):
    print('Parabéns, o computador também pesnou no número {}'.format(vlr))
    
else:
    print('Ahh, você errou! Na verdade o computador pensou no número {}'.format(sor))