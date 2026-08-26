jogador = dict()
time = list()

while True:
    jogador['nome'] = input('Nome do jogador: ').title()
    numPartidas = int(input(f'Quantas partida {jogador['nome']} jogou? '))
    jogador['gols'] = []
    for i in range(1, (numPartidas + 1)):
        print('    ', end='')
        jogador['gols'].append(int(input(f'Quantos gols na partida {i}? ')))
    jogador['total'] = sum(jogador['gols'])
    time.append(jogador.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').upper() [0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resp == "N":
        break

print('-='*30)
print(f'{"cod":^3}', f'{"nome":<20}', f'{"gols":<15}', f'{"total":^5}')
print('-'*43)
for i, v in enumerate(time):
    print(f'{i:>3}', f'{v["nome"]:<20}', f'{str(v["gols"]):<15}', f'{v["total"]:<5}' )

while True:
    print('-'*43)
    resp = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if resp == 999:
        print('<< VOLTE SEMPRE >>')
        break
    elif resp >= len(time):
        print(f'ERRO! Não existe jogador com código {resp}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[resp]['nome']}:')
        for i, v in enumerate(time[resp]['gols']):
            print('    ', end='')
            print(f'No jo {i+1} fez {v} gols.')