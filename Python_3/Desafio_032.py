# Desenvolva um código que recebe um ano e informe se ele é bissexto

vlr = int(input('Digite um ano: '))

if(vlr % 4 == 0):
    if(vlr % 100 == 0):
        if(vlr % 400 == 0):
            print('O ano {} é bissexto!!!'.format(vlr))
        else:
            print('O ano {} não é bissexto!!!'.format(vlr))
    else:
        print('O ano {} é bissexto!!!'.format(vlr))
else:
    print('O ano {} não é bissexto!!!'.format(vlr))
