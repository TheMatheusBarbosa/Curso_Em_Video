# Desenvolva um código que cria uma matriz 3x3 e preencha com valores lidos pelo teclado. No final mostre a matriz formatada e com os valores digitados

matriz = [[], [], []]

for x in range(3):
    for y in range(3):
        matriz[x].append(int(input('Digite o numero da posição ({}, {}): '.format(x, y))))

print(matriz[0])
print(matriz[1])
print(matriz[2])