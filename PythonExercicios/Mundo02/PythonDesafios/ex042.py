# Importando modulo
from random import randint

print('-='*15)
print('Analisador de Triangulo')
print('-='*15)

# Lendo valor de segmentos
s1 = int(input('Primeiro segmento: '))
s1 = randint(0, 10) if s1 == 0 else s1
s2 = int(input('Segundo segmento: '))
s2 = randint(0, 10) if s2 == 0 else s2
s3 = int(input('Terceiro segmento: '))
s3 = randint(0, 10) if s3 == 0 else s3
print('-='*15)
print(f'Primeiro segmento: {s1:.2f}')
print(f'Segundo segmento: {s2:.2f}')
print(f'Terceiro segmento: {s3:.2f}')

# Saida da verificação de se pode forma triangulo ou não
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmesntos acima PODEM FORMA um triangulo', end=' ')
    if s1 == s2 == s3:
        print('EQUILÁTERO')
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print('ISÓCELES')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO')
else:
    print('Os segmesntos acima NÃO PODEM FORMA um triangulo')
