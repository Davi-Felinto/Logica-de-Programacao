lanche = ('Hamburhue', 'Suco', 'Pizza', 'Pudim')
# Tuplas são imutaveis

# for i in range(0, len(lanche)):
#     print(lanche[i])

# for comida in lanche:
#     print(f'Eu vou comer {comida}')

for pos, i in enumerate(lanche):
    print(f'Eu vou comer {i} na posição {pos}')

print(sorted(lanche))
print(lanche)