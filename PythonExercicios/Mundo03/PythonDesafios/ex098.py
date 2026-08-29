from time import sleep

def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1)
    if passo == 0:
        passo = 1
    if inicio < fim:
        for i in range(inicio, (fim + 1), passo):
            print(i, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
    else:
        if passo > 0:
            passo *= (-1)
        for i in range(inicio, (fim - 1), passo):
            print(i, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')


print('-='*15)
contador(1, 10, 1)
print('-='*15)
contador(10, 0, 2)
print('-='*15)
print('Agora é sua vez de personalizar a contagem')
contador(int(input('inicio: ')), int(input('fim: ')), int(input('passo: ')))