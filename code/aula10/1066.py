par = 0
impar = 0
posi = 0
nega = 0

for i in range(5):
    num = int(input())
    if ((num % 2) == 0):
        par += 1
    else:
        impar += 1
    if (num > 0):
        posi += 1
    elif (num < 0):
        nega += 1

print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{posi} valor(es) positivo(s)")
print(f"{nega} valor(es) negativo(s)")