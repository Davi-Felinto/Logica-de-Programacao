# Exercício 011: calcula área de uma parede e quantidade de tinta necessária

larg = float(input('Largura da parede: '))  # lê a largura da parede
alt = float(input('Altura da parede: '))    # lê a altura da parede

a = larg*alt   # área da parede = largura x altura
tinta = a/2    # a cada 1 litro de tinta cobre-se 2m², então tinta = área / 2

print(f'Sua parede tem a dimensão de {larg}x{alt} e sua área é de {a}m².')
print(f'Para pintar  essa parede, vocé precisará de {tinta}L de tinta.')
