from pessoa import Pessoa

class Funcionario(Pessoa):
      '''classe Funcionario que representa um funcionário''' 
      def __init__(self, nome, idade, cargo, setor):
        '''construtor da classe Funcionario'''
        super().__init__(nome, idade) # chama o construtor da classe Pessoa
        self.cargo:str = cargo # atribui o cargo do funcionário
        self.setor:str = setor # atribui o setor do funcionário

      def bater_ponto(self):
        '''método para bater ponto do funcionário'''
        print(f'Funcionário [bold white]{self.nome}[/] bateu o ponto...')