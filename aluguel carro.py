km = float(input('Digite a quilometragem percorrida: '))
tempo = int(input('Digite por quantos dias o carro foi utilizado: '))
vtempo = tempo * 60
vkm = km * 0.15
vt = vtempo + vkm
print('Com base nos dados acima, o valor do aluguel é: R$ {:.2f}'.format(vt))




