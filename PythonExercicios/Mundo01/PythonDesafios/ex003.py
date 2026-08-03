# Exercício 003: soma de dois números lidos do usuário

n1 = int(input('Digite um numero: '))       # lê o 1º número e converte de texto para inteiro
n2 = int(input('Digite outro numero: '))    # lê o 2º número e converte de texto para inteiro

s = (n1 + n2)  # soma os dois números e guarda o resultado em 's'

print('a soma entre {} e {} vale: {}'.format(n1, n2, s))  # mostra n1, n2 e a soma
