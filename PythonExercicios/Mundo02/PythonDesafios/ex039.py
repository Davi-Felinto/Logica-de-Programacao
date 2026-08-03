# Exercício 039: calcula a idade e verifica situação de alistamento militar

# importando modulos
from datetime import date       # para pegar o ano atual do sistema
from random import randint      # sorteia um ano de nascimento caso o usuário digite 0

# Calculando idade 
atual = date.today().year  # ano atual do sistema
nasc = int(input('Ano de nascimento: '))
nasc = randint(1950, date.today().year) if nasc == 0 else nasc  # se digitar 0, sorteia um ano de nascimento
idade = atual - nasc  # calcula a idade aproximada
print(f'Quem nasceu em {nasc} tem {idade} em {atual}.')

# Saida do alistamento
if idade == 18:  # exatamente 18 anos: precisa se alistar agora
    print('Você tem q se alistar IMEDIATAMENTE!')
elif idade < 18:  # menor de 18: calcula quanto falta e em que ano será
    sal = 18 - idade
    print(f'Ainda faltam {sal} nascs para o alistamento.')
    ano = atual + sal
    print(f'Seu alistamento será em {ano}')
elif idade > 18:  # maior de 18: calcula há quanto tempo passou e em que ano deveria ter sido
    sal= idade - 18
    print(f'Você já deveria ter se alistado há {sal} anos.')
    ano = atual - sal
    print(f'Seu alistamento foi em {ano}')
