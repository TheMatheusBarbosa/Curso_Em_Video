# Desenvolva um código que receba cinco valores mas insira na lista de forma crescente sem usar o short

valores = []
vlr = 0.0

for i in range(5):
    vlr = float(input('Digite o {}º valor: '.format(i + 1)))

    if i == 0:
        valores.insert(i, vlr)
        print('Adcionado na posição 0 da lista...')

    else:
        for p in range(len(valores)):
            if vlr <= valores[p]:
                valores.insert(p, vlr)
                print('Adcionado na posição {} da lista...'.format(p))
                break

            if p == len(valores) - 1 and vlr > valores[p]:
                valores.append(vlr)
                print('Adicionado ao final da lista...')

print(valores)