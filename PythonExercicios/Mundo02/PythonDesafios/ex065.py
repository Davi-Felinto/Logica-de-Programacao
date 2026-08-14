n = int(input('Digite um numero: '))
resp = input('quer continuar? [S/N] ').upper()
i = 1
maior= menor = n
soma = n

while resp == 'S':
    n = int(input('Digite um numero: '))
    resp = input('quer continuar? [S/N] ').upper()
    soma += n
    i += 1
    maior = n if maior < n else maior
    menor = n if menor > n else menor
media = soma / i
print(f'Voê digitou {i} numero e a media foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')