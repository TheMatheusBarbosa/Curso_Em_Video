# Desenvolva um código que recebe o comprimeto de três retas e informe se pode formar um triângulo e qual tipo de triângulo ele forma

n1 = float(input('Digite o comprimento da 1ª reta: '))
n2 = float(input('Digite o comprimento da 2ª reta: '))
n3 = float(input('Digite o comprimento da 3ª reta: '))

tri = [n1, n2, n3]
tri.sort()

if(tri[0] + tri[1] > tri[2]):
    if(tri[0] == tri[1] and tri[1] == tri[2]):
        print('As retas com o comprimento {}, {} e {} podem formar um triângulo equilátero'.format(n1, n2, n3))
    
    elif(tri[0] == tri[1] or tri[0] == tri[2] or tri[1] == tri[2]):
        print('As retas com o comprimento {}, {} e {} podem formar um triângulo isósceles'.format(n1, n2, n3))
    
    else:
        print('As retas com o comprimento {}, {} e {} podem formar um triângulo escaleno'.format(n1, n2, n3))

else:
    print('As retas com o comprimento {}, {} e {} não podem formar um triângulo'.format(n1, n2, n3))