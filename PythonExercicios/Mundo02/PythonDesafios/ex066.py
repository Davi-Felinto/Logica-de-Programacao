soma = c = 0

while True:
    n = int(input('Digite um numero [999 para parar]: '))
    
    if n == 999:
        break
    soma += n
    c += 1

print(f'Você digitou {c} numeros e a soma entre eles foi {soma}')