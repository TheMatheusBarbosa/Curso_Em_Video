# Desenvolva um código que receba diversas notas e calcule a média, maior e menor nota. Sempre que receber uma nota, pergunte ao usuário se deseja incluir uma nova

nota = int(input('Informe uma nota:'))
media = nota
maior = nota
menor = nota
cont = 1
opc = input('Deseja inserir uma nova nota? [S/N]').upper()

while(opc == 'S'):
    nota = int(input('Informe uma nota:'))
    media += nota

    if(nota > maior):
        maior = nota
    
    elif(nota < menor):
        menor = nota

    cont += 1

    opc = input('Deseja inserir uma nova nota? [S/N]').upper()

print('A média das {} notas é {:.1f}'.format(cont, media / cont))
print('A maior nota digitada foi {}'.format(maior))
print('A menor nota digitada foi {}'.format(menor))