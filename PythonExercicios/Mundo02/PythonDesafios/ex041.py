# importando modulos
from datetime import date
from random import randint

# Calculando idade 
nasc = int(input('Ano de nascimento: '))
nasc = randint(1990, date.today().year) if nasc == 0 else nasc
idade = (date.today().year) - nasc
print(f'O atleta tem {idade} anos.')

# 
if idade <= 9:
    classificação = 'MIRIM'
    print(f'Classificação: {classificação}')
elif idade <= 14:
    classificação = 'INFANTIL'
    print(f'Classificação: {classificação}')
elif idade <= 19:
    classificação = 'JUNIOR'
    print(f'Classificação: {classificação}')
elif idade <= 25:
    classificação = 'SÊNIOR'
    print(f'Classificação: {classificação}')
elif idade > 25:
    classificação = 'MASTER'
    print(f'Classificação: {classificação}')