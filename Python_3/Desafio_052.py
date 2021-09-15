# Desenvolva um código que recebe um número e informe se ele é primo

vlr = int(input('Digite um número: '))
prm = 0

for i in range(2, vlr):
    
    if(vlr % i == 0):
        prm += 1

if(prm == 0):
    print('O número {} é primo!'.format(vlr))

else:
    print('O número {} não é primo!'.format(vlr))