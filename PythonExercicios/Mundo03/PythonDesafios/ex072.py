cont = ('zero', 'um', 'dois', 'três', 'quatro', 
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'cartoze',
        'quinze', 'dezesseis', 'dezesete', 'dezoito',
        'dezenove', 'vinte')
while True:
    while True:
        numero = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= numero <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o numero {cont[numero]}')

    while True:
        resp = input('Quer continuar? [S/N]').upper()
        if resp == 'S':
            while True:
                numero = int(input('Digite um numero entre 0 e 20: '))
                if 0 <= numero <= 20:
                    break
                print('Tente novamente. ', end='')
            print(f'Você digitou o numero {cont[numero]}')
        elif resp in 'N':
            print('Até mais!')
            break
    break
