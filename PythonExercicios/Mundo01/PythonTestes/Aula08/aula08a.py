# Aula 08a: calcula a raiz quadrada de um número e arredonda para baixo

from math import sqrt, floor  # sqrt calcula raiz quadrada, floor arredonda para baixo (piso)

num = int(input('Digite um numero:'))  # lê um número inteiro

raiz = sqrt(num)  # calcula a raiz quadrada (resultado decimal)

print(f'A raiz de {num} e é igual a {floor(raiz)}')  # floor() descarta as casas decimais arredondando para baixo
