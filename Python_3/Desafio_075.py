# Desenvolva um código que recebe quatro valores e mostre quantas vezes aparece o número 9, em que posição foi digitado o primeiro 3 e quais foram os números

lst = []
par = []

for i in range(4):
    lst.append(int(input('Digite um número: ')))
    
    if(lst[i] % 2 == 0):
        par.append(lst[i])

print('O número 9 apareceu {} vezes'.format(lst.count(9)))
print('O número 3 está na {}ª posição'.format(lst.index(3) + 1))
print('O números pares foram: {}'.format(par))