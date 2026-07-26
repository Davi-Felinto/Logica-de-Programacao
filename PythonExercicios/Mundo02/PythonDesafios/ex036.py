# Importando modulo
from random import randint
from math import ceil

# Lendo valor da casa, salario e anos do financiamento
casa = int(input('Valor da casa: R$'))
casa = randint(50000, 1000000) if casa == 0 else casa
sal = int(input('Salario do comprador: R$'))
sal = randint(1500, 15000) if sal == 0 else sal
anos = int(input('Quantos anos de financiamento: '))
anos = randint(5, 30) if anos == 0 else anos
print('-='*15)
print(f'Valor da casa: R${casa}')
print(f'Salario do comprador: R${sal}')
print(f'Anos de financiamento: {anos}')

# Calculando a parcela
parc = (casa / (anos*12))
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a pestação será de R${parc:.2f}')

# Saida se emprestimo é concedido ou negado
if parc < (sal*0.30):
    print('emprestimo pode ser CONCEDIDO!')
else:
    print('emprestimo pode ser NEGADO!')
