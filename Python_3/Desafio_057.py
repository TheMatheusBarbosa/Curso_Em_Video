# Desenvolva um código que receba o sexo de uma pessoa, mas só aceite "M" ou "F", caso receba qualquer outro valor, repita novamente a pergunta

vlr = ''

while(vlr != 'F' and vlr != 'M'):
    vlr = input('Digite o sexo da pessoa [M/F]: ').upper()
