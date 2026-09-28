from pessoa import Pessoa
from rich import print, inspect


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
