# Desenvolva um código que recebe dois números inteiros e informe qual é maior ou se os dois são iguais

n1 = int(input('Digite o 1º número inteiro: '))
n2 = int(input('Digite o 2º número inteiro: '))

if(n1 > n2):
    print('O primeiro valor é maior')

elif(n2 > n1):
    print('O segundo valor é maior')

else:
    print('Não existe valor maior, ambos são iguais')