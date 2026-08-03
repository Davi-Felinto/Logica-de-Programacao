# Exercício 018: calcula seno, cosseno e tangente de um ângulo

from math import radians, sin, cos, tan  # funções trigonométricas trabalham com radianos, não graus

angulo = int(input('Digite o ângulo que deseja: '))  # lê o ângulo em graus

rad = radians(angulo)  # converte o ângulo de graus para radianos
sen = sin(rad)          # calcula o seno do ângulo
cos = cos(rad)          # calcula o cosseno do ângulo (obs: sobrescreve a função cos importada)
tan = tan(rad)          # calcula a tangente do ângulo (obs: sobrescreve a função tan importada)

print(f'O ângulo de {int(angulo)} tem o SENO de {sen:.2f}')
print(f'O ângulo de {int(angulo)} tem o COSSENO de {cos:.2f}')
print(f'O ângulo de {int(angulo)} tem o TANGENTE de {tan:.2f}')
