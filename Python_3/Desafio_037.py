# Desenvolva um código que recebe um número inteiro e converta para uma outra base a escolha do usuário, binário, octal e hexadecimal

vlr = int(input('Digite um número inteiro: '))

print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
opc = int(input('Escolha a base de conversão: '))

if(opc == 1):
    print('O equivalente binario para o inteiro {} é {}'.format(vlr, bin(vlr)))

elif(opc == 2):
    print('O equivalente octal para o inteiro {} é {}'. format(vlr, oct(vlr)))

elif(opc == 3):
    print('O equivalente hexadecimal para o inteiro {} é {}'.format(vlr, hex(vlr)))

else:
    print('Opção inválida')