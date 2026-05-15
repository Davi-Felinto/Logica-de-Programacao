#cod1, num1, valo1 = input().split() O .split() é uma função do Python que serve para dividir uma string em partes, normalmente usando o espaço como separador.
#cod2, num2, valo2 = input().split()
cod1, num1, valo1 = map(float, input().split(';'))
cod2, num2, valo2 = map(float, input().split(';'))

#preco = (int(num1)*float(valo1)) + (int(num2)*float(valo2)) assim tenho q definir oq cada var é
preco = (num1*valo1) + (num2*valo2)

print(f"VALOR A PAGAR: R$ {preco:.2f}")