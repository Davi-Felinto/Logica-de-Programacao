from rich import print
from rich import inspect

class Pessoa:
    '''classe Pessoa que representa uma pessoa'''
    def __init__(self, nome:str = '', idade:int = 0):
        '''construtor da classe Pessoa'''
        self.nome:str = nome # atribui o nome da pessoa
        self.idade:int = idade # atribui a idade da pessoa

    def fazerAniversario(self):
        '''método para fazer aniversário da pessoa'''
        self.idade += 1 # aumenta a idade em 1


class Aluno(Pessoa):
    '''classe Aluno que representa um aluno'''
    def __init__(self, nome, idade, curso, turma):
        '''construtor da classe Aluno'''
        super().__init__(nome, idade) # chama o construtor da classe Pessoa
        self.curso = curso  # atribui o curso do aluno
        self.turma = turma # atribui a turma do aluno

    def fazerMatricula(self):
        '''método para fazer matrícula do aluno'''
        print(f'[bold white]{self.nome}[/] está fazendo matrícula...')
 
class Professor(Pessoa):
    '''classe Professor que representa um professor'''
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade) # chama o construtor da classe Pessoa
        '''construtor da classe Professor'''
        self.especialidade:str = especialidade # atribui a especialidade do professor
        self.nivel:str = nivel # atribui o nível do professor

    def darAula(self):
        '''método para dar aula do professor'''
        print(f'Professor [bold white]{self.nome}[/] está dando aula...')


class Funcionario(Pessoa):
      '''classe Funcionario que representa um funcionário''' 
      def __init__(self, nome, idade, cargo, setor):
        '''construtor da classe Funcionario'''
        super().__init__(nome, idade) # chama o construtor da classe Pessoa
        self.cargo:str = cargo # atribui o cargo do funcionário
        self.setor:str = setor # atribui o setor do funcionário

      def baterPonto(self):
        '''método para bater ponto do funcionário'''
        print(f'Funcionário [bold white]{self.nome}[/] bateu o ponto...')

aluno1 = Aluno('João', 20, 'Engenharia', 'A')
aluno1.fazerMatricula() # chama o método fazerMatricula da classe Aluno
inspect(aluno1, methods=True)

professor1 = Professor('Maria', 35, 'Matemática', 'Doutorado')
professor1.darAula() # chama o método darAula da classe Professor
inspect(professor1, methods=True)