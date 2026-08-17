num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)

num.remove(5) if 5 in num else print('Não achei o valor 5')
# num.pop(2) remove o indisse 2
print(num)
print(f'Essa lista tem {len(num)} elementos')