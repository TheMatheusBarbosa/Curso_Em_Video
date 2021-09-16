# Desenvolva um código recebe o primeiro termo e a razão de uma progressão aritimética e mostre os dez primeiros termos e depois pergunte quantos termos a mais ele quer mostrar

i = 0
opc = 10

vlr = float(input('Digite o primeiro termo da progressão aritimética: '))
rzn = float(input('Digite a razão da progressão aritimética: '))

while(opc != 0):
    while(i < opc):
        print(vlr)
        vlr += rzn
        i += 1

    opc = int(input('Quantos termos você gostaria de mostrar a mais? '))
    i = 0