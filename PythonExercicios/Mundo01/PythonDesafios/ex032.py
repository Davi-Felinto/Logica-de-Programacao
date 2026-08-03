# Exercício 032: verifica se um ano é bissexto

# Importando modulo
from datetime import date  # usado para pegar o ano atual do sistema

# Lendo valor de ano
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:  # se o usuário digitar 0, usa o ano atual do sistema
    ano = date.today().year

# Saida se é ou não bissexto
# Regra do ano bissexto: divisível por 4 e não por 100, OU divisível por 400
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÃO é BISSEXTO')
