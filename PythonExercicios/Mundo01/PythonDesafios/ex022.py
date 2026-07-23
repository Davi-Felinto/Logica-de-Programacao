nome = input('Digite seu nome completo: ').strip() # Lendo nome sem espaços antes e dps

nome_separado = nome.split() # Fartiando nome

print('Analisando seu nome...') # Analisando o nome. Saida de nome em maiusculas, minusculas, numero de letra, primeiro nome e numero de letras de letras do primeiro nome
print('Seu nome em maiúsculas é', nome.upper())
print('Seu nome em minúsculas é', nome.lower())
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras')
print(f'Seu primeiro nome é {nome_separado[0]} e ele tem {len(nome_separado[0])} letras')
# print(f'Seu primeiro nome tem {nome.find(' ')} letras')