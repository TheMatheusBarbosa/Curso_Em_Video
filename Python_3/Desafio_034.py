# Desenvolva um código que recebe um salario e calcule o aumento de 15% para salários inferiores ou iguais a R$1250.00 e de 10% para salários superiores

vlr = float(input('Informe o valor do salário: '))

if(vlr <= 1250):
    print('O aumento será de R${}'.format(vlr * 0.15))

else:
    print('O aumento será de R${}'.format(vlr * 0.10))