# Aula 07a: operações matemáticas básicas entre dois números

n1 = int(input('Um valor: '))     # lê o 1º número
n2 = int(input('Outro valor: '))  # lê o 2º número

s = n1 + n2    # soma
m =n1 * n2     # multiplicação (produto)
d = n1 / n2    # divisão real (com casas decimais)
di = n1 // n2  # divisão inteira (descarta o resto)
e = n1 ** n2   # potência (n1 elevado a n2)

print('a soma é {}'.format(s), end=' ') # end=' ' final = a um espaço, não quebra a linha para outro print
print('o produto é {} \na potência é {}'.format(m, e)) # \n faz a quebra da linha
print('a divisão é {1:.3f} e a divisão interira é {0}'.format(di, d))  # {1} e {0} indicam a ordem dos argumentos no format
