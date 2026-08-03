# Exercício 033: sorteia 3 números e descobre o maior e o menor

# IMportando modulos
from random import randint  # sorteia números aleatórios

# Sorteando os 3 numeros
a= randint(0,100)  # sorteia o 1º número entre 0 e 100
b= randint(0,100)  # sorteia o 2º número entre 0 e 100
c= randint(0,100)  # sorteia o 3º número entre 0 e 100
print(f'Segundo numero: {a}')
print(f'Primeiro numero: {b}')
print(f'Terceiro numero: {c}')

# Verificando o menor numero
menor = a  # assume inicialmente que 'a' é o menor
if b<a and b<c:  # se 'b' for menor que os outros dois, 'b' é o menor
    menor = b
elif c<a and c<b:  # se 'c' for menor que os outros dois, 'c' é o menor
    menor = c

# Verificando o maior numero
maior = a  # assume inicialmente que 'a' é o maior
if b>a and b>c:  # se 'b' for maior que os outros dois, 'b' é o maior
    maior = b
elif c>a and c>b:  # se 'c' for maior que os outros dois, 'c' é o maior
    maior = c

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
