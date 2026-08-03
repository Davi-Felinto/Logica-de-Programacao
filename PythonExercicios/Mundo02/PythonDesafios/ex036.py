# Exercício 036: simula análise de financiamento de uma casa

# Importando modulo
from random import randint  # sorteia valores caso o usuário digite 0
from math import ceil       # (importado mas não utilizado neste código)

# Lendo valor da casa, salario e anos do financiamento
casa = int(input('Valor da casa: R$'))
casa = randint(50000, 1000000) if casa == 0 else casa  # se digitar 0, sorteia um valor de casa
sal = int(input('Salario do comprador: R$'))
sal = randint(1500, 15000) if sal == 0 else sal        # se digitar 0, sorteia um salário
anos = int(input('Quantos anos de financiamento: '))
anos = randint(5, 30) if anos == 0 else anos           # se digitar 0, sorteia a quantidade de anos
print('-='*15)
print(f'Valor da casa: R${casa}')
print(f'Salario do comprador: R${sal}')
print(f'Anos de financiamento: {anos}')

# Calculando a parcela
parc = (casa / (anos*12))  # divide o valor da casa pelo número total de meses (anos * 12)
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a pestação será de R${parc:.2f}')

# Saida se emprestimo é concedido ou negado
if parc < (sal*0.30):  # a parcela não pode ultrapassar 30% do salário
    print('emprestimo pode ser CONCEDIDO!')
else:
    print('emprestimo pode ser NEGADO!')
