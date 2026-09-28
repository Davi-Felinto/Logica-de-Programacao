class Pessoa:
    '''classe Pessoa que representa uma pessoa'''
    def __init__(self, nome:str = '', idade:int = 0):
        '''construtor da classe Pessoa'''
        self.nome:str = nome # atribui o nome da pessoa
        self.idade:int = idade # atribui a idade da pessoa

    def fazerAniversario(self):
        '''método para fazer aniversário da pessoa'''
        self.idade += 1 # aumenta a idade em 1