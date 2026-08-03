# Exercício 034: calcula aumento de salário (10% ou 15% dependendo do valor)

# Importandomodulo
from random import randint  # usado para sortear um salário caso o usuário digite 0

# Lendo o valor de salario
salario = int(input('Qual éo salario do funcionrio? R$'))
salario = randint(450, 2050) if salario == 0 else salario  # se digitar 0, sorteia um salário aleatório

# Verificando porcentagem de almento
if salario > 1250:  # salários maiores que 1250 recebem 10% de aumento
    aumento = salario + (salario * 0.10)
else:  # salários de 1250 ou menos recebem 15% de aumento
    aumento = salario + (salario * 0.15)

# Saida do salario e aumento
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f} agora.')
