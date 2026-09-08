from rich import print
from rich.panel import Panel

class ControleRemoto():
    canalMax = 5
    canalMin = 1
    volumeMax = 5
    volumeMin = 1

    def __init__(self, canal = 1, volume = 2):
        self.canalAtual:int = canal
        self.volumeAtual:int = volume
        self.ligado:bool = False

    def controle(self):
        while True:
            self.mostrarTv()
            comando = str(input(f'\n < CH{self.canalAtual} > - VOL{self.volumeAtual} + ')).strip()[0]
            match comando:
                case '@':
                    self.ligarDesligar()
                case '<':
                    self.canalMenos()
                case '>':
                    self.canalMais()
                case '-':
                    self.volumeMenos()
                case '+':
                    self.volumeMais()
                case '0':
                    break
            print('\n' * 10)

    def mostrarTv(self):
        if not self.ligado:
            conteudo = f':prohibited: [red]A TV esta desligada[/]'
        else:
            conteudo = f'CANAL  = '
            for canal in range(ControleRemoto.canalMin, ControleRemoto.canalMax + 1):
                if canal == self.canalAtual: 
                    conteudo += f'[black on green] {canal} [/]'
                else:
                    conteudo += f' {canal} '
            conteudo += f'VOLUME = '
            for volume in range(ControleRemoto.volumeMin, ControleRemoto.volumeMax + 1):
                if volume >= self.volumeAtual:
                    conteudo += f'[black on cyan] [/]'
                else:
                    conteudo += f'[black on white] [/]'

        tv = Panel(conteudo, title='[ TV ]', width=30)
        print(tv)
    def ligarDesligar(self):
        self.ligado = not self.ligado

    def canalMais(self):
        if self.ligado:
            if self.canalAtual == ControleRemoto.canalMax:
                self.canalAtual = ControleRemoto.canalMin
            else:
                self.canalAtual += 1

    def canalMenos(self):
        if self.ligado:
            if self.canalAtual == ControleRemoto.canalMin:
                self.canalAtual = ControleRemoto.canalMax
            else:
                self.canalAtual -= 1

    def volumeMais(self):
        if self.ligado:
            if self.volumeAtual != ControleRemoto.volumeMax:
                self.volumeAtual += 1

    def volumeMenos(self):
        if self.ligado:
            if self.volumeAtual != ControleRemoto.volumeMin:
                self.volumeAtual -= 1


c = ControleRemoto()
c.controle()