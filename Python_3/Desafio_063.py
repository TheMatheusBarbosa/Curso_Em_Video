# Desenvolva um código que recebe um número inteiro n e mostre na tela os n primeiros elementos da sequencia de fibonacci

vlr = int(input("Que termo deseja encontrar: "))
ult = 1
pen = 1


if (vlr==1):
    print("0")

elif(vlr==2):
    print("1")

else:
    print("0")
    print("1")
    print("1")
    
    count=3
    
    while count < vlr:
        termo = ult + pen
        print(termo)
        pen = ult
        ult = termo
        count += 1