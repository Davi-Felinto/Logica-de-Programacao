import random

n1 = input('Primeiro Aluno: ') # Lendo aluno n1, n2, n3, n4 
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')

lista = [n1, n2, n3, n4] # Criando uma array com os alunos

print(f'O aluno escolido foi {random.choice(lista)}') #  Saida do aluno sorteado 