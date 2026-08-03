# Exercício 028: jogo de adivinhar o número que o computador "pensou"

from random import randint  # sorteia um número aleatório
from time import sleep      # permite pausar a execução por alguns segundos

computador = randint(0,5)  # sorteia um número entre 0 e 5 (o número "pensado" pelo computador)

print('-=' * 30)  # linha decorativa
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=' * 30)

num = int(input('Em que numero pensei? '))  # lê o palpite do usuário

print('PROCESSANDO...')
sleep(2)  # pausa de 2 segundos para dar suspense
if num == computador:  # compara o palpite do usuário com o número sorteado
    print(f'PARABENS! Você me venceu!')
else:
    print(f'Ganhei! Eu pensei no numero {computador} e não no {num}!')
