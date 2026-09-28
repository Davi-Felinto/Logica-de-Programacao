from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    
    def preparar(self):
        print('--- Iniciando Preparo ---')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print('--- Bebida Pronta ---\n')

    def ferver_agua(self):
        print('1. Fervendo agua a 100 graus Celsius.')

    @abstractmethod
    def misturar(self):
        pass
    
    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):

    def misturar(self):
        print('2. Passando agua pressurizada pelo pó de café moído.')

    
    def servir(self):
        print('3. Servindo em xicara pequena.')

class Leite(BebidaQuente):

    def misturar(self):
        print('2. Passando vapor pressurizado pelo bico do leite.')

    
    def servir(self):
        print('3. Servindo na caneca grande, já com café.')    

class Cha(BebidaQuente):

    def misturar(self):
        print('2. Mergulhando o sachê de ervas na agua.')

    
    def servir(self):
        print('3. servindo na caneca de porcelana com limão')    