# Declaração de Classes
class Garfonhoto:
    #Metodo Construtor
    def __init__(self): 
        # Atributi de instancia
        self.nome = ''
        self.idade = 0

    # Metodo de Instatancia
    def Aniversario(self):
        self.idade += 1
    
    def Mensagem(self):
        return f'{self.nome} é Garfonhoto(a) e tem {self.idade} anos de idade.'

#Declaraçao de Objetos
g1 = Garfonhoto()
g1.nome = 'Davi Felinto'
g1.idade = 19
g1.Aniversario()
print(g1.Mensagem())

g2 = Garfonhoto()
g2.nome = 'Gustavo Guanabara'
g2.idade = 43
print(g2.Mensagem())