lista = []
while True:
    valor = (int(input('Digite um valor: ')))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        resp = input('Quer continuar? [S/N] ').upper()
        if resp == 'N':
            break
        if resp == 'S':
            break
    if resp == 'N':
        break
lista.sort()
print(lista)