# Desenvolva um código que recebe um valor e simule a operação de saque de um caixa eletrônico, informando quantas notas serão entregues. considere notas de R$100, R$50 e R$20

vlr = float(input('Digite o valor desejado para saque: '))

n100 = vlr // 100
vlr -= n100 * 100

n50 = vlr // 50
vlr -= n50 * 50

n20 = vlr // 20
vlr -= n20 * 20

if(vlr == 0):
    print('Você receberá {:.0f} notas de R$100.00'.format(n100))
    print('Você receberá {:.0f} notas de R$50.00'.format(n50))
    print('Você receberá {:.0f} notas de R$20.00'.format(n20))

else:
    print('Valor indisponível para saque')