from classes import *
from rich import print
from rich.table import Table

def main():
    dist = 8

    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]

    '''entrega = Drone(dist)
    print(f'Frete de {type(entrega).__name__} em {dist}Km = {entrega.calc_frete()}')'''

    tabela = Table(title='Tabela de Fretes')
    tabela.add_column('Distacia')
    tabela.add_column('Tipo')
    tabela.add_column('Frete')

    for item in viagem:
        tabela.add_row(f'{dist}', f'{type(item).__name__}', f'{item.calc_frete()}')

    print(tabela)

if __name__ == '__main__':
    main()