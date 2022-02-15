# Desenvolva um código que calcule combinações para jogar na Mega Sena a partir da quantidade de jogos informados pelo usuário.

import random
import time

num = 0
jogo = []
jogof = []
qtd = int(input('Digite a quantidades de jogos a serem gerados: '))

for i in range(qtd):
    jogo.clear()

    for j in range(6):
        while True:
            num = random.randint(1, 60)

            if not (num in jogo):
                break
        
        jogo.append(num)

    jogof = [str(x).zfill(2) for x in jogo]

    time.sleep(1)
    print('Jogo {}: {}'.format(i + 1, sorted(jogof)))