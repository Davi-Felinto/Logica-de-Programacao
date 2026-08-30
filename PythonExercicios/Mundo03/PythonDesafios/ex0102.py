def fatorial(num, show=False):
    '''
        -> Calcula o Fatorial de um número.
    :param n: 0 número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: 0 valor do Fatorial de um número n.
    '''
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(c, end='')
            print(' x ', end='') if c > 1 else print(' = ', end='')
    return f

print(fatorial(int(input('Digite um numero para calcular o fatorial: ')), True))
help(fatorial)