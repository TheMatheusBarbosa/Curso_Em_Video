# Desenvolva um código que mostre os cinco primeiros colocados na tebla do brasileirão, os quatro últimos, em ordem alfabética e em que posição ficou o Corinthians

tbl = ['Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino', 'Ceará', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport Recife', 'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo']

print('Os 5 primeiros colocados foram:')
print(tbl[:5])
print('Os 4 últimos colocados foram:')
print(tbl[-4:])
print('Os times que participaram da competição foram:')
print(sorted(tbl))
print('o Corinthians ficou na {}ª colocação'.format(tbl.index('Corinthians') + 1))