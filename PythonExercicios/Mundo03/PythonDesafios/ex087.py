matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar= somaColuna3 = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f'Digite um valor para [{l}, {c}]: ')))
        if (matriz[l][c] % 2) == 0:
            somaPar += matriz[l][c]
        if matriz[l][c] == matriz[l][2]:
            somaColuna3 += matriz[l][c]
# if matriz[1][0] > matriz[1][1] or matriz[1][0] > matriz[1][2]:
#     maiorLinha2 = matriz[1][0]
# elif matriz[1][1] > matriz[1][2]:
#     maiorLinha2 = matriz[1][1]
# elif matriz[1][2] > matriz[1][1]:
#     maiorLinha2 = matriz[1][2]
maiorLinha2 = max(matriz[1]) # Simplificação do comentario acima

print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-='*30)
print(f'A soma dos valores pares é {somaPar}')
print(f'a soma dos valores da terceira coluna é {somaColuna3}')
print(f'O maior valor da segunda linha é {maiorLinha2}')