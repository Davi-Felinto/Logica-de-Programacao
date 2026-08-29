def dobro(lista):
    i = 0
    while i < len(lista):
        lista[i] *= 2
        i += 1
    print(lista)


valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobro(valores[:])
print(valores)