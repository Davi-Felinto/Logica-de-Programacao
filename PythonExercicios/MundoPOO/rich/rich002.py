from rich import print
from rich.panel import Panel

caixa = Panel('[white]Esse aqui e um painel de exemplo[/]', title='Mensagem', style='red', width=45)

print(caixa)