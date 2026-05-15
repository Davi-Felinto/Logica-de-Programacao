# Leitura dos valores
valores = list(map(float, input().split()))

valores.sort(reverse=True)
a, b, c = valores

if a >= b+c:
    print("NAO FORMA TRIANGULO")
else:
    if (a**2) == (b**2) + (c**2):
        print("TRIANGULO RETANGULO")
    elif (a**2) > (b**2) + (c**2):
        print("TRIANGULO OBTUSANGULO")
    elif (a**2) < (b**2) + (c**2):
        print("TRIANGULO ACUTANGULO")
    elif (a == b == c):
        print("TRIANGULO EQUILATERO")

if (a == b == c):
    print("TRIANGULO EQUILATERO")
elif (a == b) or (b == c) or (a == c):
    print("TRIANGULO ISOSCELES")