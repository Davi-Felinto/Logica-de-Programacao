#leitura do salario
sal = float(input())

#difinindo as variaveis
percentual = 0 
novoSal = 0
reajuste = 0

#definição do percentual
if sal <= 400:
    percentual = 0.15
elif sal <= 800:
    percentual = 0.12
elif sal <= 1200:
    percentual = 0.1
elif sal <= 2000:
    percentual = 0.07
else:
    percentual = 0.04

#definindo novo salrio e o reajuste
novoSal = sal + sal * percentual
reajuste = sal * percentual

#saida das informações 
print(f"Novo salario: {novoSal:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em porcentual: {(percentual * 100):.0f} %")