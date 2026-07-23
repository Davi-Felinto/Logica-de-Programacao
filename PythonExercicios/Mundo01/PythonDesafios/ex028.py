from random import randint
from time import sleep

computador = randint(0,5) # Sorteando um numero de 1 a 5

print('-=' * 30)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=' * 30)

num = int(input('Em que numero pensei? ')) # Lendo um numero

print('PROCESSANDO...')
sleep(2)
if num == computador: # Saida da verificação se é o msm numero 
    print(f'PARABENS! Você me venceu!')
else:
    print(f'Ganhei! Eu pensei no numero {computador} e não no {num}!')