# Exercício 002: pede o nome do usuário e cumprimenta

nome = input('Digite seu Nome: ')  # lê o nome digitado pelo usuário e guarda na variável 'nome'

print('É um prazer te conhecer, {}!'.format(nome))  # o .format() insere o valor de 'nome' no lugar de {}
