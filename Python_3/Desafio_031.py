# Desenvolva um código que recebe a distancia de uma viagem e calcule o preço da passagem, considerando R$0.50/Km para viagens de até 200Km e R$0.45/Km para viagens mais longas

vlr = float(input('Digite a distância da viagem: '))

if(vlr > 200):
    print('A passagem irá custar R${:.2f}'.format(vlr * 0.45))

else:
    print('A passagem irá custar R${:.2f}'.format(vlr * 0.50))