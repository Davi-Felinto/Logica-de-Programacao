from random import choice, randint
from sys import stdout

s_idade = 0
velho = 0
nome_velho = ''
cont_mulher_menos20 = 0
for i in range(1, 5):
    print('-'*5, f'{i}ª PESSOA', '-'*5)
    
    nome = input('Nome: ').strip()
    if not nome:
        nomes = ['Davi', 'Pedro', 'João', 'Ana', 'Hallana', 'Bia']
        nome = choice(nomes)
        stdout.write("\033[F") 
        print(f'Nome: {nome}')

    idade = int(input('Idade: '))
    if idade == 0:
        idade = randint(1, 50)
        stdout.write("\033[F") 
        print(f'Idade: {idade}')

    sexo = input('Sexo [M/F]: ').strip()
    if not sexo:
        if nome == 'Davi' or nome == 'Pedro' or nome == 'João':
            sexo = 'M'
        else:
            sexo = 'F'
        stdout.write("\033[F") 
        print(f'Sexo [M/F]: {sexo}')

    s_idade += idade
    if idade > velho:
        velho = idade
        nome_velho = nome
    if sexo.upper() == 'F' and idade < 20:
        cont_mulher_menos20 += 1

media_idade = (s_idade / i)
print(f'\nA media de idade do grupo é de {media_idade:.1f} anos')
print(f'O homem mais velho tem {velho} anos e se chama {nome_velho}')
print(f'Ao todo são {cont_mulher_menos20} mulheres com menos de 20 anos')