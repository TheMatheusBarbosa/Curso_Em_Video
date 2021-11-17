# Desenvolva um código que receba vários números e coloque em uma lista. Informe quantos números foram digitados, a lista de forma decrescente e se o o número 5 está ou não na lista

valores = []
qtd = 0
rep = 'S'

while(rep == 'S'):
    qtd += 1
    valores.append(float(input('Digite o {}º número: '.format(qtd))))
    rep = input('Deseja digitar um novo número? (S/N)').upper()

valores.sort(reverse=True)

print(len(valores))
print(valores)

if(valores.count(5) > 0 ):
    print('O valor 5 faz parte da lista')

else:
    print('O valor 5 não faz parte da lista')