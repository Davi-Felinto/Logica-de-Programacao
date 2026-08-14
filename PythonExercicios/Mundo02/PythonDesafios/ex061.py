print('=='*15)
texto = 'Gerador de PA'
print(f'{texto:^30}')
print('=='*15)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
i = 1

while i <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    i += 1
print('FIM')
