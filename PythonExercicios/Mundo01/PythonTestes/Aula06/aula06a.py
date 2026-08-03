# Aula 06a: exemplo de soma de dois números e formatação de saída com .format()

n1 = int(input('digite um numero: '))       # lê o 1º número
n2 = int(input('digite outro numero: '))    # lê o 2º número
s = (n1 + n2)                                # soma os dois números

#print('A soma entre ', n1, ' e ', n2, ' vale', s)  # forma alternativa usando vírgulas no print (desativada)
print('A soma entre {} e {} vale {}'.format(n1, n2, s))  # forma usando .format() para inserir os valores no texto
