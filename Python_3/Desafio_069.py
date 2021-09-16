# Desenvolva um código recebe a idade e sexo de varias pessoas. Para cada cadastro pergunte se o usuário deseja cadastrar uma nova pessoa, no final mostre quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados e quantas mulheres tem menos de 20 anos

opc = 'S'
sexo = ''
cont = 0
hom = 0
mul = 0

while(opc == 'S'):

    idade = int(input('Digite a idade da pessoa: '))
    
    while(sexo != 'M' and sexo != 'F'):
        sexo = input('Digite o sexo da pessoa: [M/F] ').upper()

    if(idade > 18):
        cont += 1

    if(sexo == 'M'):
        hom += 1

    if(sexo == 'F' and idade < 20):
        mul += 1

    opc = ''

    while(opc != 'S' and opc != 'N'):
        opc = input('Deseja cadastrar uma nova pessoa: [S/N] ').upper()

print('{} pessoas tem mais de 18 anos'.format(cont))
print('{} homens foram cadastrados'.format(hom))
print('{} mulheres tem menos de 20 anos'.format(mul))