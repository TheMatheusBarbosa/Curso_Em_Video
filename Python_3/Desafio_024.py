# Desenvolva um código que recebe o nume de uma cidade e informe se ela começa com "SANTO"

vlr = input('Digite o nome da cidade: ').strip

if(vlr[0:5].upper() == 'SANTO'):
    print('A cidade {}, começa com a palavra SANTO'.format(vlr))

else:
    print('A cidade {}, não começa com a palavra SANTO'.format(vlr))