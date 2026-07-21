dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos KM rodados? '))

pagar = (dias * 60) + (km * 0.15)

print(f'O valor a pagar é de R${pagar:.2f}')