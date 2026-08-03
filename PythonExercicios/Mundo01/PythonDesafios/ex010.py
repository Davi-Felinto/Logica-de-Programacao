# Exercício 010: converte reais em dólares

RS = float(input('Quanto dinheiro você tem na carteira: R$'))  # lê o valor em reais

print(f'Com R${RS:.2} você pode comprar US${RS/5.16:.2f}')  # divide o valor por uma cotação fixa (5.16) para obter dólares
