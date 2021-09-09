# Desenvolva um código que recebe o peso e altura de uma pessoa e calcule o IMC mostrando sua categoria

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura * altura)

if(imc < 18.5):
    print('IMC: {}. Abaixo do peso'.format(imc))

elif(imc >= 18.5 and imc < 25):
    print('IMC: {}. Peso ideal'.format(imc))

elif(imc >= 25 and imc < 30):
    print('IMC: {}. Sobrepeso'.format(imc))

elif(imc >= 30 and imc < 40):
    print('IMC: {}. Obesidade'.format(imc))

else:
    print('IMC: {}. Obesidade mórbida'.format(imc))