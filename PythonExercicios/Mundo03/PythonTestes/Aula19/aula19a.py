pessoa = {'nome': 'Davi', 'sexo': 'M', 'idade': 19}

print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos')
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

for k, v in pessoa.items():
    print(f'{k} = {v}')