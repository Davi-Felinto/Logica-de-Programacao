# Exercício 013: aplica 15% de aumento sobre um salário

salario = float(input('Qual é o salario do Funcionario? R$'))  # lê o salário atual

# salario * 1.15 = salário + 15% de aumento (100% + 15% = 115%)
print('Um funcionario que ganhava R${} com 15% de aumento, passa a receber R${:.2f}'.format(salario, (salario * 1.15)))
