from random import randint
from time import sleep


n1 = int(input('Primeiro valor: '))
n1 == randint(0,100) if n1 == 0  else n1
n2 = int(input('Segundo valor: '))
n2 = randint(0,100) if n2 == 0 else n2

menu = 0
while menu != 5:
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos numeros')
    print('[ 5 ] Sair do programa') 
    menu =  int(input('>>>>> Qual opção? '))
    if menu == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
    elif menu == 2:
        print(f'O resultado de {n1} x {n2} é {n1*n2}')
    elif menu == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior valor é {n1}')
        elif n2 > n1:
            print(f'Entre {n1} e {n2} o maior valor é {n2}')
    elif menu ==  4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif menu == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção invalida. Tente novamente')
    print('=-'*15)
    sleep(0.5)