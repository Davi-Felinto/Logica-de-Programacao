n = 1
par = 0
impar = 0
cont = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        cont += 1
        if (n % 2) == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} numeros pares e {impar} numeros impares!')
print(f'Foram digitado {cont} numeros ate ser escolido o 0')