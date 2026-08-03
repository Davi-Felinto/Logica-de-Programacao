# Exercício 040: calcula a média de duas notas e informa a situação do aluno

# Importando modulos
from random import uniform  # sorteia notas decimais caso o usuário digite 0

# lendo as notas e calculando nota
n1 = float(input('Primeira nota: '))
n1 = uniform(0, 10) if n1 == 0 else n1  # se digitar 0, sorteia uma nota decimal entre 0 e 10
n2 = float(input('Segunda nota: '))
n2 = uniform(0, 10) if n2 == 0 else n2  # se digitar 0, sorteia a 2ª nota
print('-='*10)
print(f'Primeira nota: {n1:.1f}')
print(f'Segunda nota: {n2:.1f}')
media = (n1+n2)/2  # calcula a média aritmética das duas notas
print(f'Tirando {n1:.1f} e {n2:.1f}, a media do aluno é {media:.1f}')

# saida se o aluno foi aprovado, reprovado ou e em recuperação
if media < 5.0:  # média abaixo de 5: reprovado
    print('O aluno está de REPROVADO')
elif media >= 7.0 and media < 10.0:  # média de 7 até quase 10: aprovado
    print('O aluno está de APROVADO')
elif 5 <= media < 7:  # média entre 5 e 7: recuperação
    print('O aluno está de RECUPERAÇÂO')
