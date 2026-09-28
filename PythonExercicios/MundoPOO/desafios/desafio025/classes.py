from abc import ABC, abstractmethod

class Transporte(ABC):
    
    def __init__(self, distacia:float):
        self.distacia = distacia
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    fator = 0.50

    def __init__(self, distacia):
        super().__init__(distacia)

    def calc_frete(self):
        self.frete = self.distacia * Moto.fator
        return f'R${self.frete:.2f}'

class Caminhao(Transporte):
    fator = 1.20

    def __init__(self, distacia):
        super().__init__(distacia)

    def calc_frete(self):
        if 0 < self.distacia >= 50:
            self.frete = self.distacia * Caminhao.fator
            return f'R${self.frete:.2f}'
        else:
            return 'Distacia minima de 50Km'

class Drone(Transporte):
    fator = 9.50

    def __init__(self, distacia):
        super().__init__(distacia)

    def calc_frete(self):
        if 0 < self.distacia <= 10:
            self.frete = self.distacia * Drone.fator
            return f'R${self.frete:.2f}'
        else:
            return 'Distacia maxima de 10Km'