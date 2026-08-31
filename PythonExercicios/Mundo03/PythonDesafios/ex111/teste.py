from ex111.utilidadescev import moeda

preco = float(input('Digite o preço: R$'))

moeda.resumo(preco, 35, 22)
# print(f'A metade de {moeda.moeda(preco)} é {moeda.Metade(preco, True)}')
# print(f'O drobo de {moeda.moeda(preco)} é {moeda.Dobro(preco, True)}')
# print(f'Aumentando 10%, temos {moeda.Aumentar(preco, 10, True)}')
# print(f'Redusindo 13%, temos {moeda.Diminuir(preco, 13, True)}')