valor = float(input('Qual é o preço do produto?'))

print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(valor, (valor * 0.95)))