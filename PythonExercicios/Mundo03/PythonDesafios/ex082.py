valores = []
valPar = []
valImpar = []

while True:
    valores.append(int(input('Digite um valor: ')))
    resp = input('Quer continuar? [S/N] ')
    if resp.upper() == 'N':
        break

# for i in range(0, len(valores)):
for i, v in enumerate(valores):
    if (v % 2) == 0:
        valPar.append(v)
    elif (v % 2) == 1:
        valImpar.append(v)

print('-='*30)
print(f'A lista completa é {valores}')
print(f'A lista pares é {valPar}')
print(f'A lista de impares {valImpar}')