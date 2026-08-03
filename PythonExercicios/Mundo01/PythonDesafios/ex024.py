# Exercício 024: verifica se a primeira palavra da cidade contém "santo"

city = input('Em que cidade você nasceu? ').strip().split()  # lê, remove espaços das pontas e separa em lista de palavras

pri_palavra = city[0]  # pega a primeira palavra da cidade (ex: 'Santo' em 'Santo André')

print('santo' in pri_palavra.lower())  # verifica se a substring 'santo' está contida na palavra (em minúsculas)
