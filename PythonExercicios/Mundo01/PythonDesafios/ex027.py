nome = input('Digite seu nome completo: ').strip().title().split() # Lendo nome

print('Prazer em te conehcer!') # Saida do primeiro e ultimo nome
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}')