# Exercício 038: compara dois números e diz qual é maior (ou se são iguais)

# Importando modulos
from random import randint  # sorteia valores caso o usuário digite 0

# Entrada dos valores
n1 = int(input('Primeiro numero: '))
n1 = randint(0, 100) if n1 == 0 else n1  # se digitar 0, sorteia o 1º número
n2 = int(input('Segundo numero: '))
n2 = randint(0, 100) if n2 == 0 else n2  # se digitar 0, sorteia o 2º número
print(f'Primeiro numero: {n1}')
print(f'Segundo numero: {n2}')

# Saida do resultado de qual numero é maior e se são iguais
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')
