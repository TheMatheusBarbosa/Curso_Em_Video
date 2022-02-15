# Desenvolva um código que receba 7 números e cadastre em uma unica lista mantendo separado pares e ímpares no final mostre os valores em ordem crescente

num = 0
numeros = [[], []]

for i in range(7):
    num = int(input('Digite o {}º número: '.format(i + 1)))

    if(num % 2 == 0):
        numeros[0].append(num)

    else:
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()

print('Pares: {}'.format(numeros[0]))
print('Ímpares: {}'.format(numeros[1]))