# Desenvolva um código que recebe uma palavra e informe quantas vezes a letra "A" aparece, qual a posição da primeira e última aparição

vlr = input('Digite uma palavra: ').strip

print('A letra "A" aparece {} vez(es)'.format(vlr.upper().count('A')))
print('A letra "A" aparece pela 1ª vez no caracter {}'.format(vlr.upper().find('A') + 1 ))
print('A letra "A" aparece pela última vez no caracter {}'.format(vlr.upper().rfind('A') + 1))