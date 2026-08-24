num = [[], []]

for i in range(0, 7):
    n = int(input(f'Digite o {i+1}º valor: '))

    if (n % 2) == 0:
        num[0].append(n)
    elif (n % 2) == 1:
        num[1].append(n)
num[0].sort()
num[1].sort()

print('-='*30)
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')