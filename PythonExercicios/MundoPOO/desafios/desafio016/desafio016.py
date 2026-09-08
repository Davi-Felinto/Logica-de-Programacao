from rich import print
from rich import inspect

class Funcionario():
    # Atributo de classe
    empresa = 'Curso em Video'

    def __init__(self, nome, setor, cargo):
        # Atributos de instacia
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def Apresentacao(self) -> str:
        return f':handshake: Ola, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}'


c1 = Funcionario('Davi Felinto', 'Programador', 'TI')
print(c1.Apresentacao())
# inspect(c1, methods=True)

c2 = Funcionario('Gustavo Guanabara', 'TI', 'Diretor')
print(c2.Apresentacao())