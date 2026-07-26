# importando modulos
from datetime import date
from random import randint

# Calculando idade 
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
nasc = randint(1950, date.today().year) if nasc == 0 else nasc
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} em {atual}.')

# Saida do alistamento
if idade == 18:
    print('Você tem q se alistar IMEDIATAMENTE!')
elif idade < 18:
    sal = 18 - idade
    print(f'Ainda faltam {sal} nascs para o alistamento.')
    ano = atual + sal
    print(f'Seu alistamento será em {ano}')
elif idade > 18:
    sal= idade - 18
    print(f'Você já deveria ter se alistado há {sal} anos.')
    ano = atual - sal
    print(f'Seu alistamento foi em {ano}')