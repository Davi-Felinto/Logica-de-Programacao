frase = input('Digite uma frase: ').strip() # Lendo uma frase

print(f'A letra A aparece {frase.lower().count('a')} vezes na frase.') # Saida de numeros de 'A', posição do primeiro e ultimo 'A'
print(f'A primeira letra A aparece na posição {frase.lower().find('a')+1}')
print(f'A ultima letra A aparece na posição {frase.lower().rfind('a')+1}')
