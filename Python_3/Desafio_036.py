# Desenvolva um código que recebe o valor de uma casa, o salario do comprador e em quantos anos ele irá pagar. Informe se ela consigirá o emprestimo, sen do que o valor das prestações não podem ultrapassar 30% do salário


cas = float(input('Digite o valor do imóvel: '))
sal = float(input('Digite o salário do comprador: '))
ano = float(input('Digite em quantos anos o imóvel será pago: '))

if(cas / (ano * 12) <= sal * 0.3):
    print('O empréstimo foi aprovado!!!')

else:
    print('O empréstimo foi negado!!')