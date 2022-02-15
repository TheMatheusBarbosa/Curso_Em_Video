# Desenvolva um código que receba nome e peso de diversas pessoas em uma lista e informe quantas pessoas foram cadastradas, uma listagem com o nome das pessoas das pessoas mais pesadas e mais leves

pessoas = []
pessoa = []
loop = 'S'
qtd = 0
maisPeso = []
maisLeve = []

while(loop == 'S'):
    qtd += 1
    pessoa.append(input('Digite o nome da {}ª pessoa: '.format(qtd)))
    pessoa.append(float(input('Digite o peso da {}ª pessoa: '.format(qtd))))
    pessoas.append(pessoa[:])

    if(len(maisPeso) == 0):
        maisPeso.append(pessoa[:])
    
    else:
        if(pessoa[1] > maisPeso[0][1]):
            maisPeso.clear()
            maisPeso.append(pessoa[:])
        
        elif(pessoa[1] == maisPeso[0][1]):
            maisPeso.append(pessoa[:])

    if(len(maisLeve) == 0):
        maisLeve.append(pessoa[:])

    else:
        if(pessoa[1] < maisLeve[0][1]):
            maisLeve.clear()
            maisLeve.append(pessoa[:])

        elif(pessoa[1] == maisLeve[0][1]):
            maisLeve.append(pessoa[:])

    pessoa.clear()
    loop = input('Deseja incluir mais uma pessoa? (S/N): ').upper()

print('Foram cadastradas {} pessoas'.format(len(pessoas)))
print('O maior peso foi de {}kg. Peso de {}'.format(maisPeso[0][1], maisPeso[0:-1][0]))
print('O menor peso foi de {}kg. Peso de {}'.format(maisLeve[0][1], maisLeve[0:-1][0]))