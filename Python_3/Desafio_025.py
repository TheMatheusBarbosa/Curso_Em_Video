# Desenvolva um código que recebe um nome e informe se ela tem a palavra SILVA

vlr = input('Digite um nome: ').strip

if(vlr.upper().find('SILVA') >=  0):
    print('O nome {}, possui a palavra SILVA'.format(vlr))

else:
    print('O nome {}, não possui a palavra SILVA'.format(vlr))