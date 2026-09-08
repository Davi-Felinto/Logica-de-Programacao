from rich import print

class Caneta():
    def __init__(self, corCaneta):
        match corCaneta.lower().strip():
            case 'azul':
                cor = '[blue]'
            case 'vermelha' | 'vermelho':
                cor = '[red]'
            case 'verde':
                cor = '[green]'
            case _:
                cor = '[white]'
        self.cor = cor
        self.estaDestampada = False

    def escrever(self, texto):
        if self.estaDestampada:
            print(f'{self.cor}{texto}[/]', end=' ')
        else:
            print(f':prohibited: A {self.cor}caneta[/] está tampada!')
    
    def destampar(self):
        self.estaDestampada = True

    def tampar(self):
        self.estaDestampada = False

    def quebrarLinha(self, quantidaeLinhaQuebrar=1) -> str:
        for i in range(0, quantidaeLinhaQuebrar):
            print()


c1 = Caneta('Azul')
c2 = Caneta('Vermelha')
c3 = Caneta('Verde')

c1.destampar()
c2.destampar()
# c3.destampar()

c1.escrever('Olá, tudo bem? ')
c1.quebrarLinha(2)
c2.escrever('Olá, Garfonhoto! ')
c3.escrever('Vamos exercitar!')
