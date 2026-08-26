pessoa = dict()
dados = list()
mulher = list()
somaIdade = 0

while True:
    pessoa['nome'] = input('Nome: ').capitalize()
    while True:
        pessoa['sexo'] = input('Sexo: [M/F] ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    somaIdade += pessoa['idade']
    dados.append(pessoa.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resp == "N":
        break
print('-='*30)

mediaIdade = (somaIdade / len(dados))
for p in dados:
    if p['sexo'] =='F':
        mulher.append(p['nome'])


print(f'A) Ao todo temos {len(dados)} pessoas cadastradas.')
print(f'B) A média de idade é de {mediaIdade:.2f} anos.')
print(f'C) As mulheres cadastradas foram {mulher}')
print(f'D) Lista das pessoas acima da media de idade:')
for p in dados:
    if p['idade'] > mediaIdade:
        print(p)
print('<< ENCERRADO >>')