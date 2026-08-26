jogador = dict()

jogador['nome'] = input('Nome do jogador: ').title()
numPartidas = int(input(f'Quantas partida {jogador['nome']} jogou? '))
jogador['gols'] = []
for i in range(0, numPartidas):
    jogador['gols'].append(int(input(f'Quantos gols na partida {i}? ')))
jogador['total'] = sum(jogador['gols'])

print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print('-='*30)
print(f'o joagador {jogador['nome']} jogou {len(jogador['gols'])}.')
for i, v in enumerate(jogador['gols']):
    print(f'=> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador['total']} gols.')