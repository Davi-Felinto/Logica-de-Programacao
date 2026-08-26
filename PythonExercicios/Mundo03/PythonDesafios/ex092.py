from datetime import datetime
dados = dict()

dados['nome'] = input('Nome: ').capitalize()
dados['idade'] = (datetime.now().year - int(input('Ano de Nascimento: ')))
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)

print('-='*30)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')


# print(f' - nome tem o valor {dados['nome']}')
# print(f' - idade tem o valor {dados['idade']}')
# print(f' - ctps tem o valor {dados['ctps']}')
# if dados['ctps'] != 0:
#     print(f' - contratação tem valor {dados['anoContratacao']}')
#     print(f' - salário tem valor {dados['salario']:.2f}')
#     print(f' - aposentadoria tem valor {dados['aposentadoria']}')