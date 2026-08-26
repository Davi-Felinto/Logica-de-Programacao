estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print(v, end=', ')
    print()

# for e in brasil:
#     for k, v in e.items():
#         print(f'O capmo {k} tem valor {v}')