# Declaração de Classes
class Garfonhoto:
    '''
    Essa classe cria um Garfonhoto, q é uma pessoa q tem nome e idade.
    Para criar uma nova pessoa, use
    variavel = Garfonhoto(nome, idade)
    '''
    #Metodo Construtor
    def __init__(self, nome = '', idade = 0):
        # Atributi de instancia
        self.nome = nome
        self.idade = idade

    # Metodo de Instatancia
    def Aniversario(self):
        self.idade += 1

    def __str__(self):
        return f'{self.nome} é Garfonhoto(a) e tem {self.idade} anos de idade.'

    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade}'

#Declaraçao de Objetos
g1 = Garfonhoto('Davi Felinto', 19)
g1.Aniversario()
print(g1)
print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__)

print()

g2 = Garfonhoto('Gustavo Guanabara', 43)
print(g2)
print(g2.__dict__) # Attribute
print(g2.__getstate__()) # Method
print(g2.__class__)

# print(g1.__doc__) # Dunder Attribute