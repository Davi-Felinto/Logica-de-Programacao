num = int(input('Digite um numero: '))

cont = 0
for c in range(1,num + 1):
    if (num % c) == 0:
        cont += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print(f'\n\033[mO número {num} foi divisivel {cont} vezes')

if cont == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃo É PRIMO!')