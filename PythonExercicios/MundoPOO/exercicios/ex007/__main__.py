from classes import Pessoa, Aluno, Professor, Funcionario
from rich import inspect

def main():
    a1 = Aluno('Davi Felinto', 19, 'Eng. de Software', 'ESa')
    a1.fazerAniversario()
    a1.fazerMatricula() # chama o método fazerMatricula da classe Aluno
    # inspect(a1, methods=True)

    p1 = Professor('Maria', 35, 'Matemática', 'Doutorado')
    p1.fazerAniversario()
    p1.darAula() # chama o método darAula da classe Professor
    # inspect(p1, methods=True)

    f1 = Funcionario('Claudia', 27, 'Secretaria', 'Secretaria')
    f1.fazerAniversario()
    f1.baterPonto()
    # inspect(f1, methods=True)

    a1.estudar()
    f1.estudar()
    p1.estudar()
main() if __name__ == '__main__' else None