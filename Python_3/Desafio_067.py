# Desenolva um código que mostre a tabuada de um número, o código será interrompido quando receberum número negativp

vlr = 0

while (vlr >= 0):
    vlr = int(input('Digite o número de qual tabuada quer ver: '))

    if(vlr < 0):
        break

    for i in range(11):
        print('{} x {} = {}'.format(vlr, i, vlr * i))