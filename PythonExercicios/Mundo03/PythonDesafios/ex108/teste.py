from ex108 import moeda

preco = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.Metade(preco))}')
print(f'O drobo de {moeda.moeda(preco)} é {moeda.moeda(moeda.Dobro(preco))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.Aumentar(preco, 10))}')
print(f'Redusindo 13%, temos {moeda.moeda(moeda.Diminuir(preco, 13))}')