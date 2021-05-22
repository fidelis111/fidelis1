import random
computador = random.randint(0, 5) #faz o computador pensar
print('Vou pensar em um número de 0 a 5, tente adivinhar: ')
jogador = int(input('Em que número eu pensei? ')) #o jogador tenta adivinhar
if jogador == computador:
    print('Parabéns, você acertou.')
else:
    print('Não foi dessa vez, tente de novo.')


