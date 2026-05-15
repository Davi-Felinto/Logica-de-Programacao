nome = input()
salario = float(input())
total = float(input())

comis = (total*0.15)
total_salario =  (salario + comis)

print(f"TOTAL = R$ {total_salario:.2f}")