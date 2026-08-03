print('=='*15)
texto = '10 termos de uma PA'
print(f'{texto:^30}')
print('=='*15)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 -1) * razao

for c in range(termo, decimo + razao, razao):
    print(c, end=' -> ')
print('Acabou')