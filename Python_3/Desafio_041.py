# Desenvolva um código recebe o ano de nascimento de um atleta e defina a categoria seguindo as seguinte regras. Até 9 anos, mirim; até 14 anos, infantil; até 19 anos, junior; até 20 anos, sênior e acima de 20 anos, master

import datetime

vlr = int(input('Informe o ano de nascimento do aleta: '))
idade = datetime.date.today().year - vlr

if(idade <= 9):
    print('O atleta faz parte da categoria MIRIM')

elif(idade > 9 and idade <= 14):
    print('O atleta faz parte da categoria INFANTIL')

elif(idade > 14 and idade <= 19):
    print('O atleta faz parte da categoria JUNIOR')

elif(idade > 19 and idade <= 20):
    print('O atleta faz parte da categoria SÊNIOR')

else:
    print('O atleta faz parte da categoria MASTER')