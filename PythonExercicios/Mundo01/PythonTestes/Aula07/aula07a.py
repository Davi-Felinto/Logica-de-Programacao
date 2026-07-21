n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m =n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('a soma é {}'.format(s), end=' ') #end=' ' final = a um espaço, não quebra a linha para outro print
print('o produto é {} \na potência é {}'.format(m, e)) # \n faz a quebra da linha
print('a divisão é {1:.3f} e a divisão interira é {0}'.format(di, d))