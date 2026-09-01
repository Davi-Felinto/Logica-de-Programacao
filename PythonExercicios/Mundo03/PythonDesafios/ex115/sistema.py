from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not ArquivoExiste(arq):
    CriarArquivo(arq)

while True:
    resp = (menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema']))
    if resp == 1:
        # Opção de listar o conteudo de um arquivo
        LerArquivo(arq)
    elif resp == 2:
        #Opção de cadastrar uma nova pessoa
        Cadastrar(arq)
    elif resp == 3:
        print('Saindo do sistema... Até logo!')
        break
    sleep(1)
