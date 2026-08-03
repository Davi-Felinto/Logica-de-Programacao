# Aula 09a: exemplos de métodos de string usando uma frase (letra de música) de várias linhas

frase ="""Ela de roupa é dez
Ela pelada é dez
Ela comigo é dez, dez, dez, dez
Ela de roupa é dez
Ela pelada é dez
Ela comigo é dez, dez, dez, dez"""  # string multi-linha (delimitada por três aspas)

dividido= frase.split()  # separa a frase em uma lista de palavras (usando espaços/quebras de linha como separador)

print(frase.title())                              # deixa a inicial de cada palavra maiúscula
print(frase.title().count('Dez'))                  # conta quantas vezes 'Dez' aparece depois de aplicar title()
print(len(frase))                                   # mostra o total de caracteres da frase (incluindo espaços e quebras de linha)
print(frase.title().replace('Dez', 'Onze'))         # substitui todas as ocorrências de 'Dez' por 'Onze'
print('dez' in frase)                               # verifica se a substring 'dez' (minúscula) existe na frase original
print(frase.find('comigo'))                         # retorna a posição (índice) onde 'comigo' aparece pela primeira vez
print(dividido[6][0])                               # pega a 7ª palavra da lista (índice 6) e sua 1ª letra (índice 0)
