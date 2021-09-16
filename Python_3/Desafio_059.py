# Desenvolva um código que recebe dois números e mostre um menu na tela com as seguintes opções; [1] Somar; [2] Multiplicar; [3] Maior Número; [4] Novos Números; [5] Sair

opc = 0
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número:  '))

print('[1] Somar')
print('[2] Multiplicar')
print('[3] Maior Número')
print('[4] Novos Números')
print('[5] Sair')

while(opc != 5):
    opc = int(input('Selecione uma opção: '))

    if(opc == 1):
        print(n1 + n2)
    
    elif(opc == 2):
        print(n1 * n2)

    elif(opc == 3):
        if(n1 > n2):
            print('O número {} é maior que {}'.format(n1, n2))
        
        elif(n2 > n1):
            print('O número {} é maior que {}'.format(n2, n1))
        
        else:
            print('Os números são iguais')
    
    elif(opc == 4):
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número:  '))

    elif(opc == 5):
        print('Tchau!')

    else:
        print('Opção inválida')