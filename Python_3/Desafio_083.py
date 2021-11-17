# Desenvolva um código que recebe uma espressão matemática com parenteses e informe se a expressão é valida ou não

exp = input('Digite uma expressão matemática: ')

if(exp.count('(') == exp.count(')')):
    print('Sua expressão está correta')

else:
    print('Sua expressão está errada')