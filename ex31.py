n = int(input('Digite a distância da viagem (km): '))
d = 0.50
dl = 0.45
if n <= 200:
    print('O valor da sua passagem é: R$ {:.2f}.'.format(n*d))
else:
    print('O valor da sua passagem é: R$ {:.2f}.'.format(n*dl))
