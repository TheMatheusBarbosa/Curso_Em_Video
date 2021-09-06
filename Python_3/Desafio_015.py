# Desenvolva um código que recebe a quantidade de Km percorrido por um carro e quantos dias o mesmo permaneceu alugado. Calcule o valor a ser pago considerando R$60 por dia e R$0.15 por Km rodado

dia = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos Km o carro percorreu? '))

print('O preço total do serviço foi de R${:.2f}'.format((dia * 60) + (km * 0.15)))