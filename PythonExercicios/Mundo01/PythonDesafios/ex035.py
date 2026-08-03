# Exercício 035: verifica se 3 segmentos de reta podem formar um triângulo

# Importando modulo
from random import uniform  # sorteia um número decimal caso o usuário digite 0

print('-='*15)
print('Analisador de Triangulo')
print('-='*15)

# Lendo valor de segmentos
s1 = int(input('Primeiro segmento: '))
s1 = uniform(0, 10) if s1 == 0 else s1  # se digitar 0, sorteia um valor decimal entre 0 e 10
s2 = int(input('Segundo segmento: '))
s2 = uniform(0, 10) if s2 == 0 else s2
s3 = int(input('Terceiro segmento: '))
s3 = uniform(0, 10) if s3 == 0 else s3
print('-='*15)
print(f'Primeiro segmento: {s1:.2f}')
print(f'Segundo segmento: {s2:.2f}')
print(f'Terceiro segmento: {s3:.2f}')

# Saida da verificação de se pode forma triangulo ou não
# Regra: cada lado precisa ser menor que a soma dos outros dois (desigualdade triangular)
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmesntos acima PODEM FORMA um triangulo')
else:
    print('Os segmesntos acima NÃO PODEM FORMA um triangulo')
