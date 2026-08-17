classificacao = ('Palmeiras', 'Flamengo', 'Atheletico', 'Fluminense',
                'Cruzeiro', 'BAHIA', 'RB Bragantino', 'Corinthians',
                'Coritiba', 'Botafogo', 'Atlétic-MG', 'São Paulo',
                'Vitoria', 'Grêmio', 'Mirassol', 'Internacional',
                 'Santos', 'Vasco', 'Remo', 'Chapecoense')

print('-='*10)
print(f'Lista de times do Brasileirão: {classificacao}')
print('-='*10)
print(f'Os 5 primeiros são {classificacao[:6]}')
print('-='*10)
print(f'Os 4 últimos são {classificacao[-4:]}')
print('-='*10)
print(f'Times em ordem alfabética: {sorted(classificacao)}')
print('-='*10)
print(f'O São Paulo está na {classificacao.index('São Paulo') + 1}ª posição')