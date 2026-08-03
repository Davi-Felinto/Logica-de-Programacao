# Exercício 012: aplica 5% de desconto sobre o preço de um produto

valor = float(input('Qual é o preço do produto?'))  # lê o preço original do produto

# valor * 0.95 = valor com 5% de desconto (100% - 5% = 95%)
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(valor, (valor * 0.95)))
