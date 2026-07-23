from math import hypot

co = float(input('Comprimento do cateto oposto: ')) #  Lendo comprimento dos catetos 
ca = float(input('Comprimento do cateto adjacente: '))

hi = hypot(ca, co) # Calculando o valor da hipotenusa

print('A hipotenusa vai medir {:.2f}'.format(hi)) # Saida do valor da hipotenusa

'''from math import sqrt

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = sqrt((co**2) + (ca**2))

print('A hipotenusa vai medir {:.2f}'.format(hi))'''