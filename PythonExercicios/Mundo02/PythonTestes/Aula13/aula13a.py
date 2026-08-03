from random import randint

s = 0 
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    n = randint(0, 10) if n == 0 else n
    s += n 
    print(n)
print(f'O somatorio de todos os valores foi de {s}')