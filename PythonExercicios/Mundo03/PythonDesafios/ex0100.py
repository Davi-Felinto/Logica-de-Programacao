from random import randint

def sortear(lista):
    print('Sorteando 5 valores da lista : ', end='')
    for i in range(0, 5):
        lista.append(randint(1, 10))
        print(lista[i], end=' ')
    print('PRONTO!')

def somaPar(lista):
    somaPar = 0
    for i in lista:
        if (i % 2) == 0:
            somaPar += i
    print(f'Somando os valores pares de {lista}, temos {somaPar}')

numeros = list()
sortear(numeros)
somaPar(numeros)