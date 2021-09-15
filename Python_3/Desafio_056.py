# Desenvolva um código que receba nome, idade e sexo de quatro pessoas e mostre, a média da idade do grupo, qual o nome do homem mais velho e quantas mulheres tem menos de 20 anos

media = 0
idade_velho = 0
nome_velho = ''
qtd = 0

for i in range(0, 4):
    nome = input('Digite o nome da {}ª pessoa: '.format(i + 1))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i + 1)))
    sexo = input('Informe o sexo da {}ª pessoa: '.format(i + 1)).lower()

    media += idade

    if(sexo == 'm' and idade > idade_velho):
        nome_velho = nome
        idade_velho = idade

    if(sexo == 'f' and idade < 20):
        qtd += 1

print('A média de idade do grupo é {} anos'.format(int(media / 4)))
print('O homem mais velho se chama {}'.format(nome_velho))
print('No grupo tem {} mulheres com menos de 20 anos'.format(qtd))