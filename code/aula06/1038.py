item, quantidade = map(int, input().split(' '))

if item == 1:
        valor = 4
        paga = valor * quantidade
elif item == 2:
        valor = 4.5
        paga = valor * quantidade
elif item == 3:
        valor = 5
        paga = valor * quantidade
elif item == 4:
        valor = 2
        paga = valor * quantidade
elif item == 5:
        valor = 1.50
        paga = valor * quantidade

print(f"Total: R$ {paga:.2f}")