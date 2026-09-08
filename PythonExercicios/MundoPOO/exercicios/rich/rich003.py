from rich import print
from rich.table import Table

tabela = Table(title='Tabela de Preços', style='blue')

tabela.add_column('Nome', justify='center', style='red')
tabela.add_column('Preço', justify='center', style='green')

tabela.add_row('Lapis', 'R$1.50')
tabela.add_row('Borracha', 'R$2.50')
tabela.add_row('Caderno', 'R$10')

print(tabela)