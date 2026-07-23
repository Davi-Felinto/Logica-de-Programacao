import random

n1 = input('Primeiro Aluno: ') # Lendo os alunos 
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')

lista = [n1, n2, n3, n4] # Criando lista de alunos e embaralhando a lista
random.shuffle(lista)

print('A ordem de apresentação será') # Saida da lista de alunos
print(lista)