# Importando modulos
from random import uniform

# lendo as notas e calculando nota
n1 = float(input('Primeira nota: '))
n1 = uniform(0, 10) if n1 == 0 else n1
n2 = float(input('Segunda nota: '))
n2 = uniform(0, 10) if n2 == 0 else n2
print('-='*10)
print(f'Primeira nota: {n1:.1f}')
print(f'Segunda nota: {n2:.1f}')
media = (n1+n2)/2
print(f'Tirando {n1:.1f} e {n2:.1f}, a media do aluno é {media:.1f}')

# saida se o aluno foi aprovado, reprovado ou e em recuperação
if media < 5.0:
    print('O aluno está de REPROVADO')
elif media >= 7.0 and media < 10.0:
    print('O aluno está de APROVADO')
elif 5 <= media < 7:
    print('O aluno está de RECUPERAÇÂO')