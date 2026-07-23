dias = int(input('Quantos dias alugados? ')) # Lendo o numero de dias e distancia
km = int(input('Quantos KM rodados? '))

pagar = (dias * 60) + (km * 0.15) # Calculo do valor a pagar

print(f'O valor a pagar é de R${pagar:.2f}')  # Saida do valor a pagar