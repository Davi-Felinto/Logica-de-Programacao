from rich import print
from rich import inspect

class ContaBancaria:
    '''
    Cria uma conta bacaria e permite fazer saques e depositos
    '''
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}')
    
    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo.'

    def Depositar(self, valor):
        self.saldo += valor
        print(f'Deposito de R${valor:,.2f} autorizado na conta {self.id}. Saldo atual R${self.saldo:,.2f}')

    def Sacar(self,valor):
        if self.saldo < valor:
            print(f'Saque NEGADO de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor:,.2f} autorizado na conta {self.id}. Saldo atual R${self.saldo:,.2f}')




c1 = ContaBancaria(112, 'Davi Felinto', 1000000)
inspect(c1)