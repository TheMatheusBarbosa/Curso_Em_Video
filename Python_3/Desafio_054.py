# Desenvolva um código que recebe o ano de nascimento de sete pessoas e informe quantas já atingiram a maioridade e quantas não atingiram

import datetime

s = 0

for i in range(0, 7):
    vlr = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i + 1)))
    
    if (datetime.date.today().year - vlr >= 21):
        s += 1

print('{} pessoas já são maiores de idade'.format(s))
print('{} pessoas ainda são menores de idade'.format(7 - s))