# leitura do salario
sal = float(input("Digite salario: "))

# selecionando faixa de salario, calculo do reajuste e de novo salario
if sal >= 0.0 and sal  < 400.01:
    per = 15
    reajuste = sal *(per/100)
    novosal = sal + reajuste
elif sal > 400 and sal < 800.01:
    per = 12
    reajuste = sal *(per/100)
    novosal = sal + reajuste
elif sal > 800 and sal < 1200.01:
    per = 10
    reajuste = sal *(per/100)
    novosal = sal + reajuste
elif sal > 1200 and sal < 2000.01:
    per = 7
    reajuste = sal *(per/100)
    novosal = sal + reajuste
elif sal > 2000:
    per = 4
    reajuste = sal *(per/100)
    novosal = sal + reajuste

print(f"Novo salario: {novosal:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em porcentual: {per} %")