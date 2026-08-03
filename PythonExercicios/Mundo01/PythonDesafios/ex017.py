# Exercício 017: calcula a hipotenusa de um triângulo retângulo

from math import hypot  # hypot(a, b) calcula a hipotenusa a partir dos dois catetos

co = float(input('Comprimento do cateto oposto: '))     # lê o cateto oposto
ca = float(input('Comprimento do cateto adjacente: '))   # lê o cateto adjacente

hi = hypot(ca, co)  # calcula a hipotenusa: raiz(ca² + co²)

print('A hipotenusa vai medir {:.2f}'.format(hi))

# Forma alternativa (comentada) usando sqrt para calcular manualmente
'''from math import sqrt

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = sqrt((co**2) + (ca**2))

print('A hipotenusa vai medir {:.2f}'.format(hi))'''
