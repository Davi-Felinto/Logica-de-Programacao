'''num = input('Informe um numero: ')

print(f'Analisando o numero {num}')
print(f'Uninade: {num[3]}')
print(f'Dezena: {num[2]}')
print(f'Centena: {num[1]}')
print(f'Milhar: {num[0]}')'''
from random import randint

num = randint(1,9999) # Sorteando um numero de 1 a 9999
print('Sorteando um numero')

print(f'Analisando o numero {num}') # Analisando o numero. Quantas unidade, dezenas, centenas e milhar
print(f'Uninade: {num%10}')
print(f'Dezena: {num//10 % 10}')
print(f'Centena: {num//100 % 10}')
print(f'Milhar: {num//1000 % 10}')