n = str(input('Digite o seu nome: ')).strip()
nome = n.split()
print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[len(nome) -1]))


