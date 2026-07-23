# IMportando modulos
from random import randint

# Sorteando os 3 numeros
a= randint(0,100)
b= randint(0,100)
c= randint(0,100)
print(f'Segundo numero: {a}')
print(f'Primeiro numero: {b}')
print(f'Terceiro numero: {c}')

# Verificando o menor numero
menor = a 
if b<a and b<c:
    menor = b
elif c<a and c<b:
    menor = c

# Verificando o maior numero
maior = a 
if b>a and b>c:
    maior = b
elif c>a and c>b:
    maior = c

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))