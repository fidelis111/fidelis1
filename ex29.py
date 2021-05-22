v = float(input('Digite a velocidade:'))
m = (v - 80) * 7
if v > 80:
    print('Você foi multado,o valor a ser pago é R$ {:.2f}.'.format(m))
else:
    print('Parabéns, você está dentro do limite de velocidade.')

