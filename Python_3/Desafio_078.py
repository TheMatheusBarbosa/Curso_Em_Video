# Desenvolva um código que recebe cinco valores e no final mostre suas respectivas posições na lista

vlr = []
maior = []
menor = []

for i in range(5):
    vlr.append(float(input('Digite o {}º valor: '.format(i + 1))))

    if i == 0:
        maior = [i, vlr[i]]
        menor = [i, vlr[i]]
    
    else:
        if vlr[i] > vlr[i - 1]:
             maior = [i, vlr[i]]

        if vlr[i] < vlr[i - 1]:
            menor = [i, vlr[i]]

print('O maior valor é {}, está na posição {}'.format(maior[1], maior[0]))
print('O menor valor é {}, está na posição {}'.format(menor[1], menor[0]))