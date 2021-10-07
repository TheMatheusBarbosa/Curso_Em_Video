# Desenvolva um código que recebe diversas palavras e mostre quais são as vogais dessas palavras

palavras = []
qtd = int(input('Quantas palavras irá digitar? '))
vogais = ''

for i in range(qtd):
    palavras.append(input('Digite a {}ª palvra'.format(i + 1)).upper())

for palavra in palavras:
    vogais = ''
    
    for letra in range(len(palavra)):
        if palavra[letra] in 'AEIOU':
            vogais = vogais + palavra[letra] + ' '
        
    print('Na palavra {} temos as vogais {}'.format(palavra, vogais))