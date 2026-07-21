from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = hypot(ca, co)

print('A hipotenusa vai medir {:.2f}'.format(hi))

'''from math import sqrt

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = sqrt((co**2) + (ca**2))

print('A hipotenusa vai medir {:.2f}'.format(hi))'''