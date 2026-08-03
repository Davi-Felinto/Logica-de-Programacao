# Exercício 030: sorteia um número de 0 a 100 e diz se é par ou ímpar

# Importando os módulos necessários
from time import sleep            # para pausar a execução (efeito de suspense)
from random import randint        # para sortear um número aleatório
from os import system, name       # para identificar o sistema operacional e limpar o terminal

print('-='*20)
print('Pensando em um numero!')
print('-='*20)
sleep(2)  # espera 2 segundos antes de continuar

# Limpando o terminal: 'cls' no Windows ('nt') e 'clear' em outros sistemas (Linux/Mac)
system('cls' if name == 'nt' else 'clear')

# Sorteando um numero aleatorio de 0 a 100
num = randint(0, 100)

# Saida do numero sorteado
print('-='*20)
print('Numero pensado foi: {}'.format(num))
print('-='*20)
sleep(2)

# Saida da verificação se o numero é impar ou par
system('cls' if name == 'nt' else 'clear')  # limpa a tela de novo antes de mostrar o resultado
if (num%2) == 0:  # se o resto da divisão por 2 for 0, o número é par
    print('-='*5)
    print('O numero {} é PAR'.format(num))
    print('-='*5)
else:  # caso contrário, é ímpar
    print('-='*25)
    print('O numero {} é IMPAR'.format(num))
    print('-='*25)
