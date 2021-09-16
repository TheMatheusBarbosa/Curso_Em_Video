# Desenvolva um código que recebe nome e preço de um produto, para cada produto informado, pergunte ao usuário se deseja informar mais um produto. No final mostre qual foi o total gasto na compra, quantos produtos custaram mais de R$1000.00 e qual o nome do produto mais barato

nome = input('Informe o nome do produto: ')
vlr = float(input('Informe o preço do produto:'))
total = vlr
nomeBarato = nome
vlrBarato = vlr

if(vlr > 1000):
    qtd = 1

else: 
    qtd = 0

opc = ''

while(opc != 'S' and opc != 'N'):
    opc = input('Deseja colocar um novo produto? [S/N] ').upper()

while(opc == 'S'):
    nome = input('Informe o nome do produto:  ')
    vlr = float(input('Informe o preço do produto: '))
    total += vlr

    if(vlr < vlrBarato):
        vlrBarato = vlr
        nomeBarato = nome

    if(vlr > 1000):
        qtd = 1

    opc = ''

    while(opc != 'S' and opc != 'N'):
        opc = input('Deseja colocar um novo produto? [S/N] ').upper()

print('O total gasto na compra foi de R${:.2f}'.format(total))
print('{} produtos custaram mais de R$1000.00'.format(qtd))
print('O(A) {} foi o produto mais barato'.format(nomeBarato))