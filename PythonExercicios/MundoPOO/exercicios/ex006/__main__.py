from rich import print, inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

def main():
    aluno1 = Aluno('Davi Felinto', 19, 'Eng. de Software', 'ESa')
    aluno1.fazerMatricula() # chama o método fazerMatricula da classe Aluno
    inspect(aluno1, methods=True)

    professor1 = Professor('Maria', 35, 'Matemática', 'Doutorado')
    professor1.darAula() # chama o método darAula da classe Professor
    inspect(professor1, methods=True)

main() if __name__== '__main__' else None