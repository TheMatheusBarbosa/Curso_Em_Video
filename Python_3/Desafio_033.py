# Desenvolva um código que recebe 3 numeros e informe qual é o menor

n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
n3 = float(input('Digite o 3º número: '))

num = [n1, n2, n3]
num.sort()

print('O maior valor é: {}'.format(num[2]))
print('O menor valor é: {}'.format(num[0]))