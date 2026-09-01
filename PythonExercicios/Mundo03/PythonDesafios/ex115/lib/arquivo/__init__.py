from lib.interface import *

def ArquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def CriarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
    

def LerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        Cabecalho('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>7} anos')
    finally:
        a.close()


def Cadastrar(nome):
    Cabecalho('Novo Cadastro')
    nomePessoa = input('Nome: ')
    if nomePessoa == '':
        nomePessoa = 'desconhecido'
    idade =  LeiaInt('Idade: ')
    try:
        a = open(nome, 'at')
    except:
        print('Houve um Erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nomePessoa};{idade}\n')
        except:
            print('Houve um Erro ao escrever no arquivo')
        else:
            print(f'Novo registro de {nomePessoa} adicionado')
    finally:
        a.close()