# Desenvolva um código que receba diversos números e só pare quando receber 999, mostre quantos números foram digitados e a soma de todos eles

cont = 0
soma = 0
vlr = 0

while(vlr != 999):
    vlr = int(input('Digite um número: '))
    soma += vlr
    cont += 1

print('Foram digitados {} números'.format(cont - 1))
print('A soma de todos os numeros digitados deu {}'.format(soma - 999))