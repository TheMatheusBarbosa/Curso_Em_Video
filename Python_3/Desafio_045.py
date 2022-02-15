# Desenvolva um código que jogue Jokenpô com o usuário

import random

print('Jokenpô')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

vlr = int(input('Escolha sua mão: '))
pc = random.randint(1, 3)

if(vlr == 1):
    if(pc == 3):
        print('Você ganhou!!!')
    
    elif(pc == 2):
        print('Você perdeu!!!')
    
    else:
        print('O jogo empatou!!!')

elif(vlr == 2):
    if(pc == 1):
        print('Você ganhou!!!')
    
    elif(pc == 3):
        print('Você perdeu!!!')
    
    else:
        print('O jogo empatou!!!')

elif(vlr == 3):
    if(pc == 2):
        print('Você ganhou!!!')
    
    elif(pc == 1):
        print('Você perdeu!!!')
    
    else:
        print('O jogo empatou!!!')

else:
    print('Mão inválida')