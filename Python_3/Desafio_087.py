# Desenvolva um código que cria uma matriz 3x3 e preencha com valores lidos pelo teclado. No final mostre a matriz formatada e com os valores digitados além de mostrar a soma de todos os valores pares digitados, a soma da da 3ª coluna e o maior valor da segunda linha

matriz = [[], [], []]
num = 0
sumPar = 0
sumTer = 0
maior = 0

for x in range(3):
    for y in range(3):
        num = int(input('Digite o numero da posição ({}, {}): '.format(x, y)))
        
        if(num % 2 == 0):
            sumPar += num

        if(y == 2):
            sumTer += num

        if(x == 1):
            if(y == 0):
                maior = num

            else:
                if(num > maior):
                    maior = num

        matriz[x].append(num)

print(matriz[0])
print(matriz[1])
print(matriz[2])

print('A soma de todos os números pares digitados é: {}'.format(sumPar))
print('A soma dos números da 3ª coluna é: {}'.format(sumTer))
print('O maior valor da segunda linha é: {}'.format(maior))