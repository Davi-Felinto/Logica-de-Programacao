from random import randint

numero = (randint(1,10), randint(1,10), randint(1,10), 
            randint(1,10), randint(1,10))

print(f'Os valores sorteados foram: ', end='')
for n in numero:
    print(n, end=' ')
print(f'\nO maior valor sorteado foi: {max(numero)}')
print(f'O menor valor sorteado foi: {min(numero)}')