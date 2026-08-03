# Exercício 020: sorteia a ordem de apresentação de 4 alunos

import random  # módulo usado para embaralhar a lista

n1 = input('Primeiro Aluno: ')   # lê o nome do 1º aluno
n2 = input('Segundo Aluno: ')    # lê o nome do 2º aluno
n3 = input('Terceiro Aluno: ')   # lê o nome do 3º aluno
n4 = input('Quarto Aluno: ')     # lê o nome do 4º aluno

lista = [n1, n2, n3, n4]  # cria a lista com os alunos
random.shuffle(lista)     # embaralha a lista in-place (altera a própria lista)

print('A ordem de apresentação será')
print(lista)  # mostra a lista já embaralhada
