valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    resp = input('Quer continuar? [S/N] ')
    if resp.upper() == 'N':
        break
print('-='*30)
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem descrecente são {valores}')
print('O valor 5 faz parte da lista!') if 5 in valores else print('O valor 5 não faz parte da lista!')