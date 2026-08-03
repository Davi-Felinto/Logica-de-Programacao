# Exercício 026: conta ocorrências da letra 'A' em uma frase e mostra sua primeira/última posição

frase = input('Digite uma frase: ').strip()  # lê a frase e remove espaços das pontas

print(f'A letra A aparece {frase.lower().count('a')} vezes na frase.')              # count() conta quantas vezes 'a' aparece
print(f'A primeira letra A aparece na posição {frase.lower().find('a')+1}')         # find() retorna o índice (base 0) da 1ª ocorrência, +1 para posição "humana"
print(f'A ultima letra A aparece na posição {frase.lower().rfind('a')+1}')          # rfind() retorna o índice da última ocorrência, +1 para posição "humana"
