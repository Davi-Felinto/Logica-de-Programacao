# Exercício 028: jogo de adivinhar o número que o computador "pensou"

from random import randint  # sorteia um número aleatório
from time import sleep      # permite pausar a execução por alguns segundos

computador = randint(0,10)  # sorteia um número entre 0 e 5 (o número "pensado" pelo computador)

print('-=' * 30)  # linha decorativa
print('Vou pensar em um numero entre 0 e 10.')
print('-=' * 30)
print('Você consegue adivinhar qual foi ?')

num = int(input('Qual é o seu papite? '))  # lê o palpite do usuário

c = 1
while num != computador:
    c += 1
    if num < computador:
        print('Mais...Tente masi uma vez.')
        num = int(input('Qual é o seu papite? '))
    else:
        print('Menos...Tente masi uma vez.')
        num = int(input('Qual é o seu papite? '))
print(f'Acertou com {c} tentativas. Parabéns!')