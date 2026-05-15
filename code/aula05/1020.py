idade = int(input())

ano = (idade//365)
dia = (idade%365)
mes = (dia//30)
dia = (dia%30)

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dia} dia(s)")