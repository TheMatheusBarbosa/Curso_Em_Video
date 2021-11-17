# Desenvolva um código que receba diversos valores, caso o número já exista, ele não será adicionado. Exiba todos os valores únicos de forma crescente

valores = []
vlr = 0.0
qtd = int(input('Quantas valores irá digitar? '))

for i in range(qtd):
    vlr = float(input('Digite o {}º valor: '.format(i + 1)))

    if not vlr in valores:
        valores.append(vlr)

valores.sort()

print(valores)