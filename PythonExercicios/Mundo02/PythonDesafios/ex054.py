from random import randint
from datetime import date
from sys import stdout

maior = 0
menor = 0
for i in range(1, 8):
    nasc = int(input(f'Em q ano a {i}ª pessoa nasceu? '))
    if nasc == 0:
        stdout.write("\033[F")  # Move o cursor para a linha anterior
        nasc = randint(1984, date.today().year)
        print(f'Em q ano a {i}ª pessoa nasceu? {nasc}')
    
    idade = (date.today().year - nasc)
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print(f'\nAo tivemos {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menores de idade')