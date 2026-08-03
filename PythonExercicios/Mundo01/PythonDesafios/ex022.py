# Exercício 022: analisa o nome completo digitado pelo usuário

nome = input('Digite seu nome completo: ').strip()  # lê o nome e remove espaços extras do início/fim com strip()

nome_separado = nome.split()  # split() sem argumento separa a string em uma lista de palavras usando espaços

print('Analisando seu nome...')
print('Seu nome em maiúsculas é', nome.upper())   # upper() converte tudo para maiúsculas
print('Seu nome em minúsculas é', nome.lower())   # lower() converte tudo para minúsculas
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras')  # tamanho total menos os espaços = só as letras
print(f'Seu primeiro nome é {nome_separado[0]} e ele tem {len(nome_separado[0])} letras')  # primeiro item da lista = primeiro nome
# print(f'Seu primeiro nome tem {nome.find(' ')} letras')  # linha alternativa desativada
