def Par(num=0):
    if (num % 2) == 0:
        return True
    else:
        return False

n = int(input('Digite um numero: '))
if Par(n):
    print('É par')
else:
    print('É impar')