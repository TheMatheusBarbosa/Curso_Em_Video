# Desenvolva um código que recebe a altura e largura de uma parede, calcule sua área e informe a quantidade de tinta necessária para pintá-la considerando que 1L pinta uma área de 2m²

lgr = float(input('Informe em metros a largura da parede: '))
atr = float(input('Informe em metros a altura da parede:  '))

print('Sua parede possui {}m² e será necessário {}L para pintá-la'.format(lgr * atr, (lgr * atr) / 2))