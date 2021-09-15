# Desenvolva um código que recebe o peso de cinco pessoas e informe qual foi o maior e menor peso

maior = 0
menor = 9999

for i in range(0, 5):
    vlr = float(input('Digite o peso da {}ª pessoa: '.format(i + 1)))

    if(vlr > maior):
        maior = vlr

    if(vlr < menor):
        menor = vlr

print('O maior peso recebido foi: {:.2f} Kg'.format(maior))
print('O menor peso recebido foi: {:.2f} Kg'.format(menor))