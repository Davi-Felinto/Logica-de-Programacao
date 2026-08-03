# Exercício 023: separa um número sorteado em unidade, dezena, centena e milhar

# Versão alternativa (comentada) que lia o número como string e pegava cada posição do texto
'''num = input('Informe um numero: ')

print(f'Analisando o numero {num}')
print(f'Uninade: {num[3]}')
print(f'Dezena: {num[2]}')
print(f'Centena: {num[1]}')
print(f'Milhar: {num[0]}')'''

from random import randint  # randint sorteia um número inteiro dentro de um intervalo

num = randint(1,9999)  # sorteia um número entre 1 e 9999
print('Sorteando um numero')

print(f'Analisando o numero {num}')
# Uso de operadores % (resto da divisão) e // (divisão inteira) para extrair cada dígito
print(f'Uninade: {num%10}')            # resto da divisão por 10 = último dígito (unidade)
print(f'Dezena: {num//10 % 10}')       # divide por 10 (remove a unidade) e pega o resto por 10 (dezena)
print(f'Centena: {num//100 % 10}')     # divide por 100 e pega o resto por 10 (centena)
print(f'Milhar: {num//1000 % 10}')     # divide por 1000 e pega o resto por 10 (milhar)
