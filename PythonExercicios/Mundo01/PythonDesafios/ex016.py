# Exercício 016: mostra a parte inteira de um número decimal

from math import trunc  # trunc() corta a parte decimal de um número, sem arredondar

num = float(input('Digite um valor: '))  # lê um número decimal

print(f'O valor digitado foi {num} e a sua porção interira é {trunc(num)}')

# Forma alternativa (comentada) usando int(), que também descarta a parte decimal
'''num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e a sua porção interira é {int(num)}')'''
