print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)

n = int(input('Quantos termos você quer mostrar? '))
i = 3
t1 = 0
t2= 1

print('~'*30)
print(f'{t1} -> {t2}', end='')
while i <= n:
    t3 = t1 + t2
    print(f'-> {t3}', end='')
    t1 = t2
    t2 =t3
    i += 1
print('FIM')