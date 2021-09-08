# Desenvolva um código que recebe um numero e informe se ele é par ou ímpar

vlr = float(input('Digite um número: '))

if(vlr % 2 == 0):
    print('O número {} é PAR'.format(vlr))

else:
    print('O número {} é ÍMPAR'.format(vlr))