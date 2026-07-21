from math import radians, sin, cos, tan

angulo = int(input('Digite o ângulo que deseja: '))

rad = radians(angulo)
sen = sin(rad)
cos = cos(rad)
tan = tan(rad)

print(f'O ângulo de {int(angulo)} tem o SENO de {sen:.2f}')
print(f'O ângulo de {int(angulo)} tem o COSSENO de {cos:.2f}')
print(f'O ângulo de {int(angulo)} tem o TANGENTE de {tan:.2f}')