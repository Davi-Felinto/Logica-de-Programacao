# Exercício 004: analisa características de um texto digitado

a = input('Digite algo: ')  # lê qualquer coisa digitada pelo usuário como texto (string)

# Analisando o que foi escrito
print('O tipo primitivo desse valor é', type(a))       # type() mostra o tipo da variável (aqui sempre será str)
print('Só tem espaços?', a.isspace())                   # isspace() -> True se só houver espaços em branco
print('É um numero?', a.isnumeric())                    # isnumeric() -> True se todos os caracteres forem números
print('É alfabetico?', a.isalpha())                      # isalpha() -> True se todos os caracteres forem letras
print('É alfanumerico?', a.isalnum())                    # isalnum() -> True se só houver letras e/ou números (sem espaços/símbolos)
print('Esta em maiusculas?', a.isupper())                # isupper() -> True se todas as letras estiverem em maiúsculo
print('Esta em minusculas?', a.islower())                # islower() -> True se todas as letras estiverem em minúsculo
print('Esta capitalizado?', a.istitle())                 # istitle() -> True se cada palavra começar com letra maiúscula
