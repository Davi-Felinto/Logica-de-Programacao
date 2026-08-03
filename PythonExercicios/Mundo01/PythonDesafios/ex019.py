# Exercício 019: sorteia um aluno entre 4 para apresentar um trabalho

import random  # módulo usado para sortear valores aleatórios

n1 = input('Primeiro Aluno: ')   # lê o nome do 1º aluno
n2 = input('Segundo Aluno: ')    # lê o nome do 2º aluno
n3 = input('Terceiro Aluno: ')   # lê o nome do 3º aluno
n4 = input('Quarto Aluno: ')     # lê o nome do 4º aluno

lista = [n1, n2, n3, n4]  # cria uma lista com os 4 alunos

print(f'O aluno escolido foi {random.choice(lista)}')  # random.choice() sorteia um item aleatório da lista
