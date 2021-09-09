# Desenvolva um código que receba o ano de nascimento de uma pessoa e informe se está na hora de se alistar, se anda precisa se alistar e em quanto tempo ou se já passou o tempo de se alistar e quanto tempo passou

import datetime

vlr = int(input('Informe o ano do seu nascimento: '))

if(datetime.date.today().year - vlr < 18):
    print('Ainda não chegou sua hora de se alistar, faltam {} anos'.format(18 - (datetime.date.today().year - vlr)))

elif(datetime.date.today().year - vlr > 18):
    print('Já passou da hora de se alistar, você devia ter feito o alistamento a {} anos'.format((datetime.date.today().year - vlr) - 18))

else:
    print('Está na hora de se alistar')