from rich import print
from rich.panel import Panel

class Churrasco():
    consumoPadrao:float = 0.4
    precoCarne:float = 82.40

    def __init__(self, titulo, quantidadePessoas):
        self.titulo = titulo
        self.quantidadePessoas = quantidadePessoas

    def calcularQuantidadeCarne(self) -> float:
        return self.quantidadePessoas * Churrasco.consumoPadrao

    def calcularCustoTotal(self) -> float:
        return self.calcularQuantidadeCarne() * Churrasco.precoCarne

    def calcularCustoPessoa(self) -> float:
        return self.calcularCustoTotal() / self.quantidadePessoas

    def analisar(self):

        conteudo = f'Analisando [green]{self.titulo}[/] com [blue]{self.quantidadePessoas} convidados[/]\n'
        conteudo += f'Cada participante comera {Churrasco.consumoPadrao}Kg e da Kg custa R${Churrasco.precoCarne}\n'
        conteudo += f'Recomendo [blue]comprar {self.calcularQuantidadeCarne():.3f}Kg[/] de carne\n'
        conteudo += f'O custo total sera de [green]R${self.calcularCustoTotal():,.2f}[/]\n'
        conteudo += f'Cada pessoa pagara [yellow]R${self.calcularCustoPessoa()}[/] para cada participante'

        painel = Panel(conteudo, title=f'{self.titulo}', width=100)
        print(painel)



c1 = Churrasco('Churras dos Amigos', 15)
c1.analisar()

c2 = Churrasco('Festa do Fim de Ano', 80)
c2.analisar()

c3 = Churrasco('Festa do Fim de Ano', 50)
c3.analisar()