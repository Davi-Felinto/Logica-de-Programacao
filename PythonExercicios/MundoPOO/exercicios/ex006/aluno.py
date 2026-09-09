from pessoa import Pessoa

class Aluno(Pessoa):
    '''classe Aluno que representa um aluno'''
    def __init__(self, nome, idade, curso, turma):
        '''construtor da classe Aluno'''
        super().__init__(nome, idade) # chama o construtor da classe Pessoa
        self.curso = curso  # atribui o curso do aluno
        self.turma = turma # atribui a turma do aluno

    def fazer_matricula(self):
        '''método para fazer matrícula do aluno'''
        print(f'[bold white]{self.nome}[/] está fazendo matrícula...')