# Importando os mudulos necessarios
from time import sleep
from random import randint
from os import system, name

print('-='*20) 
print('Pensando em um numero!')
print('-='*20)
sleep(2)

# Limpando o terminal
system('cls' if name == 'nt' else 'clear')

 # Sorteado um numero aleatorio de 0 a 100
num = randint(0, 100)

# Saida do numero sorteado
print('-='*20)
print('Numero pensado foi: {}'.format(num))
print('-='*20)
sleep(2)

# Saida da verificação se o numero é impar ou par
system('cls' if name == 'nt' else 'clear')
if (num%2) == 0:
    print('-='*5)
    print('O numero {} é PAR'.format(num))
    print('-='*5)
else:
    print('-='*25)
    print('O numero {} é IMPAR'.format(num))
    print('-='*25)