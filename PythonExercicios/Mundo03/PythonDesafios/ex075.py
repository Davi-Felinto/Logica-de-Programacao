num = (int(input('Digite um numero: ')), 
        int(input('Digite outro numero: ')),
        int(input('Digite mais um numero: ')),
        int(input('Digite o ultimo numero: ')))
contPar = 0

print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
print(f'O valor 3 apareceu na {num.index(3)+1}ª posição') if 3 in num else print('O valor 3 não foi digitado em nunhuma posição')
print(f'Os valores pares digitados foram', end=' ')
for n in num:
    print(n, end=' ') if (n %2) == 0 else n