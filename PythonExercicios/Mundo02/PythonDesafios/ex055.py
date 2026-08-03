from random import uniform
from sys import stdout

for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    if peso == 0:
        stdout.write("\033[F")  # Move o cursor para a linha anterior
        peso = uniform(40, 120)
        print(f'Peso da {i}ª pessoa: {peso:.1f}')
    
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f'\nO maior peso lido foi de {maior:.1f}Kg')
print(f'O menor peso lido foi de {menor:.1f}Kg')