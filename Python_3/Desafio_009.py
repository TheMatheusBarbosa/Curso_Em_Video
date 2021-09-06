# Desenolva um código que mostre a tabuada de um número

vlr = int(input('Digite o número de qual tabuada quer ver: '))

for i in range(11):
    print('{} x {} = {}'.format(vlr, i, vlr * i))