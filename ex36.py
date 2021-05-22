casa = float(input('Qual será o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
prazo = int(input('Por quantos anos você quer pagar? '))
mensalidade = casa / (prazo * 12)
print('Sua parcela de empréstimo é: R${:.2f}'.format(mensalidade))
if mensalidade > (salario * 0.30):
    print('Seu empréstimo foi rejeitado.')
else:
    print('Seu empréstimo foi aprovado.')


