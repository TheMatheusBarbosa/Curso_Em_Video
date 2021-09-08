# Desenvolva um código que recebe um número entre 0 e 9999 e mostre cada um dos digitos separados

vlr = int(input('Digite um número: '))

print('Unidade: {}'.format(int(((vlr % 1000) % 100) % 10)))
print('Dezena:  {}'.format(int(((vlr % 1000) % 100) / 10)))
print('Centena: {}'.format(int((vlr % 1000) / 100)))
print('Milhar:  {}'.format(int(vlr / 1000)))