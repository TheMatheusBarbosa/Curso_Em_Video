# Desenvolva um código que receba uma valor em reais e mostre o equivalente em dólar

vlr = float(input('Digite um valor em reais: '))

print('R${} equivale a US${:.2f}'.format(vlr, vlr / 5.19))