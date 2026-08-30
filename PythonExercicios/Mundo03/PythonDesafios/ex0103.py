def FichaJogador(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gols(s) no campeonato.'


nome = input('Nome do jogador: ').strip()
gols = input('Numero de gol(s): ').strip()
if nome == '':
    nome ='<desconhecido>'
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0


print(FichaJogador(nome, gols))