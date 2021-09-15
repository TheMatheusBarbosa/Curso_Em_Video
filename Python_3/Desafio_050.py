# Desenvolva um código que receba seis números inteiros e mostre a soma apenas daqueles que forem pares

s = 0

for i in range(0, 6):
    vlr = int(input('Informe o {}º número: '.format(i + 1)))
    
    if(vlr % 2 == 0):
        s += vlr

print('A soma dos números pares é {}'.format(s))