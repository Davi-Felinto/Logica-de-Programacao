def LeiaDinheiro(txt):
    while True:
        resp = input(txt).strip().replace(',', '.')
        if resp.isalpha() or resp == '':
            print(f'\033[0;31mERRO: "{resp}" é um preço invalido!\033[m')
        else:
            resp = float(resp)
            break        
    return resp

def LeiaInt(txt):
    while True:
        num = input(txt)
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('\033[0;31mERRO! Digite um numero inteiro valido\033[m')
    return num 