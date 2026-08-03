# Exercício 027: mostra o primeiro e o último nome de uma pessoa

nome = input('Digite seu nome completo: ').strip().title().split()
# strip() remove espaços das pontas, title() deixa cada palavra com inicial maiúscula, split() separa em lista

print('Prazer em te conehcer!')
print(f'Seu primeiro nome é {nome[0]}')            # primeiro elemento da lista
print(f'Seu último nome é {nome[len(nome)-1]}')    # último elemento da lista (índice = tamanho - 1)
