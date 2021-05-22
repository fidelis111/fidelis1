n = float(input('Digite o seu salário (R$): '))
if n > 1250.00:
    print('O seu aumento é de: R$ {:.2f}.'.format(n * 0.10))
else:
    print('O seu aumento é de: R$ {:.2f}.'.format(n * 0.15))
