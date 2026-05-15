num = [float(input()) for i in range(6)]

posi = len([i for i in num if i > 0])

print(f'{posi} valores positivos')