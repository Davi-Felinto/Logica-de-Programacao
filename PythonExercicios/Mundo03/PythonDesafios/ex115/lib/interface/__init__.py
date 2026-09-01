def Linha (tamanho=42):
    return ('-' * tamanho)

def Cabecalho(txt, tamanho=42):
    print(Linha(tamanho))
    print(txt.center(len(Linha(tamanho))))
    print(Linha(tamanho))

def menu(listaOpcoes, tamanho=42):
    Cabecalho('Menu Principal', tamanho)
    for i, v in enumerate(listaOpcoes):
        print(f'\033[m{i+1}\033[m - \033[m{v}\033[m')
    print(Linha(tamanho))
    opc = LeiaInt('Sua opção: ')
    return opc

def LeiaInt(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TabError):
            print('\033[0;31mERRO! Digite uma opção valida!\033[m')
            continue
        except KeyboardInterrupt:
            print(('\n\033[0;31mEntrada de dados interrompida pelo usuario.\033[m'))
            return 0
        else:
            return num 