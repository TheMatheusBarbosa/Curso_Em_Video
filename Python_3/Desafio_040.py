# Desenvolva um código que recebe duas notas e informe se ele foi aprovado , reprovado ou ficou de recuperação, sendo abaixo 5, reprovado, entre 5 e 6.9 de reuperação e maior ou igual a 7, aprovado

n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))

if(round((n1 + n2) / 2, 1) < 5):
    print('Reprovado')

elif(round((n1 + n2) / 2, 2) >= 7):
    print('Aprovado')

else:
    print('Recuperação')