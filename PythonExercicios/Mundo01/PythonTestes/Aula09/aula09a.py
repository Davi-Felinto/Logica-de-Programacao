frase ="""Ela de roupa é dez
Ela pelada é dez
Ela comigo é dez, dez, dez, dez
Ela de roupa é dez
Ela pelada é dez
Ela comigo é dez, dez, dez, dez"""

dividido= frase.split()

print(frase.title())
print(frase.title().count('Dez'))
print(len(frase))
print(frase.title().replace('Dez', 'Onze'))
print('dez' in frase)
print(frase.find('comigo'))
print(dividido[6][0])