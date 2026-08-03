# Exercício 015: calcula o valor a pagar por um aluguel de carro

dias = int(input('Quantos dias alugados? '))  # lê quantos dias o carro foi alugado
km = int(input('Quantos KM rodados? '))       # lê quantos km foram rodados

pagar = (dias * 60) + (km * 0.15)  # cada dia custa R$60 e cada km rodado custa R$0,15

print(f'O valor a pagar é de R${pagar:.2f}')
