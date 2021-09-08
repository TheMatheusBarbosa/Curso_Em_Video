# Desenvolva um código que recebe a velocidade de um carro e calcule a multa caso ultrapasse 80Km/h, sendo R$7.00 por cada Km acima do limite

vlr = float(input('Digite a velocidade do carro: '))

if(vlr > 80):
    print('A multa foi de R${:.2f}'.format((vlr - 80) * 7))

else:
    print('O carro não ultrapassou a velocidade máxima!')