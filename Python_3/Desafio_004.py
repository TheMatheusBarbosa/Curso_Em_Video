# Desenvolva um código que analise o tipo primitivo do seu input e todas as suas caracteristicas

vlr = input('Digite algo: ')

print('o tipo primitivo do que você digitou é: {}'.format(type(vlr)))
print('O que você digitou, é ALFANUMÉRICO? {}'.format(vlr.isalnum()))
print('O que você digitou, é ALFABÉTICO? {}'.format(vlr.isalpha()))
print('O que você digitou, é NUMÉRICO? {}'.format(vlr.isnumeric()))
print('O que você digitou, é DECIMAL? {}'.format(vlr.isdecimal()))
print('O que você digitou, tem a primeira letra de cada palavra em CAIXA ALTA? {}'.format(vlr.istitle()))
print('O que você digitou, é CAIXA ALTA? {}'.format(vlr.isupper()))
print('O que você digitou, é CAIXA BAIXA? {}'.format(vlr.islower()))
print('O que você digitou, tem apenas ESPAÇO? {}'.format(vlr.isspace()))
print('O que você digitou, é PADRÃO ASCII? {}'.format(vlr.isascii()))
print('O que você digitou, é DIGITO? {}'.format(vlr.isdigit()))
print('O que você digitou, é um IDENTIFICADOR? {}'.format(vlr.isidentifier()))
print('O que você digitou, é IMPRIMÍVEL? {}'.format(vlr.isprintable()))