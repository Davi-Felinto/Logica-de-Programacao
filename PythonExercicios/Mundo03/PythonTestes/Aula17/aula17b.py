valores = list()
quantidade = int(input('Digite a quantidade de numeros q vc quer adiconar: '))
i = 1
while i <= quantidade:
    valores.append(int(input('Digite um valor: ')))
    i += 1


for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')