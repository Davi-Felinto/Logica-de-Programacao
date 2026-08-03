c_num = 0
s = 0
for c in range(1, 501, 2):
    if (c % 3) == 0:
        s += c
        c_num += 1
print(f'a soma de todos os {c_num} valores solicitados é {s}')