from time import sleep

c = ('\033[m',  # sem cor
     '\033[0;30;41m',  # vermelho
     '\033[0;30;42m',  # verde
     '\033[0;30;43m',  # amarelo
     '\033[0;30;44m',  # azul
     '\033[0;30;45m',  # roxo
     '\033[0;30;47m',  # branco
    );

def ajuda(com):
    titulo(f'Acessando manual do comando \'{com}\'', 4)
    print(c[0], end='')
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(c[0], end='')
    sleep(1)

comando = ''
while True:
    titulo('SISTEMA DE AJUDA - HelPy', 2)
    comando = str(input('Função ou Library: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)


























# def Ajuda():
#     while True:
#         print('~' * len(' SISTEMA DE AJUDA PyHELP '))
#         print(' SISTEMA DE AJUDA PyHELP ')
#         print('~' * len(' SISTEMA DE AJUDA PyHELP '))

#         funcao = input('Função ou Biblioteca > ').strip()
#         if funcao.upper() == 'FIM':
#             print('~' * len(' ATÉ LOGO! '))
#             print(' ATÉ LOGO! ')
#             print('~' * len(' ATÉ LOGO! '))
#             break
#         else:
#             print('~' * len(f" Acessando o manual do comando '{funcao}' "))
#             print(f" Acessando o manual do comando '{funcao}' ")
#             print('~' * len(f" Acessando o manual do comando '{funcao}' "))
#             help(funcao)


# Ajuda()