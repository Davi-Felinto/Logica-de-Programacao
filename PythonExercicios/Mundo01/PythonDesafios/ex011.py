larg = float(input('Largura da parede: ')) # Lendo as medidas 
alt = float(input('Altura da parede: '))

a = larg*alt # Calculos de area e consumo de tinta
tinta = a/2

print(f'Sua parede tem a dimensão de {larg}x{alt} e sua área é de {a}m².')  # Saida da area e da tinta 
print(f'Para pintar  essa parede, vocé precisará de {tinta}L de tinta.')