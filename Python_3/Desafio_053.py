# Desenvolva um código que recebe uma frase é informe se é um palíndromo

vlr = input('Digite uma frase: ')
plm = ''

vlr = vlr.replace(' ','')

for i in range(len(vlr) - 1, -1, -1):
    plm += vlr[i]

if(vlr == plm):
    print('A frase é um palíndromo')

else:
    print('A frase não é um palíndromo')