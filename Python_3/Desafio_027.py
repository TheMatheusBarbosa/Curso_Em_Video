# Desenvolva um código que recebe um nome e exiba o primeiro e último nome

vlr = input('Digite um nome: ').strip

print('Primeiro nome: {}'.format(vlr.split()[0]))
print('Último nome  : {}'.format(vlr.split()[len(vlr.split()) - 1]))