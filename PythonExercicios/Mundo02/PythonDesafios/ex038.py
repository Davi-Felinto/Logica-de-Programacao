# Importando modulos
from random import randint

# Entrada dos valores
n1 = int(input('Primeiro numero: '))
n1 = randint(0, 100) if n1 == 0 else n1
n2 = int(input('Segundo numero: '))
n2 = randint(0, 100) if n2 == 0 else n2
print(f'Primeiro numero: {n1}')
print(f'Segundo numero: {n2}')

# Saida do resultado de qual numero é maior e se são iguais
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')