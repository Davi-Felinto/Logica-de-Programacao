print('=='*15)
texto = 'Gerador de PA'
print(f'{texto:^30}')
print('=='*15)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
i = 1
tot = 0
mais = 10
while mais != 0:
    tot = mais + tot
    while i <= tot:
        print(f'{termo} -> ', end='')
        termo += razao
        i += 1
    print('PAUSA')
    i = 0
    mais = int(input('Quantos termos você quer a mais? '))