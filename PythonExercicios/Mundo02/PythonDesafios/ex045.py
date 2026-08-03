from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0,2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogado = int(input('Qual a sua jogada? '))
jogado = randint(0,2) if jogado == 3 else jogado

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('-='*12)
print(f'O jogador jogou {itens[jogado]}')
print(f'O computador jogou {itens[comp]}')
print('-='*12)
sleep(1)

if comp == 0: # pedra
    if jogado == 0: # pedra
        print('EMPATE')
    elif jogado == 1:# papel
        print('JOGADOR VENCEU')
    elif jogado == 2: # tesoura
        print('COMPUTADOR VENCEU')
    else:
        print('OPÇÃO INVALIDA!')
elif comp == 1:# papel
    if jogado == 0: # pedra
        print('COMPUTADOR VENCEU')
    elif jogado == 1:# papel
        print('EMPATE')
    elif jogado == 2: # tesoura
        print('JOGADOR VENCEU')
    else:
        print('OPÇÃO INVALIDA!')
elif comp == 2: # tesoura
    if jogado == 0: # pedra
        print('JOGADOR VENCEU')
    elif jogado == 1:# papel
        print('COMPUTADOR VENCEU')
    elif jogado == 2: # tesoura
        print('EMPATE')
    else:
        print('OPÇÃO INVALIDA!')
else:
    print('OPÇÃO INVALIDA!')