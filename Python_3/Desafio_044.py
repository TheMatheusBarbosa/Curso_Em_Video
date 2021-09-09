# Desenvolva um código que recebe o valor de um produto e calcule o novo preço de acordo com a condição de pagamento, sendo, dinheiro/cheque, 10% de desconto; à vista no cartão, 5% de desconto; 2x no cartão, preço normal; 3x ou mais no cartão, 20% de juros

vlr = float(input('Digite o valor do produto: '))

print('1 - Dinheiro/Cheque')
print('2 - Cartão')

opc = int(input('Digite a opção de pagamento: '))

if(opc == 1):
    print('O valor final do produto é R${:.2f}'.format(vlr * 0.9))

elif(opc == 2):
    par = int(input('Digite a quantidade de parcelas: '))

    if(par == 1):
        print('O valor final do produto é R${:.2f}'.format(vlr * 0.95))
    
    elif(par == 2):
        print('O valor final do produto é R${:.2f}'.format(vlr))

    else:
        print('O valor final do produto é R${:.2f}'.format(vlr * 1.2))

else:
    print('Opção inválida')