# Desenvolva um código que calcule a soma entre todos os números ímpares que são múltiplos de 3 e estão no intervalo entre 1 e 500

s = 0

for i in range(1, 501):
    
    if(i % 2 == 1 and i % 3 == 0):
        s += i

print(s)