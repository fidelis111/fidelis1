n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Binario
[2] Octal
[3] Hexadecimal''')
opçao = int(input('Sua opção é: '))
if opçao == 1:
    print('A forma binária de {} é: {}'.format(n, bin(n) [2:]))
elif opçao == 2:
    print('A forma octal de {} é: {}'.format(n, oct(n) [2:]))
elif opçao == 3:
    print('A forma octal de {} é: {}'.format(n, hex(n) [2:]))
    # o [2:] é um fatiamento pra começar da posição 2



