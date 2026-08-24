from random import randint
from time import sleep
sorteio = list()
jogos = list()

print('-'*30)
print(f'{'JOGA NA MEGA SENA':^30}')
print('-'*30)
numJogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*3, f'  SORTEANDO {numJogos} JOGOS  ', '-='*3)

for c in range(0, numJogos):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in sorteio:
            sorteio.append(num)
            cont += 1
        if cont == 6:
            break
    sorteio.sort()
    jogos.append(sorteio[:])
    sorteio.clear()
    sleep(0.5)
    print(f'Jogo {c+1} : {jogos[c]}')
print('-='*5, '< BOA SORTE! >', '-='*5)