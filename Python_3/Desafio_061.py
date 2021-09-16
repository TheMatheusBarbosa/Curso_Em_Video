# Desenvolva um código recebe o primeiro termo e a razão de uma progressão aritimética e mostre os dez primeiros termos

i = 0

vlr = float(input('Digite o primeiro termo da progressão aritimética: '))
rzn = float(input('Digite a razão da progressão aritimética: '))

while(i < 10):
    print(vlr)
    vlr += rzn
    i += 1