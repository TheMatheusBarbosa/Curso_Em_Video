# Desenvolva um código que recebe um valor entre 0 e 20 e retorne o número por extenso

ext = ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte']

vlr = int(input('Digite um número entre 0 e 20: '))

if(vlr >= 0 and vlr <= 20):
    print('O número {} por extenso é {}'.format(vlr, ext[vlr]))

else:
    print('Número inválido')