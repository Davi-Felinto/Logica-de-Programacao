from rich import print
from rich.panel import Panel

class Gamer():

    def __init__(self, nomeReal, nickName):
        self.nome = nomeReal
        self.nick = nickName
        self.favoritos = list()

    def addFavoritos(self, jogoFavorito):
        self.favoritos.append(jogoFavorito)

    def ficha(self):
        conteudo = f'Nome real: [black on blue]{self.nome}\n[/]'
        conteudo += f'Jogos Favoritos:\n'
        self.favoritos.sort()
        for jogo in self.favoritos:
            conteudo += f':video_game: [blue]{jogo}[/]\n'
        painel = Panel(conteudo, title=f'Jogador <{self.nick}>', width=50)
        print(painel)


j1 = Gamer('Davi Felinto', 'davifd0978')
j1.addFavoritos('God of War')
j1.addFavoritos('The Last of Us')
j1.addFavoritos('GTA VI')
j1.ficha()

j2 = Gamer('Olivia Souza', 'peach_raivosa')
j2.addFavoritos('Mario Bros')
j2.addFavoritos('Call of Duty')
j2.ficha()