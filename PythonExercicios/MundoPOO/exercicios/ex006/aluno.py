from pessoa import Pessoa
from rich import print, inspect


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