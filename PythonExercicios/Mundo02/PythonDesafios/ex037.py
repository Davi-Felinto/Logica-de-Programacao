# Exercício 037: converte um número inteiro para binário, octal ou hexadecimal

# importando modulo
from random import randint  # sorteia um número caso o usuário digite 0

# Lendo numero para converter
num = int(input('Digite um numero inteiro: '))
num = randint(-999, 999) if num == 0 else num  # se digitar 0, sorteia um número entre -999 e 999
print(num)

# Escolha da base de conversão
print('[ 1 ] converter para BINARIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))  # lê a opção escolhida pelo usuário

# Saida da conversão
# bin(), oct() e hex() retornam o número em texto com prefixo (0b, 0o, 0x); [2:] remove esse prefixo
if opcao == 1:
    print(f'{num} convertido para BINARIO é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção invalida. Tente novamente.')
