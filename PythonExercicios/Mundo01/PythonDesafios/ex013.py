salario = float(input('Qual é o salario do Funcionario? R$')) # Lendo salario

print('Um funcionario que ganhava R${} com 15% de aumento, passa a receber R${:.2f}'.format(salario, (salario * 1.15))) # Saida do salario e aumento de 15%