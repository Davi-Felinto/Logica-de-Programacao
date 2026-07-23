# Importandomodulo
from random import randint

# Lendo o valor de salario
salario = int(input('Qual éo salario do funcionrio? R$'))
salario = randint(450, 2050) if salario == 0 else salario

# Verificando porcentagem de almento
if salario > 1250:
    aumento = salario + (salario * 0.10)
else:
    aumento = salario + (salario * 0.15)

# Saida do salario e aumento
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f} agora.')