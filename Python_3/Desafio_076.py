# Desenvolva um código que recebe o nome de produtos e seus respectivos preços na sequência

prod = []
qtd = int(input('Quantos produtos irá cadastrar? '))

for i in range(qtd):
    prod.append(input('Digite o nome do produto: '))
    prod.append(float(input('Digite o preço do produto: ')))

for i in range(0, qtd * 2, 2):
    print('{}, R${:.2f}'.format(prod[i],  prod[i + 1]))