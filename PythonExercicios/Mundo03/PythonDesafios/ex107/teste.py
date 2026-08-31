from ex107 import moeda

preco = float(input('Digite o preço: R$'))

print(f'A metade de {preco} é {moeda.Metade(preco)}')
print(f'O drobo de {preco} é {moeda.Dobro(preco)}')
print(f'Aumentando 10%, temos {moeda.Aumentar(preco, 10)}')
print(f'Redusindo 13%, temos {moeda.Diminuir(preco, 13)}')