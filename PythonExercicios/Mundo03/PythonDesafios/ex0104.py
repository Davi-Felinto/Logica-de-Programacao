def LeiaInt(txt):
    while True:
        num = input(txt)
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('\033[0;31mERRO! Digite um numero inteiro valido\033[m')
    return num 


n = LeiaInt('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')