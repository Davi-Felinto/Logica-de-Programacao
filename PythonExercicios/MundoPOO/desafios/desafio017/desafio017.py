from rich import print
from rich.panel import Panel

class Produto():

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f'{self.nome} custa R${self.preco:,.2f}'

    def Etiqueta(self):
        conteudo = f'{self.nome.center(30, ' ')}'
        conteudo += ('-'*30)
        precoF = f'R${self.preco:,.2f}'
        conteudo += f'{precoF.center(30, '.')}'
        etiqueta = Panel(conteudo, title='Produto', width=34)
        print(etiqueta)

p1 = Produto('Iphone 15 Pro', 7_000.95)
# print(p1.__str__())
p1.Etiqueta()

p2 = Produto('Notebook Gamer', 8_000)
p2.Etiqueta()