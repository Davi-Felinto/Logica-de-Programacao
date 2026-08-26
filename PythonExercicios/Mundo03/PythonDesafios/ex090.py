aluno = dict()

aluno['nome'] = input('Nome: ').capitalize()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
print('-='*30)

if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] < 7 and aluno['média'] >= 5:
    aluno['situação'] = 'Recuperação'
elif aluno['média'] < 5:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'- {k} é igual a {v}')