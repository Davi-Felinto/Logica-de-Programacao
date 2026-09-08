from rich import print
from time import sleep

class Livro():
    def __init__(self, tituloLivro, quantidadePaginas):
        self.titulo = tituloLivro
        self.quantidadePaginas = quantidadePaginas
        self.paginaAtual = 1
        
        print(f':open_book: [blue]Você acabou de abrir o livro "[red]{self.titulo}[blue]" que tem [green]{self.quantidadePaginas} paginas [blue]no total. Você agora está na [yellow]pagina {self.paginaAtual}')

    def avancarPagina(self, quantidadePaginasAvancar = 1) -> str:
        destino = self.paginaAtual + quantidadePaginasAvancar
        quantidadeAvancada = 0

        destino = self.quantidadePaginas if destino > self.quantidadePaginas else destino
        
        for pagina in range(self.paginaAtual + 1, destino + 1):
            print(f'Pág{pagina}', end=' > ')
            self.paginaAtual = pagina
            quantidadeAvancada += 1
            sleep(0.25)
        
        print(f'[blue]Você avançou {quantidadeAvancada} paginas e agora está na [yellow]página {self.paginaAtual}')
        print(f'[red]Você chegou ao final do livro "{self.titulo}') if self.paginaAtual == self.quantidadePaginas else None



l1 = Livro('10 coisas que aprendi', 20)
l1.avancarPagina(5)
l1.avancarPagina(10)
l1.avancarPagina(1)
l1.avancarPagina(7)