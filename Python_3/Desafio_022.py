# Desenvolva um código que recebe um nome e mostre com todas as letras maiúsculas, minúsculas, quntas letras existem e quantas letras tem no primeiro nome

vlr = input('Digite seu nome completo: ').strip

print('Maiúscula: {}'.format(vlr.upper()))
print('Minúscula: {}'.format(vlr.lower()))
print('{} possui {} letras'.format(vlr, len(vlr) - vlr.count(' ')))
print('{} possui {} letras'.format(vlr.split()[0], len(vlr.split()[0])))