n = int(input('Digite um numero [999 para parar]: '))
soma = 0
c = 0

while n != 999:
    soma += n
    n = int(input('Digite um numero [999 para parar]: '))
    c += 1
print(f'Você digitou {c} numeros e a soma entre eles foi {soma}')