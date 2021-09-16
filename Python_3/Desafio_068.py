# Desenvolva um código que receba um numero e jogue par ou ímpar com o usuário, o programa deve parar quando o usuário perder

import random

while(True):
    vlr = int(input('Digite um valor: '))
    opc = input('Par ou Ímpar: [P/I]: ').upper()
    sor = random.randint(1, 2)

    #or (((vlr + sor) / 2) % 2 == 1 and opc == 'I')

    if(((vlr + sor) % 2 == 0 and opc == 'P') or ((vlr + sor) % 2 == 1 and opc == 'I')):
        print('Você jogou {} e o computador {}. Você ganhou!'.format(vlr, sor))

    else: 
        print('Você jogou {} e o computador {}. Você perdeu!'.format(vlr, sor))
        break

    print('Vamos jogar novamente')