def LeiaInt(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TabError):
            print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m')
            continue
        except KeyboardInterrupt:
            print(('\n\033[0;31mEntrada de dados interrompida pelo usuario.\033[m'))
            return 0
        else:
            return num 


def LeiaFloat(txt):
    while True:
        try:
            num = float(input(txt))
        except (ValueError, TabError):
            print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m')
            continue
        except KeyboardInterrupt:
            print(('\n\033[0;31mEntrada de dados interrompida pelo usuario.\033[m'))
            return 0
        else:
            return num 

n1 = LeiaInt('Digite um Inteiro: ')
n2 = LeiaFloat('Digite um Real: ')
print(f'O valor interio digitado foi {n1} e o real foi {n2}')