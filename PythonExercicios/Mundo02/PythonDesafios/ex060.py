'''from math import factorial
num = int(input('Digite um número para calcular seu fatorial: '))
print(f'O fatoria de {num} é {factorial(num)}')'''


num = int(input('Digite um número para calcular seu fatorial: '))

print(f'Calculando {num}! = ', end='')
fatorial = 1
while num != 0:
    print(f'{num} x ', end='')
    fatorial = num * fatorial
    num -= 1

print(f'= {fatorial}')
