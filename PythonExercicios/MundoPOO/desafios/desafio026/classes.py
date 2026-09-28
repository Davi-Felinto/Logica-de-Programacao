from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print

class Funcionario(ABC):
    sal_min = 1612
    inss = 7.5

    def __init__(self, nome=None):
        self.sal_bruto= 0
        self.salario = 0
        self.nome = nome


    @abstractmethod
    def calc_sal():
        pass

    def analisar_sal(self):
        conteudo = f'''O salario de [blue]{self.nome}[/] ([purple]{self.__class__.__name__}[/]) e de [green]R${self.salario:.2f}[/] e corresponde a [yellow]{self.salario/self.sal_min:.1f} salarios minimos[/]'''
        painel = Panel(conteudo, title='Analise de Salario', width=45)
        print(painel)


class Horista(Funcionario):
    
    def __init__(self, nome, valor_hora= 7.37, horas_trab= 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
        self.sal_bruto = self.valor_hora*self.horas_trab

    def calc_sal(self):
        self.salario = (self.sal_bruto - (self.sal_bruto*(Funcionario.inss/100)))


class Mensalista(Funcionario):
    
    def __init__(self, nome, sal_bruto):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calc_sal(self):
        self.salario = (self.sal_bruto - (self.sal_bruto*(Funcionario.inss/100)))