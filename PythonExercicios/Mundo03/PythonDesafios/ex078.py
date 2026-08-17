valores = []
menor = maior = 0
for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        menor = maior = valores[i] 
    else: 
        if maior < valores[i]:
            maior = valores[i]
        if menor > valores[i]:
            menor = valores[i]


print('=-' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for i, val in enumerate(valores):
    print(f'{i}...', end=' ')if val == max(valores) else val
print()
print(f'O menor valor digitado foi {min(valores)} nas posições ', end='')
for i, val in enumerate(valores):
    print(f'{i}...', end=' ') if val == min(valores) else val
print()