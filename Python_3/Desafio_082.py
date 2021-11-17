# Desenvolva um código que receba vários números e separe em 2 listas, uma de números pares e outra com números ímpares, no final, mostre as 3 listas

valores = []
pares = []
impares = []
qtd = 0
rep = 'S'

while(rep == 'S'):
    qtd += 1
    valores.append(float(input('Digite o {}º número: '.format(qtd))))

    if(valores[-1] % 2 == 0):
        pares.append(valores[-1])
    
    else:
        impares.append(valores[-1])

    rep = input('Deseja digitar um novo número? (S/N)').upper()

print(valores)
print(pares)
print(impares)