a = [2, 3, 4, 7]
b = a[:] # a = b faz uma ligação entre a e b, já b = a[:] faz b receber todos os valores da lista a e não ligar as duas 
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')